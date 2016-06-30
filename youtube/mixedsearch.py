from youtube.search import BaseSearch
from youtube.playlistsearchparser import PlaylistSearchParser
from youtube.channelsearchparser import ChannelSearchParser
from youtube.videosearchparser import VideoSearchParser

class MixedSearch(BaseSearch):
    _base_search_url = 'https://www.youtube.com/results?search_query='

    def search(self, search_string):
        page_source = self._get_page_content(self._make_search_url(search_string))
        return {
                'videos': VideoSearchParser().parse(page_source),
                'playlists': PlaylistSearchParser().parse(page_source),
                'channels': ChannelSearchParser().parse(page_source),
        }
