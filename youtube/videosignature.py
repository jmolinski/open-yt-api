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
