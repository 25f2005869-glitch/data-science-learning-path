# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Graph BFS Traversal
# Day         : 40
# Description : Breadth First Search traversal of a graph.
# ==========================================================

from collections import deque

graph = {

    "A": ["B", "C"],

    "B": ["A", "D", "E"],

    "C": ["A", "F"],

    "D": [],

    "E": [],

    "F": []

}


def bfs(graph, start):

    visited = set()

    queue = deque([start])

    visited.add(start)

    while queue:

        vertex = queue.popleft()

        print(vertex, end=" ")

        for neighbor in graph[vertex]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)


print("BFS Traversal:")

bfs(graph, "A")