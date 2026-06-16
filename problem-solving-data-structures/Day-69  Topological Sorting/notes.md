# Day 69 – Topological Sorting

## Objective

The goal of this session is to understand Topological Sorting and how it is used in Directed Acyclic Graphs (DAGs).

---

## What is Topological Sorting?

Topological Sorting is a linear ordering of vertices in a Directed Acyclic Graph (DAG).

In this ordering:

For every directed edge

U → V

Vertex U appears before Vertex V.

---

## Example

Graph:

A → C

B → C

C → D

Possible Topological Order:

A B C D

Another Valid Order:

B A C D

Both are correct because:

A appears before C

B appears before C

C appears before D

---

## Where is it Used?

Topological Sorting is useful when tasks have dependencies.

Examples:

- Course Scheduling
- Project Planning
- Build Systems
- Task Scheduling
- Dependency Resolution

---

## Directed Acyclic Graph (DAG)

Topological Sorting works only on:

Directed Acyclic Graphs

Acyclic means:

No Cycles

---

## Example DAG

      A      B
       \    /
        \  /
         C
         |
         D

Dependencies:

A → C

B → C

C → D

---

## Key Idea

A vertex with:

In-Degree = 0

can be processed first.

---

## What is In-Degree?

In-Degree:

Number of incoming edges.

Example:

A → C

B → C

In-Degree(C)

=

2

---

## Kahn's Algorithm

Topological Sorting can be performed using:

Kahn's Algorithm

Steps:

1. Compute In-Degree of every vertex.
2. Insert vertices with In-Degree 0 into a queue.
3. Remove a vertex from queue.
4. Add it to result.
5. Reduce In-Degree of neighbors.
6. If neighbor becomes 0:
   Add it to queue.
7. Repeat until queue becomes empty.

---

## Example

Initial In-Degree:

A = 0

B = 0

C = 2

D = 1

---

Queue:

A B

---

Process A

Queue:

B

---

Process B

C becomes:

0

Queue:

C

---

Process C

D becomes:

0

Queue:

D

---

Process D

Finished.

Topological Order:

A B C D

---

## Detecting Cycles

If all vertices are not processed:

Cycle Exists

Topological Sorting is impossible.

---

## Applications

### Course Scheduling

Prerequisite management.

### Project Management

Task ordering.

### Build Systems

Compilation order.

### Dependency Resolution

Package installation order.

---

## Time Complexity

O(V + E)

Where:

V = Number of Vertices

E = Number of Edges

---

## Space Complexity

O(V)

---

## Key Concepts Learned

- Topological Sorting
- Directed Acyclic Graph
- In-Degree
- Kahn's Algorithm
- Dependency Graph

---

## Summary

Topological Sorting provides a valid order for processing vertices in a Directed Acyclic Graph while respecting all dependencies.