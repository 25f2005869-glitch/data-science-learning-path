Day 41 – Graph DFS Traversal
Objective

The goal of this session is to understand Depth First Search (DFS) traversal in graphs using recursion.

What is Graph DFS?

Depth First Search (DFS) is a graph traversal algorithm that explores as far as possible along a branch before backtracking.

DFS visits a node, then one of its neighbors, then a neighbor of that neighbor, and so on.

DFS Principle

DFS uses:

Stack (LIFO)

or

Recursion

to remember previously visited vertices.

Example Graph
       A
      / \
     B   C
    / \   \
   D   E   F
DFS Traversal

Start from:

A

Go Deep:

A → B → D

Backtrack:

D → B

Continue:

B → E

Backtrack:

E → B → A

Move to:

C → F

Final Traversal:

A B D E C F
DFS Algorithm
Visit current vertex.
Mark it as visited.
Visit all unvisited neighbors recursively.
Backtrack when no neighbor remains.
Pseudocode
DFS(vertex)

Mark vertex visited

Visit(vertex)

FOR each neighbor

    IF neighbor not visited

        DFS(neighbor)
Example Execution

Start:

A

Visit:

B

Visit:

D

Backtrack:

B

Visit:

E

Backtrack:

A

Visit:

C

Visit:

F

Traversal Complete.

Applications
Maze Solving
Cycle Detection
Topological Sorting
Path Finding
Connected Components
Backtracking Problems
Time Complexity
O(V + E)

Where:

V = Number of Vertices

E = Number of Edges
Space Complexity
O(V)

For recursion stack and visited set.

DFS vs BFS
Feature	DFS	BFS
Data Structure	Stack	Queue
Traversal	Depth Wise	Level Wise
Memory Usage	Less	More
Shortest Path	No	Yes (Unweighted Graph)
Key Concepts Learned
Graph DFS
Recursion
Stack
Backtracking
Graph Traversal
Summary

Graph DFS explores a graph deeply before backtracking. It is one of the most important graph traversal algorithms and serves as the foundation for many advanced graph techniques.