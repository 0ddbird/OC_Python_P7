from utils.profiling import perf_timer
from models import Algorithm
from knapsack_rs.knapsack_rs import rs_brute_force, Item, Combination


class RsBruteForce(Algorithm):
    @property
    def name(self):
        return f"brute_force - {self.lang.name}"

    @perf_timer
    def compute(self, items: list[Item], capacity: int) -> Combination:
        if len(items) > 20:
            raise ValueError(
                "Brute force solution can't be used with more than 20 items"
            )
        return rs_brute_force(items, capacity)
