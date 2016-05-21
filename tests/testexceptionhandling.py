import unittest
from youtube.api import YoutubeApi
from test_tools import FakeFetcher
from youtube.errors import YoutubeApiRandomException


class YoutubeApiRandomExceptionHandling(unittest.TestCase):
    def test_api_random_exceptions(self):
        with self.assertRaises(YoutubeApiRandomException):
            video = YoutubeApi(FakeFetcher('damaged html'), True).get_video('nVjsGKrE6E8')
