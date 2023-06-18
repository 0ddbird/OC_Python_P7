from abc import ABC, abstractmethod
from decimal import Decimal


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
        self.rate: Decimal = rate / coefficient
        self.value: Decimal = weight * self.rate
        self.coefficient: int = coefficient
        self.weighted_weight: int = int(weight * coefficient)
        self.weighted_rate: int = int(rate * coefficient)
        self.weighted_value: int = int(
            self.weighted_weight * self.weighted_rate
        )

    def __repr__(self):
        return f"Item({self.name=}, {self.weight=}, {self.rate=})"

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.rate}, {self.value}"


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


class Algorithm(ABC):
    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def compute(self, items: list[Item], max_weight: int) -> Combination:
        raise NotImplementedError
