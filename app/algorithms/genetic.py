from ..models import Algorithm, Combination, Item
from ..utils.profiling import perf_timer


class Genetic(Algorithm):
    @property
    def name(self):
        return f"Genetic -{self.lang.name}"

    @perf_timer
    def py_compute(self, items: list[Item], capacity: int) -> Combination:
        raise NotImplementedError

    @perf_timer
    def rs_compute(self, items: dict[Item], capacity: int) -> Combination:
        pass
