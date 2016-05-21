import unittest
from youtube.api import YoutubeApi
from youtube.videosignature import VideoSignature
from youtube.errors import YoutubeInvalidIdError
from youtube.errors import YoutubeApiConnectionError
from test_tools import FakeFetcher, read_in_file, ExceptionRaisingFetcher


class YoutubeApiGetPlaylistTest(unittest.TestCase):
    def test_api_get_playlist(self):
        html_code = read_in_file('tests/htmls/playlist_sample_source.txt')
        playlist = YoutubeApi(FakeFetcher(html_code), True).get_playlist(
                                        'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.get_id(),
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.get_name(),
                         'Lana Del Rey - All songs playlist')
        self.assertEqual(playlist.get_author(), 'juluatanaya')
        self.assertEqual(int(playlist.get_length()), 118)
        self.assertEqual(playlist.get_url(),
                         'https://www.youtube.com/playlist?list=' +
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.get_thumbnail_url(),
                         'https://i.ytimg.com/vi/cE6wxDqdOV0/mqdefault.jpg')
        video = playlist.get_video(0)
        self.assertEqual(video.get_id(), 'nVjsGKrE6E8')
        self.assertEqual(video.get_title(), 'Lana Del Rey - Summertime Sadness')
        self.assertEqual(video.get_author(), 'LanaDelRey')
        self.assertTrue(video.get_length(), '4:43')
        for video in playlist.get_videos():
            self.assertIsInstance(video, VideoSignature)

    def test_real_get_playlist(self):
        playlist = YoutubeApi(nocache=True).get_playlist('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.get_id(),
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.get_name(),
                         'Lana Del Rey - All songs playlist')
        self.assertEqual(playlist.get_author(), 'juluatanaya')
        self.assertTrue(int(playlist.get_length()) >= 105)
        self.assertEqual(playlist.get_url(),
                         'https://www.youtube.com/playlist?list=' +
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        for video in playlist.get_videos():
            self.assertIsInstance(video, VideoSignature)

    def test_youtubeplaylist_constructor(self):
        html_code = read_in_file('tests/htmls/playlist_sample_source.txt')
        playlist = YoutubeApi(FakeFetcher(html_code), True).get_playlist('PL        ')
        self.assertTrue(playlist is not None)

    def test_real_get_video_invalid_id(self):
        self.assertRaises(YoutubeInvalidIdError,
                          lambda: YoutubeApi(nocache=True).get_playlist('hdsvhbdhdsvhhdsv'))
