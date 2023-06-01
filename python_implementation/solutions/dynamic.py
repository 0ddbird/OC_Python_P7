from _decimal import getcontext

from models import Item
from utils import perf_timer


def get_best_combination_items(items, keep, max_weight):
    included_items = []
    for i in range(len(items) - 1, -1, -1):
        if max_weight == 0:
            break
        current_row = keep[i]
        if current_row[max_weight] == 1:
            included_items.append(items[i])
            max_weight -= items[i].weight
    included_items.reverse()

    return included_items


@perf_timer
def dynamic_programming(
    items: list[Item],
    max_weight: int,
    coeff: int,
) -> list[Item]:
    """
    Solve the 0/1 knapsack problem using dynamic programming.

    :param items: A list of items to combine.
    :type items: list[Item]
    :param max_weight: The maximum weight.
    :type max_weight: int
    :return: A tuple containing the best combination of items as a list
    of strings and the maximum value as a float.
    :rtype: tuple[list[Item], float]
    """
    getcontext().prec = 4
    n = len(items)
    table = [[0 for _ in range(max_weight + 1)] for _ in range(n)]
    keep = [[0 for _ in range(max_weight + 1)] for _ in range(n)]

    for i in range(n):
        for curr_max_weight in range(max_weight + 1):
            if i == 0 or curr_max_weight == 0:
                continue
            item = items[i]
            prev_row = table[i - 1]
            current_row = table[i]
            if item.weight > curr_max_weight:
                current_row[curr_max_weight] = prev_row[curr_max_weight]
            else:
                value_with_item = (
                    item.value + prev_row[curr_max_weight - item.weight]
                )
                value_without_item = prev_row[curr_max_weight]
                current_row[curr_max_weight] = max(
                    value_with_item, value_without_item
                )
                keep[i][curr_max_weight] = (
                    1 if value_with_item > value_without_item else 0
                )

    return get_best_combination_items(items, keep, max_weight)
