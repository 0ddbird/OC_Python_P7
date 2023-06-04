from models import Item, Combination


def compute(algorithm, items: list[Item, ...], max_weight: int) -> Combination:
    return algorithm.compute(items=items, max_weight=max_weight)
