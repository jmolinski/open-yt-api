import unittest
from youtube.api import YoutubeApi
from youtube.videosignature import VideoSignature
from youtube.errors import YoutubeInvalidIdError
from youtube.errors import YoutubeApiConnectionError
from test_tools import FakeFetcher, read_in_file, ExceptionRaisingFetcher


class YoutubeApiGetVideoTest(unittest.TestCase):
    def test_api_get_video(self):
        html_code = read_in_file('tests/htmls/video_sample_source.txt')
        video = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).get_video('nVjsGKrE6E8')
        self.assertEqual(video.video_id, 'nVjsGKrE6E8')
        self.assertEqual(video.url, 'https://www.youtube.com/watch?v=nVjsGKrE6E8')
        self.assertEqual(video.title, 'Lana Del Rey - Summertime Sadness')
        self.assertEqual(video.author, 'UCqk3CdGN_j8IR9z4uBbVPSg')
        self.assertEqual(video.views, 247990936)
        self.assertTrue(video.length, '4:43')
        self.assertEqual(video.length_in_seconds, 283)
        self.assertIsInstance(video.next_video, VideoSignature)
        self.assertEqual(len(video.related_videos), 17)
        self.assertEqual(video.thumbnail,
                         "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(video.video_id))
        for video in video.related_videos:
            self.assertIsInstance(video, VideoSignature)

    def test_real_get_video(self):
        video = YoutubeApi(nocache=True).get_video('nVjsGKrE6E8')
        self.assertEqual(video.video_id, 'nVjsGKrE6E8')
        self.assertEqual(video.title, 'Lana Del Rey - Summertime Sadness')
        self.assertEqual(video.author, 'UCqk3CdGN_j8IR9z4uBbVPSg')
        self.assertTrue(int(video.views) >= 49740141)
        self.assertEqual(video.length, '4:43')
        self.assertEqual(video.length_in_seconds, 283)
        self.assertIsInstance(video.next_video, VideoSignature)
        self.assertTrue(len(video.related_videos) > 12)
        for video in video.related_videos:
            self.assertIsInstance(video, VideoSignature)

    def test_youtubevideo_constructor(self):
        html_code = read_in_file('tests/htmls/video_sample_source.txt')
        video = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).get_video('           ')
        self.assertTrue(video is not None)

    def test_real_get_video_invalid_id(self):
        self.assertRaises(YoutubeInvalidIdError,
                          lambda: YoutubeApi(nocache=True).get_video('hdsvhbdhdsvhhdsv'))

    def test_real_get_video_invalid_fetcher(self):
        self.assertRaises(YoutubeApiConnectionError,
                          lambda: YoutubeApi(
                                    http_fetcher=ExceptionRaisingFetcher(),
                                    nocache=True).get_video('nVjsGKrE6E8'))
