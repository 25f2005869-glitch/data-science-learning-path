# Day 14 – Space Complexity

## Objective

The goal of this session is to understand how much memory an algorithm uses during execution.

---

## What is Space Complexity?

Space Complexity measures the amount of memory required by an algorithm as the input size increases.

It includes:

* Input Space
* Auxiliary Space (extra memory used by the algorithm)

---

## Why Space Complexity?

Two algorithms may take the same amount of time but use different amounts of memory.

In many applications, memory usage is as important as execution time.

---

## Input Size

Input size is represented by:

```text
n
```

Example:

* Array of 10 elements → n = 10
* Array of 1000 elements → n = 1000

---

## O(1) – Constant Space

The algorithm uses a fixed amount of memory.

Example:

```python
a = 10
b = 20
sum_result = a + b
```

Memory usage remains constant.

---

## O(n) – Linear Space

Memory usage grows with input size.

Example:

```python
numbers = []

for i in range(n):
    numbers.append(i)
```

As n increases, memory usage increases.

---

## O(n²) – Quadratic Space

Memory grows as n × n.

Example:

```python
matrix = []

for i in range(n):
    row = []

    for j in range(n):
        row.append(0)

    matrix.append(row)
```

This creates an n × n matrix.

---

## Time Complexity vs Space Complexity

| Time Complexity         | Space Complexity        |
| ----------------------- | ----------------------- |
| Measures execution time | Measures memory usage   |
| Focuses on speed        | Focuses on memory       |
| Represented using Big O | Represented using Big O |

---

## Examples

### Constant Space

```python
x = 5
y = 10
z = x + y
```

Space Complexity:

```text
O(1)
```

### Linear Space

```python
numbers = [1, 2, 3, 4, 5]
```

Space Complexity:

```text
O(n)
```

---

## Key Concepts Learned

* Space Complexity
* Auxiliary Space
* Constant Space
* Linear Space
* Quadratic Space
* Memory Analysis

---

## Summary

Space Complexity helps determine how efficiently an algorithm uses memory and is an important factor in algorithm design.
