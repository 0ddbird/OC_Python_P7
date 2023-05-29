#[derive(Debug)]
pub struct Action {
    pub name: &'static str,
    pub cost: i32,
    pub value: f64,
}