from youtube.search import BaseSearch
from youtube.videosearchparser import VideoSearchParser

class VideoSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q='

    def search(self, search_string):
        return VideoSearchParser().parse(
            self._get_page_content(self._make_search_url(search_string))
        )
