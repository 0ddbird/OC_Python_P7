use itertools::Itertools;
use crate::models::Action;
use std::cmp::Ordering;

pub fn bruteforce(actions: &[Action], max_weight: i32) -> (Vec<&Action>, f64) {
    let mut all_combinations = vec![];
    for i in 1..=actions.len() {
        let combinations: Vec<Vec<&Action>> = actions.iter().combinations(i).collect();
        all_combinations.extend(combinations);
    }

    let mut possible_solutions = vec![];
    for combination in &all_combinations {
        let weight: i32 = combination.iter().map(|action| action.cost).sum();
        if weight <= max_weight {
            let value: f64 = combination.iter().map(|action| action.cost as f64 * action.value).sum();
            possible_solutions.push((combination, value));
        }
    }

    let (best_solution, best_value) = possible_solutions
        .into_iter()
        .max_by(|a, b| a.1.partial_cmp(&b.1).unwrap_or(Ordering::Equal))
        .unwrap();

    let best_solution_actions: Vec<&Action> = best_solution.to_vec();

    (best_solution_actions, best_value)
}