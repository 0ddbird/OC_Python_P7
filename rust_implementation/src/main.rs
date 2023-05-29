use rust_implementation::models::Action;
use rust_implementation::bruteforce::bruteforce;

fn main() {
    let max_weight = 500;
    let actions: Vec<Action> = vec![
        Action { name: "action_1", cost: 20, value: 0.05 },
        Action { name: "action_2", cost: 30, value: 0.1 },
        Action { name: "action_3", cost: 50, value: 0.15 },
        Action { name: "action_4", cost: 70, value: 0.2 },
        Action { name: "action_5", cost: 60, value: 0.17 },
        Action { name: "action_6", cost: 80, value: 0.25 },
        Action { name: "action_7", cost: 22, value: 0.07 },
        Action { name: "action_8", cost: 26, value: 0.11 },
        Action { name: "action_9", cost: 48, value: 0.13 },
        Action { name: "action_10", cost: 34, value: 0.27 },
        Action { name: "action_11", cost: 42, value: 0.17 },
        Action { name: "action_12", cost: 110, value: 0.09 },
        Action { name: "action_13", cost: 38, value: 0.23 },
        Action { name: "action_14", cost: 14, value: 0.01 },
        Action { name: "action_15", cost: 18, value: 0.03 },
        Action { name: "action_16", cost: 8, value: 0.08 },
        Action { name: "action_17", cost: 4, value: 0.12 },
        Action { name: "action_18", cost: 10, value: 0.14 },
        Action { name: "action_19", cost: 24, value: 0.21 },
        Action { name: "action_20", cost: 114, value: 0.18 },
    ];

    let (actions, value) = bruteforce(&actions, max_weight);

    for action in &actions {
        println!("{:?}", action);
    }
    println!("Total value: {:?}", value);

}
