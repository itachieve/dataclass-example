from abc import ABCMeta
from dataclasses import dataclass

from field.base import TitleField, ValueField


@dataclass
class DocType(metaclass=ABCMeta):
    title: TitleField
    value: ValueField


@dataclass
class Trained(metaclass=ABCMeta):
    pass


@dataclass
class Truth(metaclass=ABCMeta):
    extract_match: float
    similiar_match: float
    accuracy: float
    recall: float
