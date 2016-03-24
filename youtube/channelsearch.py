from youtube.search import BaseSearch
from youtube.channelsearchparser import ChannelSearchParser

class ChannelSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?sp=EgIQAg%253D%253D&q='

    def search(self, search_string):
        return ChannelSearchParser().parse(self._get_page_content(self._make_search_url(search_string)))
