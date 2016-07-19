from youtube.http_fetcher import CouldntFetchContentError


class FakeFetcher():
    def __init__(self, page_source, page_source2=None):
        self._page_source = [page_source, page_source if page_source2 is None else page_source2]
        self._index = 1

    def fetch_page(self, url):
        self._index += 1
        return self._page_source[self._index % 2]


class ExceptionRaisingFetcher():
    def fetch_page(self, url):
        raise CouldntFetchContentError()


class FakeSignature():
    def get_url(self):
        return 'https://www.'  # invalid url


def read_in_file(filepath):
    f = open(filepath, 'r')
    content = f.read()
    f.close()
    return content
