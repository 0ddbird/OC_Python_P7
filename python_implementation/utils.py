import os
import csv
import sys
import time
from functools import wraps

from models import Item, ImplChoice


def perf_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"{func.__name__} execution time: {end_time - start_time} seconds"
        )
        return result

    return wrapper


def calc_multiplication_coefficient(data):
    max_decimal_places = 0
    all_zeros = True

    for row in data:
        for value in row[1:]:
            decimal_places = (
                str(value).split(".")[1] if "." in str(value) else ""
            )
            max_decimal_places = max(max_decimal_places, len(decimal_places))

            if all_zeros and any(digit != "0" for digit in decimal_places):
                all_zeros = False

    if all_zeros:
        max_decimal_places = 0

    return 10**max_decimal_places


def read_from_csv(file_path: str):
    items = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = [row for row in reader]

    coeff = calc_multiplication_coefficient(data)
    for row in data:
        name, weight, rate = row
        weight = int(float(weight) * coeff)
        rate = float(rate) / coeff
        if weight <= 0 or rate <= 0:
            continue
        items.append(Item(name=name, weight=weight, rate=rate))

    return items, coeff


def write_to_text(file_path, best_combination, total_value):
    directory = os.path.dirname(file_path)
    total_weight = sum(item.weight for item in best_combination)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, "w") as text_file:
        text_file.write("Best Combination:\n")
        for item in best_combination:
            text_file.write(f"- {item}\n")
        text_file.write(f"Total cost: {total_weight}\n")
        text_file.write(f"Profit: {total_value}")


def get_file_name():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(
            "Usage: python main.py <dataset_file_name> "
            "<max_weight> [--bruteforce | --dp | --greedy]"
        )
        return None
    return sys.argv[1]


def get_dataset_path(file_name):
    if file_name is None:
        return None
    return f"../datasets/{file_name}.csv"


def get_export_path(file_name: str, solution: ImplChoice):
    if file_name is None:
        return None
    return f"../exports/python/{file_name}_{solution.name}_result.txt"


def get_max_weight():
    try:
        given_max_weight = int(sys.argv[2])
    except ValueError:
        print("Error: max_weight must be an integer")
        return None
    return given_max_weight


def get_items_and_max_weight(dataset_path):
    try:
        items, coeff = read_from_csv(dataset_path)
    except FileNotFoundError:
        print("Error: file was not found")
        return None, None
    max_weight = int(get_max_weight() * coeff)
    return items, max_weight, coeff


def choose_implementation() -> ImplChoice:
    if len(sys.argv) == 4:
        implementation_arg = sys.argv[3]
        match implementation_arg:
            case "--bruteforce":
                return ImplChoice.BruteForce
            case "--dp":
                return ImplChoice.Dynamic
            case "--greedy":
                return ImplChoice.Greedy
            case _:
                print(
                    "Error: Invalid solution option. "
                    "Please use either '--bruteforce', '--dp' or '--greedy'."
                )
                return None
