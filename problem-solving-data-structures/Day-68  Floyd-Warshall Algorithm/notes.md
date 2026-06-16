# Day 68 – Floyd-Warshall Algorithm

## Objective

The goal of this session is to understand the Floyd-Warshall Algorithm and how it finds the shortest paths between every pair of vertices in a graph.

---

## What is Floyd-Warshall Algorithm?

Floyd-Warshall is a Dynamic Programming algorithm used to find:

Shortest Paths Between All Pairs of Vertices

in a weighted graph.

It works with:

- Positive edge weights
- Negative edge weights

but

- No Negative Cycles

---

## Why Do We Need It?

Dijkstra's Algorithm:

Finds shortest path from one source.

Bellman-Ford Algorithm:

Finds shortest path from one source and handles negative weights.

Floyd-Warshall Algorithm:

Finds shortest paths between every pair of vertices.

---

## Example Graph

Vertices:

A, B, C

Edges:

A → B = 4

A → C = 11

B → C = 2

---

## Initial Distance Matrix

      A    B    C

A     0    4   11

B     ∞    0    2

C     ∞    ∞    0

---

## Key Idea

Try every vertex as an intermediate vertex.

Question:

Can path

A → B → C

be shorter than

A → C ?

---

## Example

Current Distance:

A → C

=

11

---

Using B as Intermediate:

A → B

+

B → C

=

4 + 2

=

6

---

Update Distance:

A → C

=

6

✅ Better Path Found

---

## Dynamic Programming Relation

For every vertex k:

Check whether

i → k → j

is shorter than

i → j

Update:

distance[i][j]

=

min(

distance[i][j],

distance[i][k] + distance[k][j]

)

---

## Algorithm

1. Create distance matrix.
2. Choose an intermediate vertex.
3. Update all vertex pairs.
4. Repeat for every vertex.
5. Final matrix contains shortest paths.

---

## Example Final Matrix

      A    B    C

A     0    4    6

B     ∞    0    2

C     ∞    ∞    0

---

## Applications

### Network Routing

Shortest routes between devices.

### Transportation Systems

All city-to-city shortest routes.

### Social Networks

Connection analysis.

### Graph Analytics

Reachability and path optimization.

---

## Time Complexity

O(V³)

Where:

V = Number of Vertices

---

## Space Complexity

O(V²)

---

## Floyd-Warshall vs Bellman-Ford

| Feature | Floyd-Warshall | Bellman-Ford |
|-----------|-----------|-----------|
| Source Vertices | All Pairs | Single Source |
| Negative Edges | Yes | Yes |
| Negative Cycle Detection | Yes | Yes |
| Time Complexity | O(V³) | O(VE) |

---

## Key Concepts Learned

- Floyd-Warshall Algorithm
- All-Pairs Shortest Path
- Dynamic Programming
- Distance Matrix
- Graph Optimization

---

## Summary

Floyd-Warshall is a Dynamic Programming algorithm that computes the shortest paths between all pairs of vertices by repeatedly considering intermediate vertices and updating path costs.