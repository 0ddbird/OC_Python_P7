use pyo3::prelude::*;
use pyo3::types::{PyList, PyTuple};
use rust_decimal::Decimal;
use rust_decimal::prelude::FromPrimitive;
use crate::models::Item;


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

        if rate_parts.len() == 2 {
            (max_dec_places, no_dec_places) =  eval_max_dec_places(max_dec_places, no_dec_places, &rate_parts);
            max_dec_places = max_dec_places;
            no_dec_places = no_dec_places;
        }

        if weight_parts.len() == 2 {
            (max_dec_places, no_dec_places) = eval_max_dec_places(max_dec_places, no_dec_places, &weight_parts);
            max_dec_places = max_dec_places;
            no_dec_places = no_dec_places;
        }
    }

    if no_dec_places {
        max_dec_places = 0;
    }

    10u32.pow(max_dec_places as u32)
}


pub fn item_factory(raw_items: &[(String, String, String)], coefficient: u32) -> Vec<Item> {

    let mut items: Vec<Item> = vec![];

    for raw_item in raw_items {
        let (name, weight, rate) = raw_item;
        let dec_weight: Decimal = Decimal::from_str_exact(weight).unwrap();
        let dec_rate: Decimal = Decimal::from_str_exact(rate).unwrap();

        let dec_zero: Decimal = Decimal::from_u8(0).unwrap();

        if dec_weight <= dec_zero || dec_rate <= dec_zero  {
            continue
        }

        let item = Item::new(
            name.to_string(),
            dec_weight,
            dec_rate,
            coefficient,
        );
        items.push(item)
    }
    items
}

#[pyfunction]
pub fn build_items(py_items: &PyList) -> PyResult<Vec<Item>> {
    let raw_items: Vec<(String, String, String)> = py_items.into_iter()
            .map(|item| {
                let item: &PyTuple = item.extract()?;
                let item_0: String = item.get_item(0)?.extract()?;
                let item_1: String = item.get_item(1)?.extract()?;
                let item_2: String = item.get_item(2)?.extract()?;
                Ok::<(String, String, String), PyErr>((item_0, item_1, item_2))
            })
            .collect::<Result<_, _>>()?;

    let coefficient: u32 = get_coefficient(&raw_items);
    let items: Vec<Item> = item_factory(&raw_items, coefficient);

    Ok(items)
}