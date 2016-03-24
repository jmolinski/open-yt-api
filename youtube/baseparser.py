from bs4 import BeautifulSoup

class BaseParser():
    _html_parser = None  # beautifulsoup parser

    def _initialize_parser(self, html_code):
        self._html_parser = BeautifulSoup(html_code, 'html.parser')

    def _find_by_class(self, tag, class_name):
        return self._html_parser.find(tag, {'class': class_name})

    def _remove_non_breaking_spaces(self, string):
        return string.replace('\xa0', '')

    def _extract_results(self, html_source, class_name, tag='div'):
        self._initialize_parser(html_source)
        return self._html_parser.find_all(tag, class_=class_name)

class BaseSearchParser(BaseParser):
    def parse(self, html_source):
        search_results = self._extract_results(html_source, self._tile_class_name)
        return [self._parse_single_result(result) for result in search_results]
