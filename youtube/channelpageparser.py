from youtube.baseparser import BaseParser
from youtube.channelsignature import ChannelSignature
from youtube.videosignature import VideoSignature

class ChannelPageParser(BaseParser):
    _author = None

    def get_videos(self, page_html):
        self._initialize_parser(repr(page_html))
        self._author = self._extract_channel_id()
        return [self._parse_video(video) for video in self._extract_results(page_html, 'yt-lockup-video', 'div')]

    def _parse_video(self, video):
        self._initialize_parser(repr(video))
        return VideoSignature(self._extract_id(),
                              self._extract_title(),
                              self._author,
                              self._extract_views(),
                              self._extract_length())

    def _extract_length(self):
        return str(self._find_by_class('span', 'video-time').string)

    def _extract_title(self):
        return str(self._find_by_class('h3', 'yt-lockup-title').a.string)

    def _extract_id(self):
        return self._html_parser.div['data-context-item-id']

    def _extract_views(self):
        return ''.join([x for x in self._html_parser.select('.yt-lockup-meta-info li')[1].string if self._is_digit(x)])

    def get_signature(self, page_html):
        self._initialize_parser(repr(page_html))
        return ChannelSignature(self._extract_channel_id(),
                                self._extract_channel_name(),
                                self._extract_channel_videos_amount(),
                                self._extract_channel_subscriptions(),
                                self._extract_channel_thumbnail_url())

    def _extract_channel_id(self):
        return self._html_parser.select('.qualified-channel-title-text a')[0]['href'].split('/')[2]

    def _extract_channel_name(self):
        return str(self._html_parser.select('.qualified-channel-title-text a')[0].string)

    def _extract_channel_videos_amount(self):
        return 'NOTSET'  # data can't be extracted

    def _extract_channel_thumbnail_url(self):
        return self._html_parser.select('.channel-header-profile-image')[0]['src']

    def _extract_channel_subscriptions(self):
        return ''.join([x for x in self._html_parser.select('.about-stats span b')[0].string if self._is_digit(x)])

    def _is_digit(self, digit):
        return '9' >= digit >= '0'
