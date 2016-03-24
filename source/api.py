from source.http_fetcher import UrllibPageFetcher
from source.videosearch import VideoSearch
from source.channelsearch import ChannelSearch
from source.playlistsearch import PlaylistSearch
from source.video import YoutubeVideo
from source.playlist import YoutubePlaylist
from source.channel import YoutubeChannel

class YoutubeApi():
    _http_fetcher = None

    def __init__(self, http_fetcher=None):
        if http_fetcher is None:
            http_fetcher = UrllibPageFetcher()
        self._http_fetcher = http_fetcher

    def search_videos(self, search_string):
        yt_searcher = VideoSearch(self._http_fetcher)
        return yt_searcher.search(search_string)

    def search_channels(self, search_string):
        yt_searcher = ChannelSearch(self._http_fetcher)
        return yt_searcher.search(search_string)

    def search_playlists(self, search_string):
        yt_searcher = PlaylistSearch(self._http_fetcher)
        return yt_searcher.search(search_string)

    def get_video(self, video_id):
        return YoutubeVideo(self._http_fetcher, video_id)

    def get_playlist(self, playlist_id):
        return YoutubePlaylist(self._http_fetcher, playlist_id)

    def get_channel(self, channel_id):
        return YoutubeChannel(self._http_fetcher, channel_id)
