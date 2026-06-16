# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Connected Components in Graph
# Day         : 42
# Description : Finding connected components using DFS.
# ==========================================================

graph = {

    "A": ["B", "C"],

    "B": ["A"],

    "C": ["A"],

    "D": ["E"],

    "E": ["D"]

}


def dfs(graph, vertex, visited):

    visited.add(vertex)

    print(vertex, end=" ")

    for neighbor in graph[vertex]:

        if neighbor not in visited:

            dfs(graph, neighbor, visited)


visited = set()

components = 0

print("Connected Components:\n")

for vertex in graph:

    if vertex not in visited:

        components += 1

        print(f"Component {components}: ", end="")

        dfs(graph, vertex, visited)

        print()

print("\nTotal Components =", components)