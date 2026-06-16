# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Topological Sorting
# Day         : 69
# Description : Topological Sort using Kahn's Algorithm.
# ==========================================================

from collections import deque

graph = {

    "A": ["C"],

    "B": ["C"],

    "C": ["D"],

    "D": []

}

in_degree = {

    vertex: 0

    for vertex in graph

}

for vertex in graph:

    for neighbor in graph[vertex]:

        in_degree[neighbor] += 1

queue = deque()

for vertex in in_degree:

    if in_degree[vertex] == 0:

        queue.append(vertex)

topological_order = []

while queue:

    current = queue.popleft()

    topological_order.append(current)

    for neighbor in graph[current]:

        in_degree[neighbor] -= 1

        if in_degree[neighbor] == 0:

            queue.append(neighbor)

print("Topological Order:\n")

print(topological_order)