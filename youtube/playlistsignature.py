from youtube.signature import BaseSignature

class PlaylistSignature(BaseSignature):
    def __init__(self, playlist_id, name, playlist_length, author, thumbnail, first_video_id):
        self._validate_not_empty_str(playlist_id)
        self._playlist_id = playlist_id
        self._validate_not_empty_str(name)
        self._name = name
        self._validate_not_empty_str(playlist_length)
        self._playlist_length = playlist_length
        self._validate_not_empty_str(author)
        self._author = author
        self._validate_not_empty_str(thumbnail)
        self._thumbnail = thumbnail
        self._validate_not_empty_str(first_video_id)
        self._first_video_id = first_video_id

    def get_url(self):
        return 'https://www.youtube.com/playlist?list=' + self._playlist_id

    def get_id(self):
        return self._playlist_id

    def get_name(self):
        return self._name

    def get_length(self):
        return self._playlist_length

    def get_thumbnail_url(self):
        return self._thumbnail

    def get_author(self):
        return self._author

    def get_first_video_id(self):
        return self._first_video_id

    def get_first_video_url(self):
        return 'https://www.youtube.com/watch?v={0}&list={1}'.format(self._first_video_id, self._playlist_id)
