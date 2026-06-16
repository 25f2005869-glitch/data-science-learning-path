# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Cycle Detection in Graph
# Day         : 43
# Description : Detecting cycles in an undirected graph
#               using DFS.
# ==========================================================

graph = {

    "A": ["B", "C"],

    "B": ["A", "C"],

    "C": ["A", "B"],

    "D": []

}


def has_cycle(graph, vertex, visited, parent):

    visited.add(vertex)

    for neighbor in graph[vertex]:

        if neighbor not in visited:

            if has_cycle(graph, neighbor, visited, vertex):

                return True

        elif neighbor != parent:

            return True

    return False


visited = set()

cycle_found = False

for vertex in graph:

    if vertex not in visited:

        if has_cycle(graph, vertex, visited, None):

            cycle_found = True

            break


if cycle_found:

    print("Cycle Detected")

else:

    print("No Cycle Found")