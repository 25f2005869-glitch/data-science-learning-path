Day 39 – Graph Representation (Adjacency Matrix & Adjacency List)
Objective

The goal of this session is to understand the two most common methods used to represent graphs in computer memory.

Why Graph Representation?

Graphs exist conceptually as vertices and edges.

To perform graph algorithms efficiently, graphs must be stored in memory.

Two standard representations are:

Adjacency Matrix
Adjacency List
Example Graph
      A
     / \
    B   C
     \ /
      D

Vertices:

A, B, C, D

Edges:

(A,B)
(A,C)
(B,D)
(C,D)
1. Adjacency Matrix

An Adjacency Matrix is a 2D matrix where:

matrix[i][j]

indicates whether an edge exists between vertices i and j.

Matrix Representation
      A B C D

A     0 1 1 0

B     1 0 0 1

C     1 0 0 1

D     0 1 1 0
Interpretation
A → B = 1

A → D = 0

1 means edge exists.

0 means edge does not exist.

Advantages
Easy to implement
Fast edge lookup
O(1)
Disadvantages
Wastes memory for sparse graphs
Requires O(V²) space
2. Adjacency List

Each vertex stores a list of connected vertices.

Representation
A → B, C

B → A, D

C → A, D

D → B, C
Memory Usage

Only existing edges are stored.

Space Complexity:

O(V + E)
Advantages
Efficient memory usage
Best for sparse graphs
Disadvantages
Edge lookup slower than matrix
O(degree)
Comparison
Feature	Adjacency Matrix	Adjacency List
Space	O(V²)	O(V + E)
Edge Search	O(1)	O(degree)
Memory Usage	High	Low
Sparse Graphs	Poor	Excellent
Dense Graphs	Good	Good
When to Use?
Use Adjacency Matrix
Small Graphs
Dense Graphs
Frequent Edge Checks
Use Adjacency List
Large Graphs
Sparse Graphs
BFS and DFS Algorithms
Applications
Social Networks
Road Maps
Computer Networks
Recommendation Systems
Search Engines
Key Concepts Learned
Graph Representation
Adjacency Matrix
Adjacency List
Space Complexity
Dense Graph
Sparse Graph
Summary

Adjacency Matrix and Adjacency List are the two fundamental methods for storing graphs. Most real-world graph algorithms prefer Adjacency Lists because they use memory efficiently.