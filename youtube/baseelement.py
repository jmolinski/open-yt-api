from youtube.errors import YoutubeApiConnectionError, YoutubeInvalidIdError

class BaseElement():
    _http_fetcher = None
    _signature = None
    _parser = None

    def __init__(self, http_fetcher, element_id, *, parser=None):
        self._http_fetcher = http_fetcher
        if not self._is_valid_id(element_id):
            raise YoutubeInvalidIdError()
        self._parser = parser or self._get_default_parser()
        page_html = self._get_page_content(self._make_url(element_id))
        self._signature = self._parser.get_signature(page_html)
        self._build_page(page_html)

    def _get_page_content(self, url):
        try:
            return self._http_fetcher.fetch_page(url)
        except:  # pylint:disable=bare-except
            raise YoutubeApiConnectionError(message='Could not fetch page')
