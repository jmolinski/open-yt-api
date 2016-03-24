from youtube.baseparser import BaseParser
from youtube.videosignature import VideoSignature

class VideoPageParser(BaseParser):
    def get_next_video(self, page_html):
        return self._parse_next_video(self._extract_next_video(page_html))

    def _extract_next_video(self, page_html):
        self._initialize_parser(page_html)
        return self._html_parser.select('#watch7-sidebar-modules div.autoplay-bar')

    def _parse_next_video(self, video):
        self._initialize_parser(repr(video))
        return VideoSignature(self._extract_id_next_video(),
                              self._extract_title_next_video(),
                              self._extract_author_next_video(),
                              self._extract_views_next_video(),
                              self._extract_length_next_video())

    def _extract_id_next_video(self):
        return self._find_by_class('span', 'yt-uix-simple-thumb-wrap')['data-vid']

    def _extract_title_next_video(self):
        return self._find_by_class('a', 'content-link')['title']

    def _extract_author_next_video(self):
        return self._find_by_class('span', 'g-hovercard')['data-ytid']

    def _extract_views_next_video(self):
        return self._remove_non_breaking_spaces(self._find_by_class('span', 'view-count').string.split(' ')[0])

    def _extract_length_next_video(self):
        return str(self._find_by_class('span', 'video-time').string)

    def parse_related_videos(self, page_html):
        related_videos = self._extract_related_videos(page_html)
        return [self._parse_related_video(video) for video in related_videos]

    def _extract_related_videos(self, page_html):
        self._initialize_parser(page_html)
        return self._html_parser.select('#watch-related li.related-list-item-compact-video')

    def _parse_related_video(self, video):
        return self._parse_next_video(video)

    def get_signature(self, page_html):
        self._initialize_parser(repr(page_html))
        return VideoSignature(self._extract_id(), self._extract_title(),
                              self._extract_author(), self._extract_views(),
                              self._extract_length())

    def _extract_author(self):
        return self._html_parser.select('#watch7-content meta [itemprop=channelId]')[0]['content']

    def _extract_title(self):
        return self._html_parser.select('#watch7-content meta')[0]['content']

    def _extract_id(self):
        return self._html_parser.select('#watch7-content meta')[4]['content']

    def _extract_views(self):
        return self._html_parser.select('#watch7-content meta [itemprop=interactionCount]')[0]['content']

    def _extract_length(self):
        raw_time = self._html_parser.select('#watch7-content meta [itemprop=duration]')[0]['content']
        [mins, secs] = raw_time.replace('PT', '')[:-1].split('M')
        hrs = int(mins) // 60
        mins = str(int(mins) - 60 * hrs)
        return ':'.join(([str(hrs)] if not str(hrs) == '0' else []) +
                        [mins if not str(mins) == '0' else '00'] + [secs])
