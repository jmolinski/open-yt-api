from simplestruct import Struct, TypedField

class VideoSignature(Struct):
    video_id = TypedField(str)
    title = TypedField(str)
    author = TypedField(str)
    views = TypedField(int)
    length = TypedField(str)

    @property
    def url(self):
        return 'https://www.youtube.com/watch?v=' + self.video_id

    @property
    def thumbnail(self):
        return "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(self.video_id)

    def as_dict(self):
        return {
            'id': self.video_id,
            'title': self.title,
            'author': self.author,
            'views': self.views,
            'length': self.length,
            'url': self.url,
            'thumbnail': self.thumbnail
        }
