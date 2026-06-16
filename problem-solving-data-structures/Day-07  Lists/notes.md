# Day 07 – Lists

## Objective

The goal of this session is to understand how multiple values can be stored and managed using lists.

---

## What is a List?

A list is a collection of items stored in a single variable.

Lists are:

* Ordered
* Mutable (can be changed)
* Allow duplicate values

---

## Creating a List

Example:

```python id="l701"
numbers = [10, 20, 30, 40, 50]
```

---

## Accessing Elements

Lists use indexing.

```python id="l702"
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])
```

Output:

```text id="l703"
10
20
```

---

## Modifying Elements

```python id="l704"
numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)
```

Output:

```text id="l705"
[10, 25, 30]
```

---

## Adding Elements

### append()

Adds an item at the end.

```python id="l706"
numbers.append(40)
```

---

## Removing Elements

### remove()

```python id="l707"
numbers.remove(20)
```

---

## Length of a List

```python id="l708"
print(len(numbers))
```

---

## Traversing a List

```python id="l709"
for item in numbers:
    print(item)
```

---

## Key Concepts Learned

* List
* Indexing
* Updating Elements
* append()
* remove()
* len()
* List Traversal

---

## Summary

Lists help store multiple related values in a single variable and are one of the most important data structures in programming.
