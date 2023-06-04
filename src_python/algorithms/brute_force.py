import itertools

from models import Item, Combination, Algorithm
from utils.profiling import perf_timer


class BruteForce(Algorithm):
    @property
    def name(self):
        return "brute_force"

    @perf_timer
    def compute(self, items: list[Item], max_weight: int) -> Combination:
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
            combination_weight = sum(item.weight for item in combination)

            if combination_weight >= max_weight:
                continue

            value = sum(item.value for item in combination)
            possible_solutions.append((combination, value))

        best_solution = max(possible_solutions, key=lambda x: x[1])
        best_list = [item for item in best_solution[0]]

        return Combination(best_list)
