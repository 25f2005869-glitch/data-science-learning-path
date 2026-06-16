# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Graph Representation
# Day         : 39
# Description : Adjacency Matrix and Adjacency List
#               representation of a graph.
# ==========================================================

# Adjacency Matrix

adj_matrix = [

    [0, 1, 1, 0],

    [1, 0, 0, 1],

    [1, 0, 0, 1],

    [0, 1, 1, 0]

]

print("Adjacency Matrix:\n")

for row in adj_matrix:

    print(row)


# Adjacency List

graph = {

    "A": ["B", "C"],

    "B": ["A", "D"],

    "C": ["A", "D"],

    "D": ["B", "C"]

}

print("\nAdjacency List:\n")

for vertex in graph:

    print(vertex, "->", graph[vertex])