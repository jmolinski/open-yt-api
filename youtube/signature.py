class BaseSignature():
    def _validate_not_empty_str(self, value):
        if type(value) != str:
            raise ValueError('Invalid data type')
        if value == '':
            raise ValueError('String cannot be empty')

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
