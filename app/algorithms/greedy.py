from models import Algorithm, Combination, Item
from utils.profiling import perf_timer


class Greedy(Algorithm):
    @property
    def name(self):
        return "Greedy - {self.lang.name}"

    @perf_timer
    def py_compute(self, items: list[Item], capacity: int) -> Combination:
        current_weight = 0
        combination = []

        sorted_items = sorted(items, key=lambda x: x.value, reverse=True)

        for item in sorted_items:
            if item.weight >= capacity - current_weight:
                continue
            combination.append(item)
            current_weight += item.weight

        return Combination(combination)

    @perf_timer
    def rs_compute(self, items: dict[Item], capacity: int) -> Combination:
        pass
