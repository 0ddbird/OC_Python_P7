use pyo3::types::{IntoPyDict, PyDict};
use pyo3::{FromPyObject, IntoPy, PyAny, PyErr, PyObject, PyResult, Python};
use rust_decimal::prelude::{FromPrimitive, ToPrimitive};
use rust_decimal::Decimal;
use std::fmt;
use std::fmt::Debug;
use std::str::FromStr;

#[derive(Debug)]
pub enum ItemCreationError {
    CoefficientConversionError(String),
    WeightOutOfRange(String),
    ValueOutOfRange(String),
    DecimalParseError(String, rust_decimal::Error),
}

impl fmt::Display for ItemCreationError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ItemCreationError::CoefficientConversionError(msg) => write!(f, "{}", msg),
            ItemCreationError::WeightOutOfRange(msg) => write!(f, "{}", msg),
            ItemCreationError::ValueOutOfRange(msg) => write!(f, "{}", msg),
            ItemCreationError::DecimalParseError(msg, e) => write!(f, "{}: {}", msg, e),
        }
    }
}

#[derive(Debug, Clone)]
pub struct Item {
    pub name: String,
    pub weight: Decimal,
    pub value: Decimal,
    pub coefficient: u32,
    pub weighted_weight: u64,
    pub weighted_value: u64,
}

impl Item {
    pub fn new(
        name: String,
        weight: Decimal,
        value: Decimal,
        coefficient: u32,
    ) -> Result<Self, ItemCreationError> {
        let coefficient_dec: Decimal =
            Decimal::from_u32(coefficient).ok_or(ItemCreationError::CoefficientConversionError(
                "Failed to convert coefficient to Decimal".to_string(),
            ))?;

        let dec_weighted_weight: Decimal = weight * coefficient_dec;
        let dec_weighted_value: Decimal = value * coefficient_dec;

        let weighted_weight: u64 =
            dec_weighted_weight
                .to_u64()
                .ok_or(ItemCreationError::WeightOutOfRange(
                    "Weight out of range".to_string(),
                ))?;

        let weighted_value: u64 =
            dec_weighted_value
                .to_u64()
                .ok_or(ItemCreationError::ValueOutOfRange(
                    "Value out of range".to_string(),
                ))?;

        Ok(Item {
            name,
            weight,
            value,
            coefficient,
            weighted_weight,
            weighted_value,
        })
    }
}

impl IntoPy<PyObject> for Item {
    fn into_py(self, py: Python) -> PyObject {
        let dict = [
            ("name", self.name.into_py(py)),
            ("weight", self.weight.to_string().into_py(py)),
            ("value", self.value.to_string().into_py(py)),
            ("coefficient", self.coefficient.into_py(py)),
            ("weighted_weight", self.weighted_weight.into_py(py)),
            ("weighted_value", self.weighted_value.into_py(py)),
        ]
        .into_py_dict(py);

        dict.into()
    }
}

impl<'source> FromPyObject<'source> for Item {
    fn extract(ob: &'source PyAny) -> PyResult<Self> {
        let dict: &PyDict = ob.downcast()?;
        let name: String = dict.get_item("name").unwrap().extract()?;

        let weight_str: String = dict.get_item("weight").unwrap().extract()?;
        let weight: Decimal = Decimal::from_str(weight_str.as_str()).map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!("Failed to parse weight: {}", e))
        })?;

        let value_str: String = dict.get_item("value").unwrap().extract()?;
        let value: Decimal = Decimal::from_str(value_str.as_str()).map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!("Failed to parse rate: {}", e))
        })?;

        let coefficient: u32 = dict.get_item("coefficient").unwrap().extract()?;

        let item: Item = Item::new(name, weight, value, coefficient).map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!("Failed to create item: {}", e))
        })?;

        Ok(item)
    }
}

impl fmt::Display for Item {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Item {{\n\tname: {},\n\tweight: {},\n\tvalue: {},\n\tcoefficient: {},\n\tweighted_weight: {},\n\tweighted_value: {}\n}}",
               self.name, self.weight, self.value, self.coefficient, self.weighted_weight, self.weighted_value)
    }
}

// pub struct Combination(Vec<Item>);
