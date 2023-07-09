use pyo3::{pyfunction, PyResult};
use crate::models::{Combination, Item};
use std::cmp;

#[pyfunction]
pub fn rs_dynamic(items: Vec<Item>, capacity: usize) -> PyResult<Combination> {
    let coefficient: usize = items[0].coefficient as usize;
    let weighted_capacity: usize = capacity * coefficient;
    let mut table:Vec<Vec<usize>> = vec![vec![0; weighted_capacity as usize + 1]; items.len() + 1];

    for i in 1..=items.len() {
        for w in 0..=weighted_capacity {
            if items[i-1].weighted_weight > w as u64  {
                table[i][w] = table[i - 1][w];
            }
            else {
                table[i][w] = cmp::max(
                    items[i-1].weighted_value as usize + table[i-1][w - (items[i-1].weighted_weight as usize)],
                    table[i-1][w]
                )
            }
        }
    }
    // Backtracking
    let mut knapsack_items: Vec<Item> = vec![];
    let mut w: usize = weighted_capacity;

    for i in (1..=items.len()).rev() {
        if table[i][w] != table[i-1][w] {
            knapsack_items.push(items[i-1].clone());
            w -= items[i-1].weighted_weight as usize;
        }
    }

    Ok(Combination::new(knapsack_items))
}
