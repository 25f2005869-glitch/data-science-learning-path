# Day 21 – Linked Lists

## Objective

The goal of this session is to understand Linked Lists, their structure, and how they differ from arrays.

---

## What is a Linked List?

A Linked List is a linear data structure where elements are stored in separate nodes.

Each node contains:

1. Data
2. Reference (Link) to the next node

---

## Structure of a Node

```text id="ll01"
+------+------+
| Data | Next |
+------+------+
```

Example:

```text id="ll02"
10 → 20 → 30 → 40 → NULL
```

---

## Why Linked Lists?

Arrays have a fixed structure and insertions/deletions can be costly.

Linked Lists provide:

* Dynamic size
* Efficient insertion
* Efficient deletion

---

## Components

### Node

Stores data and link.

### Head

The first node of the linked list.

### NULL

Marks the end of the list.

---

## Example

```text id="ll03"
Head

 ↓

10 → 20 → 30 → NULL
```

---

## Traversal

To visit every node:

```text id="ll04"
Start from Head

Move to Next Node

Repeat until NULL
```

---

## Advantages

* Dynamic size
* Easy insertion
* Easy deletion
* Memory allocated as needed

---

## Disadvantages

* Extra memory for links
* Sequential access only
* Cannot directly access elements by index

---

## Array vs Linked List

| Feature   | Array      | Linked List    |
| --------- | ---------- | -------------- |
| Memory    | Contiguous | Non-Contiguous |
| Size      | Fixed      | Dynamic        |
| Access    | O(1)       | O(n)           |
| Insertion | Costly     | Efficient      |
| Deletion  | Costly     | Efficient      |

---

## Time Complexity

| Operation              | Complexity |
| ---------------------- | ---------- |
| Access                 | O(n)       |
| Search                 | O(n)       |
| Insertion at Beginning | O(1)       |
| Deletion at Beginning  | O(1)       |

---

## Key Concepts Learned

* Linked List
* Node
* Head
* Next Pointer
* Traversal
* Dynamic Memory

---

## Summary

A Linked List is a dynamic linear data structure where nodes are connected using links. It provides efficient insertion and deletion operations compared to arrays.
