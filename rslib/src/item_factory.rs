use crate::models::{Item, ItemCreationError};
use pyo3::prelude::*;
use pyo3::types::{PyList, PyTuple};
use rust_decimal::Decimal;
use std::str::FromStr;

fn eval_max_dec_places(max_dec_places: i32, no_dec_places: bool, slice: &[&str]) -> (i32, bool) {
    let dec_places: usize = slice[1].len();
    let new_max_dec_places: i32 = max_dec_places.max(dec_places as i32);

    let mut new_no_dec_places: bool = no_dec_places;
    if no_dec_places && slice[1].chars().any(|c| c != '0') {
        new_no_dec_places = false;
    }

    (new_max_dec_places, new_no_dec_places)
}

fn get_coefficient(raw_items: &[(String, String, String)]) -> u32 {
    let mut max_dec_places: i32 = 0;
    let mut no_dec_places: bool = true;

    for raw_item in raw_items {
        let (_, weight, rate) = raw_item;
        let weight_parts: Vec<&str> = weight.split('.').collect();
        let rate_parts: Vec<&str> = rate.split('.').collect();

        let mut max_dec_places_rate = max_dec_places;
        let mut max_dec_places_weight = max_dec_places;

        if rate_parts.len() == 2 {
            let (temp_max_dec_places, temp_no_dec_places) =
                eval_max_dec_places(max_dec_places_rate, no_dec_places, &rate_parts);
            max_dec_places_rate = temp_max_dec_places;
            no_dec_places = temp_no_dec_places;
        }

        if weight_parts.len() == 2 {
            let (temp_max_dec_places, temp_no_dec_places) =
                eval_max_dec_places(max_dec_places_weight, no_dec_places, &weight_parts);
            max_dec_places_weight = temp_max_dec_places;
            no_dec_places = temp_no_dec_places;
        }

        max_dec_places = std::cmp::max(max_dec_places_rate, max_dec_places_weight);
    }

    if no_dec_places {
        max_dec_places = 0;
    }

    10u32.pow(max_dec_places as u32)
}

pub fn item_factory(
    raw_items: &[(String, String, String)],
    coefficient: u32,
) -> Result<Vec<Item>, PyErr> {
    raw_items
        .iter()
        .map(|(name, weight, value)| {
            let dec_weight = Decimal::from_str(weight)
                .map_err(|e| {
                    ItemCreationError::DecimalParseError("Failed to parse weight".to_string(), e)
                })
                .map_err(|e: ItemCreationError| {
                    PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!("{}", e))
                })?;

            let dec_value = Decimal::from_str(value)
                .map_err(|e| {
                    ItemCreationError::DecimalParseError("Failed to parse value".to_string(), e)
                })
                .map_err(|e: ItemCreationError| {
                    PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!("{}", e))
                })?;

            Item::new(name.to_string(), dec_weight, dec_value, coefficient).map_err(
                |e: ItemCreationError| {
                    PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!("{}", e))
                },
            )
        })
        .collect()
}

#[pyfunction]
pub fn build_items(py_items: &PyList) -> PyResult<Vec<Item>> {
    let raw_items: Vec<(String, String, String)> = py_items
        .into_iter()
        .map(|item| {
            let item: &PyTuple = item.extract()?;
            let item_0: String = item.get_item(0)?.extract()?;
            let item_1: String = item.get_item(1)?.extract()?;
            let item_2: String = item.get_item(2)?.extract()?;
            Ok::<(String, String, String), PyErr>((item_0, item_1, item_2))
        })
        .collect::<Result<_, _>>()?;

    let coefficient: u32 = get_coefficient(&raw_items);
    let items: Vec<Item> = item_factory(&raw_items, coefficient)?;

    Ok(items)
}
