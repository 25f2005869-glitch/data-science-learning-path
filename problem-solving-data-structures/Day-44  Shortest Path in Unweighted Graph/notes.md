📘 Day 44 – Shortest Path in Unweighted Graph
notes.md
Day 44 – Shortest Path in Unweighted Graph
Objective

The goal of this session is to understand how Breadth First Search (BFS) can be used to find the shortest path in an unweighted graph.

What is Shortest Path?

The Shortest Path between two vertices is the path that uses the minimum number of edges.

In an unweighted graph:

All edges have equal cost.

Therefore:

Minimum Edges = Shortest Path
Example Graph
      A
     / \
    B   C
   /     \
  D ----- E
Find Shortest Path

Source:

A

Destination:

E

Possible Paths:

A → C → E

Length:

2 Edges
A → B → D → E

Length:

3 Edges

Shortest Path:

A → C → E
Why BFS?

BFS explores vertices level by level.

The first time a vertex is reached:

Shortest Path Found

because BFS always visits vertices using the minimum number of edges.

BFS Levels

Starting from A:

Level 0

A
Level 1

B, C
Level 2

D, E

E is reached at Level 2.

Therefore:

Distance = 2
Algorithm
Start BFS from source.
Maintain:
Queue
Visited Set
Distance Dictionary
For every neighbor:
Distance = Current Distance + 1
Continue until destination is reached.
Pseudocode
BFS(source)

distance[source] = 0

WHILE queue not empty

    current = dequeue()

    FOR each neighbor

        IF neighbor not visited

            distance[neighbor]

            = distance[current] + 1
Applications
GPS Navigation
Social Networks
Network Routing
Game Path Finding
Web Crawlers
Time Complexity
O(V + E)

Where:

V = Number of Vertices

E = Number of Edges
Space Complexity
O(V)

For queue and distance storage.

Key Concepts Learned
Shortest Path
BFS
Distance Array
Unweighted Graph
Graph Traversal
Summary

BFS is the standard algorithm for finding the shortest path in an unweighted graph because it explores vertices level by level.