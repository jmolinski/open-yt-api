import unittest
from youtube.api import YoutubeApi
from youtube.signatures import VideoSignature
from youtube.errors import YoutubeInvalidIdError
from youtube.errors import YoutubeApiConnectionError
from test_tools import FakeFetcher, read_in_file, ExceptionRaisingFetcher


class YoutubeApiGetPlaylistTest(unittest.TestCase):
    def test_api_get_playlist(self):
        html_code = read_in_file('tests/htmls/playlist_sample_source.txt')
        playlist = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).get_playlist(
                                        'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.playlist_id,
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.name,
                         'Lana Del Rey - All songs playlist')
        self.assertEqual(playlist.author, 'juluatanaya')
        self.assertEqual(int(playlist.length), 118)
        self.assertEqual(playlist.url,
                         'https://www.youtube.com/playlist?list=' +
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.thumbnail,
                         'https://i.ytimg.com/vi/cE6wxDqdOV0/mqdefault.jpg')
        video = playlist.videos[0]
        self.assertEqual(video.video_id, 'nVjsGKrE6E8')
        self.assertEqual(video.title, 'Lana Del Rey - Summertime Sadness')
        self.assertEqual(video.author, 'LanaDelRey')
        self.assertTrue(video.length, '4:43')
        for video in playlist.videos:
            self.assertIsInstance(video, VideoSignature)

    def test_real_get_playlist(self):
        playlist = YoutubeApi(nocache=True).get_playlist('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.playlist_id,
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(playlist.name,
                         'Lana Del Rey - All songs playlist')
        self.assertEqual(playlist.author, 'juluatanaya')
        self.assertTrue(int(playlist.length) >= 105)
        self.assertEqual(playlist.url,
                         'https://www.youtube.com/playlist?list=' +
                         'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        for video in playlist.videos:
            self.assertIsInstance(video, VideoSignature)

    def test_youtubeplaylist_constructor(self):
        html_code = read_in_file('tests/htmls/playlist_sample_source.txt')
        playlist = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).get_playlist('PL        ')
        self.assertTrue(playlist is not None)

    def test_real_get_video_invalid_id(self):
        self.assertRaises(YoutubeInvalidIdError,
                          lambda: YoutubeApi(nocache=True).get_playlist('hdsvhbdhdsvhhdsv'))

    def test_as_dict(self):
        def test_api_get_playlist(self):
            html_code = read_in_file('tests/htmls/playlist_sample_source.txt')
            playlist = YoutubeApi(http_fetcher=FakeFetcher(html_code), nocache=True).get_playlist(
                                            'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')

            keys_playlist = ['videos', 'id', 'name', 'author', 'length', 'url', 'thumbnail']
            self.assertTrue(all(x in playlist.as_dict() for x in keys_playlist))
            keys_video = ['id', 'title', 'author', 'length', 'url', 'thumbnail', 'views']
            for video in playlist.as_dict()['videos']:
                self.assertTrue(all(x in video for x in keys_video))
