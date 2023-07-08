use pyo3::exceptions::PyTypeError;
use pyo3::{pyclass, pymethods, PyErr, PyResult};
use rust_decimal::prelude::{FromPrimitive, ToPrimitive};
use rust_decimal::Decimal;
use std::fmt::{Debug, Display, Formatter, Result};

#[pyclass]
#[derive(Clone)]
pub struct Item {
    #[pyo3(get, set)]
    pub name: String,
    #[pyo3(get, set)]
    pub weight: Decimal,
    #[pyo3(get, set)]
    pub rate: Decimal,
    #[pyo3(get, set)]
    pub coefficient: u32,
    #[pyo3(get, set)]
    pub weighted_weight: u64,
    #[pyo3(get, set)]
    pub weighted_rate: u64,
    #[pyo3(get, set)]
    pub value: Decimal,
    #[pyo3(get, set)]
    pub weighted_value: u64,
}

#[pymethods]
impl Item {
    #[new]
    pub fn new(name: String, weight: Decimal, rate: Decimal, coefficient: u32) -> PyResult<Self> {
        let coefficient_dec: Decimal = Decimal::from_u32(coefficient).ok_or_else(|| {
            PyErr::new::<PyTypeError, _>("Failed to convert coefficient to Decimal")
        })?;

        let dec_weighted_weight: Decimal = weight * coefficient_dec;
        let dec_weighted_rate: Decimal = rate * coefficient_dec;

        let weighted_weight: u64 = dec_weighted_weight
            .to_u64()
            .ok_or_else(|| PyErr::new::<PyTypeError, _>("Weight out of range"))?;

        let weighted_rate: u64 = dec_weighted_rate
            .to_u64()
            .ok_or_else(|| PyErr::new::<PyTypeError, _>("Value out of range"))?;

        let value: Decimal =
            weight * rate / Decimal::from_u8(100).unwrap();

        let weighted_value: u64 = weighted_weight
            * weighted_rate
                .to_u64()
                .ok_or_else(|| PyErr::new::<PyTypeError, _>("Invalid weighted value"))?;

        Ok(Item {
            name,
            weight,
            rate,
            value,
            coefficient,
            weighted_weight,
            weighted_rate,
            weighted_value,
        })
    }


    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("Item(name={}, weight={}, value={})", self.name, self.weight, self.value))
    }

    fn __str__(&self) -> PyResult<String> {
        Ok(format!("{}, {}, {}", self.name, self.weight, self.value))
    }
}

impl Display for Item {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "{}, {}, {}", self.name, self.weight, self.value)
    }
}

impl Debug for Item {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        f.debug_struct("Item")
         .field("name", &self.name)
         .field("weight", &self.weight)
         .field("value", &self.value)
         .finish()
    }
}

#[pyclass]
pub struct Combination {
    items: Vec<Item>,
}

#[pymethods]
impl Combination {
    #[new]
    pub fn new(items: Vec<Item>) -> Self {
        Combination { items }
    }

    #[getter]
    pub fn get_items(&self) -> Vec<Item> {
        self.items.clone()
    }

    #[getter]
    pub fn get_weight(&self) -> Decimal {
        self.items.iter().map(|item| item.weight).sum()
    }

    #[getter]
    pub fn get_value(&self) -> Decimal {
        self.items.iter().map(|item| item.value).sum()
    }
}
