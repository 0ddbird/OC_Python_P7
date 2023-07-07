use pyo3::prelude::*;

mod brute_force;
mod item_factory;
mod models;
mod utils;

/// A Python module implemented in Rust.
#[pymodule]
fn src_rust_lib(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(item_factory::build_items, m)?)?;
    m.add_function(wrap_pyfunction!(utils::print_items, m)?)?;
    m.add_function(wrap_pyfunction!(brute_force::brute_force, m)?)?;
    // m.add_function(wrap_pyfunction!(greedy::greedy,m)?)?;
    // m.add_function(wrap_pyfunction!(dp::dynamic,m)?)?;

    Ok(())
}
