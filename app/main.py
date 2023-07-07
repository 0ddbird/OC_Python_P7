from _decimal import getcontext

from src_rust_lib import src_rust_lib as rs_factory

from algorithms import compute
from models import LangChoice
import utils.factory as py_factory
from utils.factory import read_from_csv
from utils.input import get_params
from utils.output import write_to_text

getcontext().prec = 6


def main():
    filename, path, capacity, lang, implementation, write, log = get_params()

    raw_items, coefficient = read_from_csv(path, coeff=True)

    if lang == LangChoice.Python:
        items = py_factory.build_items(raw_items, coefficient)
    else:
        items = rs_factory.build_items(raw_items)

    combination = compute(implementation, items, capacity)

    if write:
        write_to_text(filename, combination, implementation)

    if log:
        print(combination)


if __name__ == "__main__":
    main()
