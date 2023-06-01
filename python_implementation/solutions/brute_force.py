import itertools
from typing import List, Tuple

from models import Item
from utils import perf_timer


@perf_timer
def brute_force(items: List[Item], max_weight: int, coeff: int) -> List[Item]:
    """
    Solve the 0/1 knapsack problem using a brute force approach.

    :param items: A list of items to combine.
    :type items: List[Item]
    :param max_weight: The maximum weight.
    :type max_weight: int
    :return: A tuple containing the best combination of items as a list of
    strings and the maximum value as a float.
    :rtype: List[Item]
    """
    if len(items) > 20:
        raise ValueError(
            "Brute force solution can't be used with more than 20 items"
        )
    all_combinations = []
    for r in range(1, len(items) + 1):
        combinations_object = itertools.combinations(items, r)
        all_combinations += combinations_object

    possible_solutions = []
    for combination in all_combinations:
        weight = sum(item.weight for item in combination)
        if weight <= max_weight:
            value = sum(item.value for item in combination)
            possible_solutions.append((combination, value))

    best_solution = max(possible_solutions, key=lambda x: x[1])
    best_solution_actions = [item for item in best_solution[0]]

    return best_solution_actions
