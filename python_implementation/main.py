from models import ImplChoice
from solutions.brute_force import brute_force
from solutions.dynamic import dynamic_programming
from solutions.genetic import genetic_algorithm
from solutions.greedy import greedy

from utils import (
    write_to_text,
    get_file_name,
    get_dataset_path,
    get_export_path,
    get_items_and_max_weight,
    choose_implementation,
)


def main():
    file_name = get_file_name()
    dataset_path = get_dataset_path(file_name)
    items, max_weight, coeff = get_items_and_max_weight(dataset_path)
    solution = choose_implementation()
    export_path = get_export_path(file_name, solution)

    match solution:
        case ImplChoice.BruteForce:
            combination = brute_force(items, max_weight, coeff)
        case ImplChoice.Greedy:
            combination = greedy(items, max_weight, coeff)
        case ImplChoice.Dynamic:
            combination = dynamic_programming(items, max_weight, coeff)
        case ImplChoice.Genetic:
            combination = genetic_algorithm(items, max_weight, coeff)
        case _:
            combination = dynamic_programming(items, max_weight, coeff)

    def generate_export_data(combination, coeff):
        for item in combination:
            item.weight = item.weight / coeff
            item.rate = item.rate * coeff

        combination_value = float(
            sum(item.value for item in combination) / coeff
        )
        return combination, combination_value

    combination, value = generate_export_data(combination, coeff)
    write_to_text(export_path, combination, value)


if __name__ == "__main__":
    main()
