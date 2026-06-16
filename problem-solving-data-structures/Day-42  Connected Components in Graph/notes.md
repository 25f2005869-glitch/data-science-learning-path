📘 Day 42 – Connected Components in Graph
notes.md
Day 42 – Connected Components in Graph
Objective

The goal of this session is to understand Connected Components in an undirected graph and how DFS can be used to find them.

What is a Connected Component?

A Connected Component is a group of vertices where every vertex is reachable from every other vertex in the same group.

If a graph has isolated groups of vertices, each group forms a separate connected component.

Example Graph
      A ----- B

      |       |

      C ----- D


      E ----- F

This graph contains:

Component 1:

A, B, C, D

Component 2:

E, F

Total Connected Components:

2
Understanding Connectivity

Vertices belong to the same component if there exists a path between them.

Example:

A → C → D → B

Therefore:

A, B, C, D

belong to the same component.

Why Connected Components?

Connected Components help us:

Find isolated groups
Analyze networks
Detect disconnected systems
Study social networks
Process maps and routes
Finding Connected Components

Use DFS or BFS.

Algorithm:

Mark all vertices unvisited.
Traverse every vertex.
If a vertex is unvisited:
Start DFS.
Mark all reachable vertices.
Count one connected component.
Repeat until all vertices are visited.
Example Traversal

Graph:

A --- B

|

C


D --- E

Start DFS from A:

A → B → C

Component Count:

1

Next Unvisited Vertex:

D → E

Component Count:

2
Pseudocode
components = 0

FOR each vertex

    IF vertex not visited

        DFS(vertex)

        components += 1
Applications
Social Network Analysis
Computer Networks
Road Maps
Image Processing
Community Detection
Time Complexity

DFS Traversal:

O(V + E)

Where:

V = Number of Vertices

E = Number of Edges
Space Complexity
O(V)

For visited set and recursion stack.

Key Concepts Learned
Connected Component
DFS
Graph Connectivity
Reachability
Component Counting
Summary

A Connected Component is a group of vertices that are connected to each other. DFS and BFS are commonly used to identify and count connected components in graphs.