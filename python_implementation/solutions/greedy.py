from models import Item
from utils import perf_timer


@perf_timer
def greedy(
    items: list[Item, ...], max_weight: int, coeff: int
) -> list[Item]:
    """
    Solve the 0/1 knapsack problem using a greedy approach.

    :param items: A list of items to combine.
    :type items: List[Item]
    :param max_weight: The maximum weight.
    :type max_weight: int
    :return: A tuple containing the best combination of items as a list of
    strings and the maximum value as a float.
    :rtype: Tuple[List[str], float]
    """
    current_weight = 0
    best_combination = []

    sorted_items = sorted(items, key=lambda x: x.value, reverse=True)

    for item in sorted_items:
        if item.weight <= max_weight - current_weight:
            best_combination.append(item)
            current_weight += item.weight

    return best_combination
