from youtube.baseparser import BaseSearchParser
from youtube.playlistsignature import PlaylistSignature

class PlaylistSearchParser(BaseSearchParser):
    _tile_class_name = 'yt-lockup-playlist'

    def _parse_single_result(self, search_result):
        self._initialize_parser(repr(search_result))
        return PlaylistSignature(self._extract_id(),
                                 self._extract_name(),
                                 self._extract_playlist_length(),
                                 self._extract_author(),
                                 self._extract_thumbnail_url(),
                                 self._extract_first_video_id())

    def _extract_id(self):
        return self._find_by_class('li', 'overflow-menu-choice')['data-list-id']

    def _extract_name(self):
        return str(self._find_by_class('a', 'yt-uix-tile-link').string)

    def _extract_playlist_length(self):
        return str(self._find_by_class('span', 'formatted-video-count-label').b.string)

    def _extract_thumbnail_url(self):
        return 'https:' + self._find_by_class('span', 'yt-thumb-simple').img['src']

    def _extract_author(self):
        return str(self._find_by_class('a', 'g-hovercard').string)

    def _extract_first_video_id(self):
        link = self._find_by_class('ol', 'yt-lockup-playlist-items').li.a['href']
        return link.replace('&list=', ' ').replace('tch?v=', ' ').split(' ')[1]
