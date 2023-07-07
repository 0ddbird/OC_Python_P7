import csv
from pathlib import Path

from _decimal import Decimal

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


def read_from_csv(file_path: Path, coeff=False) -> list[tuple[str, str, str]]:
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        raw_items = [tuple(row) for row in reader]
        if coeff:
            coefficient = get_coefficient(raw_items)
            return raw_items, coefficient
        return raw_items


def build_items(raw_items: list[tuple[str, str, str]], coefficient: int) -> list[Item]:
    items = []

    for item in raw_items:
        name, weight, value = item
        weight = Decimal(weight)
        value = Decimal(value)

        if weight <= 0 or value <= 0:
            print(
                f"Excluding invalid item: {name}. "
                "Please make sure the weight and rate are positive values."
            )
            continue

        item = Item(name=name, weight=weight, value=value, coefficient=coefficient)
        items.append(item)

    return items
