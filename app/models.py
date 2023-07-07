from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum
from typing import Union


class Item:
    def __init__(
        self,
        name: str,
        weight: Decimal,
        value: Decimal,
        coefficient: int,
    ):
        self.name: str = name
        self.weight: Decimal = weight
        self.value: Decimal = value
        self.coefficient: int = coefficient
        self.weighted_weight: int = int(weight * coefficient)
        self.weighted_rate: int = int(value * coefficient)

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
        return "{:.2f}".format(total_value)

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
        self, items: Union[list[Item], list[dict]], capacity: int
    ) -> Combination:
        if self.lang == LangChoice.Python:
            return self.py_compute(items, capacity)
        else:
            return self.rs_compute(items, capacity)

    @abstractmethod
    def rs_compute(self, items: list[dict], capacity: int) -> Combination:
        raise NotImplementedError

    @abstractmethod
    def py_compute(self, items: list[Item], capacity: int) -> Combination:
        raise NotImplementedError
