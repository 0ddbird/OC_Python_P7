use crate::models::{Combination, Item};
use pyo3::prelude::*;

mod brute_force;
mod dp;
mod greedy;
mod item_factory;
mod models;
mod utils;

#[pymodule]
fn knapsack_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Item>()?;
    m.add_class::<Combination>()?;
    m.add_function(wrap_pyfunction!(item_factory::rs_build_items, m)?)?;
    m.add_function(wrap_pyfunction!(utils::rs_print_items, m)?)?;
    m.add_function(wrap_pyfunction!(brute_force::rs_brute_force, m)?)?;
    m.add_function(wrap_pyfunction!(greedy::rs_greedy, m)?)?;
    m.add_function(wrap_pyfunction!(dp::rs_dynamic, m)?)?;
    m.add_function(wrap_pyfunction!(item_factory::rs_get_coefficient, m)?)?;
    Ok(())
}
