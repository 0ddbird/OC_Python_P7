from _decimal import getcontext
from algorithms import compute
from algorithms.dynamic import Dynamic
from utils.factory import PythonItemFactory, RustItemFactory
from models import LangChoice
from utils.input import get_params
from utils.output import write_to_text

getcontext().prec = 8


def main():
    get_coeff = False
    # Get execution parameters.
    filename, path, capacity, lang, algorithm, write, log = get_params()

    # Build items from CSV.
    if lang == LangChoice.Python:
        factory = PythonItemFactory(lang, path)
    else:
        factory = RustItemFactory(lang, path)

    if isinstance(algorithm, Dynamic):
        get_coeff = True

    items = factory.build_items(get_coeff=get_coeff)

    # Compute the best combination of items.
    combination = compute(algorithm, items, capacity)

    # Export the results.
    if write:
        write_to_text(filename, combination, algorithm)

    if log:
        for item in combination.items:
            print(
                f"{item.name}\n"
                f"{item.weight=}, {item.weighted_weight=}\n"
                f"{item.rate=}, {item.weighted_rate=}\n"
                f"{item.value=}, {item.weighted_value=}\n"
                f"{item.coefficient}"
            )
        print(f"{combination.value=}\n{combination.weight=}")


if __name__ == "__main__":
    main()
