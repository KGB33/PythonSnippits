class JsonParser:
    def __init__(self, _json):
        self._json = _json

        for key, val in self._json.items():
            if isinstance(val, dict):
                self._json[key] = JsonParser(val)

    def __getattr__(self, attr):
        try:
            return self._json[attr]
        except KeyError:
            raise AttributeError

    # Iterable
    def __len__(self):
        return len(self._json)

    def __getitem__(self, i):
        return list(self._json.values())[i]

    def __eq__(self, other):
        if isinstance(other, JsonParser):
            return self._json == other._json
        elif isinstance(other, dict):
            return self._json, other
        else:
            return NotImplementedError
