from youtube.baseparser import BaseParser
from youtube.playlistsignature import PlaylistSignature
from youtube.videosignature import VideoSignature

class PlaylistPageParser(BaseParser):
    def get_signature(self, page_html):
        self._initialize_parser(repr(page_html))
        return PlaylistSignature(self._extract_playlist_id(),
                                 self._extract_playlist_name(),
                                 self._extract_playlist_length(),
                                 self._extract_playlist_author(),
                                 self._extract_playlist_thumbnail(),
                                 self._extract_playlist_first_video_id())

    def _extract_playlist_id(self):
        return self._html_parser.select('#pl-header')[0]['data-full-list-id']

    def _extract_playlist_name(self):
        return self._html_parser.select('.pl-header-title')[0].string.strip('\n \\n')

    def _extract_playlist_length(self):
        return str(self._html_parser.select('.pl-header-details li')[1].string).split(' ')[0]

    def _extract_playlist_author(self):
        return self._html_parser.select('.pl-header-details li a')[0]['href'].split('/')[2]

    def _extract_playlist_thumbnail(self):
        return 'https:' + self._html_parser.select('.pl-header-thumb img')[0]['src']

    def _extract_playlist_first_video_id(self):  # pylint:disable=invalid-name
        link = self._html_parser.select('.pl-header-thumb a')[0]['href']
        return link.replace('?v=', ' ').replace('&list', ' ').split(' ')[1]

    def get_videos(self, page_html):
        return [self._parse_single_video(video) for video in self._extract_results(page_html, 'pl-video', 'tr')]

    def _parse_single_video(self, video):
        self._initialize_parser(repr(video))
        return VideoSignature(self._extract_id(),
                              self._extract_title(),
                              self._extract_author(),
                              self._extract_views(),
                              self._extract_length())

    def _extract_length(self):
        return str(self._find_by_class('div', 'timestamp').span.string)

    def _extract_title(self):
        return self._html_parser.tr['data-title']

    def _extract_id(self):
        return self._html_parser.tr['data-video-id']

    def _extract_author(self):
        return self._html_parser.select('.pl-video-owner a')[0]['href'].split('/')[2]

    def _extract_views(self):  # views amount data is not present on the page
        return 'NOTSET'
