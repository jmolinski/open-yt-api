import unittest
from youtube.api import YoutubeApi
from youtube.videosignature import VideoSignature
from youtube.channelsignature import ChannelSignature
from youtube.playlistsignature import PlaylistSignature
from youtube.errors import YoutubeApiConnectionError
from test_tools import FakeFetcher, ExceptionRaisingFetcher, read_in_file

class YoutubeApiVideoSearchTest(unittest.TestCase):
    def test_api_search_no_results(self):
        html_code = read_in_file('tests/htmls/search_no_results.txt')
        found_items = YoutubeApi(FakeFetcher(html_code), True).search('')
        self.assertEqual(len(found_items), 0)

    def test_api_search(self):
        html_code = read_in_file('tests/htmls/search_mixed_17_results.txt')
        found_items = YoutubeApi(FakeFetcher(html_code), True).search('')
        self.assertEqual(len(found_items), 20)
        videos = [item for item in found_items if isinstance(item, VideoSignature)]
        playlists = [item for item in found_items if isinstance(item, PlaylistSignature)]
        channels = [item for item in found_items if isinstance(item, ChannelSignature)]
        self.assertEqual(len(videos), 17)
        self.assertEqual(len(playlists), 1)
        self.assertEqual(len(channels), 2)

    def test_real_search(self):
        found_items = YoutubeApi(nocache=True).search('lana del rey')
        self.assertEqual(len(found_items), 20)
        videos = [item for item in found_items if isinstance(item, VideoSignature)]
        playlists = [item for item in found_items if isinstance(item, PlaylistSignature)]
        channels = [item for item in found_items if isinstance(item, ChannelSignature)]
        self.assertTrue(len(videos) >= 15)
        self.assertTrue(len(playlists) >= 1)
        self.assertTrue(len(channels) >= 1)

    def test_real_search_no_results(self):
        found_results = YoutubeApi(nocache=True).search('dbg76i6bncw6ogefnxbwegfbnl')
        self.assertEqual(len(found_results), 0)

    def test_real_search_multiple_results(self):
        found_results = YoutubeApi(nocache=True).search('pink floyd')
        self.assertEqual(len(found_results), 20)

    def test_real_search_invalid_url(self):
        with self.assertRaises(YoutubeApiConnectionError):
            YoutubeApi(ExceptionRaisingFetcher(), True).search('')
