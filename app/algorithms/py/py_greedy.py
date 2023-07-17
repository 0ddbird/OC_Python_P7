from models import Algorithm, Combination, Item as Item
from utils.profiling import perf_timer


class PyGreedy(Algorithm):
    @property
    def name(self):
        return f"Greedy - {self.lang.name}"

    @perf_timer
    def compute(self, items: list[Item], capacity: int) -> Combination:
        current_weight = 0
        combination = []

        sorted_items = sorted(items, key=lambda x: x.value, reverse=True)

        for item in sorted_items:
            if item.weight >= capacity - current_weight:
                continue
            combination.append(item)
            current_weight += item.weight

        return Combination(combination)
