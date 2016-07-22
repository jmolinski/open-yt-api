import unittest

from youtube.http_fetcher import CouldntFetchContentError, DefaultFetcher


class HttpFetcherTest(unittest.TestCase):
    _fetcher = DefaultFetcher()

    def test_real_fetch_page(self):
        url = 'https://www.youtube.com/watch?v=vksfnZaZ0A4'
        response = self._fetcher.fetch_page(url)
        self.assertTrue(type(response) is str)
        self.assertTrue(len(response) > 5000)

    def test_real_invalid_url(self):
        url = 'https://www.'
        self.assertRaises(CouldntFetchContentError,
                          lambda: self._fetcher.fetch_page(url))
