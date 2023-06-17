use std::fmt;
use std::fmt::{Debug, Display, Formatter};
use rust_decimal::Decimal;
use rust_decimal::prelude::{FromPrimitive, ToPrimitive};

fn compute_weighted_rate(rate: Decimal, coefficient: i32) -> Result<i32, ConversionError> {
    match rate.to_f64() {
        Some(f) => Ok((f * (coefficient as f64)).round() as i32),
        None => Err(ConversionError),
    }
}

#[derive(Debug, Clone)]
pub struct Item {
    pub name: String,
    pub weight: i32,
    pub rate: Decimal,
    pub value: Decimal,
    pub coefficient: i32,
    pub weighted_weight: i32,
    pub weighted_rate: i32,
    pub weighted_value: i32,
}

impl Item {
    pub fn new(name: String, weight: i32, f_rate: f64, coefficient: i32) -> Result<Item, ConversionError> {

        let rate: Decimal = Decimal::from_f64(f_rate).unwrap() / Decimal::from(coefficient);
        let value: Decimal = Decimal::from(weight) * rate;
        let weighted_weight: i32 = weight * coefficient;


        match compute_weighted_rate(rate, coefficient) {
            Ok(weighted_rate) => {
                let weighted_value: i32 = weighted_weight * weighted_rate;
                Ok(Item { name, weight, rate, value, coefficient, weighted_weight, weighted_rate, weighted_value})
            },
            Err(e) => {
                println!("Error: {}", e);
                Err(e)
            }
        }
    }
}

pub struct Combination(Vec<Item>);

pub struct ConversionError;


impl Display for ConversionError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Failed to convert rate to f64")
    }
}

impl Debug for ConversionError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "Failed to convert rate to f64")
    }
}

impl std::error::Error for ConversionError {}

