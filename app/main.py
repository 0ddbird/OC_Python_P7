from _decimal import getcontext
from algorithms import compute
from algorithms.dynamic import Dynamic
from utils.factory import PythonItemFactory, RustItemFactory
from models import LangChoice
from utils.input import get_params
from utils.output import write_to_text, print_to_terminal

getcontext().prec = 8


def main():
    filename, path, capacity, lang, algorithm, write, log = get_params()

    if lang == LangChoice.Python:
        factory = PythonItemFactory(lang, path)
    else:
        factory = RustItemFactory(lang, path)

    get_coefficient = False
    if isinstance(algorithm, Dynamic):
        get_coefficient = True

    items = factory.build_items(get_coefficient=get_coefficient)

    combination = compute(algorithm, items, capacity)

    if log:
        print_to_terminal(combination)

    if write:
        write_to_text(filename, combination, algorithm)


if __name__ == "__main__":
    main()
