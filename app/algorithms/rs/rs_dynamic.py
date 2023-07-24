from models import Algorithm
from utils.profiling import perf_timer
from knapsack_rs.knapsack_rs import rs_dynamic, Item, Combination


class RsDynamic(Algorithm):
    @property
    def name(self):
        return f"Dynamic programming - {self.lang.name}"

    @perf_timer
    def compute(self, items: list[Item], capacity: int) -> Combination:
        return rs_dynamic(items, capacity)
