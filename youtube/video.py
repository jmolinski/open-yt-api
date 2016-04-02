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

    def get_url(self):
        return self._signature.get_url()

    def get_length(self):
        return self._signature.get_length()

    def get_length_in_seconds(self):
        time = self._signature.get_length().split(":")[::-1]
        [secs, mins, hrs, *__] = time + ['0', '0', '0'] # noqa
        hrs, mins, secs = int(hrs), int(mins), int(secs)
        return 3600 * hrs + 60 * mins + secs

    def get_author(self):
        return self._signature.get_author()

    def get_title(self):
        return self._signature.get_title()

    def get_id(self):
        return self._signature.get_id()

    def get_views(self):
        return self._signature.get_views()

    def get_next_video(self):
        return self._next_video

    def get_related_videos(self):
        return self._related_videos[:]

    def get_thumbnail_url(self):
        return self._signature.get_thumbnail_url()
