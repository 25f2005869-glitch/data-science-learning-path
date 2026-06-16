Day 56 – Prim's Algorithm
Objective

The goal of this session is to understand Prim's Algorithm and how it is used to construct a Minimum Spanning Tree (MST).

What is Prim's Algorithm?

Prim's Algorithm is a Greedy Algorithm used to find the:

Minimum Spanning Tree (MST)

of a weighted, connected, undirected graph.

Key Idea

Prim's Algorithm starts from any vertex and repeatedly adds:

Minimum Weight Edge

that connects a visited vertex to an unvisited vertex.

Example Graph
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
Step 1

Start from:

A

Visited:

A

Available Edges:

AB = 2

AC = 3

Choose:

AB = 2
Step 2

Visited:

A, B

Available Edges:

AC = 3

BD = 1

Choose:

BD = 1
Step 3

Visited:

A, B, D

Available Edges:

AC = 3

CD = 4

Choose:

AC = 3
Final MST

Selected Edges:

AB = 2

BD = 1

AC = 3

Total Cost:

6
Prim's Algorithm Steps
Start from any vertex.
Mark it visited.
Add all connected edges into a Min Heap.
Select minimum weight edge.
Add new vertex to MST.
Repeat until all vertices are included.
Why Greedy Works?

At every step:

Choose Minimum Available Edge

This ensures minimum total cost while avoiding cycles.

Applications
Network Design
Internet Networks
Telephone Systems
Transportation
Road Networks
Railway Systems
Utility Systems
Water Pipelines
Electric Grids
Time Complexity

Using Min Heap:

O(E log V)

Where:

V = Vertices

E = Edges
Space Complexity
O(V + E)
Prim vs Kruskal
Feature	Prim	Kruskal
Approach	Vertex Based	Edge Based
Data Structure	Min Heap	Union-Find
Builds Tree	Gradually	Edge Selection
Best For	Dense Graphs	Sparse Graphs
Key Concepts Learned
Prim's Algorithm
Minimum Spanning Tree
Greedy Algorithm
Min Heap
Graph Optimization
Summary

Prim's Algorithm constructs a Minimum Spanning Tree by repeatedly selecting the minimum weight edge that connects the current tree to an unvisited vertex.