use crate::models::{Combination, Item};
use pyo3::{pyfunction, PyResult};
use rust_decimal::prelude::FromPrimitive;
use rust_decimal::Decimal;

struct TempCombination<'a> {
    items: Vec<&'a Item>,
    value: Decimal,
    weight: Decimal,
}

impl<'a> TempCombination<'a> {
    fn new() -> Self {
        Self {
            items: Vec::new(),
            value: Decimal::from_i32(0).expect("Cannot convert 0 to Decimal"),
            weight: Decimal::from_i32(0).expect("Cannot convert 0 to Decimal"),
        }
    }

    fn add_item(&mut self, item: &'a Item) {
        self.items.push(item);
        self.value += item.value;
        self.weight += item.weight;
    }
}

struct Tracker<'a> {
    combination: TempCombination<'a>,
    value: Decimal,
    weight: Decimal,
}

impl<'a> Tracker<'a> {
    fn new() -> Self {
        Self {
            combination: TempCombination::new(),
            value: Decimal::from_i32(0).expect("Cannot convert 0 to Decimal"),
            weight: Decimal::from_i32(0).expect("Cannot convert 0 to Decimal"),
        }
    }

    fn set_new_best(&mut self, combination: TempCombination<'a>) {
        self.combination = combination;
        self.value = self.combination.value;
        self.weight = self.combination.weight;
    }
}

#[pyfunction]
pub fn rs_brute_force(items: Vec<Item>, capacity: i32) -> PyResult<Combination> {
    let decimal_capacity =
        Decimal::from_i32(capacity).expect("Cannot convert capacity from capacity");
    let mut tracker = Tracker::new();
    let n = items.len();

    for i in 1..(2u32.pow(n as u32)) {
        let mut combination = TempCombination::new();

        for j in 0..n {
            if (i >> j) & 1 == 1 {
                let item = &items[j];
                if combination.weight + item.weight > decimal_capacity {
                    break;
                }
                combination.add_item(item);
            }
        }

        if combination.value > tracker.value {
            tracker.set_new_best(combination);
        }
    }

    let selected_items = tracker
        .combination
        .items
        .into_iter()
        .map(|item| item.clone())
        .collect();

    Ok(Combination::new(selected_items))
}
