import unittest

from youtube.signatures import VideoSignature


class YoutubeVideoSignatureTest(unittest.TestCase):
    def test_videosignature_constructor(self):
        self.assertRaises(Exception, lambda: VideoSignature(' ', 55, ' ', ' ', 55))
        VideoSignature(' ', ' ', ' ', 0, ' ')

    def test_get_video_url(self):
        signature = VideoSignature('TdrL3QxjyVw', ' ', ' ', 0, ' ')
        self.assertEqual(signature.url, 'https://www.youtube.com/watch?v=TdrL3QxjyVw')

    def test_as_dict(self):
        signature = VideoSignature('TdrL3QxjyVw', 'a', 'b', 0, 'c')
        self.assertEqual(signature.as_dict(), {
                'id': 'TdrL3QxjyVw',
                'title': 'a',
                'author': 'b',
                'views': 0,
                'length': 'c',
                'url': 'https://www.youtube.com/watch?v=TdrL3QxjyVw',
                'thumbnail': 'https://i.ytimg.com/vi/TdrL3QxjyVw/mqdefault.jpg'
        })
