# Day 11 – Sets

## Objective

The goal of this session is to understand how sets store unique elements and support set operations.

---

## What is a Set?

A set is a collection of unique elements.

Characteristics:

* Unordered
* Mutable
* No duplicate values allowed

---

## Creating a Set

Example:

```python
numbers = {10, 20, 30, 40}
```

---

## Duplicate Values

Sets automatically remove duplicates.

Example:

```python
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

---

## Adding Elements

Using `add()`:

```python
numbers.add(50)
```

---

## Removing Elements

Using `remove()`:

```python
numbers.remove(20)
```

---

## Set Operations

### Union

Combines all unique elements.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
```

Output:

```text
{1, 2, 3, 4, 5}
```

---

### Intersection

Common elements.

```python
print(A & B)
```

Output:

```text
{3}
```

---

### Difference

Elements present in first set only.

```python
print(A - B)
```

Output:

```text
{1, 2}
```

---

## Traversing a Set

```python
for item in numbers:
    print(item)
```

---

## Key Concepts Learned

* Set
* Unique Elements
* add()
* remove()
* Union
* Intersection
* Difference

---

## Summary

Sets are useful when duplicate values are not required and fast membership checking is needed.
