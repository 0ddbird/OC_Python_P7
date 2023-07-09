from models import Algorithm, PyCombination, Item
from utils.profiling import perf_timer
from knapsack_rs.knapsack_rs import (
    rs_dynamic,
    Item as RsItem,
    Combination as RsCombination,
)


class Dynamic(Algorithm):
    @property
    def name(self):
        return f"Dynamic programming - {self.lang.name}"

    @perf_timer
    def py_compute(self, items: list[Item, ...], capacity: int) -> PyCombination:
        coefficient = items[0].coefficient
        weighted_capacity = int(capacity * coefficient)

        table = [
            [0 for w in range(weighted_capacity + 1)] for i in range(len(items) + 1)
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

        return PyCombination(knapsack_items)

    @perf_timer
    def rs_compute(self, items: list[RsItem, ...], capacity: int) -> RsCombination:
        return rs_dynamic(items, capacity)
