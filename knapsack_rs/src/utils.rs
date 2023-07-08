use crate::models::Item;
use pyo3::prelude::*;
use pyo3::types::PyList;

#[pyfunction]
pub fn rs_print_items(py_items: &PyList) -> PyResult<()> {
    let mut items = vec![];
    for py_item in py_items {
        let item = Item::extract(py_item)?;
        items.push(item);
    }

    for item in items {
        println!("{}", item);
    }
    Ok(())
}
