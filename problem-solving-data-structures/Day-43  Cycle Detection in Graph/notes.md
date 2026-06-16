Day 43 – Cycle Detection in Graph
Objective

The goal of this session is to understand how to detect cycles in an undirected graph using Depth First Search (DFS).

What is a Cycle?

A cycle exists when a path starts from a vertex and eventually returns to the same vertex.

Example:

A ----- B
|       |
|       |
C -------

Cycle:

A → B → C → A
Why Detect Cycles?

Cycle Detection is important in:

Network Analysis
Deadlock Detection
Circuit Design
Social Networks
Graph Algorithms
Example 1: Graph with Cycle
      A
     / \
    B---C

Possible Path:

A → B → C → A

Cycle Found ✅

Example 2: Graph without Cycle
A ----- B ----- C

No path returns to the starting vertex.

Cycle Not Found ❌

DFS Approach

While performing DFS:

Mark current node as visited.
Visit neighbors.
Ignore the parent node.
If a visited node is found that is not the parent, a cycle exists.
Visualization

Graph:

A ----- B
|       |
|       |
C -------

DFS Traversal:

A → B → C

From C:

C → A

A is already visited and not the parent.

Therefore:

Cycle Detected
Algorithm
Start DFS.
Maintain:
Visited Set
Parent Node
For every neighbor:
If unvisited → DFS
If visited and not parent → Cycle Found
Pseudocode
DFS(vertex, parent)

Mark vertex visited

FOR each neighbor

    IF neighbor not visited

        DFS(neighbor, vertex)

    ELSE IF neighbor != parent

        RETURN True
Applications
Deadlock Detection
Network Routing
Dependency Analysis
Compiler Design
Circuit Verification
Time Complexity
O(V + E)

Where:

V = Number of Vertices

E = Number of Edges
Space Complexity
O(V)

For recursion stack and visited set.

Key Concepts Learned
Cycle
Cycle Detection
DFS
Parent Node
Graph Traversal
Summary

Cycle Detection determines whether a graph contains a closed path. DFS is one of the most common and efficient methods for detecting cycles in undirected graphs.