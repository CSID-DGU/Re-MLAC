class DataFrameSingleton:
    _instance = None

    def __init__(self):
        self._data = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, df):
        self._data = df


class DataBodySingleton:
    _instance = None

    def __init__(self):
        self._data = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, df):
        self._data = df