import csv
from _decimal import Decimal
from pathlib import Path

from models import Item


def get_coefficient(raw_items: list) -> int:
    dec_places = 0
    no_dec_places = True

    for item in raw_items:
        weight = item[1]
        value = item[2]
        w_dec_places = weight.split(".")[1] if "." in weight else ""
        v_dec_places = value.split(".")[1] if "." in value else ""
        dec_places = max(dec_places, len(w_dec_places), len(v_dec_places))
        decimal_places: str = w_dec_places + v_dec_places
        if no_dec_places and any(digit != "0" for digit in decimal_places):
            no_dec_places = False

    if no_dec_places:
        dec_places = 0
    return 10**dec_places


def read_from_csv(file_path: Path) -> list[list[str, str, str]]:
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        raw_items = [row for row in reader]
        coefficient = get_coefficient(raw_items)

    return raw_items, coefficient


def item_factory(
    raw_items: list[list[str, str, str]], coefficient: int
) -> list[Item]:
    items = []

    for item in raw_items:
        name, weight, rate = item
        weight = Decimal(weight)
        rate = Decimal(rate)

        if weight <= 0 or rate <= 0:
            print(
                f"Excluding invalid item: {name}. "
                "Please make sure the weight and rate are positive values."
            )
            continue

        item = Item(
            name=name, weight=weight, rate=rate, coefficient=coefficient
        )
        items.append(item)

    return items


def get_cleaned_items(path: Path) -> list[Item, ...]:
    raw_items, coefficient = read_from_csv(path)
    items = item_factory(raw_items, coefficient)
    return items
