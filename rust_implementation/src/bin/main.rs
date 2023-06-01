use rust_implementation::models::Item;
use rust_implementation::solutions::brute_force::brute_force;

fn main() {
    let max_weight = 500;
    let actions: Vec<Item> = vec![
        Item::new("action_1", 20, 0.05 ),
        Item::new("action_2", 30, 0.1 ),
        Item::new("action_3", 50, 0.15 ),
        Item::new("action_4", 70, 0.2 ),
        Item::new("action_5", 60, 0.17 ),
        Item::new("action_6", 80, 0.25 ),
        Item::new("action_7", 22, 0.07 ),
        Item::new("action_8", 26, 0.11 ),
        Item::new("action_9", 48, 0.13 ),
        Item::new("action_10", 34, 0.27 ),
        Item::new("action_11", 42, 0.17 ),
        Item::new("action_12", 110, 0.09 ),
        Item::new("action_13", 38, 0.23 ),
        Item::new("action_14", 14, 0.01 ),
        Item::new("action_15", 18, 0.03 ),
        Item::new("action_16", 8, 0.08 ),
        Item::new("action_17", 4, 0.12 ),
        Item::new("action_18", 10, 0.14 ),
        Item::new("action_19", 24, 0.21 ),
        Item::new("action_20", 114, 0.18 ),
    ];

    let (actions, rate) = brute_force(&actions, max_weight);

    for action in &actions {
        println!("{:?}", action);
    }
    println!("Total rate: {:?}", rate);

}
