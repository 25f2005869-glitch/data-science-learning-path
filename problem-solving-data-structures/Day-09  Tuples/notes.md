# Day 09 – Tuples

## Objective

The goal of this session is to understand tuples and how they differ from lists.

---

## What is a Tuple?

A tuple is a collection of ordered elements.

Unlike lists, tuples are **immutable**, which means their values cannot be changed after creation.

---

## Creating a Tuple

Example:

```python
numbers = (10, 20, 30, 40, 50)
```

---

## Accessing Elements

Tuples use indexing just like lists.

```python
numbers = (10, 20, 30)

print(numbers[0])
print(numbers[1])
```

Output:

```text
10
20
```

---

## Tuple Length

The `len()` function returns the number of elements.

```python
numbers = (10, 20, 30)

print(len(numbers))
```

Output:

```text
3
```

---

## Tuple Traversal

A tuple can be traversed using a loop.

```python
numbers = (10, 20, 30)

for item in numbers:
    print(item)
```

Output:

```text
10
20
30
```

---

## Tuple Concatenation

Two tuples can be joined using the `+` operator.

```python
a = (1, 2)
b = (3, 4)

print(a + b)
```

Output:

```text
(1, 2, 3, 4)
```

---

## Difference Between List and Tuple

| List            | Tuple              |
| --------------- | ------------------ |
| Mutable         | Immutable          |
| Uses []         | Uses ()            |
| Can be modified | Cannot be modified |

---

## Key Concepts Learned

* Tuple
* Immutability
* Indexing
* Traversal
* Concatenation
* len()

---

## Summary

Tuples are useful when data should remain fixed and protected from accidental modification.
