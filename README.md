# OpenClassrooms - Python certification - Project #7

## <a id="index">Index</a>

1. [Introduction](#intro)
2. [Installation](#install)
3. [Links](#links)
4. [Algorithm complexity breakdown](#complexity)


## 1. <a id="intro">Introduction</a>

:mag: **To read the algorithms analysis, please check the `presentation/` folder.** 

Algorithm Project : the objective of this project is to implement 2 algorithms to solve the Knapsack problem.

### Part 1: Brute Force Solution

The goal of this part is to provide an initial "brute force" solution that should generate the list of items to choose from a list of 20 elements.

### Part 2: Optimized Solution

This part requires implementing a second solution that can read a file containing items and propose the best possible combination.

It is also required to provide a set of slides containing the following:

- An analysis of the brute force algorithm.
- A diagram, flowchart, or pseudocode describing the thought process behind the optimized solution.
- The algorithm chosen for the optimized version and the algorithm's limitations (edge cases).
- A comparison of the efficiency and performance of the brute force algorithm versus the optimized algorithm using Big-O notation, time complexity, and memory analysis.


## 2. <a id="install">Installation</a>

You need to have Python >= 3.9 installed.

### Clone the project from Github

```bash
git clone https://github.com/0ddbird/OC_Python_P7.git
```

### Create a new virtual environment

```bash
python -m venv <name_of_the_venv>
```

### Activate the virtual environment

```bash
source <name_of_the_venv>/bin/activate
```

### Go to the `app/` directory  and install the requirements
```bash
cd app/ ; pip install -r requirements.txt
```

### Optional: install Rust and build the knapsack_rs library

Each of the project algorithms have also been implemented in Rust, and have been made usable through the application as an optional python dependency.

If you want to use this dependency, you need to have Rust installed on your computer, and build the `knapsack_rs` library.  
- To install Rust on your computer, follow the instructions from [https://doc.rust-lang.org](https://doc.rust-lang.org/book/ch01-01-installation.html)
- Then navigate to the `knapsack_rs/` directory and run

```bash
maturin develop
```
This will compile the Rust library and add it as a python dependency in the current virtual environment.

### 6. Run the script

To be guided by the interactive prompt, run:  
```bash
python -m main
```

To pass arguments via the CLI, run :  
```bash
python main.py <dataset_name> <max_capacity> <algorithm> <language> <optional_flags>
```

#### Parameters
**dataset_name**: must be the name of a CSV file located in the `project_data/datasets/` directory.  

**max_capacity**: must be a positive integer (the knapsack capacity)  

**algorithm**: three possible choices:
- **--bf**: a brute force algorithm that generates all possible combinations from the given items, and return the one with the best value within the constraint of `max_capacity`.
- **--gr**: a greedy algorithm that sorts all items by value (descending)
- **--dp**: a dynamic programming algorithm  

**language**: two choices Python or Rust.
- -**-py** will run the Python version of the chosen algorithm
- --rs will run the Rust version of the chosen algorithm

**-p** (optional): enables verbose mode to print the result to the console  

**-w** (optional): if enabled, will write the results to `project_data/results/` as a text file. 


### Examples

`python main.py dataset0 500 --bf --py -p`  
`python main.py dataset1 500 --gr --py -w`  
`python main.py dataset2 500 --dp --rs -p -w`  


[:arrow_up_small: Back to top](#index)
## 3. <a id="links">Links</a>

[Project diagram](https://whimsical.com/BzsL865mDueuqFBd5RSfjU)  

[:arrow_up_small: Back to top](#index)