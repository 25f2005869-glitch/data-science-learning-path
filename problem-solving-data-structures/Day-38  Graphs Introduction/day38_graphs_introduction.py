# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Graphs Introduction
# Day         : 38
# Description : Graph representation using Adjacency List.
# ==========================================================

graph = {

    "A": ["B", "C"],

    "B": ["A", "D"],

    "C": ["A", "D"],

    "D": ["B", "C"]

}

print("Graph Adjacency List:\n")

for vertex in graph:

    print(vertex, "->", graph[vertex])