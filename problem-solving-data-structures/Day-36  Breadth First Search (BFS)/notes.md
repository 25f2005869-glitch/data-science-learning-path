# Day 36 – Breadth First Search (BFS)

## Objective

The goal of this session is to understand Breadth First Search (BFS) and how it explores nodes level by level.

---

## What is BFS?

Breadth First Search (BFS) is a graph/tree traversal algorithm that visits nodes level by level.

It explores all neighboring nodes before moving to the next level.

---

## BFS Principle

BFS uses a:

```text
Queue (FIFO)
```

Data Structure.

The first node inserted into the queue is processed first.

---

## Example Tree

```text
         A
       /   \
      B     C
     / \   / \
    D   E F   G
```

---

## BFS Traversal

Start from Root:

```text
A
```

Visit Level 1:

```text
B C
```

Visit Level 2:

```text
D E F G
```

Final BFS Order:

```text
A B C D E F G
```

---

## BFS Algorithm

1. Create an empty queue.
2. Insert the starting node.
3. While queue is not empty:

   * Remove front node.
   * Visit node.
   * Insert all unvisited neighbors.

---

## Pseudocode

```text
BFS(start)

CREATE queue

ENQUEUE start

WHILE queue is not empty

    node = DEQUEUE

    VISIT node

    FOR each neighbor

        ENQUEUE neighbor
```

---

## Why BFS?

BFS is useful when:

* Finding shortest paths in unweighted graphs
* Level order traversal in trees
* Network routing
* Web Crawlers
* Social Network Analysis

---

## Time Complexity

For Graphs:

```text
O(V + E)
```

Where:

* V = Vertices
* E = Edges

For Binary Trees:

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

Queue may store an entire level.

---

## BFS vs DFS

| Feature        | BFS              | DFS               |
| -------------- | ---------------- | ----------------- |
| Data Structure | Queue            | Stack / Recursion |
| Traversal      | Level Wise       | Depth Wise        |
| Shortest Path  | Yes (Unweighted) | No                |
| Memory Usage   | More             | Less              |

---

## Key Concepts Learned

* Breadth First Search
* Queue
* Level Order Traversal
* Graph Traversal
* O(V + E)

---

## Summary

BFS explores nodes level by level using a queue and is one of the most important traversal algorithms in computer science.
