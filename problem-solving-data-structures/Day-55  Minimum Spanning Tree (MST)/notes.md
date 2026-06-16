📘 Day 55 – Minimum Spanning Tree (MST)
notes.md
Day 55 – Minimum Spanning Tree (MST)
Objective

The goal of this session is to understand the Minimum Spanning Tree (MST) concept and its importance in graph optimization problems.

What is a Spanning Tree?

A Spanning Tree is a subgraph that:

Includes all vertices.
Connects all vertices.
Contains no cycles.

For a graph with:

V vertices

a spanning tree contains:

V - 1 edges
Example Graph
       A
      / \
    4/   \3
    B-----C
       2

Vertices:

A, B, C

Edges:

AB = 4

AC = 3

BC = 2
Possible Spanning Trees
Tree 1
A --- B
 \
  \
   C

Cost:

4 + 3 = 7
Tree 2
A --- C --- B

Cost:

3 + 2 = 5
Tree 3
A --- B --- C

Cost:

4 + 2 = 6
Minimum Spanning Tree

The spanning tree having the smallest total edge weight is called:

Minimum Spanning Tree (MST)

For the above graph:

A --- C --- B

Cost:

5

MST Found ✅

Properties of MST
Connects All Vertices

Every vertex must be reachable.

No Cycles

A cycle increases cost unnecessarily.

Minimum Cost

Among all spanning trees, MST has the lowest weight.

Why MST?

MST helps minimize:

Cost
Distance
Resources
Network Length
Applications
Network Design
Internet Cables
Telephone Networks
Electrical Grids
Road Construction

Connect cities using minimum road cost.

Water Pipelines

Reduce pipe installation cost.

Computer Networks

Optimize communication links.

MST Algorithms
Prim's Algorithm

Build MST by expanding one vertex at a time.

Kruskal's Algorithm

Build MST by selecting minimum weight edges.

These are the two most famous MST algorithms.

Example MST

Graph:

       A
      / \
    4/   \3
    B-----C
       2

Choose smallest edges:

BC = 2

AC = 3

Total Cost:

5
Time Complexity

Depends on algorithm.

Prim's Algorithm
O(E log V)
Kruskal's Algorithm
O(E log E)

Where:

V = Vertices

E = Edges
Key Concepts Learned
Spanning Tree
Minimum Spanning Tree
Graph Optimization
Edge Weight
Prim's Algorithm
Kruskal's Algorithm
Summary

A Minimum Spanning Tree is a spanning tree with the minimum possible total edge weight. MSTs are widely used in network design, transportation systems, and infrastructure optimization.