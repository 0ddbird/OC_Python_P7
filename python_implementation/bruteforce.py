import itertools
from typing import List, Tuple
from typehints import Action


def bruteforce(actions: List[Action], max_weight: int) -> Tuple[List[str], float]:

    all_combinations = []
    for r in range(1, len(actions) + 1):
        combinations_object = itertools.combinations(actions, r)
        all_combinations += combinations_object

    possible_solutions = []
    for combination in all_combinations:
        weight = sum(item[1] for item in combination)
        if weight <= max_weight:
            value = sum(item[1] * item[2] for item in combination)
            possible_solutions.append((combination, value))

    best_solution = max(possible_solutions, key=lambda x: x[1])
    best_solution_actions = [item[0] for item in best_solution[0]]
    best_solution_value = best_solution[1]

    return best_solution_actions, best_solution_value
