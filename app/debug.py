def print_rs_items(items: list[dict]):
    keys = [
        "name",
        "weight",
        "weighted_weight",
        "rate",
        "weighted_rate",
        "value",
        "weighted_value",
        "coefficient",
    ]

    for dict_ in items:
        (
            name,
            weight,
            weighted_weight,
            rate,
            weighted_rate,
            value,
            weighted_value,
            coefficient,
        ) = [dict_.get(key, "Not found") for key in keys]

        print(
            "-----------------\n"
            f"{name=}\n"
            f"{weight=}\n"
            f"{weighted_weight=}\n"
            f"{rate=}\n"
            f"{weighted_rate=}\n"
            f"{value=}\n"
            f"{weighted_value=}\n"
            f"{coefficient=}\n"
            "-----------------\n"
        )
