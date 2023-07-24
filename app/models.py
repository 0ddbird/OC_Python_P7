from abc import ABC, abstractmethod
import csv
from decimal import Decimal
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional


@dataclass
class Item:
    name: str
    weight: Decimal
    rate: Decimal
    coefficient: int

    @property
    def value(self) -> Decimal:
        return self.weight * self.rate / 100

    @property
    def weighted_weight(self) -> int:
        return int(self.weight * Decimal(self.coefficient))

    @property
    def weighted_rate(self) -> int:
        return int(self.rate * Decimal(self.coefficient))

    @property
    def weighted_value(self) -> int:
        return int(self.weighted_weight * self.weighted_rate)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.value}"


class Combination:
    def __init__(self, items: list[Item]):
        self.items = items

    @property
    def weight(self):
        return f"{sum(item.weight for item in self.items)}"

    @property
    def value(self):
        total_value = sum(item.value for item in self.items)
        return "{:.6f}".format(total_value)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)


class LangChoice(Enum):
    Python = "--py"
    Rust = "--rs"


class AbstractItemFactory(ABC):
    def __init__(self, language: LangChoice, file_path: Path) -> None:
        self.raw_items: Optional[list[tuple[str, str, str]]] = None
        self.language: LangChoice = language
        self.coefficient: int = 1
        self.file_path: Path = file_path

    @abstractmethod
    def _get_coefficient(self) -> int:
        raise NotImplementedError

    def _get_raw_items(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.reader(f)
            next(reader)
            self.raw_items = [tuple(row) for row in reader]

    @abstractmethod
    def build_items(self, get_coeff: bool = False) -> list[Item]:
        raise NotImplementedError


class Algorithm(ABC):
    def __init__(self, lang: LangChoice):
        self.lang = lang

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def compute(self, items: list[Item], capacity: int) -> Combination:
        raise NotImplementedError
