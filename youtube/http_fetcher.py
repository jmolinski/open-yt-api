import urllib.request
import urllib.error

class CouldntFetchContentError(Exception):
    pass

class UrllibPageFetcher():
    def fetch_page(self, url, tries_left=3):
        try:
            response = urllib.request.urlopen(url)
        except:  # pylint:disable=bare-except
            if tries_left > 0:
                return self.fetch_page(url, tries_left - 1)  # try again
            else:
                raise CouldntFetchContentError()
        return response.read().decode('utf-8')
