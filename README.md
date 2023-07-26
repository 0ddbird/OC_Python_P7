# OpenClassrooms - Python certification - Project #7

## <a id="index">Index</a>

1. [Introduction](#intro)
2. [Installation](#install)
3. [Links](#links)
4. [Algorithm complexity breakdown](#complexity)


## 1. <a id="intro">Introduction</a>

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
### 1. Clone the project from Github

```bash
git clone https://github.com/0ddbird/OC_Python_P7.git
```

### <a id="step2">2.</a> Navigate to the `app` directory  
```bash
`cd /app`
```

### 3. Run the script
The command structure is :  
```bash
python main.py <dataset_name> <max_capacity> <algorithm> <language> <optional_flags
```

#### Parameters
**dataset_name**: must be the name of a CSV file located in the `project_data/datasets/` directory.  

**max_capacity**: must be a positive integer (the knapsack capacity)  

**algorithm**: three possible choices:
- --bf: a brute force algorithm that generates all possible combinations from the given items, and >return the one with the best value within the constraint of `max_capacity`.
- --gr: a greedy algorithm that sorts all items by value (descending)
- --dp: a dynamic programming algorithm  

**<language**: two choices Python or Rust.
- --py will run the Python version of the chosen algorithm
- --rs will run the Rust version of the chosen algorithm

**-p (optional)**: enables verbose mode to print the result to the console  

**-w (optional)**: if enabled, will write the results to `project_data/results/` as a text file. 


### Examples

`python main.py dataset0 500 --bf --py -p`  
`python main.py dataset1 500 --gr --py -w`  
`python main.py dataset2 500 --dp --rs -p -w`  

## Optional : Rust version

You need to have Rust installed on your computer to build the `knapsack_rs` python dependency. 
You can follow the installation instructions from [https://doc.rust-lang.org](https://doc.rust-lang.org/book/ch01-01-installation.html)

### 1. Clone the project from Github

```bash
git clone https://github.com/0ddbird/OC_Python_P7.git`
```

### 2. Go to the `app/` directory  

### 2. Create a new virtual environment

```bash
python -m venv <name_of_the_venv>
```

### 3. Activate the virtual environment

```bash
source <name_of_the_venv>/bin/activate
```

### 4. Install the requirements

```bash
pip install -r requirements.txt
```

Alternatively, since there is only one package required, you can simply run  

```bash
pip install maturin`
```


### 5. Navigate to the `knapsack_rs/` directory and run

```bash
maturin develop
```

This will compile the binary for your platform and install it as a python dependency in your virtual environment.

### 6. [Go to Python Installation step #2](#step2)


[:arrow_up_small: Back to top](#index)
## 3. <a id="links">Links</a>

[Project diagram](https://whimsical.com/BzsL865mDueuqFBd5RSfjU)  
[Algorigrams](https://whimsical.com/p7-algorigrammes-AxG7CBJ1VWqR25my86c9Rw)  

[:arrow_up_small: Back to top](#index)
## 4. <a id="complexity">Algorithm complexity breakdown</a>

### Brute force
1. Check if the number of items is greater than 20: **O(1)**.
2. Getting all combinations of items: **O(n*2^n)**.
3. Checking the weight and calculating the value of each combination: **O(n*2^n)**.
4. Finding the maximum value combination: **O(2^n)**.
5. Creating a list of the items in the best solution: **O(n)**.

**Equation : f(n) = 1 + 3n*2^n + 2^n + n**  
**Overall time complexity: O(n*2^n).**  


###  Dynamic

1. Initialization of a 2D table of size (n+1) x (capacity+1): **O(n*capacity)**.
2. Filling the table using a double loop with max operations: **O(n*capacity)**.
3. Linear scan over the sorted list of items: **O(n)**. 

**Equation : f(n, capacity) = 2n*capacity + n**  
**Overall time complexity: O(n*capacity).**  

###  Greedy

1. Sorting the items based on their value: **O(n log n)**, where n is the number of items.  
2. Linear scan over the sorted list of items: **O(n)**.  


**Equation f(n) = n log n + n**  
**Overall time complexity: O(n log n)**  

[:arrow_up_small: Back to top](#index)