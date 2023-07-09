import csv
from abc import ABC, abstractmethod
from pathlib import Path
from knapsack_rs.knapsack_rs import rs_get_coefficient, rs_build_items
from _decimal import Decimal
from typing import Optional, Union

from models import Item as PyItem, LangChoice
from knapsack_rs.knapsack_rs import Item as RsItem


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
    def build_items(self, get_coeff: bool = False) -> Union[list[PyItem, ...], list[RsItem, ...]]:
        raise NotImplementedError


class PythonItemFactory(AbstractItemFactory):
    def __init__(self, language: LangChoice, file_path: Path) -> None:
        super().__init__(language, file_path)

    def _get_coefficient(self) -> int:
        dec_places = 0
        no_dec_places = True

        for item in self.raw_items:
            weight = item[1]
            rate = item[2]
            w_dec_places = weight.split(".")[1] if "." in weight else ""
            r_dec_places = rate.split(".")[1] if "." in rate else ""
            dec_places = max(dec_places, len(w_dec_places), len(r_dec_places))
            decimal_places: str = w_dec_places + r_dec_places
            if no_dec_places and any(digit != "0" for digit in decimal_places):
                no_dec_places = False

        if no_dec_places:
            dec_places = 0
        return 10**dec_places

    def build_items(self, get_coefficient: bool = False) -> list[PyItem, ...]:
        self._get_raw_items()
        if get_coefficient:
            self.coefficient = self._get_coefficient()

        items = []
        for item in self.raw_items:
            name, weight, rate = item
            weight = Decimal(weight)
            rate = Decimal(rate)

            if weight <= 0 or rate <= 0:
                print(
                    f"Excluding invalid item: {name}. "
                    "Please make sure all weights and rates are greater than 0.0"
                )
                continue
            item = Item(
                name=name, weight=weight, rate=rate, coefficient=self.coefficient
            )

            items.append(item)
        return items


class RustItemFactory(AbstractItemFactory):
    def __init__(self, language: LangChoice, file_path: Path) -> None:
        super().__init__(language, file_path)

    def _get_coefficient(self) -> int:
        return rs_get_coefficient(self.raw_items)

    def build_items(self, get_coefficient: bool = False) -> list[RsItem]:
        self._get_raw_items()
        if get_coefficient:
            self.coefficient = self._get_coefficient()
        return rs_build_items(self.raw_items, self.coefficient)
