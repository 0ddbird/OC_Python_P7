from utils.profiling import perf_timer
from models import Item, Combination, Algorithm

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

        n = len(items)
        combinations = []

        for i in range(1, 2**n):
            combination = {
            "items": [],
            "value": 0,
            "weight": 0,
        }
            for j in range(n):
                if ((i >> j) & 1) == 1:
                    combination["items"].append(items[j])
                    combination["value"] += items[j].value
                    combination["weight"] += items[j].weight
            if combination["weight"] <= capacity:
                combinations.append(combination)

        best_combination = max(combinations, key=lambda combination: combination["value"])

        return Combination(best_combination["items"])
