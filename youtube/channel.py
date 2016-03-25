from youtube.baseelement import BaseElement
from youtube.channelpageparser import ChannelPageParser

class YoutubeChannel(BaseElement):
    _videos = None

    def _make_url(self, channel_id):
        return 'https://www.youtube.com/user/{}/about'.format(channel_id)

    def _is_valid_id(self, channel_id):
        return len(channel_id) != ''

    def _get_default_parser(self):
        return ChannelPageParser()

    def _build_page(self, page_html):
        page_html = self._get_page_content(self._make_videos_url(self.get_id()))
        self._videos = self._parser.get_videos(page_html)

    def _make_videos_url(self, channel_id):
        return 'https://www.youtube.com/user/{}/videos?view=0&sort=p&flow=list'.format(channel_id)

    def get_url(self):
        return self._signature.get_url()

    def get_id(self):
        return self._signature.get_id()

    def get_name(self):
        return self._signature.get_name()

    def get_videos_amount(self):
        return self._signature.get_videos_amount()

    def get_subscriptions(self):
        return self._signature.get_subscriptions()

    def get_thumbnail_url(self):
        return self._signature.get_thumbnail_url()

    def get_uploaded_videos(self):
        return self._videos[:]
