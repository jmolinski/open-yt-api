import unittest
from youtube.api import YoutubeApi
from youtube.videosignature import VideoSignature
from youtube.errors import YoutubeApiConnectionError
from test_tools import FakeFetcher, ExceptionRaisingFetcher, read_in_file

class YoutubeApiVideoSearchTest(unittest.TestCase):
    def test_search_no_results(self):
        html_code = read_in_file('tests/htmls/search_no_results.txt')
        found_videos = YoutubeApi(FakeFetcher(html_code), True).search_videos('')
        self.assertEqual(len(found_videos), 0)

    def test_search_17_results(self):
        html_code = read_in_file('tests/htmls/search_mixed_17_results.txt')
        found_videos = YoutubeApi(FakeFetcher(html_code), True).search_videos('')
        self.assertEqual(len(found_videos), 17)
        for video in found_videos:
            self.assertIsInstance(video, VideoSignature)
        signature = VideoSignature('JRWox-i6aAk', 'Lana Del Rey - Blue Jeans',
                                    'LanaDelReyVEVO', '146576399', '4:21')
        self.assertTrue(signature in found_videos)
        invalid_signature = VideoSignature(' ', ' ', ' ', ' ', ' ')
        self.assertTrue(invalid_signature not in found_videos)
        self.assertEqual(found_videos[0].get_thumbnail_url(),
                         "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(
                          found_videos[0].get_id()))

    def test_search_only_videos_20_results(self):
        html_code = read_in_file('tests/htmls/search_videos_20_results.txt')
        found_videos = YoutubeApi(FakeFetcher(html_code), True).search_videos('')
        self.assertEqual(len(found_videos), 20)
        for video in found_videos:
            self.assertIsInstance(video, VideoSignature)

    def test_real_search_no_results(self):
        found_videos = YoutubeApi(nocache=True).search_videos('dbg76i6bncw6ogefnxbwegfbnl')
        self.assertEqual(len(found_videos), 0)

    def test_real_search_multiple_results(self):
        found_videos = YoutubeApi(nocache=True).search_videos('pink floyd')
        self.assertTrue(len(found_videos) > 15)
        for video in found_videos:
            self.assertIsInstance(video, VideoSignature)

    def test_real_search_invalid_url(self):
        self.assertRaises(
                YoutubeApiConnectionError,
                lambda: YoutubeApi(ExceptionRaisingFetcher(), True).search_videos(''))
