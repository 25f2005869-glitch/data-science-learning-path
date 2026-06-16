# Day 13 – Time Complexity

## Objective

The goal of this session is to understand how the running time of an algorithm is measured and compared.

---

## What is Time Complexity?

Time Complexity is a measure of how the execution time of an algorithm grows as the input size increases.

It helps us compare algorithms and choose the more efficient solution.

---

## Why Time Complexity?

Consider two algorithms solving the same problem.

Algorithm A:

```text
Runs in 10 steps
```

Algorithm B:

```text
Runs in 1,000 steps
```

For small inputs both may work, but for large inputs Algorithm A is better.

---

## Input Size

Input size is usually represented by:

```text
n
```

Example:

* List of 10 elements → n = 10
* List of 1000 elements → n = 1000

---

## Big O Notation

Big O notation describes the growth rate of an algorithm.

Common notations:

### O(1) – Constant Time

Execution time remains constant.

Example:

```python
numbers = [10, 20, 30]
print(numbers[0])
```

---

### O(n) – Linear Time

Execution time grows proportionally with n.

Example:

```python
for item in numbers:
    print(item)
```

---

### O(n²) – Quadratic Time

Usually occurs with nested loops.

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

---

## Common Time Complexities

| Complexity | Name         |
| ---------- | ------------ |
| O(1)       | Constant     |
| O(log n)   | Logarithmic  |
| O(n)       | Linear       |
| O(n log n) | Linearithmic |
| O(n²)      | Quadratic    |
| O(n³)      | Cubic        |
| O(2ⁿ)      | Exponential  |

---

## Rule of Thumb

As input size grows:

```text
O(1)
   ↓
O(log n)
   ↓
O(n)
   ↓
O(n log n)
   ↓
O(n²)
   ↓
O(n³)
   ↓
O(2ⁿ)
```

Efficiency decreases as we move downward.

---

## Key Concepts Learned

* Time Complexity
* Input Size (n)
* Big O Notation
* Constant Time
* Linear Time
* Quadratic Time

---

## Summary

Time Complexity helps evaluate the efficiency of algorithms and is one of the most important concepts in Data Structures and Algorithms.
