from models import Algorithm, PyCombination, Item as PyItem
from utils.profiling import perf_timer
from knapsack_rs.knapsack_rs import (
    rs_greedy,
    Item as RsItem,
    Combination as RsCombination,
)


class Greedy(Algorithm):
    @property
    def name(self):
        return f"Greedy - {self.lang.name}"

    @perf_timer
    def py_compute(self, items: list[PyItem, ...], capacity: int) -> PyCombination:
        current_weight = 0
        combination = []

        sorted_items = sorted(items, key=lambda x: x.value, reverse=True)

        for item in sorted_items:
            if item.weight >= capacity - current_weight:
                continue
            combination.append(item)
            current_weight += item.weight

        return PyCombination(combination)

    @perf_timer
    def rs_compute(self, items: list[RsItem, ...], capacity: int) -> RsCombination:
        return rs_greedy(items, capacity)
