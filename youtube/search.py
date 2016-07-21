import urllib.parse

from youtube.channelsearchparser import ChannelSearchParser
from youtube.errors import YoutubeApiConnectionError
from youtube.playlistsearchparser import PlaylistSearchParser
from youtube.videosearchparser import VideoSearchParser


class BaseSearch():
    _http_fetcher = None

    def __init__(self, http_fetcher):
        self._http_fetcher = http_fetcher

    def _make_search_url(self, search_string):
        return self._base_search_url + self._escape_url(search_string)

    def _escape_url(self, url):
        return urllib.parse.quote_plus(url)

    def _get_page_content(self, url):
        try:
            return self._http_fetcher.fetch_page(url)
        except:  # pylint:disable=bare-except
            raise YoutubeApiConnectionError(message='Could not fetch page')

    def _get_raw(self, search_string):
        return self._get_page_content(self._make_search_url(search_string))

    def search(self, search_string):
        return self._parser().parse(self._get_raw(search_string))


class VideoSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q='
    _parser = VideoSearchParser


class PlaylistSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?sp=EgIQAw%253D%253D&q='
    _parser = PlaylistSearchParser


class ChannelSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?sp=EgIQAg%253D%253D&q='
    _parser = ChannelSearchParser


class MixedSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?search_query='

    def search(self, search_string):
        page_source = self._get_raw(search_string)
        return {
                'videos': VideoSearchParser().parse(page_source),
                'playlists': PlaylistSearchParser().parse(page_source),
                'channels': ChannelSearchParser().parse(page_source),
        }
