
class _YoutubeCache():
    def get_search_result(self, search_type, query):
        try:
            return self._cache._search_results.get(search_type).get(query)  # pylint:disable=protected-access
        except AttributeError:  # None.get(query)
            return None

    def add_search_result(self, search_type, query, result):
        if search_type not in self._cache._search_results:  # pylint:disable=protected-access
            self._cache._search_results[search_type] = {}  # pylint:disable=protected-access
        self._cache._search_results[search_type][query] = result  # pylint:disable=protected-access

    def get_object(self, id_):
        return self._cache._objects.get(id_)  # pylint:disable=protected-access

    def add_object(self, id_, result):
        self._cache._objects[id_] = result  # pylint:disable=protected-access

    def clear_cache(self):
        self._cache._search_results = {}  # pylint:disable=protected-access
        self._cache._objects = {}  # pylint:disable=protected-access


class YoutubeLocalCache(_YoutubeCache):
    def __init__(self):
        self._search_results = {}
        self._objects = {}
        self._cache = self


class YoutubeGlobalCache(_YoutubeCache):
    _global_cache = YoutubeLocalCache()

    def __init__(self):
        self._cache = YoutubeGlobalCache._global_cache
