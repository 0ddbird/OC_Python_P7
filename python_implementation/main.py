from typehints import Action
from bruteforce import bruteforce
# from python_implementation.optimized import optimized_knapsack

max_cost = 500

actions: list[Action] = [
    ("action_1", 20, 0.05),
    ("action_2", 30, 0.1),
    ("action_3", 50, 0.15),
    ("action_4", 70, 0.2),
    ("action_5", 60, 0.17),
    ("action_6", 80, 0.25),
    ("action_7", 22, 0.07),
    ("action_8", 26, 0.11),
    ("action_9", 48, 0.13),
    ("action_10", 34, 0.27),
    ("action_11", 42, 0.17),
    ("action_12", 110, 0.09),
    ("action_13", 38, 0.23),
    ("action_14", 14, 0.01),
    ("action_15", 18, 0.03),
    ("action_16", 8, 0.08),
    ("action_17", 4, 0.12),
    ("action_18", 10, 0.14),
    ("action_19", 24, 0.21),
    ("action_20", 114, 0.18),
]


best_combination, total_value = bruteforce(actions, max_cost)
print(best_combination, total_value)

# second_set = optimized_knapsack(actions, max_cost)
# print(second_set)
