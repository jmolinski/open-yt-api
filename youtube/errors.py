class YoutubeApiError(Exception):
    pass

class YoutubeApiConnectionError(YoutubeApiError):
    def __init__(self, message='', parent_error=None):
        self.message = message
        self.parent_error = parent_error

class YoutubeInvalidIdError(YoutubeApiError):
    def __init__(self, parent_error=None):
        self.parent_error = parent_error

class YoutubeApiRandomException(YoutubeApiError):
    def __init__(self, parent_error):
        self.parent_error = parent_error
