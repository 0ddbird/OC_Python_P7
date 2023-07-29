# Algorithms breakdown

## <a id="index">Index</a>

1. [Introduction](#intro)
2. [Brute force algorithm](#bf)
3. [Greedy algorithm](#gr)
4. [Dynamic programming algorithm](#dp)


## <a id="intro">1. Introduction</a>

[Algorigrams](https://whimsical.com/p7-algorigrammes-AxG7CBJ1VWqR25my86c9Rw)  

## Data used in examples
|Knapsack capacity| 4        |       |       |
|:------:|:--------:|:-----:|:-----:|
|Item   | Weight    | Rate  | Value |
| 1     | 3         |50%    | 1.5   |
| 2     | 2         |45%    | 0.9   |
| 3     | 2         |40%    | 0.8   |


## Size of a single item

```python
from decimal import Decimal
from dataclasses import dataclass
import sys

@dataclass
class Item:
    name: str
    weight: Decimal
    rate: Decimal
    coefficient: int

    @property
    def value(self) -> Decimal:
        return self.weight * self.rate / 100

    @property
    def weighted_weight(self) -> int:
        return int(self.weight * Decimal(self.coefficient))

    @property
    def weighted_rate(self) -> int:
        return int(self.rate * Decimal(self.coefficient))

    @property
    def weighted_value(self) -> int:
        return int(self.weighted_weight * self.weighted_rate)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.value}"


item = Item("Action-1", Decimal(10.15), Decimal(20.49), 1)

print(sys.getsizeof(item))  # 48 bytes

```
[:arrow_up_small: Back to top](#index)

## <a id="bf"> 2. Brute force</a>

### Steps

1. Check if the number of items is greater than 20: **O(1)**.
2. Getting all combinations of items: **O(n*2^n)**.
3. Checking the weight and calculating the value of each combination: **O(n*2^n)**.
4. Finding the maximum value combination: **O(2^n)**.
5. Creating a list of the items in the best solution: **O(n)**.


**Equation:** `f(n) = 1 + 3n*2^n + 2^n + n`  
**Overall time complexity:** `O(n*2^n)`  

### Example

|Combination        | weight    | value  | < capacity    | best value?   |
|:------------------|:----------|:------ |:--------------|:--------------|
|Item1              | 3         | 1.5    | YES           | NO            |
|Item2              | 2         | 0.9    | YES           | NO            |
|Item3              | 2         | 0.8    | YES           | NO            |
|Item1, Item2       | 5         | 2.4    | NO            | -             |
|Item1, Item3       | 5         | 2.3    | NO            | -             |
|Item2, Item3       | **4**     | **1.7**| YES           | YES           |
|Item1, Item2, Item3| 7         | 3.2    | NO            | -             |

> **Result:** 
>- **Combination:** Item2, Item3
>- **Weight:** 4
>- **Value:** 1.7

### Memory complexity
- let n be the number of items  
- let r be then number of items chosen 

```
nCr = n! / r! * (n - r)!
```


We must compute all possible combinations including one item to combinations including n items.

If n = 3 (3 items):

```
result = sum(3c1, 3c2, 3c3)
```
ex.:  
3c1 = 3 (We can make 3 different combinations if we have 3 items and we make combinations of one)  
3c3 = 1 (We can make only 1 combination with 3 items if we have 3 items)  

```python
def get_all_combinations(items):
    n = len(items)
    combinations = []
    items = 0
    
    for i in range(1, 2**n):
        combination = []
        for j in range(n):
            if ((i >> j) & 1) == 1:
                combination.append(j)
        combinations.append(combination)
        items += len(combination)

    return len(combinations), items


lst = [1, 2, 3]

combinations_number, items = get_all_combinations(lst)

print(combinations_number, items)

```

Result for 3 items:
- 7 combinations
- 12 items total

Since we know the size of an item is of 48 bytes, this first step uses 576 bytes

However, we can optimize this solution by filtering the combinations for which the combination weight is greater than the total capcity.

This leaves only:

- 4 combinations
- 5 items total

The new memory requirement is now only: 240 bytes  

[:arrow_up_small: Back to top](#index)  

##  <a id="gr">3. Greedy algorithm</a>

### Steps

1. Sorting the items based on their value: **O(n log n)**, where n is the number of items.  
2. Linear scan over the sorted list of items: **O(n)**.  

**Equation:** `f(n) = n log n + n`  
**Overall time complexity:** `O(n log n)`

### Example

**1. Sort items by value (descending)**

|Items              | weight    | value  |
|:------------------|:----------|:------ |
|Item1              | 3         | 1.5    |
|Item2              | 2         | 0.9    |
|Item3              | 2         | 0.8    |

**2. Fill knapsack starting from best value item:**

|Items              | weight    | value  | remaining capacity | fits ? |
|:------------------|:----------|:------ |:-------------------|:-------|
|Item1              | 3         | 1.5    |4                   | YES    |
|Item2              | 2         | 0.9    |4 - 3 = 1           | NO     |
|Item3              | 2         | 0.8    |1                   | NO     |


>**Result:** 
>- **Combination:** Item 1
>- **Weight:** 3
>- **Value:** 1.5

### Memory complexity

This algorithm sorts the list of items by value.  
Then it fills a new list by appending the items from the best value one to the lowest value one, until the capacity cap is reached.

For n items, in the worst case scenario, we have to append all n items.  
So for 3 items, we would have at some point 2 lists holding up to 3 items each.  

3 * 48 bytes * 2  = 144 bytes

In the best case scenario, no item fits because of its weight being greater than the max capacity.
This would make 0 byte.  

[:arrow_up_small: Back to top](#index)

## <a id="dp">4. Dynamic programming algorithm</a>

This solution divides the problem in smaller parts:  
For each item we check if it fits if the capacity of the knapsack was 1, 2, ... until we reach the real capacity (4 in our example)
If the item fits, we check if we could obtain a better value for the same capacity (1, 2, 3, 4) from the previous item(s).  
If the was already a better value obtained from previous items, we don't include it, otherwise we do.  


### Steps

1. Initialization of a 2D table of size (n+1) x (capacity+1): **O(n*capacity)**.
2. Filling the table using a double loop with max operations: **O(n*capacity)**.
3. Linear scan over the sorted list of items: **O(n)**. 

**Equation:** `f(n, capacity) = 2n*capacity + n`  
**Overall time complexity:** `O(n*capacity)`  

Since we need to be able to use the items weight as list indices, they must be integers.

To stay accurate while converting Decimals to integers, we must first find the coefficient to multiply each weight and value by.

ex:
For an item with a value of 
- weight = `Decimal(12.16)` 
- rate - `Decimal(16.495)`
we would need a coefficient of 1000 to obtain:
- weighted_weight = 12 160
- weighted_rate = 16 495

However, this has no direct impact on the item size (still 48 bytes), since the `weighted_weight` and `weighted_value` are computed properties of the `Item` class and are not stored per se.

### Memory complexity

#### 1. Creating a 2D table filled with zeros.


| Capacity  | 0 | 1 | 2 | 3 | 4 |
|:---------:|:-:|:-:|:-:|:-:|:-:|  
|-          | 0 | 0 | 0 | 0 | 0 |
|Item 1     | 0 | 0 | 0 | 0 | 0 |
|Item 2     | 0 | 0 | 0 | 0 | 0 |
|Item 3     | 0 | 0 | 0 | 0 | 0 |

```python
import sys

items = 3
capacity = 4
zero = 0
# print(sys.getsizeof(zero))  # 24 bytes

table = [
    [0 for w in range(capacity + 1)] for i in range(items + 1)
]
empty_list_size = sys.getsizeof(table)
total_size = empty_list_size
sublists_sizes = 0
sublists_count = 0
items_size = 0
item_count = 0

for sublist in table:
    sublist_size = sys.getsizeof(sublist)
    sublists_sizes += sublist_size
    sublists_count += 1

    total_size += sublist_size
    
    for item in sublist:
        item_count += 1
        item_size = sys.getsizeof(item)
        items_size += item_size
        total_size += item_size

print(
    f"{empty_list_size=}\n"
    "----------"
    ) # 88 bytes

print(f"{item_count=}") # 20 items
print(
    f"{items_size=}\n"
    "----------"
    )  # 480 bytes (20 items * 48 bytes)print()
print(f"{sublists_count=}")
print(
    f"{sublists_sizes=}\n"
      "----------"
      )  # 480 bytes (120 bytes / list)

print(
    f"{total_size=} (empty_list_size + items_size + sublist_sizes)\n"
    "----------"
    )  # 1048 = 88 + 480 + 480

print("size = empty_list_size + capacity * items * item_size")

```

#### 2. Replacing zeros by Item instances except for 1st sublist and 1st column:  
88 + 480 + 4 * 3 * 48 = 1144 bytes

#### Creating a new list to backtrack the 2D table

```python
import sys
items = [Item1, Item2, Item3]
items_size = sys.getsizeof(items)  # 88 + 3 * 48 = 232 bytes

```

1048 + 232 = 1280  
Total memory usage for Dynamic programming solution : 1280 bytes for a capacity of 4 and 3 items.

[:arrow_up_small: Back to top](#index)