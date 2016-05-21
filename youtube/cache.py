
class _YoutubeCache():
    _search_results = {}
    _objects = {}

    @staticmethod
    def get_search_result(search_type, query):
        try:
            return _YoutubeCache._search_results.get(search_type).get(query)
        except AttributeError:  # None.get(query)
            return None

    @staticmethod
    def add_search_result(search_type, query, result):
        if search_type not in _YoutubeCache._search_results:
            _YoutubeCache._search_results[search_type] = {}
        _YoutubeCache._search_results[search_type][query] = result

    @staticmethod
    def get_object(id_):
        return _YoutubeCache._objects.get(id_)

    @staticmethod
    def add_object(id_, result):
        _YoutubeCache._objects[id_] = result

    @staticmethod
    def clear_cache():
        _YoutubeCache._search_results = {}
        _YoutubeCache._objects = {}
