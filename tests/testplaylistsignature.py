import unittest
from youtube.playlistsignature import PlaylistSignature

class YoutubePlaylistSignatureTest(unittest.TestCase):
    def test_playlistsignature_constructor(self):
        self.assertRaises(Exception, lambda: PlaylistSignature(' ', 55, ' ', ' ', 55, ' '))
        PlaylistSignature(' ', ' ', ' ', ' ', ' ', ' ')

    def test_get_playlist_url(self):
        signature = PlaylistSignature('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi', ' ', ' ', ' ', ' ', ' ')
        self.assertEqual(signature.url,
                                    'https://www.youtube.com/playlist?' +
                                    'list=PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')

    def test_get_first_video_url(self):
        signature = PlaylistSignature('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi',
                                    ' ', ' ', ' ', ' ', 'nVjsGKrE6E8')
        self.assertEqual(signature.first_video_url,
                        'https://www.youtube.com/watch?v=' +
                        'nVjsGKrE6E8&list=PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')

    def test_getters(self):
        signature = PlaylistSignature('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi',
                                'name', '11', 'author', 'thumb', 'nVjsGKrE6E8')
        self.assertEqual(signature.playlist_id,
                                        'PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        self.assertEqual(signature.length, '11')
        self.assertEqual(signature.author, 'author')
        self.assertEqual(signature.thumbnail, 'thumb')
        self.assertEqual(signature.name, 'name')
        self.assertEqual(signature.first_video_id, 'nVjsGKrE6E8')
