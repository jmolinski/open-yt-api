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
        return ChannelSignature(self._extract_id(),
                                self._extract_name(),
                                self._extract_videos_amount(),
                                self._extract_subscriptions(),
                                self._extract_thumbnail_url())

    def _extract_id(self):
        return self._html_parser.select('.qualified-channel-title-text a')[0]['href'].split('/')[2]

    def _extract_name(self):
        return str(self._html_parser.select('.qualified-channel-title-text a')[0].string)

    def _extract_videos_amount(self):
        return 'NOTSET'  # data can't be extracted

    def _extract_thumbnail_url(self):
        return self._html_parser.select('.channel-header-profile-image')[0]['src']

    def _extract_subscriptions(self):
        return self._remove_non_breaking_spaces(str(self._html_parser.select('.about-stats span b')[0].string))
