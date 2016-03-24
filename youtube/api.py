from youtube.http_fetcher import UrllibPageFetcher
from youtube.videosearch import VideoSearch
from youtube.channelsearch import ChannelSearch
from youtube.playlistsearch import PlaylistSearch
from youtube.video import YoutubeVideo
from youtube.playlist import YoutubePlaylist
from youtube.channel import YoutubeChannel

class YoutubeApi():
    _http_fetcher = None

    def __init__(self, http_fetcher=None):
        self._http_fetcher = http_fetcher if http_fetcher is not None else UrllibPageFetcher()

    def search_videos(self, search_string):
        return VideoSearch(self._http_fetcher).search(search_string)

    def search_channels(self, search_string):
        return ChannelSearch(self._http_fetcher).search(search_string)

    def search_playlists(self, search_string):
        return PlaylistSearch(self._http_fetcher).search(search_string)

    def get_video(self, video_id):
        return YoutubeVideo(self._http_fetcher, video_id)

    def get_playlist(self, playlist_id):
        return YoutubePlaylist(self._http_fetcher, playlist_id)

    def get_channel(self, channel_id):
        return YoutubeChannel(self._http_fetcher, channel_id)
