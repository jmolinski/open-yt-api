import unittest
from youtube.api import YoutubeApi
from youtube.videosignature import VideoSignature
from test_tools import FakeFetcher, read_in_file, ExceptionRaisingFetcher

class YoutubeApiGetChannelTest(unittest.TestCase):
    def test_api_get_channel_signature(self):
        html_code = read_in_file('tests/htmls/channel_about_page.txt')
        html_code2 = read_in_file('tests/htmls/channel_videos_page.txt')
        channel = YoutubeApi(http_fetcher=FakeFetcher(html_code, html_code2), nocache=True).get_channel('LanaDelReyVEVO')

        self.assertEqual(channel.channel_id, 'LanaDelReyVEVO')
        self.assertEqual(channel.url, 'https://www.youtube.com/user/LanaDelReyVEVO')
        self.assertEqual(channel.name, 'LanaDelReyVEVO')
        self.assertEqual(channel.videos_amount, 0)
        self.assertEqual(channel.subscriptions, 3983841)
        self.assertEqual(channel.thumbnail,
                         'https://yt3.ggpht.com/-JXK6ocQ08J8/AAAAAAAAAAI/' +
                         'AAAAAAAAAAA/aGPAhXfQpMw/s100-c-k-no/photo.jpg')

    def test_api_get_channel_videos(self):
        html_code = read_in_file('tests/htmls/channel_about_page.txt')
        html_code2 = read_in_file('tests/htmls/channel_videos_page.txt')
        channel = YoutubeApi(http_fetcher=FakeFetcher(html_code, html_code2), nocache=True).get_channel('LanaDelReyVEVO')
        signature = VideoSignature('JRWox-i6aAk', 'Lana Del Rey - Blue Jeans',
                                    'LanaDelReyVEVO', 149473022, '4:21')
        self.assertTrue(signature in channel.uploaded_videos)
        for video in channel.uploaded_videos:
            self.assertIsInstance(video, VideoSignature)

    def test_real_get_channel_about(self):
        channel = YoutubeApi(nocache=True).get_channel('LanaDelReyVEVO')
        self.assertEqual(channel.channel_id, 'LanaDelReyVEVO')
        self.assertEqual(channel.url, 'https://www.youtube.com/user/LanaDelReyVEVO')
        self.assertEqual(channel.name, 'LanaDelReyVEVO')
        self.assertTrue(int(channel.subscriptions) >= 3983841)

    def test_real_get_channel_videos(self):
        channel = YoutubeApi(nocache=True).get_channel('LanaDelReyVEVO')
        blue_jeans = [x for x in channel.uploaded_videos if x.video_id == 'JRWox-i6aAk']
        self.assertEqual(len(blue_jeans), 1)
        blue_jeans = blue_jeans[0]
        self.assertEqual(blue_jeans.video_id, 'JRWox-i6aAk')
        self.assertEqual(blue_jeans.title, 'Lana Del Rey - Blue Jeans')
        self.assertEqual(blue_jeans.author, 'LanaDelReyVEVO')
        self.assertEqual(blue_jeans.length, '4:21')

        for video in channel.uploaded_videos:
            self.assertIsInstance(video, VideoSignature)

    def test_youtubechannel_constructor(self):
        html_code = read_in_file('tests/htmls/channel_about_page.txt')
        html_code2 = read_in_file('tests/htmls/channel_videos_page.txt')
        channel = YoutubeApi(http_fetcher=FakeFetcher(html_code, html_code2), nocache=True).get_channel('           ')
        self.assertTrue(channel is not None)
