use crate::models::{Item};
use pyo3::{pyfunction, PyResult};

#[pyfunction]
pub fn greedy(items: &[Item], capacity: i32) -> PyResult<Vec<&Item>> {
    let mut current_weight = 0;
    let mut combination: Vec<&Item> = vec![];

    let mut sorted_items: Vec<Vec<&Item>> = items.iter().collect();
    sorted_items.sort_by(|a, b| b.value.cmp(&a.value));

    for &item in sorted_items {
        if current_weight + item.weight <= capacity {
            current_weight += item.weight;
            combination.push(item);
        }
    }
    Ok(combination)
}