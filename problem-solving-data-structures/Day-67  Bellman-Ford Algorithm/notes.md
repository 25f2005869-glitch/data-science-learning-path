# Day 67 – Bellman-Ford Algorithm

## Objective

The goal of this session is to understand the Bellman-Ford Algorithm and how it finds shortest paths in graphs containing negative edge weights.

---

## What is Bellman-Ford Algorithm?

Bellman-Ford is a shortest path algorithm used to find the minimum distance from a source vertex to all other vertices in a weighted graph.

Unlike Dijkstra's Algorithm:

Bellman-Ford can handle negative edge weights.

---

## Why Do We Need Bellman-Ford?

Dijkstra's Algorithm works only when:

All edge weights are non-negative.

If negative weights exist:

Dijkstra may produce incorrect results.

Bellman-Ford solves this problem.

---

## Example Graph

Vertices:

A, B, C

Edges:

A → B = 4

A → C = 5

B → C = -2

---

## Shortest Path

Source:

A

Direct Path:

A → C

Cost = 5

---

Alternative Path:

A → B → C

Cost =

4 + (-2)

= 2

---

Shortest Distance:

A → B → C

Cost = 2

✅

---

## Key Idea

Relax all edges repeatedly.

Relaxation means:

If a shorter path is found,

update the distance.

---

## Initialization

Distance from source:

A = 0

All Others:

∞

Initial Table:

A = 0

B = ∞

C = ∞

---

## First Iteration

Relax:

A → B

Distance[B] = 4

---

Relax:

A → C

Distance[C] = 5

---

Relax:

B → C

Distance[C]

=

min(5, 4 + (-2))

=

2

---

Updated Distances:

A = 0

B = 4

C = 2

---

## Number of Iterations

For a graph with:

V vertices

Bellman-Ford performs:

V − 1

iterations.

This guarantees shortest paths.

---

## Negative Cycle Detection

After V − 1 iterations:

Perform one more iteration.

If any distance still decreases:

Negative Cycle Exists

---

## What is a Negative Cycle?

A cycle whose total weight is negative.

Example:

A → B = 1

B → C = -3

C → A = 1

Total:

1 + (-3) + 1

=

-1

Negative Cycle ❌

Shortest path becomes undefined.

---

## Algorithm

1. Initialize distances.
2. Repeat V−1 times:
   - Relax every edge.
3. Check for negative cycles.
4. Return shortest distances.

---

## Applications

### Network Routing

Shortest path computation.

### Transportation Systems

Route optimization.

### Currency Exchange

Arbitrage detection.

### Graph Analysis

Negative cycle detection.

---

## Time Complexity

O(V × E)

Where:

V = Number of Vertices

E = Number of Edges

---

## Space Complexity

O(V)

---

## Bellman-Ford vs Dijkstra

| Feature | Bellman-Ford | Dijkstra |
|----------|-------------|-----------|
| Negative Edges | Yes | No |
| Negative Cycles | Detects | No |
| Time Complexity | O(VE) | O(E log V) |
| Faster | No | Yes |

---

## Key Concepts Learned

- Bellman-Ford Algorithm
- Shortest Path
- Edge Relaxation
- Negative Weights
- Negative Cycle Detection

---

## Summary

Bellman-Ford is a shortest path algorithm capable of handling graphs with negative edge weights. It repeatedly relaxes edges and can also detect negative cycles.