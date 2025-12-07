class Entry:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __eq__(self, other):
        if not isinstance(other, Entry):
            return False
        return self.key == other.key and self.value == other.value

    def __str__(self):
        return f"<{self._key} : {self._value}>"

    def __repr__(self):
        return f"<{self._key} : {self._value}>"
