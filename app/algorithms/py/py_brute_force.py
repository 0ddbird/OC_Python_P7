from utils.profiling import perf_timer
from models import Item, Combination, Algorithm


class TempCombination:
    def __init__(self):
        self.items: list[Item] = []
        self.value: int = 0
        self.weight: int = 0

    def add_item(self, item: Item) -> None:
        self.items.append(item)
        self.value += item.value
        self.weight += item.weight


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

        best_combination = TempCombination()
        n = len(items)

        for i in range(1, 2**n):
            combination = TempCombination()

            for j in range(n):
                item = items[j]

                if combination.weight + item.weight > capacity:
                    break

                if ((i >> j) & 1) == 1:
                    combination.add_item(item)

            if combination.value > best_combination.value:
                best_combination = combination

        return Combination(best_combination.items)
