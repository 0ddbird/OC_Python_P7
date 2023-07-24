from _decimal import getcontext
from algorithms.py.py_dynamic import PyDynamic
from utils.py_factory import PythonItemFactory
from models import LangChoice
from utils.input import get_params
from utils.output import write_to_text, print_to_terminal

getcontext().prec = 8


def main():
    filename, path, capacity, lang, algorithm, write, log = get_params()
    get_coefficient = False

    if lang == LangChoice.Python:
        factory = PythonItemFactory(lang, path)
        if isinstance(algorithm, PyDynamic):
            get_coefficient = True

    else:
        from utils.rs_factory import RustItemFactory
        from algorithms.rs.rs_dynamic import RsDynamic

        factory = RustItemFactory(lang, path)
        if isinstance(algorithm, RsDynamic):
            get_coefficient = True

    items = factory.build_items(get_coefficient)
    combination = algorithm.compute(items, capacity)

    if log:
        print_to_terminal(combination)

    if write:
        write_to_text(filename, combination, algorithm)


if __name__ == "__main__":
    main()
