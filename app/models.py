from abc import ABC, abstractmethod
from decimal import Decimal
from dataclasses import dataclass
from enum import Enum
from typing import Union
from knapsack_rs.knapsack_rs import Item as RsItem
from knapsack_rs.knapsack_rs import Combination as RsCombination


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


class Algorithm(ABC):
    def __init__(self, lang: LangChoice):
        self.lang = lang

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    def compute(
        self, items: Union[list[Item], list[RsItem]], capacity: int
    ) -> Combination:
        if self.lang == LangChoice.Python:
            return self.py_compute(items, capacity)
        else:
            return self.rs_compute(items, capacity)

    @abstractmethod
    def rs_compute(self, items: list[RsItem], capacity: int) -> RsCombination:
        raise NotImplementedError

    @abstractmethod
    def py_compute(self, items: list[Item], capacity: int) -> Combination:
        raise NotImplementedError
