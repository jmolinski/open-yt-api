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

found_items = YoutubeApi().search('lana del rey')
found_playlists = YoutubeApi().search_playlists('lana del rey')

print(found_items)
```

License
--------------------
MIT license.
