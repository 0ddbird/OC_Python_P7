use crate::models::{Combination, Item};
use pyo3::{pyfunction, PyResult};
use rust_decimal::prelude::FromPrimitive;
use rust_decimal::Decimal;
use rust_decimal_macros::dec;

#[pyfunction]
pub fn rs_greedy(items: Vec<Item>, capacity: i32) -> PyResult<Combination> {
    let dec_capacity = Decimal::from_i32(capacity).unwrap();
    let mut current_weight: Decimal = dec!(0);
    let mut selected_items: Vec<Item> = vec![];

    let mut sorted_items: Vec<Item> = items.iter().cloned().collect();

    sorted_items.sort_by(|a, b| b.value.cmp(&a.value));

    for item in sorted_items {
        if current_weight + item.weight <= dec_capacity {
            current_weight += item.weight;
            selected_items.push(item);
        }
    }

    Ok(Combination::new(selected_items))
}
