# Day 27 – Deque (Double Ended Queue)

## Objective

The goal of this session is to understand the Deque data structure and how it allows insertion and deletion from both ends.

---

## What is a Deque?

Deque stands for:

```text id="dq01"
Double Ended Queue
```

A Deque is a linear data structure in which insertion and deletion can occur at both the front and rear ends.

---

## Representation

```text id="dq02"
Front                    Rear

10 ↔ 20 ↔ 30 ↔ 40
```

Elements can be added or removed from either side.

---

## Operations

### Insert at Front

```text id="dq03"
10 → 20 → 30

Insert 5

5 → 10 → 20 → 30
```

---

### Insert at Rear

```text id="dq04"
10 → 20 → 30

Insert 40

10 → 20 → 30 → 40
```

---

### Delete from Front

```text id="dq05"
10 → 20 → 30

Delete Front

20 → 30
```

---

### Delete from Rear

```text id="dq06"
10 → 20 → 30

Delete Rear

10 → 20
```

---

## Types of Deque

### Input Restricted Deque

* Insertion allowed only at one end
* Deletion allowed at both ends

### Output Restricted Deque

* Deletion allowed only at one end
* Insertion allowed at both ends

---

## Applications

* Browser History
* Undo and Redo Operations
* Task Scheduling
* Sliding Window Problems
* Palindrome Checking

---

## Time Complexity

| Operation    | Complexity |
| ------------ | ---------- |
| Insert Front | O(1)       |
| Insert Rear  | O(1)       |
| Delete Front | O(1)       |
| Delete Rear  | O(1)       |
| Peek Front   | O(1)       |
| Peek Rear    | O(1)       |

---

## Queue vs Deque

| Feature      | Queue | Deque |
| ------------ | ----- | ----- |
| Insert Front | ❌     | ✅     |
| Insert Rear  | ✅     | ✅     |
| Delete Front | ✅     | ✅     |
| Delete Rear  | ❌     | ✅     |

---

## Key Concepts Learned

* Deque
* Front Insertion
* Rear Insertion
* Front Deletion
* Rear Deletion
* Double Ended Queue

---

## Summary

A Deque is a flexible version of a queue that allows insertion and deletion from both ends, making it useful for many advanced algorithms.
