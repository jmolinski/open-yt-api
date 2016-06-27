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

    @property
    def author(self):
        return self._signature.author

    @property
    def name(self):
        return self._signature.name

    @property
    def playlist_id(self):
        return self._signature.playlist_id

    @property
    def length(self):
        return self._signature.length

    @property
    def thumbnail(self):
        return self._signature.thumbnail

    @property
    def url(self):
        return self._signature.url

    @property
    def videos(self):
        return self._videos[:]

    def as_dict(self):
        return {
            'id': self.playlist_id,
            'name': self.name,
            'author': self.author,
            'length': self.length,
            'url': self.url,
            'thumbnail': self.thumbnail,
            'videos': [video.as_dict() for video in self.videos]
        }
