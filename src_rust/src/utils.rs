use crate::models::{Item};


pub fn get_coefficient(raw_items: &[(&str, i32, f64)]) -> i32 {
    let mut dec_places = 0;
    let mut no_dec_places = true;

    for item in raw_items {
        let weight: i32 = item.1;
        let value: f64 = item.2;
        let w_dec_places: usize = weight.to_string().split(".").nth(1).unwrap_or("").len();
        let v_dec_places: usize = value.to_string().split(".").nth(1).unwrap_or("").len();
        dec_places = dec_places.max(w_dec_places).max(v_dec_places);
        let decimal_places: String = format!("{}{}", weight, value);
        if no_dec_places && decimal_places.chars().any(|digit| digit != '0') {
            no_dec_places = false;
        }
    }

    if no_dec_places {
        dec_places = 0;
    }

    return 10i32.pow(dec_places as u32);
}



pub fn item_factory(raw_items: &[(&str, i32, f64)], coefficient: i32) -> Vec<Item> {

    let mut items: Vec<Item> = vec![];

    for raw_item in raw_items {
        let (name, weight, rate): (&str, i32, f64) = *raw_item;

        if weight <= 0 || rate <= 0.0 {
            continue
        }

        let item = Item::new(name.to_string(), weight, rate, coefficient);
        match item {
            Ok(item) => {
                items.push(item)
            },
            Err(_)=> {
                continue
            }
        }

    }
    items
}