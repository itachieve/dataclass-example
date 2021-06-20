from abc import ABCMeta
from types import SimpleNamespace


class RecursiveNamespace(SimpleNamespace, metaclass=ABCMeta):
    @staticmethod
    def map_entry(entry):
        if isinstance(entry, dict):
            return RecursiveNamespace(**entry)

        return entry

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, val in kwargs.items():
            if isinstance(val) == dict:
                setattr(self, key, RecursiveNamespace(**val))
            elif isinstance(val) == list:
                setattr(self, key, list(map(self.map_entry, val)))
