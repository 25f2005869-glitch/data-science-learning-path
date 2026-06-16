# Day 26 – Circular Queue

## Objective

The goal of this session is to understand the Circular Queue data structure and how it improves the utilization of memory compared to a simple queue.

---

## What is a Circular Queue?

A Circular Queue is a type of queue in which the last position is connected back to the first position.

Instead of moving only in one direction, the queue forms a circle.

---

## Why Circular Queue?

In a simple queue, deleted positions at the front cannot be reused efficiently.

Example:

```text id="cq01"
Front                  Rear

10 → 20 → 30 → 40
```

After deleting 10 and 20:

```text id="cq02"
_  _  30  40
```

Empty spaces are wasted.

Circular Queue reuses these spaces.

---

## Circular Structure

```text id="cq03"
       +-----+
       |     |
       v     |
10 → 20 → 30 → 40
^              |
|______________|
```

The rear can wrap around to the beginning.

---

## Operations

### Enqueue

Insert an element at the rear.

### Dequeue

Remove an element from the front.

### Front

View the first element.

### Rear

View the last element.

### Is Empty

Check whether the queue is empty.

### Is Full

Check whether the queue is full.

---

## Applications

* CPU Scheduling
* Memory Buffers
* Keyboard Buffers
* Network Packet Processing
* Streaming Systems

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Front     | O(1)       |
| Rear      | O(1)       |
| Is Empty  | O(1)       |
| Is Full   | O(1)       |

---

## Queue vs Circular Queue

| Feature            | Queue          | Circular Queue |
| ------------------ | -------------- | -------------- |
| Memory Utilization | Less Efficient | More Efficient |
| Space Reuse        | No             | Yes            |
| Structure          | Linear         | Circular       |

---

## Key Concepts Learned

* Circular Queue
* Front Pointer
* Rear Pointer
* Wrap Around
* Efficient Space Utilization

---

## Summary

A Circular Queue solves the memory wastage problem of a simple queue by connecting the last position back to the first position.
