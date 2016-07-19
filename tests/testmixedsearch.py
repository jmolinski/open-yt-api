import unittest

from test_tools import ExceptionRaisingFetcher, FakeFetcher, read_in_file
from youtube.api import YoutubeApi
from youtube.errors import YoutubeApiConnectionError


class YoutubeApiVideoSearchTest(unittest.TestCase):
    def test_api_search_no_results(self):
        html_code = read_in_file('tests/htmls/search_no_results.txt')
        found_items = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).search('')
        length = len(found_items['videos'] + found_items['playlists'] + found_items['channels'])
        self.assertEqual(length, 0)

    def test_api_search(self):
        html_code = read_in_file('tests/htmls/search_mixed_17_results.txt')
        found_items = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).search('')
        length = len(found_items['videos'] + found_items['playlists'] + found_items['channels'])
        self.assertEqual(length, 20)
        self.assertEqual(len(found_items['videos']), 17)
        self.assertEqual(len(found_items['playlists']), 1)
        self.assertEqual(len(found_items['channels']), 2)

    def test_real_search(self):
        found_items = YoutubeApi(nocache=True).search('lana del rey')
        length = len(found_items['videos'] + found_items['playlists'] + found_items['channels'])
        self.assertEqual(length, 20)
        self.assertTrue(len(found_items['videos']) >= 15)
        self.assertTrue(len(found_items['playlists']) >= 1)
        self.assertTrue(len(found_items['channels']) >= 1)

    def test_real_search_no_results(self):
        found_results = YoutubeApi(nocache=True).search('dbg76i6bncw6ogefnxbwegfbnl')
        length = len(found_results['videos'] + found_results['playlists'] + found_results['channels'])
        self.assertEqual(length, 0)

    def test_real_search_multiple_results(self):
        found_results = YoutubeApi(nocache=True).search('pink floyd')
        length = len(found_results['videos'] + found_results['playlists'] + found_results['channels'])
        self.assertTrue(length >= 20)

    def test_real_search_invalid_url(self):
        with self.assertRaises(YoutubeApiConnectionError):
            YoutubeApi(http_fetcher=ExceptionRaisingFetcher(), nocache=True).search('')
