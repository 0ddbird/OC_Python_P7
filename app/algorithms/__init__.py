from models import Item, LangChoice, Combination


def compute(
    algorithm, items: list[Item, ...], capacity: int
) -> Combination:
    if algorithm.lang == LangChoice.Python:
        return algorithm.py_compute(items=items, capacity=capacity)
    else:
        return algorithm.rs_compute(items=items, capacity=capacity)
