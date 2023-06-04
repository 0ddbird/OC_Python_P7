from _decimal import getcontext

from algorithms import compute
from utils.factory import get_cleaned_items
from utils.input import get_params
from utils.output import write_to_text

getcontext().prec = 6


def main():
    filename, path, max_weight, algorithm, write = get_params()
    items = get_cleaned_items(path)
    combination = compute(algorithm, items, max_weight)
    if write:
        write_to_text(filename, combination, algorithm)
    else:
        print(combination)


if __name__ == "__main__":
    main()
