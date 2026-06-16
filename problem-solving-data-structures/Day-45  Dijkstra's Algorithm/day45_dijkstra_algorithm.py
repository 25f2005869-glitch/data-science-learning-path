# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Dijkstra's Algorithm
# Day         : 45
# Description : Shortest path in a weighted graph using
#               Dijkstra's Algorithm.
# ==========================================================

import heapq

graph = {

    "A": [("B", 4), ("C", 1)],

    "B": [],

    "C": [("B", 2)]

}


def dijkstra(graph, start):

    distances = {

        vertex: float("inf")

        for vertex in graph

    }

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_vertex = heapq.heappop(

            priority_queue

        )

        if current_distance > distances[current_vertex]:

            continue

        for neighbor, weight in graph[current_vertex]:

            distance = (

                current_distance + weight

            )

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(

                    priority_queue,

                    (distance, neighbor)

                )

    return distances


result = dijkstra(graph, "A")

print("Shortest Distances From A:\n")

for vertex in result:

    print(vertex, ":", result[vertex])