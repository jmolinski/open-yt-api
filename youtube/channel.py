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

    def _build_page(self, page_html):  # TODO unused argument?
        page_html = self._get_page_content(self._make_videos_url(self.channel_id))
        self._videos = self._parser.get_videos(page_html)

    def _make_videos_url(self, channel_id):
        return 'https://www.youtube.com/user/{}/videos?view=0&sort=p&flow=list'.format(channel_id)

    @property
    def url(self):
        return self._signature.url

    @property
    def channel_id(self):
        return self._signature.channel_id

    @property
    def name(self):
        return self._signature.name

    @property
    def videos_amount(self):
        return self._signature.videos_amount

    @property
    def subscriptions(self):
        return self._signature.subscriptions

    @property
    def thumbnail(self):
        return self._signature.thumbnail

    @property
    def uploaded_videos(self):
        return self._videos[:]
