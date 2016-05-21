import unittest
from youtube.api import YoutubeApi
from youtube.channelsignature import ChannelSignature
from test_tools import FakeFetcher, read_in_file

class YoutubeApiChannelSearchTest(unittest.TestCase):
    def test_search_no_results(self):
        html_code = read_in_file('tests/htmls/search_no_results.txt')
        found_channels = YoutubeApi(FakeFetcher(html_code), True).search_channels('')
        self.assertEqual(len(found_channels), 0)

    def test_search_only_channels_20_results(self):
        html_code = read_in_file('tests/htmls/search_channels_20_results.txt')
        found_channels = YoutubeApi(FakeFetcher(html_code), True).search_channels('')
        self.assertEqual(len(found_channels), 20)
        for channel in found_channels:
            self.assertIsInstance(channel, ChannelSignature)

        signature = ChannelSignature('UC3N5y6UWKJaKqoU2b_0MfTQ',
                                    'LanaDelReyVEVO', '31', '3 947 232',
                    'https://yt3.ggpht.com/-JXK6ocQ08J8/AAAAAAAAAAI/' +
                    'AAAAAAAAAAA/aGPAhXfQpMw/s176-c-k-no/photo.jpg')

        self.assertTrue(signature in found_channels)
        invalid_signature = ChannelSignature(' ', ' ', ' ', ' ', ' ')
        self.assertTrue(invalid_signature not in found_channels)

    def test_real_search_no_results(self):
        found_channels = YoutubeApi(nocache=True).search_channels('dbg76i6bncw6ogefnxbwegf')
        self.assertEqual(len(found_channels), 0)

    def test_real_search_multiple_results(self):
        found_channels = YoutubeApi(nocache=True).search_channels('lana del rey')
        self.assertEqual(len(found_channels), 20)
        for channel in found_channels:
            self.assertIsInstance(channel, ChannelSignature)
