📘 Day 40 – Graph BFS Traversal
notes.md
Day 40 – Graph BFS Traversal
Objective

The goal of this session is to understand Breadth First Search (BFS) traversal in graphs using a queue.

What is Graph BFS?

Breadth First Search (BFS) is a graph traversal algorithm that explores vertices level by level.

It visits all neighboring vertices before moving to the next level.

BFS Principle

BFS uses:

Queue (FIFO)

The first vertex inserted into the queue is processed first.

Example Graph
       A
      / \
     B   C
    / \   \
   D   E   F
BFS Traversal

Start from:

A

Visit Neighbors:

B C

Visit Next Level:

D E F

Final Traversal:

A B C D E F
BFS Algorithm
Create an empty queue.
Mark starting vertex as visited.
Insert it into the queue.
While queue is not empty:
Remove front vertex.
Visit vertex.
Add all unvisited neighbors.
Pseudocode
BFS(start)

Create Queue

Mark start as visited

Enqueue(start)

WHILE Queue not empty

    vertex = Dequeue()

    Visit(vertex)

    FOR each neighbor

        IF not visited

            Mark visited

            Enqueue(neighbor)
Example Execution

Initial Queue:

[A]

After Visiting A:

[B, C]

After Visiting B:

[C, D, E]

After Visiting C:

[D, E, F]

Final Queue:

[]
Applications
Shortest Path in Unweighted Graph
Social Networks
Web Crawlers
GPS Navigation
Network Broadcasting
Time Complexity
O(V + E)

Where:

V = Number of Vertices

E = Number of Edges
Space Complexity
O(V)

For Queue and Visited Set.

Key Concepts Learned
Graph BFS
Queue
Visited Set
Level Order Traversal
O(V + E)
Summary

Graph BFS explores vertices level by level using a queue and guarantees the shortest path in an unweighted graph.