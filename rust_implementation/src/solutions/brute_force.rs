use itertools::Itertools;
use crate::models::{Item};
use std::cmp::Ordering;

pub fn brute_force(items: &[Item], max_weight: i32) -> (Vec<&Item>, f64) {
    let mut all_combinations = vec![];
    for i in 1..=items.len() {
        let combinations: Vec<Vec<&Item>> = items.iter().combinations(i).collect();
        all_combinations.extend(combinations);
    }

    let mut possible_solutions = vec![];
    for combination in &all_combinations {
        let weight: i32 = combination.iter().map(|item| item.weight).sum();
        if weight <= max_weight {
            let value: f64 = combination.iter().map(|item| item.weight as f64 * item.value).sum();
            possible_solutions.push((combination, value));
        }
    }

    let (best_solution, max_value) = possible_solutions
        .into_iter()
        .max_by(|a, b| a.1.partial_cmp(&b.1).unwrap_or(Ordering::Equal))
        .unwrap();

    let best_combination: Vec<&Item> = best_solution.to_vec();

    (best_combination, max_value)
}