from models import Combination, Item


def compute(algorithm, items: list[Item, ...], max_weight: int) -> Combination:
    return algorithm.compute(items=items, capacity=max_weight)
