import unittest
from source.channelsignature import ChannelSignature

class YoutubeChannelSignatureTest(unittest.TestCase):
    def test_channelsignature_constructor(self):
        self.assertRaises(Exception,
                          lambda: ChannelSignature(' ', 55, ' ', ' ', 55))
        self.assertRaises(Exception,
                          lambda: ChannelSignature(' ', ' ', ' ', ' ', ''))
        ChannelSignature(' ', ' ', ' ', ' ', ' ')

    def test_get_channel_url(self):
        signature = ChannelSignature('UCAw23LRxypuNn0ilUu1o1Cw',
                                    ' ', ' ', ' ', ' ')
        self.assertEqual(signature.get_url(),
                    'https://www.youtube.com/channel/UCAw23LRxypuNn0ilUu1o1Cw')

    def test_getters(self):
        signature = ChannelSignature('UCAw23LRxypuNn0ilUu1o1Cw',
                                    'name', '11', '3555', 'thumb')
        self.assertEqual(signature.get_id(), 'UCAw23LRxypuNn0ilUu1o1Cw')
        self.assertEqual(signature.get_videos_amount(), '11')
        self.assertEqual(signature.get_subscriptions(), '3555')
        self.assertEqual(signature.get_thumbnail_url(), 'thumb')
        self.assertEqual(signature.get_name(), 'name')
