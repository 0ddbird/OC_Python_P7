from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum
from typing import Union
from knapsack_rs.knapsack_rs import Item as RsItem
from knapsack_rs.knapsack_rs import Combination as RsCombination


class Item:
    def __init__(
        self,
        name: str,
        weight: Decimal,
        rate: Decimal,
        coefficient: int,
    ):
        self.name: str = name
        self.weight: Decimal = weight
        self.rate: Decimal = rate
        self.value: Decimal = self.weight * self.rate / 100
        self.coefficient: int = coefficient
        self.weighted_weight: int = int(weight * coefficient)
        self.weighted_rate: int = int(rate * Decimal(coefficient))
        self.weighted_value: int = int(self.weighted_weight * self.weighted_rate)

    def __repr__(self):
        return f"Item({self.name=}, {self.weight=}, {self.value=})"

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
