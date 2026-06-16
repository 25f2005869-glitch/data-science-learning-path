# Day 57 – Kruskal's Algorithm

## Objective

The goal of this session is to understand Kruskal's Algorithm and how it is used to construct a Minimum Spanning Tree (MST).

---

## What is Kruskal's Algorithm?

Kruskal's Algorithm is a Greedy Algorithm used to find the Minimum Spanning Tree (MST) of a weighted, connected, undirected graph.

Unlike Prim's Algorithm, Kruskal's Algorithm focuses on selecting edges rather than expanding vertices.

---

## Key Idea

Always choose the smallest available edge that does not create a cycle.

---

## Example Graph

        A
      /   \
    2/     \3
    B-------C
      \     /
      1\   /4
         D

Edge Weights:

AB = 2

AC = 3

BD = 1

CD = 4

---

## Step 1

Sort all edges by weight.

BD = 1

AB = 2

AC = 3

CD = 4

---

## Step 2

Choose:

BD = 1

Current MST Cost = 1

---

## Step 3

Choose:

AB = 2

Current MST Cost = 3

---

## Step 4

Choose:

AC = 3

Current MST Cost = 6

Now all vertices are connected.

MST Completed.

---

## Final MST

Selected Edges:

BD = 1

AB = 2

AC = 3

Total Cost:

6

---

## Why Greedy Works?

At every step:

Choose the Minimum Available Edge

while avoiding cycles.

This guarantees the Minimum Spanning Tree.

---

## Cycle Detection

Kruskal's Algorithm uses:

Union-Find (Disjoint Set)

to efficiently detect cycles.

Operations:

Make Set

Find

Union

---

## Kruskal's Algorithm Steps

1. Sort all edges by weight.
2. Initialize each vertex as a separate set.
3. Pick the smallest edge.
4. If it creates a cycle:
   Skip it.
5. Otherwise:
   Add it to MST.
6. Repeat until MST contains V−1 edges.

---

## Applications

### Network Design

Internet Networks

Telephone Systems

---

### Transportation

Road Networks

Railway Systems

---

### Utility Systems

Electric Grids

Water Pipelines

---

## Time Complexity

Sorting Edges:

O(E log E)

Union-Find Operations:

O(E α(V))

Overall:

O(E log E)

Where:

V = Vertices

E = Edges

---

## Space Complexity

O(V)

---

## Prim vs Kruskal

| Feature | Prim | Kruskal |
|----------|----------|----------|
| Approach | Vertex Based | Edge Based |
| Data Structure | Min Heap | Union-Find |
| Best For | Dense Graphs | Sparse Graphs |
| Cycle Check | Implicit | Explicit |

---

## Key Concepts Learned

- Kruskal's Algorithm
- Minimum Spanning Tree
- Greedy Algorithm
- Union-Find
- Cycle Detection
- Graph Optimization

---

## Summary

Kruskal's Algorithm constructs a Minimum Spanning Tree by repeatedly selecting the smallest edge that does not form a cycle.