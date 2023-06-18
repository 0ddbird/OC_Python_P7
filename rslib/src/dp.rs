use crate::models::Item;
use std::cmp;

pub fn dynamic(items: &[Item], capacity: i32) -> Vec<&Item> {

    let coefficient: i32 = items[0].coefficient;
    let weighted_capacity: i32 = capacity * coefficient;
    let mut table:Vec<Vec<i32>> = vec![vec![0; weighted_capacity as usize + 1]; items.len() + 1];

    for i in 1..=items.len() {
        for w in 0..(weighted_capacity + 1) as usize {
            if items[i-1].weighted_weight > w as i32  {
                table[i][w] = table[i - 1][w];
            }
            else {
                table[i][w] = cmp::max(
                    items[i-1].weighted_value + table[i-1][w-(items[i-1].weighted_weight as usize)],
                    table[i-1][w]
                )
            }
        }
    }
    // Backtracking
    let mut knapsack_items: Vec<&Item> = vec![];
    let mut w: usize = weighted_capacity as usize;

    for i in (1..=items.len()).rev() {
        if table[i][w] != table[i-1][w] {
            knapsack_items.push(&items[i-1]);
            w -= items[i-1].weighted_weight as usize;
        }
    }

    knapsack_items
}

