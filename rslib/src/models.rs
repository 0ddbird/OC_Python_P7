use std::fmt::{Debug};
use pyo3::{IntoPy, PyObject, Python};
use pyo3::types::IntoPyDict;
use rust_decimal::Decimal;


#[derive(Debug, Clone)]
pub struct Item {
    pub name: String,
    pub weight: Decimal,
    pub rate: Decimal,
    pub value: Decimal,
    pub coefficient: u32,
    pub weighted_weight: i32,
    pub weighted_rate: i32,
    pub weighted_value: i32,
}


impl Item {
    pub fn new(name: String, weight: Decimal, rate: Decimal, coefficient: u32) -> Self {
        let name: String = name;
        let rate:Decimal = rate;
        let value: Decimal = Decimal::from(weight) * rate;
        let coefficient: u32 = coefficient;
        let weighted_weight: i32 = 0;
        let weighted_rate: i32 = 0;
        let weighted_value: i32 = 0;

        Item {
            name,
            weight,
            rate,
            value,
            coefficient,
            weighted_weight,
            weighted_rate,
            weighted_value
        }
    }
}

impl IntoPy<PyObject> for Item {
    fn into_py(self, py: Python) -> PyObject {
        let dict = [
            ("name", self.name.into_py(py)),
            ("weight", self.weight.to_string().into_py(py)),
            ("rate", self.rate.to_string().into_py(py)),
            ("value", self.value.to_string().into_py(py)),
            ("coefficient", self.coefficient.into_py(py)),
            ("weighted_weight", self.weighted_weight.into_py(py)),
            ("weighted_rate", self.weighted_rate.into_py(py)),
            ("weighted_value", self.weighted_value.into_py(py)),
        ].into_py_dict(py);

        dict.into()
    }
}

// pub struct Combination(Vec<Item>);
