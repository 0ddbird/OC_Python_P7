from utils.profiling import perf_timer
from models import Item, Combination, Algorithm


def get_all_combinations(items):
    n = len(items)
    combinations = []

    for i in range(1, 2**n):
        combination = []
        for j in range(n):
            if ((i >> j) & 1) == 1:
                combination.append(items[j])
        combinations.append(combination)

    return combinations


class PyBruteForce(Algorithm):
    @property
    def name(self):
        return f"brute_force - {self.lang.name}"

    @perf_timer
    def compute(self, items: list[Item], capacity: int) -> Combination:
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

        return Combination(best_list)
