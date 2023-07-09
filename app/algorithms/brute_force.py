from models import Algorithm, PyCombination, Item as PyItem
from utils.profiling import perf_timer
from knapsack_rs.knapsack_rs import (
    rs_brute_force,
    Item as RsItem,
    Combination as RsCombination,
)


def get_all_combinations(items):
    n = len(items)
    combinations = []

    for i in range(1, 2**n):  # Start from 1 to exclude the empty set
        combination = []
        for j in range(n):
            if ((i >> j) & 1) == 1:  # Check if jth bit of i is set
                combination.append(items[j])
        combinations.append(combination)

    return combinations


class BruteForce(Algorithm):
    @property
    def name(self):
        return f"brute_force - {self.lang.name}"

    @perf_timer
    def py_compute(self, items: list[PyItem, ...], capacity: int) -> PyCombination:
        if len(items) > 20:
            raise ValueError(
                "Brute force solution can't be used with more than 20 items"
            )

        all_combinations = get_all_combinations(items)

        possible_solutions = []
        for combination in all_combinations:
            combination_weight = sum(item.weight for item in combination)

            if combination_weight >= capacity:
                continue

            value = sum(item.value for item in combination)
            possible_solutions.append((combination, value))

        best_solution = max(possible_solutions, key=lambda x: x[1])
        best_list = [item for item in best_solution[0]]

        return PyCombination(best_list)

    @perf_timer
    def rs_compute(self, items: list[RsItem, ...], capacity: int) -> RsCombination:
        if len(items) > 20:
            raise ValueError(
                "Brute force solution can't be used with more than 20 items"
            )
        return rs_brute_force(items, capacity)
