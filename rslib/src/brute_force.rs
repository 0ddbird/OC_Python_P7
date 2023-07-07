use crate::models::Item;
use itertools::Itertools;
use pyo3::types::PyList;
use pyo3::{pyfunction, FromPyObject, IntoPy, PyObject, PyResult, Python};
use rust_decimal::prelude::FromPrimitive;
use rust_decimal::Decimal;
use std::cmp::Ordering;

#[pyfunction]
pub fn brute_force(py: Python, py_items: &PyList, capacity: i32) -> PyResult<Vec<PyObject>> {
    let items: Vec<Item> = py_items
        .iter()
        .map(|py_item| Item::extract(py_item).unwrap())
        .collect();

    let dec_capacity = Decimal::from_i32(capacity).expect("Cannot convert capacity");
    let mut all_combinations: Vec<Vec<Item>> = vec![];
    for i in 1..=items.len() {
        let combinations: Vec<Vec<Item>> = items.iter().cloned().combinations(i).collect();
        all_combinations.extend(combinations);
    }

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

    let py_items: Vec<PyObject> = best_combination
        .into_iter()
        .map(|item| item.into_py(py))
        .collect();

    Ok(py_items)
}
