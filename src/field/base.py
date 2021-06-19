from abc import ABCMeta
from typing import Optional, Any
from datetime import datetime

from dataclasses import dataclass


@dataclass
class Field(metaclass=ABCMeta):
    pass


@dataclass
class TitleField(Field):
    name: str
    value: Optional[str]


@dataclass
class ValueField(Field, metaclass=ABCMeta):
    name: str
    value: Optional[Any]


@dataclass
class DateTimeField(ValueField):
    value: Optional[datetime]


@dataclass
class IntField(ValueField):
    value: Optional[int]


@dataclass
class CertainDateTimeField(DateTimeField):
    value: Optional[str]

    def __post_init__(self):
        if not isinstance(self.value, (str, type(None))):
            raise TypeError(
                f"{self.__class__.__name__}'s Value Need String Type")
