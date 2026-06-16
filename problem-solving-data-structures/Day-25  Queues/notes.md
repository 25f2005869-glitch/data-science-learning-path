# Day 25 – Queues

## Objective

The goal of this session is to understand the Queue data structure and its operations.

---

## What is a Queue?

A Queue is a linear data structure that follows the:

```text id="q01"
FIFO

(First In, First Out)
```

The first element inserted is the first element removed.

---

## Real Life Example

Queue at a Ticket Counter:

```text id="q02"
Front                    Rear

[A] → [B] → [C] → [D]
```

Person A entered first and will leave first.

---

## Queue Operations

### Enqueue

Insert an element at the rear.

Example:

```text id="q03"
Enqueue 10

Queue:

10
```

---

### Dequeue

Remove an element from the front.

Example:

```text id="q04"
10 → 20 → 30

Dequeue

10 Removed
```

---

### Front

View the first element without removing it.

Example:

```text id="q05"
Front Element = 10
```

---

### Rear

View the last element.

Example:

```text id="q06"
Rear Element = 30
```

---

### Is Empty

Checks whether the queue is empty.

---

## Queue Representation

```text id="q07"
Front              Rear

10 → 20 → 30 → 40
```

---

## Applications of Queues

* CPU Scheduling
* Printer Queue
* Task Scheduling
* Breadth First Search (BFS)
* Network Packet Processing
* Customer Service Systems

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Front     | O(1)       |
| Rear      | O(1)       |
| Is Empty  | O(1)       |

---

## Advantages

* Efficient insertion and deletion
* Easy implementation
* Useful in scheduling problems

---

## Key Concepts Learned

* Queue
* FIFO
* Enqueue
* Dequeue
* Front
* Rear

---

## Summary

A Queue is a FIFO data structure where insertion occurs at the rear and deletion occurs at the front.
