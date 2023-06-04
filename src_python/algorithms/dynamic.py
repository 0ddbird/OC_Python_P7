from models import Algorithm, Combination, Item
from utils.profiling import perf_timer


class Dynamic(Algorithm):
    @property
    def name(self):
        return "dynamic"

    @perf_timer
    def compute(self, items: list[Item], capacity: int) -> Combination:
        coefficient = items[0].coefficient
        weighted_capacity = capacity * coefficient

        table = [
            [0 for w in range(weighted_capacity + 1)]
            for i in range(len(items) + 1)
        ]

        for i in range(len(items) + 1):
            for w in range(weighted_capacity + 1):
                if i == 0 or w == 0:
                    table[i][w] = 0
                elif items[i - 1].weighted_weight <= w:
                    table[i][w] = max(
                        items[i - 1].weighted_value
                        + table[i - 1][w - items[i - 1].weighted_weight],
                        table[i - 1][w],
                    )
                else:
                    table[i][w] = table[i - 1][w]

        max_value = table[len(items)][weighted_capacity]

        knapsack_items = []
        w = weighted_capacity

        for i in range(len(items), 0, -1):
            if max_value <= 0:
                break

            if max_value == table[i - 1][w]:
                continue
            else:
                knapsack_items.append(items[i - 1])
                max_value -= items[i - 1].weighted_value
                w = w - items[i - 1].weighted_weight

        return Combination(knapsack_items)