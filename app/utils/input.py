import sys
from pathlib import Path

import questionary
from algorithms.py.py_brute_force import PyBruteForce
from algorithms.py.py_dynamic import PyDynamic
from algorithms.py.py_greedy import PyGreedy
from models import Algorithm, LangChoice


def valid_args_count(args: list[str]) -> bool:
    return len(args) > 3


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
    if algo_arg not in ["--bf", "--dp", "--gr"]:
        print(f"{algo_arg} is not a valid choice\n" f"Choices: --bf | --dp | --gr")
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
    implementations = {
        LangChoice.Python: {
            "Brute Force": PyBruteForce(lang_choice),
            "Dynamic Programming": PyDynamic(lang_choice),
            "Greedy": PyGreedy(lang_choice),
        }
    }

    if lang_choice == LangChoice.Rust:
        from algorithms.rs.rs_brute_force import RsBruteForce
        from algorithms.rs.rs_dynamic import RsDynamic
        from algorithms.rs.rs_greedy import RsGreedy

        implementations[LangChoice.Rust] = {
            "Brute Force": RsBruteForce(lang_choice),
            "Dynamic Programming": RsDynamic(lang_choice),
            "Greedy": RsGreedy(lang_choice),
        }

    return implementations[lang_choice][algo]


def get_algorithm(algo_arg: str) -> str:
    algo_choice_dict = {
        "--bf": "Brute Force",
        "--dp": "Dynamic Programming",
        "--gr": "Greedy",
    }

    if algo_arg not in algo_choice_dict:
        print(f"{algo_arg} is not a valid choice\n" f"Choices: --bf | --dp | --gr")
        exit(1)
    return algo_choice_dict[algo_arg]


def prompt_params() -> tuple[str, Path, int, Algorithm, bool]:
    filename = questionary.select(
        "Please enter the filename:", choices=["dataset0", "dataset1", "dataset2"]
    ).ask()
    path = get_dataset_path(filename)

    capacity = questionary.text(
        "Please enter the capacity (0-500):",
        validate=lambda x: x.isdigit() and int(x) in range(0, 501),
    ).ask()
    capacity = get_max_weight(capacity)

    algo = questionary.select(
        "Choose an algorithm:", choices=["Brute Force", "Dynamic Programming", "Greedy"]
    ).ask()

    lang_choice_dict = {"Python": LangChoice.Python, "Rust": LangChoice.Rust}
    lang_friendly = questionary.select(
        "Choose a programming language:", choices=list(lang_choice_dict.keys())
    ).ask()
    lang = lang_choice_dict[lang_friendly]

    implementation = get_implementation(algo, lang)

    options = questionary.checkbox(
        "Options:", choices=["Generate text output", "Print to the console"]
    ).ask()
    write = "Generate text output" in options
    log = "Print to the console" in options

    return filename, path, capacity, lang, implementation, write, log


def get_params() -> tuple[str, Path, int, Algorithm, bool]:
    valid_count = valid_args_count(sys.argv)
    if valid_count:
        (_, filename, capacity, algo_arg, lang_arg, *remaining) = sys.argv
        path = get_dataset_path(filename)
        capacity = get_max_weight(capacity)
        algo = get_algorithm(algo_arg)
        lang = get_lang(lang_arg)
        implementation = get_implementation(algo, lang)
        write, log = get_optional_flags(remaining)
    else:
        print("Switching to interactive prompt since arguments are missing")
        filename, path, capacity, lang, implementation, write, log = prompt_params()
    return filename, path, capacity, lang, implementation, write, log
