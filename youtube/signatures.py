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


class PlaylistSignature(Struct):
    playlist_id = TypedField(str)
    name = TypedField(str)
    length = TypedField(int)
    author = TypedField(str)
    thumbnail = TypedField(str)
    first_video_id = TypedField(str)

    @property
    def url(self):
        return 'https://www.youtube.com/playlist?list=' + self.playlist_id

    @property
    def first_video_url(self):
        return 'https://www.youtube.com/watch?v={0}&list={1}'.format(self.first_video_id, self.playlist_id)

    def as_dict(self):
        return {
            'id': self.playlist_id,
            'name': self.name,
            'author': self.author,
            'first_video_url': self.first_video_url,
            'first_video_id': self.first_video_id,
            'length': self.length,
            'url': self.url,
            'thumbnail': self.thumbnail
        }


class ChannelSignature(Struct):
    channel_id = TypedField(str)
    name = TypedField(str)
    videos_amount = TypedField(int)
    subscriptions = TypedField(int)
    thumbnail = TypedField(str)

    @property
    def url(self):
        if self.channel_id[:2] == 'UC':
            return 'https://www.youtube.com/channel/' + self.channel_id
        else:
            return 'https://www.youtube.com/user/' + self.channel_id

    def as_dict(self):
        return {
            'id': self.channel_id,
            'name': self.name,
            'videos_amount': self.videos_amount,
            'subscriptions': self.subscriptions,
            'url': self.url,
            'thumbnail': self.thumbnail
        }
