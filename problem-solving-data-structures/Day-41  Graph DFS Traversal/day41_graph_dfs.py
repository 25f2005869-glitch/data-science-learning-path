# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Graph DFS Traversal
# Day         : 41
# Description : Depth First Search traversal of a graph.
# ==========================================================

graph = {

    "A": ["B", "C"],

    "B": ["D", "E"],

    "C": ["F"],

    "D": [],

    "E": [],

    "F": []

}


def dfs(graph, vertex, visited):

    visited.add(vertex)

    print(vertex, end=" ")

    for neighbor in graph[vertex]:

        if neighbor not in visited:

            dfs(graph, neighbor, visited)


visited = set()

print("DFS Traversal:")

dfs(graph, "A", visited)