from youtube.http_fetcher import UrllibPageFetcher
from youtube.mixedsearch import MixedSearch
from youtube.videosearch import VideoSearch
from youtube.channelsearch import ChannelSearch
from youtube.playlistsearch import PlaylistSearch
from youtube.video import YoutubeVideo
from youtube.playlist import YoutubePlaylist
from youtube.cache import YoutubeLocalCache, YoutubeGlobalCache
from youtube.tools import search_wrapper, get_object_wrapper

__all__ = ['YoutubeApi']

class YoutubeApi():
    _http_fetcher = None
    _nocache = None
    _cache = None

    def __init__(self, *, http_fetcher=None, nocache=False, global_cache=False):
        self._http_fetcher = http_fetcher if http_fetcher is not None else UrllibPageFetcher()
        self._nocache = nocache
        self._cache = YoutubeGlobalCache() if global_cache else YoutubeLocalCache()

    def search(self, search_string):
        return search_wrapper('MixedSearch', search_string, self._cache, self._nocache,
                              lambda: MixedSearch(self._http_fetcher).search(search_string))

    def search_videos(self, search_string):
        return search_wrapper('VideoSearch', search_string, self._cache, self._nocache,
                              lambda: VideoSearch(self._http_fetcher).search(search_string))

    def search_channels(self, search_string):
        return search_wrapper('ChannelSearch', search_string, self._cache, self._nocache,
                              lambda: ChannelSearch(self._http_fetcher).search(search_string))

    def search_playlists(self, search_string):
        return search_wrapper('PlaylistSearch', search_string, self._cache, self._nocache,
                              lambda: PlaylistSearch(self._http_fetcher).search(search_string))

    def get_video(self, video_id):
        return get_object_wrapper(video_id, self._cache, self._nocache,
                                  lambda: YoutubeVideo(self._http_fetcher, video_id))

    def get_playlist(self, playlist_id):
        return get_object_wrapper(playlist_id, self._cache, self._nocache,
                                  lambda: YoutubePlaylist(self._http_fetcher, playlist_id))

    def clear_cache(self):
        self._cache.clear_cache()
