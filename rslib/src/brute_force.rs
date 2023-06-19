use itertools::Itertools;
use crate::models::{Item};
use std::cmp::Ordering;
use rust_decimal::Decimal;
use pyo3::{pyfunction, PyResult};

#[pyfunction]
pub fn brute_force(items: &[Item], capacity: i32) -> PyResult<Vec<&Item>> {
    let mut all_combinations:Vec<Vec<&Item>> = vec![];
    for i in 1..=items.len() {
        let combinations: Vec<Vec<&Item>> = items.iter().combinations(i).collect();
        all_combinations.extend(combinations);
    }

    let mut possible_solutions:Vec<(&Vec<&Item>, Decimal)> = vec![];
    for combination in &all_combinations {
        let weight: i32 = combination.iter().map(|item| item.weight).sum();
        if weight <= capacity {
            let value: Decimal = combination.iter().map(|item| Decimal::from(item.weight) * item.value).sum();

            possible_solutions.push((combination, value));
        }
    }

    let best_solution:Option<(&Vec<&Item>, Decimal)> = possible_solutions
        .into_iter()
        .max_by(|a, b| a.1.partial_cmp(&b.1).unwrap_or(Ordering::Equal));

    let best_combination: Vec<&Item> = if let Some((combination, _)) = best_solution {
    combination.clone()
    } else {
        vec![]
    };

    Ok(best_combination)
}