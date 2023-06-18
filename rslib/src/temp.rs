// use src_rust::brute_force::brute_force;
use src_rust::dp::dynamic;
use src_rust::models::Item;
use src_rust::utils::{get_coefficient, item_factory};
use crate::dp::dynamic;
use crate::models::Item;
use crate::utils::{get_coefficient, item_factory};

fn main() {
    let capacity: i32 = 500;

    let raw_items: Vec<(&str, i32, f64)> = vec![
        ("action_1", 20, 0.05 ),
        ("action_2", 30, 0.1 ),
        ("action_3", 50, 0.15 ),
        ("action_4", 70, 0.2 ),
        ("action_5", 60, 0.17 ),
        ("action_6", 80, 0.25 ),
        ("action_7", 22, 0.07 ),
        ("action_8", 26, 0.11 ),
        ("action_9", 48, 0.13 ),
        ("action_10", 34, 0.27 ),
        ("action_11", 42, 0.17 ),
        ("action_12", 110, 0.09 ),
        ("action_13", 38, 0.23 ),
        ("action_14", 14, 0.01 ),
        ("action_15", 18, 0.03 ),
        ("action_16", 8, 0.08 ),
        ("action_17", 4, 0.12 ),
        ("action_18", 10, 0.14 ),
        ("action_19", 24, 0.21 ),
        ("action_20", 114, 0.18 ),
    ];

    let coefficient: i32 = get_coefficient(&raw_items);

    let items: Vec<Item> = item_factory(&raw_items, coefficient);

    // let combination = brute_force(&items, capacity);

    let combination:Vec<&Item> = dynamic(&items, capacity);

    for item in combination {
        println!("{:?}", item);
    }

    println!("Done!");

}
