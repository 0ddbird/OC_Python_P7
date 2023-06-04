from utils.profiling import perf_timer

from models import Item, Combination, Algorithm


class Greedy(Algorithm):
    @property
    def name(self):
        return "greedy"

    @perf_timer
    def compute(self, items: list[Item], max_weight: int) -> Combination:
        current_weight = 0
        combination = []

        sorted_items = sorted(items, key=lambda x: x.value, reverse=True)

        for item in sorted_items:
            if item.weight >= max_weight - current_weight:
                continue
            combination.append(item)
            current_weight += item.weight

        return Combination(combination)
