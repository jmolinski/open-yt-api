from youtube.cache import _YoutubeCache
from youtube.errors import YoutubeApiRandomException

# theses 2 functions manage caching
def search_wrapper(search_type, search_string, nocache, actual_search):
    if nocache:
        return _exception_handling_wrapper(actual_search)

    cached = _YoutubeCache.get_search_result(search_type, search_string)
    if cached:
        return cached
    else:
        results = _exception_handling_wrapper(actual_search)  # executes lambda
        _YoutubeCache.add_search_result(search_type, search_string, results)
        return results

def get_object_wrapper(object_id, nocache, actual_search):
    if nocache:
        return _exception_handling_wrapper(actual_search)

    cached = _YoutubeCache.get_object(object_id)
    if cached:
        return cached
    else:
        result = _exception_handling_wrapper(actual_search)  # executes lambda
        _YoutubeCache.add_object(object_id, result)
        return result

# if there was an random exception caused by eg. damaged html - repeat query
def _exception_handling_wrapper(search_function, max_tries=5):
    while True:
        try:
            return search_function()
        except (LookupError, ValueError, TypeError) as err:
            if max_tries == 1:
                raise YoutubeApiRandomException(err)
            else:
                max_tries -= 1
