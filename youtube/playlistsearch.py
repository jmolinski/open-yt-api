from youtube.search import BaseSearch
from youtube.playlistsearchparser import PlaylistSearchParser

class PlaylistSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?sp=EgIQAw%253D%253D&q='

    def search(self, search_string):
        return PlaylistSearchParser().parse(self._get_page_content(self._make_search_url(search_string)))
