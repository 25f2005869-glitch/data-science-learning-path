📘 Day 38 – Graphs Introduction
Objective

The goal of this session is to understand Graphs, their components, and why they are one of the most important data structures in computer science.

What is a Graph?

A Graph is a non-linear data structure consisting of:

Vertices (Nodes)
Edges (Connections)

A graph represents relationships between different objects.

Graph Structure
A ----- B
|       |
|       |
C ----- D

Vertices:

A, B, C, D

Edges:

(A,B)
(A,C)
(B,D)
(C,D)
Terminology
Vertex (Node)

A point in a graph.

A
B
C
D
Edge

A connection between two vertices.

A ----- B
Degree

Number of edges connected to a vertex.

Example:

A ----- B
|
|
C

Degree of A:

2
Types of Graphs
Undirected Graph

Edges have no direction.

A ----- B

A can reach B and B can reach A.

Directed Graph (Digraph)

Edges have direction.

A -----> B

A can reach B.

B cannot reach A.

Weighted Graph

Edges contain weights.

A --5-- B

A --2-- C

Weight may represent:

Distance
Cost
Time
Graph Representation
Adjacency Matrix
      A B C D

A     0 1 1 0
B     1 0 0 1
C     1 0 0 1
D     0 1 1 0
Adjacency List
A → B, C

B → A, D

C → A, D

D → B, C

Most graph algorithms use adjacency lists.

Applications of Graphs
Google Maps
Social Networks
Computer Networks
Flight Routes
Recommendation Systems
Web Page Linking
Artificial Intelligence
Example Graph
      A
     / \
    B   C
     \ /
      D

Adjacency List:

A → B, C

B → A, D

C → A, D

D → B, C
Time Complexity

Adjacency List:

Operation	Complexity
Add Vertex	O(1)
Add Edge	O(1)
Traverse	O(V + E)

Where:

V = Vertices
E = Edges
Key Concepts Learned
Graph
Vertex
Edge
Degree
Directed Graph
Undirected Graph
Weighted Graph
Adjacency Matrix
Adjacency List
Summary

Graphs are powerful data structures used to represent relationships between objects. They form the foundation of many real-world systems such as maps, networks, social media platforms, and search engines.