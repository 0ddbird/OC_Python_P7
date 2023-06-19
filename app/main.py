from _decimal import getcontext
from src_rust_lib import build_items;
from algorithms import compute
from utils.factory import get_cleaned_items
from utils.input import get_params
from utils.output import write_to_text

getcontext().prec = 6


def main():

    # --------------------------------------
    # Temporary - testing Rust bindings
    raw_items = [
        ('Action_1', '2.0', '1.0'),
        ('Action_2', '3.1', '1.2'),
    ]
    rs_items = build_items(raw_items)

    keys = ["name", 'value', 'rate', 'coefficient']
    for dict_ in rs_items:
        name, value, rate, coefficient = [dict_.get(key) for key in keys]
        print(name, value, rate, coefficient)
    # --------------------------------------

    filename, path, max_weight, algorithm, write = get_params()
    items = get_cleaned_items(path)
    combination = compute(algorithm, items, max_weight)
    if write:
        write_to_text(filename, combination, algorithm)
    else:
        print(combination)


if __name__ == "__main__":
    main()
