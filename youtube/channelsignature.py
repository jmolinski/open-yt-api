from simplestruct import Struct, TypedField

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
