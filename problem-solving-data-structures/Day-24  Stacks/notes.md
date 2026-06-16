# Day 24 – Stacks

## Objective

The goal of this session is to understand the Stack data structure and its operations.

---

## What is a Stack?

A Stack is a linear data structure that follows the:

```text id="stk01"
LIFO

(Last In, First Out)
```

The last element inserted is the first element removed.

---

## Real Life Example

Stack of Plates:

```text id="stk02"
Top
 ↓

[Plate 4]
[Plate 3]
[Plate 2]
[Plate 1]
```

The last plate placed on top is removed first.

---

## Stack Operations

### Push

Insert an element onto the stack.

Example:

```text id="stk03"
Push 10

Stack:

10
```

---

### Pop

Remove the top element.

Example:

```text id="stk04"
10
20
30

Pop

30 Removed
```

---

### Peek (Top)

View the top element without removing it.

Example:

```text id="stk05"
Top Element = 30
```

---

### Is Empty

Checks whether the stack contains elements.

---

## Stack Representation

```text id="stk06"
Top
 ↓

30
20
10
```

---

## Applications of Stacks

* Function Calls
* Recursion
* Undo Operations
* Expression Evaluation
* Browser History
* Backtracking Algorithms

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| Is Empty  | O(1)       |

---

## Advantages

* Simple implementation
* Fast insertion and deletion
* Useful in many algorithms

---

## Key Concepts Learned

* Stack
* LIFO
* Push
* Pop
* Peek
* Is Empty

---

## Summary

A Stack is a LIFO data structure where insertion and deletion happen only at the top of the stack.
