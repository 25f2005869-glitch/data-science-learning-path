# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Shortest Path in Unweighted Graph
# Day         : 44
# Description : Finding shortest distance using BFS.
# ==========================================================

from collections import deque

graph = {

    "A": ["B", "C"],

    "B": ["A", "D"],

    "C": ["A", "E"],

    "D": ["B", "E"],

    "E": ["C", "D"]

}


def shortest_path(graph, start):

    distance = {start: 0}

    queue = deque([start])

    while queue:

        current = queue.popleft()

        for neighbor in graph[current]:

            if neighbor not in distance:

                distance[neighbor] = distance[current] + 1

                queue.append(neighbor)

    return distance


distances = shortest_path(graph, "A")

print("Shortest Distances From A:\n")

for vertex in distances:

    print(vertex, ":", distances[vertex])