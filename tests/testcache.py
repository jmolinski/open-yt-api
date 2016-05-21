import unittest
from timeit import default_timer as timer
from youtube.api import YoutubeApi

class YoutubeApiTestCache(unittest.TestCase):
    def test_search_cache_time(self):
        api = YoutubeApi()

        # actual http request and parsing
        start = timer()
        videos_a = api.search('Lana')
        videos = api.search('Lana del')
        videos = api.search('Lana del rey')
        time1 = timer() - start

        # get cached version
        start = timer()
        videos_f = api.search('Lana')
        videos = api.search('Lana del')
        videos = api.search('Lana del rey')
        time2 = timer() - start

        # cached should be at least 1000 times faster
        self.assertTrue(time1 > time2 * 1000)

        api.clear_cache()

    def test_search_cache_right_values(self):
        api = YoutubeApi()

        # actual http request and parsing
        videos_a = api.search('Lana')

        # get cached version
        videos_c = api.search('Lana')

        # check if cache stores right values
        self.assertEqual(videos_a, videos_c)

        api.clear_cache()

    def test_clear_cache(self):
        api = YoutubeApi()

        # actual http request and parsing
        start = timer()
        videos = api.search('Lana del rey')
        time1 = timer() - start

        # get cached version
        start = timer()
        videos = api.search('Lana del rey')
        time2 = timer() - start

        # clear cache
        api.clear_cache()

        # actual http request and parsing again
        start = timer()
        videos = api.search('Lana del rey')
        time3 = timer() - start

        self.assertTrue(min(time1, time3) > time2 * 1000)

        api.clear_cache()

    def test_get_object_cache_time(self):
        api = YoutubeApi()

        start = timer()
        video = api.get_video('nVjsGKrE6E8')
        channel = api.get_channel('LanaDelReyVEVO')
        playlist = api.get_playlist('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        time1 = timer() - start

        start = timer()
        video = api.get_video('nVjsGKrE6E8')
        channel = api.get_channel('LanaDelReyVEVO')
        playlist = api.get_playlist('PLLUYFDT7vPkqBZQsTGBpGCjIoePETnOxi')
        time2 = timer() - start

        self.assertTrue(time1 > time2 * 1000)

        api.clear_cache()

    def test_get_object_right_values(self):
        api = YoutubeApi()

        video1 = api.get_video('nVjsGKrE6E8')
        video2 = api.get_video('nVjsGKrE6E8')

        self.assertEqual(video1, video2)

        api.clear_cache()
