from youtube.signature import BaseSignature

class ChannelSignature(BaseSignature):
    def __init__(self, channel_id, name, videos_amount, subscriptions, thumbnail):
        self._validate_not_empty_str(channel_id)
        self._channel_id = channel_id
        self._validate_not_empty_str(name)
        self._name = name
        self._validate_not_empty_str(videos_amount)
        self._videos_amount = videos_amount
        self._validate_not_empty_str(subscriptions)
        self._subscriptions = subscriptions
        self._validate_not_empty_str(thumbnail)
        self._thumbnail = thumbnail

    def get_url(self):
        if self._channel_id[:2] == 'UC':
            return 'https://www.youtube.com/channel/' + self._channel_id
        else:
            return 'https://www.youtube.com/user/' + self._channel_id

    def get_id(self):
        return self._channel_id

    def get_name(self):
        return self._name

    def get_videos_amount(self):
        return self._videos_amount

    def get_subscriptions(self):
        return self._subscriptions

    def get_thumbnail_url(self):
        return self._thumbnail
