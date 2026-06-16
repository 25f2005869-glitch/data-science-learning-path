# Day 15 – Arrays

## Objective

The goal of this session is to understand arrays, their characteristics, and basic operations.

---

## What is an Array?

An array is a collection of elements stored in contiguous memory locations.

All elements generally belong to the same data type.

In Python, lists are commonly used to represent arrays.

---

## Why Arrays?

Arrays help:

* Store multiple values using one variable
* Access elements quickly using indexes
* Process large amounts of data efficiently

---

## Example

```python
numbers = [10, 20, 30, 40, 50]
```

Array Representation:

```text
Index :  0   1   2   3   4

Value : 10  20  30  40  50
```

---

## Accessing Elements

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

## Updating Elements

```python
numbers[1] = 25
```

Result:

```text
[10, 25, 30, 40, 50]
```

---

## Traversing an Array

```python
for item in numbers:
    print(item)
```

---

## Array Operations

### Access

```python
numbers[2]
```

Time Complexity:

```text
O(1)
```

---

### Traversal

```python
for item in numbers:
    print(item)
```

Time Complexity:

```text
O(n)
```

---

### Search

Searching an element one by one.

Time Complexity:

```text
O(n)
```

---

## Advantages

* Fast access using index
* Easy traversal
* Simple implementation

---

## Limitations

* Fixed logical ordering
* Insertion and deletion may be costly
* Large arrays consume more memory

---

## Key Concepts Learned

* Array
* Index
* Access
* Update
* Traversal
* Linear Search

---

## Summary

Arrays are one of the most fundamental data structures and form the basis for many advanced data structures and algorithms.
