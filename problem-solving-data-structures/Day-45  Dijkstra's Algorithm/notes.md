📘 Day 45 – Dijkstra's Algorithm
notes.md
Day 45 – Dijkstra's Algorithm
Objective

The goal of this session is to understand Dijkstra's Algorithm and how it finds the shortest path in a weighted graph.

What is Dijkstra's Algorithm?

Dijkstra's Algorithm is used to find the shortest distance from a source vertex to all other vertices in a weighted graph.

Condition:

All edge weights must be non-negative.
Why Do We Need Dijkstra?

BFS works only for:

Unweighted Graphs

When edges have different weights:

Distance ≠ Number of Edges

Therefore BFS cannot guarantee the shortest path.

Example Weighted Graph
       A
     /   \
   4/     \1
   B ----- C
      2

Edge Weights:

A → B = 4

A → C = 1

C → B = 2
Finding Shortest Path

Source:

A

Direct Path:

A → B

Cost = 4

Alternative Path:

A → C → B

Cost = 1 + 2 = 3

Shortest Path:

A → C → B

Cost = 3
Key Idea

Always choose:

Vertex with Minimum Distance

and update distances of its neighbors.

This process is called:

Relaxation
Dijkstra Algorithm Steps
Set source distance = 0
Set all other distances = ∞
Select vertex with minimum distance
Update neighboring distances
Repeat until all vertices are processed
Distance Table

Initial:

Vertex    Distance

A         0

B         ∞

C         ∞

After Processing A:

Vertex    Distance

A         0

B         4

C         1

After Processing C:

Vertex    Distance

A         0

B         3

C         1
Priority Queue

Dijkstra is usually implemented using:

Min Heap (Priority Queue)

to efficiently obtain the minimum distance vertex.

Applications
Google Maps
GPS Navigation
Network Routing
Robotics
Airline Route Planning
Logistics Systems
Time Complexity

Using Priority Queue:

O((V + E) log V)

Where:

V = Vertices

E = Edges
Space Complexity
O(V)
Limitations

Dijkstra cannot handle:

Negative Edge Weights

For negative weights:

Bellman-Ford Algorithm

is used.

Key Concepts Learned
Weighted Graph
Shortest Path
Dijkstra Algorithm
Relaxation
Priority Queue
Min Heap
Summary

Dijkstra's Algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights.