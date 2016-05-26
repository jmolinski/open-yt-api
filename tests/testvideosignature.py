import unittest
from youtube.videosignature import VideoSignature

class YoutubeVideoSignatureTest(unittest.TestCase):
    def test_videosignature_constructor(self):
        self.assertRaises(Exception, lambda: VideoSignature(' ', 55, ' ', ' ', 55))
        VideoSignature(' ', ' ', ' ', ' ', ' ')

    def test_get_video_url(self):
        signature = VideoSignature('TdrL3QxjyVw', ' ', ' ', ' ', ' ')
        self.assertEqual(signature.url, 'https://www.youtube.com/watch?v=TdrL3QxjyVw')
