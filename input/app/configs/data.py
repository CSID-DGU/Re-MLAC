import pandas as pd


class DataFrameSingleton:
    _instance = None

    def __init__(self):
        self._data = None
        self._length = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TestDataSingleton()
        return cls._instance

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, df):
        self._data = df
        self._length = len(df)

    @property
    def length(self):
        return self._length


class TestDataSingleton:
    _instance = None

    def __init__(self):
        self._data = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TestDataSingleton()
        return cls._instance

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, df):
        self._data = df

    def save(self, label, attack_type):
        if self._data is None:
            self._data = []
        self._data.append([label, attack_type])

    def save_to_csv(self, filename):
        if self._data is not None:
            df = pd.DataFrame(list(self._data), columns=['origin', 'predict'])
            df.to_csv(filename, index=False)


