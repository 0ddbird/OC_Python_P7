from typing import Union

from models import Combination, Item, LangChoice


def compute(
    algorithm, items: list[Item, ...], capacity: int
) -> Union[Combination, list[dict]]:
    if algorithm.lang == LangChoice.Python:
        return algorithm.py_compute(items=items, capacity=capacity)
    else:
        return algorithm.rs_compute(items=items, capacity=capacity)
