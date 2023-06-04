from models import Item, Combination, Algorithm
from utils.profiling import perf_timer


class Genetic(Algorithm):
    @property
    def name(self):
        return "genetic"

    @perf_timer
    def compute(self, items: list[Item], max_weight: int) -> Combination:
        raise NotImplementedError
