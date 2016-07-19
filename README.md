# open-yt-api
[![Code Health](https://landscape.io/github/Glenpl/open-yt-api/master/landscape.svg?style=flat)](https://landscape.io/github/Glenpl/open-yt-api/master)
[![Build Status](https://travis-ci.org/Glenpl/open-yt-api.svg?branch=master)](https://travis-ci.org/Glenpl/open-yt-api)
[![Coverage Status](https://coveralls.io/repos/github/Glenpl/open-yt-api/badge.svg?branch=master)](https://coveralls.io/github/Glenpl/open-yt-api?branch=master)

This is an open YouTube API library.
It might be slow because it scrapes and parses actual YouTube HTMLs.

The library is still under development and there may be significant differences between versions.

Installation
--------------------
```bash
pip install openytapi
```

Usage example
--------------------
```python
from youtube.api import YoutubeApi

videos = YoutubeApi().search_videos('lana del rey')

for video in videos:
    print(video.title)
```

Documentation
--------------------
The main API class is YoutubeApi, which consists of 7 methods:
```
constructor(http_fetcher=None, nocache=False, global_cache=False)

search(search_string: str, target='mixed': str) -> default target: Dict of VideoSignature, ChannelSignature and PlaylistSignature
search_videos(search_string: str) -> Tuple of VideoSignature
search_channels(search_string: str) -> Tuple of ChannelSignature
search_playlists(search_string: str) -> Tuple of PlaylistSignature
get_video(video_id: str) -> YoutubeVideo object
get_playlist(playlist_id: str) -> YoutubePlaylist object
clear_cache() -> None
```
Youtube.search is a generic search, you can specify target using `target` argument (available: mixed, videos, channels, playlists).
`Youtube.search('query', target='videos')` is a synonym of `Youtube.search_videos('query')`.
YoutubeApi constructor takes 3 optional, keyword-only arguments: http_fetcher, nocache flag and global_cache flag.
Object passed as http_fetcher is used to fetch page source - it has to implement such an interface:
```python
class Fetcher():
    def fetch_page(self, url): pass  # returns utf-8 decoded page source
```

YoutubeApi.search with default target ('mixed') returns result in such format:
```python
{
  'videos': Tuple of found VideoSignature,
  'playlists': Tuple of found PlaylistSignature,
  'channels': Tuple of found ChannelSignature
}
```
It's probably best to just let the YoutubeApi use it's default http_fetcher - the one that works just fine.
Important note: if you want to supply your own http_fetcher which doesn't make real http calls, it's best to set nocache to True.
If nocache is set to True no cache is used at all. If nocache is set to False or omitted cache is used.
If global_cache is set to True global cache (shared among all YoutubeApi instances with global_cache set to True) is used.
If global_cache is set to False or omitted local cache (available just to this one particular YoutubeApi instance) is used.

---

#####VideoSignature
It's a hashable value object.
May throw exceptions during construction.
All fields are immutable.
```
url: str
video_id: str
length: str
title: str
author: str
views: int
thumbnail: str
as_dict() -> dict
```

---

#####ChannelSignature
It's a hashable value object.
May throw exceptions during construction.
All fields are immutable.
```
url: str
channel_id: str
name: str
videos_amount: int
subscriptions: int
thumbnail: str
as_dict() -> dict
```

---

#####PlaylistSignature
It's a hashable value object.
May throw exceptions during construction.
All fields are immutable.
```
url: str
playlist_id: str
name: str
length: int
thumbnail: str
author: str
first_video_id: str
first_video_url: str
as_dict() -> dict
```

---

#####YoutubeVideo
It's a hashable value object.
May throw exceptions during construction.
All fields are immutable.
```
url: str
length: str
length_in_seconds: int
author: str
title: str
video_id: str
views: int
thumbnail: str
next_video: VideoSignature
related_videos: Tuple of VideoSignature
as_dict() -> dict
```

---

#####YoutubePlaylist
It's a hashable value object.
May throw exceptions during construction.
All fields are immutable.
```
url: str
playlist_id: str
name: str
author: str
length: str
thumbnail: str
videos: Tuple of VideoSignature
as_dict() -> dict
```

---

License
--------------------
MIT license.
