from youtube.videopageparser import VideoPageParser
from youtube.baseelement import BaseElement

class YoutubeVideo(BaseElement):
    _next_video = None
    _related_videos = None

    def _make_url(self, video_id):
        return 'https://www.youtube.com/watch?v=' + video_id

    def _is_valid_id(self, video_id):
        return len(video_id) == 11

    def _get_default_parser(self):
        return VideoPageParser()

    def _build_page(self, page_html):
        self._next_video = self._parser.get_next_video(page_html)
        self._related_videos = self._parser.parse_related_videos(page_html)

    @property
    def url(self):
        return self._signature.url

    @property
    def length(self):
        return self._signature.length

    @property
    def length_in_seconds(self):
        time = self._signature.length.split(":")[::-1]
        [secs, mins, hrs, *__] = time + ['0', '0', '0'] # noqa
        hrs, mins, secs = int(hrs), int(mins), int(secs)
        return 3600 * hrs + 60 * mins + secs

    @property
    def author(self):
        return self._signature.author

    @property
    def title(self):
        return self._signature.title

    @property
    def video_id(self):
        return self._signature.video_id

    @property
    def views(self):
        return self._signature.views

    @property
    def next_video(self):
        return self._next_video

    @property
    def related_videos(self):
        return self._related_videos[:]

    @property
    def thumbnail(self):
        return self._signature.thumbnail

    def as_dict(self):
        return {
            'id': self.video_id,
            'title': self.title,
            'author': self.author,
            'views': self.views,
            'length': self.length,
            'length_in_seconds': self.length_in_seconds,
            'url': self.url,
            'thumbnail': self.thumbnail,
            'next_video': self.next_video.as_dict(),
            'related_videos': [video.as_dict() for video in self.related_videos]
        }
