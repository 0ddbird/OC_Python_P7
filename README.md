# OpenClassrooms - Python certification - Project #7

## Usage

### Prerequisites

- You need to have Rust installed on your computer to build the `knapsack_rs` python dependency. 
You can follow the installation instructions from [https://doc.rust-lang.org(https://doc.rust-lang.org/book/ch01-01-installation.html)
- You need to have Python >= 3.9 installed.

### Installation

1. Clone the project from Github with  
`git clone https://github.com/0ddbird/OC_Python_P7.git`  


2. In the project directory, create a new virtual environment

`python -m venv <name_of_the_venv>`  


3. Activate the virtual environment

`source <name_of_the_venv>/bin/activate`  

4. Install the requirements by running   

`pip install -r requirements.txt`  

Alternatively, since there is only one package required, you can simply run  

`pip install maturin`


5. Navigate to the `knapsack_rs/` directory and run  

`maturin develop`  

This will compile the binary for your platform and install it as a python dependency in your virtual environment.

6. Go to the `app/` directory  

7. Run the script
The command structure is the following:  
`python main.py <dataset_name> <max_capacity> <algorithm_implementation [--bf | --gr | --dp]> <language_implementation [--py| --rs]> <optional : -p> <optional : -w>`

#### Parameters
**<dataset_name>**: must be the name of a csv file located in the `project_data/datasets/` directory.  

**<max_capacity>**: must be a positive integer (the knapsack max capacity)  

**<algorithm_implementation>**: three possible choices:
- --bf: a brute force algorithm that generates all possible combinations from the given items, and return the one with the best value within the constraint of `max_capacity`.
- --gr: a greedy algorithm that sorts all items by value (descending)
- --dp: a dynamic programming algorithm  

**<language_implementation>**: two choices Python or Rust.
- --py will run the Python version of the chosen algorithm
- --rs will run the Rust version of the chosen algorithm

**-p (optional)**: enables verbose mode to print the result to the console
**-w (optional)**: if enabled, will write the results to `project_data/results` as a text file. 


#### Examples

`python main.py dataset0 500 --bf --py -p`  
`python main.py dataset1 500 --gr --py -w`  
`python main.py dataset2 500 --dp --rs -p -w`  

## Introduction

Algorithm Project : the objective of this project is to implement 2 algorithms to solve the Knapsack problem.

## Part 1: Brute Force Solution

The goal of this part is to provide an initial "brute force" solution that should generate the list of items to choose from a list of 20 elements.

## Part 2: Optimized Solution

This part requires implementing a second solution that can read a file containing items and propose the best possible combination.

It is also required to provide a set of slides containing the following:

- An analysis of the brute force algorithm.
- A diagram, flowchart, or pseudocode describing the thought process behind the optimized solution.
- The algorithm chosen for the optimized version and the algorithm's limitations (edge cases).
- A comparison of the efficiency and performance of the brute force algorithm versus the optimized algorithm using Big-O notation, time complexity, and memory analysis.


## Links

[Project diagram](https://whimsical.com/BzsL865mDueuqFBd5RSfjU)