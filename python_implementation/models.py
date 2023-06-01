from decimal import Decimal, getcontext
from enum import Enum

getcontext().prec = 4


class Item:
    def __init__(self, name: str, weight: int, rate: Decimal):
        self.name: str = name
        self.weight: int = weight
        self.rate: Decimal = Decimal(str(rate))
        self.value: Decimal = Decimal(self.weight) * self.rate

    def __repr__(self):
        return (
            f"Item({self.name=}, {self.weight=}, {self.rate=}, {self.value=})"
        )

    def __str__(self):
        return f"{self.name}, {self.weight / 100}, {self.rate}"


class ImplChoice(Enum):
    BruteForce = 1
    Greedy = 2
    Dynamic = 3
