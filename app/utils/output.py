import os
from models import Algorithm, Combination


def write_to_text(
    filename: str,
    combination: Combination,
    algorithm: Algorithm,
) -> None:
    export_name = f"../project_data/results/{filename}_{algorithm.name}.txt"
    directory = os.path.dirname(export_name)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(export_name, "w") as text_file:
        text_file.write("Combination:\n")
        for item in combination.items:
            text_file.write(f"- {item}\n")
        text_file.write(f"Total cost: {combination.weight}\n")
        text_file.write(f"Profit: {combination.value}")

    print(f"Exported results to {export_name}")


def print_to_terminal(combination: Combination) -> None:
    for item in combination.items:
        print(
            f"{item.name}\n"
            f"{item.weight=}, {item.weighted_weight=}\n"
            f"{item.rate=}, {item.weighted_rate=}\n"
            f"{item.value=}, {item.weighted_value=}\n"
            f"{item.coefficient}"
        )
    print(f"{combination.value=}\n{combination.weight=}")
