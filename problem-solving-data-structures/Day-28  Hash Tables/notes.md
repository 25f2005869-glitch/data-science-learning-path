# Day 28 – Hash Tables

## Objective

The goal of this session is to understand Hash Tables and how they provide fast data storage and retrieval.

---

## What is a Hash Table?

A Hash Table is a data structure that stores data in the form of:

```text
Key → Value
```

pairs.

It uses a hash function to determine where data should be stored.

---

## Real Life Example

Student Records:

```text
101 → Saloni
102 → Rahul
103 → Priya
```

Student ID acts as the key and the student name acts as the value.

---

## Hash Function

A hash function converts a key into an index.

Example:

```text
Hash(101) = 1
Hash(102) = 2
Hash(103) = 3
```

The generated index determines where data is stored.

---

## Hash Table Representation

```text
Index    Value

0        Empty
1        Saloni
2        Rahul
3        Priya
4        Empty
```

---

## Basic Operations

### Insert

Store a key-value pair.

```text
101 → Saloni
```

---

### Search

Find a value using its key.

```text
Search(101)

Result: Saloni
```

---

### Delete

Remove a key-value pair.

```text
Delete(101)
```

---

## Collision

A collision occurs when two different keys produce the same index.

Example:

```text
Hash(21) = 1
Hash(31) = 1
```

Both keys map to the same location.

---

## Collision Handling Techniques

### Chaining

Store multiple values at the same index using a list.

```text
Index 1

21 → 31 → 41
```

### Open Addressing

Find another empty location.

Methods:

* Linear Probing
* Quadratic Probing
* Double Hashing

---

## Time Complexity

| Operation | Average Case |
| --------- | ------------ |
| Insert    | O(1)         |
| Search    | O(1)         |
| Delete    | O(1)         |

Worst Case:

```text
O(n)
```

(if many collisions occur)

---

## Applications

* Dictionaries in Python
* Database Indexing
* Caching Systems
* Symbol Tables
* Password Verification
* Search Engines

---

## Key Concepts Learned

* Hash Table
* Key-Value Pair
* Hash Function
* Collision
* Chaining
* Open Addressing

---

## Summary

Hash Tables provide very fast insertion, searching, and deletion operations by using keys and hash functions.
