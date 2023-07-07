import itertools
from models import Algorithm, Combination, Item
from utils.profiling import perf_timer
from src_rust_lib import brute_force


class BruteForce(Algorithm):
    @property
    def name(self):
        return f"brute_force - {self.lang.name}"

    @perf_timer
    def py_compute(self, items: list[Item], capacity: int) -> Combination:
        if len(items) > 20:
            raise ValueError(
                "Brute force solution can't be used with more than 20 items"
            )

        # Faire les combinaisons à la main
        all_combinations = []
        for r in range(1, len(items) + 1):
            combinations_object = itertools.combinations(items, r)
            all_combinations += combinations_object

        possible_solutions = []
        for combination in all_combinations:
            combination_weight = sum(item.weight for item in combination)

            if combination_weight >= capacity:
                continue

            value = sum(item.value for item in combination)
            possible_solutions.append((combination, value))

        best_solution = max(possible_solutions, key=lambda x: x[1])
        best_list = [item for item in best_solution[0]]

        return Combination(best_list)

    @perf_timer
    def rs_compute(self, items: list[dict], capacity: int) -> Combination:
        return brute_force(items, capacity)
