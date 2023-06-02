#[derive(Debug)]
pub struct Item {
    pub name: &'static str,
    pub weight: i32,
    pub rate: f64,
    pub value: f64,
}

impl Item {
    pub fn new(name: &'static str, weight: i32, rate: f64) -> Item {
        let value = weight as f64 * rate;
        Item { name, weight, rate, value}
    }
}

pub struct Combination(Vec<Item>);