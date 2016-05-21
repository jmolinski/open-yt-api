from youtube.http_fetcher import UrllibPageFetcher
from youtube.mixedsearch import MixedSearch
from youtube.videosearch import VideoSearch
from youtube.channelsearch import ChannelSearch
from youtube.playlistsearch import PlaylistSearch
from youtube.video import YoutubeVideo
from youtube.playlist import YoutubePlaylist
from youtube.channel import YoutubeChannel
from youtube.cache import _YoutubeCache

__all__ = ['YoutubeApi']

# theses 2 functions manage caching
def _search_wrapper(search_type, search_string, nocache, actual_search):
    if nocache:
        return actual_search()

    cached = _YoutubeCache.get_search_result(search_type, search_string)
    if cached:
        return cached
    else:
        results = actual_search() # executes lambda
        _YoutubeCache.add_search_result(search_type, search_string, results)
        return results

def _get_object_wrapper(object_id, nocache, actual_search):
    if nocache:
        return actual_search()

    cached = _YoutubeCache.get_object(object_id)
    if cached:
        return cached
    else:
        result = actual_search() # executes lambda
        _YoutubeCache.add_object(object_id, result)
        return result


class YoutubeApi():
    _http_fetcher = None
    _nocache = None

    def __init__(self, http_fetcher=None, nocache=False):
        self._http_fetcher = http_fetcher if http_fetcher is not None else UrllibPageFetcher()
        self._nocache = nocache

    def search(self, search_string):
        return _search_wrapper('MixedSearch', search_string, self._nocache,
            lambda: MixedSearch(self._http_fetcher).search(search_string))

    def search_videos(self, search_string):
        return _search_wrapper('VideoSearch', search_string, self._nocache,
            lambda: VideoSearch(self._http_fetcher).search(search_string))

    def search_channels(self, search_string):
        return _search_wrapper('ChannelSearch', search_string, self._nocache,
            lambda: ChannelSearch(self._http_fetcher).search(search_string))

    def search_playlists(self, search_string):
        return _search_wrapper('PlaylistSearch', search_string, self._nocache,
            lambda: PlaylistSearch(self._http_fetcher).search(search_string))

    def get_video(self, video_id):
        return _get_object_wrapper(video_id, self._nocache,
            lambda: YoutubeVideo(self._http_fetcher, video_id))

    def get_playlist(self, playlist_id):
        return _get_object_wrapper(playlist_id, self._nocache,
            lambda: YoutubePlaylist(self._http_fetcher, playlist_id))

    def get_channel(self, channel_id):
        return _get_object_wrapper(channel_id, self._nocache,
            lambda: YoutubeChannel(self._http_fetcher, channel_id))

    def clear_cache(self):
        _YoutubeCache.clear_cache()
