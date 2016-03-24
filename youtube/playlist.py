from youtube.baseelement import BaseElement
from youtube.playlistpageparser import PlaylistPageParser

class YoutubePlaylist(BaseElement):
    _videos = None

    def _build_page(self, page_html):
        self._videos = self._parser.get_videos(page_html)

    def _make_url(self, playlist_id):
        return 'https://www.youtube.com/playlist?list=' + playlist_id

    def _is_valid_id(self, playlist_id):
        return playlist_id[:2] == 'PL'

    def _get_default_parser(self):
        return PlaylistPageParser()

    def get_author(self):
        return self._signature.get_author()

    def get_name(self):
        return self._signature.get_name()

    def get_id(self):
        return self._signature.get_id()

    def get_length(self):
        return self._signature.get_length()

    def get_thumbnail_url(self):
        return self._signature.get_thumbnail_url()

    def get_url(self):
        return self._signature.get_url()

    def get_video(self, index):
        return self._videos[index]

    def get_videos(self):
        return self._videos[:]
