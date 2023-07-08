use crate::models::{Combination, Item};
use pyo3::{pyfunction, PyResult};
use rust_decimal::prelude::FromPrimitive;
use rust_decimal::Decimal;
use std::cmp::Ordering;

fn get_all_combinations(items: &Vec<Item>) -> Vec<Vec<Item>> {
    let n = items.len();
    let mut combinations = vec![];

    for i in 1..(2u32.pow(n as u32)) {
        let mut combination = vec![];
        for j in 0..n {
            if (i >> j) & 1 == 1 {
                combination.push(items[j].clone());
            }
        }
        combinations.push(combination);
    }

    combinations
}

#[pyfunction]
pub fn rs_brute_force(items: Vec<Item>, capacity: i32) -> PyResult<Combination> {
    let dec_capacity = Decimal::from_i32(capacity).expect("Cannot convert capacity");
    let all_combinations: Vec<Vec<Item>> = get_all_combinations(&items);

    let mut possible_solutions: Vec<(Vec<Item>, Decimal)> = vec![];
    for combination in &all_combinations {
        let weight: Decimal = combination.iter().map(|item| item.weight).sum();
        if weight <= dec_capacity {
            let value: Decimal = combination.iter().map(|item| item.value).sum();
            possible_solutions.push((combination.clone(), value));
        }
    }

    let best_solution: Option<(Vec<Item>, Decimal)> = possible_solutions
        .into_iter()
        .max_by(|a, b| a.1.partial_cmp(&b.1).unwrap_or(Ordering::Equal));

    let best_combination: Vec<Item> = if let Some((combination, _)) = best_solution {
        combination
    } else {
        vec![]
    };

    Ok(Combination::new(best_combination))
}
