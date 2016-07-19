import unittest
from youtube.api import YoutubeApi
from youtube.signatures import PlaylistSignature
from test_tools import FakeFetcher, read_in_file

class YoutubeApiPlaylistSearchTest(unittest.TestCase):
    def test_search_no_results(self):
        html_code = read_in_file('tests/htmls/search_no_results.txt')
        found_results = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).search_playlists('')
        self.assertEqual(len(found_results), 0)

    def test_search_only_playlists_20_results(self):
        html_code = read_in_file('tests/htmls/search_playlists_20_results.txt')
        found_playlists = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).search_playlists('')
        self.assertEqual(len(found_playlists), 20)
        for playlist in found_playlists:
            self.assertIsInstance(playlist, PlaylistSignature)

        signature = PlaylistSignature('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi',
                                      'Lana Del Rey - All songs playlist',
                                      119, 'juluatanaya',
                            'https://i.ytimg.com/vi/nVjsGKrE6E8/mqdefault.jpg',
                                      'nVjsGKrE6E8')

        self.assertTrue(signature in found_playlists)
        invalid_signature = PlaylistSignature(' ', ' ', 0, ' ', ' ', ' ')
        self.assertTrue(invalid_signature not in found_playlists)

    def test_real_search_no_results(self):
        found_playlists = YoutubeApi(nocache=True).search_playlists('dbg76i6bncw6ogefnxbwe')
        self.assertEqual(len(found_playlists), 0)

    def test_real_search_multiple_results(self):
        found_playlists = YoutubeApi(nocache=True).search_playlists('lana del rey')
        self.assertEqual(len(found_playlists), 20)
        for playlist in found_playlists:
            self.assertIsInstance(playlist, PlaylistSignature)
