import unittest
from youtube.signatures import ChannelSignature

class YoutubeChannelSignatureTest(unittest.TestCase):
    def test_channelsignature_constructor(self):
        self.assertRaises(Exception, lambda: ChannelSignature(' ', 55, ' ', ' ', 55))
        ChannelSignature(' ', ' ', 0, 0, ' ')

    def test_get_channel_url(self):
        signature = ChannelSignature('UCAw23LRxypuNn0ilUu1o1Cw', ' ', 0, 0, ' ')
        self.assertEqual(signature.url, 'https://www.youtube.com/channel/UCAw23LRxypuNn0ilUu1o1Cw')

    def test_getters(self):
        signature = ChannelSignature('UCAw23LRxypuNn0ilUu1o1Cw', 'name', 11, 3555, 'thumb')
        self.assertEqual(signature.channel_id, 'UCAw23LRxypuNn0ilUu1o1Cw')
        self.assertEqual(signature.videos_amount, 11)
        self.assertEqual(signature.subscriptions, 3555)
        self.assertEqual(signature.thumbnail, 'thumb')
        self.assertEqual(signature.name, 'name')

    def test_as_dict(self):
        signature = ChannelSignature('UCAw23LRxypuNn0ilUu1o1Cw', 'name', 11, 3555, 'thumb')
        self.assertEqual(signature.as_dict(), {
                'id': 'UCAw23LRxypuNn0ilUu1o1Cw',
                'name': 'name',
                'videos_amount': 11,
                'subscriptions': 3555,
                'url': 'https://www.youtube.com/channel/UCAw23LRxypuNn0ilUu1o1Cw',
                'thumbnail': 'thumb'
        })
