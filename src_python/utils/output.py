import os

from models import Combination, Algorithm


def write_to_text(
    filename: str, combination: Combination, algorithm: Algorithm
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
