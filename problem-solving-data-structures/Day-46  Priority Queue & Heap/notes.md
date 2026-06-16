📘 Day 46 – Priority Queue & Heap
notes.md
Day 46 – Priority Queue & Heap
Objective

The goal of this session is to understand Priority Queues and Heaps, which are widely used in scheduling systems, shortest path algorithms, and many optimization problems.

What is a Priority Queue?

A Priority Queue is a special queue where elements are processed according to priority rather than insertion order.

Normal Queue:

FIFO

First In First Out

Priority Queue:

Highest Priority First

or

Lowest Priority First

depending on implementation.

Example

Patients arriving at a hospital:

Patient A (Priority 3)

Patient B (Priority 1)

Patient C (Priority 2)

Processing Order:

Patient B

Patient C

Patient A
What is a Heap?

A Heap is a complete binary tree used to efficiently implement a Priority Queue.

Types of Heap
Min Heap

Smallest element remains at the root.

Example:

        10
       /  \
     20    30
    / \
   40 50

Root:

10

Minimum element is always available.

Max Heap

Largest element remains at the root.

Example:

        50
       /  \
     40    30
    / \
   20 10

Root:

50

Maximum element is always available.

Heap Properties
Complete Binary Tree

All levels are completely filled except possibly the last level.

Heap Order Property

Min Heap:

Parent ≤ Children

Max Heap:

Parent ≥ Children
Heap Operations
Insert

Add a new element.

Steps:

Insert at last position.
Heapify Up.
Delete Root

Steps:

Replace root with last element.
Heapify Down.
Peek

View root element.

Example Min Heap
Insert:

20, 10, 30

Heap:

      10
     /  \
   20    30
Applications
Dijkstra's Algorithm
CPU Scheduling
Task Management
Event Simulation
Network Routing
Operating Systems
Time Complexity
Operation	Complexity
Insert	O(log n)
Delete	O(log n)
Peek	O(1)
Build Heap	O(n)
Priority Queue vs Queue
Feature	Queue	Priority Queue
Processing Order	FIFO	Priority Based
Insertion	O(1)	O(log n)
Removal	O(1)	O(log n)
Key Concepts Learned
Priority Queue
Heap
Min Heap
Max Heap
Heapify
Complete Binary Tree
Summary

A Heap is an efficient tree-based data structure used to implement Priority Queues. It enables fast insertion, deletion, and retrieval of the highest or lowest priority element.