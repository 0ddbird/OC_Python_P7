use crate::models::Item;
use pyo3::prelude::*;
use pyo3::types::{PyList, PyTuple};
use rust_decimal::prelude::*;
use rust_decimal::Decimal;

fn eval_max_dec_places(max_dec_places: i32, no_dec_places: bool, slice: &[&str]) -> (i32, bool) {
    let dec_places: usize = slice[1].len();
    let new_max_dec_places: i32 = max_dec_places.max(dec_places as i32);

    let mut new_no_dec_places: bool = no_dec_places;
    if no_dec_places && slice[1].chars().any(|c| c != '0') {
        new_no_dec_places = false;
    }

    (new_max_dec_places, new_no_dec_places)
}

pub fn item_factory(
    raw_items: &Vec<(String, String, String)>,
    coefficient: u32,
) -> Option<Vec<Item>> {
    if raw_items.is_empty() {
        return None;
    }

    Some(raw_items
        .iter()
        .filter_map(|(name, weight_str, value_str)| {
    let weight: Decimal = match Decimal::from_str(&weight_str) {
        Ok(w) => w,
        Err(e) => {
            eprintln!("Failed to parse weight: {}. Skipping item {}", e, name);
            return None;
        }
    };

    let value: Decimal = match Decimal::from_str(&value_str) {
        Ok(v) => v,
        Err(e) => {
            eprintln!("Failed to parse value: {}. Skipping item {}", e, name);
            return None;
        }
    };

    if weight <= Decimal::ZERO || value <= Decimal::ZERO {
        eprintln!(
            "Excluding invalid item: {}. Please make sure all weights and rates are greater than 0.0",
            name
        );
        None
    } else {
        match Item::new(name.clone(), weight, value, coefficient) {
            Ok(item) => Some(item),
            Err(e) => {
                eprintln!("Failed to create item {}: {}", name, e);
                None
            }
        }
    }
    })
    .collect())
}

fn extract_items(py_items: &PyList) -> Vec<(String, String, String)> {
    py_items
        .into_iter()
        .filter_map(|item| {
            let item_tuple: &PyTuple = match item.extract() {
                Ok(it) => it,
                Err(_) => return None,
            };
            match item_tuple.extract() {
                Ok((name, weight, rate)) => Some((name, weight, rate)),
                Err(_) => None,
            }
        })
        .collect()
}

#[pyfunction]
pub fn rs_build_items(py_items: &PyList, coefficient: u32) -> Option<Vec<Item>> {
    let raw_items: Vec<(String, String, String)> = extract_items(py_items);
    item_factory(&raw_items, coefficient)
}

#[pyfunction]
pub fn rs_get_coefficient(py_items: &PyList) -> u32 {
    let raw_items = extract_items(py_items);
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
