import os
import sys
from pathlib import Path

from algorithms.brute_force import BruteForce
from algorithms.dynamic import Dynamic
from algorithms.greedy import Greedy
from models import Algorithm, LangChoice


def validate_args_count(args: list[str]) -> None:
    if len(args) < 3:
        print(
            "Usage: python main.py <dataset_file_name> "
            "<max_weight> [bf | dp | greedy]"
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


def get_algorithm(algo_arg: str) -> Algorithm:
    if algo_arg not in ["bf", "dp", "gr"]:
        print(f"{algo_arg} is not a valid choice\n" f"Choices: bf | dp | gr")
        exit(1)
    return algo_arg


def get_lang(lang) -> LangChoice:
    try:
        return LangChoice(lang)
    except ValueError:
        print(f"{lang} is not a valid choice\n" f"Choices: --py | --rs")
        exit(1)


def get_optional_flags(args: list[str]) -> bool:
    write = False
    log = False
    if "-w" in args:
        write = True
    if "-p" in args:
        log = True
    return write, log


def get_implementation(algo, lang_choice):
    match algo:
        case "bf":
            return BruteForce(lang_choice)
        case "dp":
            return Dynamic(lang_choice)
        case "gr":
            return Greedy(lang_choice)
        case _:
            return Dynamic(lang_choice)


def get_params() -> tuple[str, Path, int, Algorithm, bool]:
    validate_args_count(sys.argv)
    (_, filename, capacity, algo, lang, *remaining) = sys.argv
    path = get_dataset_path(filename)
    capacity = get_max_weight(capacity)
    algo = get_algorithm(algo)
    lang = get_lang(lang)
    implementation = get_implementation(algo, lang)
    write, log = get_optional_flags(remaining)

    return filename, path, capacity, lang, implementation, write, log
