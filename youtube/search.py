import urllib.parse
from youtube.errors import YoutubeApiConnectionError

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
            raise YoutubeApiConnectionError('Could not fetch page')
