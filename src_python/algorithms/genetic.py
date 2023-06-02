from models import Item
from utils import perf_timer


@perf_timer
def genetic_algorithm(
    items: list[Item],
    max_weight: int,
    coeff: int,
) -> list[Item]:
    raise NotImplementedError
