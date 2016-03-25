from youtube.baseparser import BaseParser
from youtube.channelsignature import ChannelSignature
from youtube.videosignature import VideoSignature

class ChannelPageParser(BaseParser):
    def get_videos(self, page_html):
        # TODO video search - same parser? check it
        return [self._parse_video(video) for video in self._extract_results(page_html, 'yt-lockup-video', 'div')]

    def _parse_video(self, video):
        self._initialize_parser(repr(video))
        return VideoSignature(self._extract_id(),
                              self._extract_title(),
                              self._extract_author(),
                              self._extract_views(),
                              self._extract_length())

    def get_signature(self, page_html):
        self._initialize_parser(repr(page_html))
        # return ChannelSignature()
