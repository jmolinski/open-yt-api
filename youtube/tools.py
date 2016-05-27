from youtube.errors import YoutubeApiRandomException

# TODO create additional classes to handle caching eg. Search instead of search_wrapper function

# theses 2 functions manage caching
def search_wrapper(search_type, search_string, cache, nocache, actual_search):
    if nocache:
        return _exception_handling_wrapper(actual_search)

    cached = cache.get_search_result(search_type, search_string)
    if cached:
        return cached
    else:
        results = _exception_handling_wrapper(actual_search)  # executes lambda
        cache.add_search_result(search_type, search_string, results)
        return results

def get_object_wrapper(object_id, cache, nocache, actual_search):
    if nocache:
        return _exception_handling_wrapper(actual_search)

    cached = cache.get_object(object_id)
    if cached:
        return cached
    else:
        result = _exception_handling_wrapper(actual_search)  # executes lambda
        cache.add_object(object_id, result)
        return result

# if there was an random exception caused by eg. damaged html - repeat query
def _exception_handling_wrapper(search_function, *, max_tries=5):
    while True:
        try:
            return search_function()
        except (ValueError, TypeError, AttributeError, IndexError, KeyError) as err:
            if max_tries == 1:
                raise YoutubeApiRandomException(parent_error=err) from err
            else:
                max_tries -= 1
