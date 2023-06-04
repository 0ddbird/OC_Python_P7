import os
import sys
from pathlib import Path

from algorithms.brute_force import BruteForce
from algorithms.dynamic import Dynamic
from algorithms.greedy import Greedy
from models import Algorithm


def validate_args_count(args: list[str]) -> None:
    if len(args) < 3:
        print(
            "Usage: python main.py <dataset_file_name> "
            "<max_weight> [bruteforce | dp | greedy]"
        )
        exit(1)


def get_dataset_path(dataset_path_arg: str) -> Path:
    dataset_path = Path(f"../project_data/datasets/{dataset_path_arg}.csv")
    if not dataset_path.is_file():
        print(f"File {dataset_path} not found.")
        exit(1)
    return dataset_path


def get_max_weight(max_weight_arg: str) -> int:
    try:
        max_weight = int(max_weight_arg)
        if max_weight <= 0:
            raise ValueError
        return max_weight
    except ValueError:
        print(f"{max_weight_arg} is not a valid maximum weight.")
        exit(1)


def get_implementation(implementation_arg: str) -> Algorithm:
    if implementation_arg not in ["bruteforce", "dp", "greedy"]:
        print(
            f"{implementation_arg} is not a valid choice\n"
            f"Choices: bruteforce | dp | greedy"
        )
        exit(1)

    match implementation_arg:
        case "bruteforce":
            return BruteForce()
        case "dp":
            return Dynamic()
        case "greedy":
            return Greedy()
        case _:
            return Dynamic()


def get_optional_flags(args: list[str]) -> bool:
    if "-w" in args:
        return True
    return False


def get_params() -> tuple[str, Path, int, Algorithm, bool]:
    validate_args_count(sys.argv)

    filename = sys.argv[1]
    max_weight = sys.argv[2]
    implementation_arg = sys.argv[3]

    path = get_dataset_path(filename)
    max_weight = get_max_weight(max_weight)
    implementation = get_implementation(implementation_arg)
    write = get_optional_flags(sys.argv)

    return filename, path, max_weight, implementation, write
