from pathlib import Path
from models import AbstractItemFactory, LangChoice
from knapsack_rs.knapsack_rs import Item
from knapsack_rs.knapsack_rs import rs_get_coefficient, rs_build_items

class RustItemFactory(AbstractItemFactory):
    def __init__(self, language: LangChoice, file_path: Path) -> None:
        super().__init__(language, file_path)

    def _get_coefficient(self) -> int:
        return rs_get_coefficient(self.raw_items)

    def build_items(self, get_coefficient: bool = False) -> list[Item]:
        self._get_raw_items()
        if get_coefficient:
            self.coefficient = self._get_coefficient()
        return rs_build_items(self.raw_items, self.coefficient)
