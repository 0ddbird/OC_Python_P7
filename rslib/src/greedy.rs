use itertools::sorted;
use crate::models::Item;

pub fn greedy(items: &[Item], capacity: i32) -> Vec<&Item> {
    let mut current_weight = 0;
    let mut combination: Vec<&Item> = vec![];

    let sorted_items = items.iter().collect();
    sorted_items.sort_by(|a, b| b.value.cmp(&a.value));

    for &item in sorted_items {
        if current_weight + items.weight <= capacity {
            current_weight += item.weight;
            combination.push(item);
        }
    }
    combination
}