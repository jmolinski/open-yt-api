from youtube.http_fetcher import CouldntFetchContentError

class FakeFetcher():
    def __init__(self, page_source):
        self._page_source = page_source

    def fetch_page(self, url):
        return self._page_source

class ExceptionRaisingFetcher():
    def fetch_page(self, url):
        raise CouldntFetchContentError()

class FakeSignature():
    def get_url(self):
        return 'https://www.' # invalid url

def read_in_file(filepath):
    f = open(filepath, 'r')
    content = f.read()
    f.close()
    return content
