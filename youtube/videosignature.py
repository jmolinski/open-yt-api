from youtube.signature import BaseSignature

class VideoSignature(BaseSignature):
    def __init__(self, video_id, title, author, views, length): # noqa
        self._validate_not_empty_str(video_id)
        self._video_id = video_id
        self._validate_not_empty_str(title)
        self._title = title
        self._validate_not_empty_str(views)
        self._views = views
        self._validate_not_empty_str(length)
        self._length = length
        self._validate_not_empty_str(author)
        self._author = author

    def get_url(self):
        return 'https://www.youtube.com/watch?v=' + self._video_id

    def get_id(self):
        return self._video_id

    def get_length(self):
        return self._length

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_views(self):
        return self._views

    def get_thumbnail_url(self):
        return "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(self._video_id)
