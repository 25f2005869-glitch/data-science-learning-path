# Day 37 – Depth First Search (DFS)

## Objective

The goal of this session is to understand Depth First Search (DFS) and how it explores nodes deeply before backtracking.

---

## What is DFS?

Depth First Search (DFS) is a graph/tree traversal algorithm that explores a branch completely before moving to another branch.

DFS goes as deep as possible and then backtracks.

---

## DFS Principle

DFS uses:

```text
Stack (LIFO)
```

or

```text
Recursion
```

to keep track of nodes.

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

## DFS Traversal

Starting from Root:

```text
A
```

Move Left:

```text
B
```

Move Left Again:

```text
D
```

No Child Available

Backtrack to:

```text
B
```

Visit:

```text
E
```

Backtrack to:

```text
A
```

Visit Right Subtree:

```text
C → F → G
```

Final DFS Order:

```text
A B D E C F G
```

---

## DFS Algorithm

1. Visit current node.
2. Mark it as visited.
3. Recursively visit unvisited children.
4. Backtrack when no child remains.

---

## Pseudocode

```text
DFS(node)

VISIT node

FOR each child

    DFS(child)
```

---

## Applications

* Maze Solving
* Path Finding
* Cycle Detection
* Topological Sorting
* Backtracking Problems
* Artificial Intelligence

---

## Time Complexity

For Graphs:

```text
O(V + E)
```

Where:

* V = Vertices
* E = Edges

For Trees:

```text
O(n)
```

---

## Space Complexity

```text
O(h)
```

Where h is the height of the tree.

Worst Case:

```text
O(n)
```

---

## BFS vs DFS

| Feature        | BFS        | DFS               |
| -------------- | ---------- | ----------------- |
| Data Structure | Queue      | Stack / Recursion |
| Traversal      | Level Wise | Depth Wise        |
| Shortest Path  | Yes        | No                |
| Memory Usage   | More       | Less              |

---

## Key Concepts Learned

* Depth First Search
* Recursion
* Stack
* Backtracking
* Graph Traversal

---

## Summary

DFS explores one path completely before moving to another path and is one of the most important graph and tree traversal algorithms.
