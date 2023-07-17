from models import Algorithm
from utils.profiling import perf_timer
from knapsack_rs.knapsack_rs import (
    rs_greedy,
    Item,
    Combination,
)


class RsGreedy(Algorithm):
    @property
    def name(self):
        return f"Greedy - {self.lang.name}"

    @perf_timer
    def compute(self, items: list[Item], capacity: int) -> Combination:
        return rs_greedy(items, capacity)
