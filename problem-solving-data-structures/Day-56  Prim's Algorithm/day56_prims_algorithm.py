# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Prim's Algorithm
# Day         : 56
# Description : Minimum Spanning Tree using Prim's
#               Algorithm and Min Heap.
# ==========================================================

import heapq

graph = {

    "A": [("B", 2), ("C", 3)],

    "B": [("A", 2), ("D", 1)],

    "C": [("A", 3), ("D", 4)],

    "D": [("B", 1), ("C", 4)]

}


def prim(graph, start):

    visited = set()

    min_heap = [(0, start)]

    total_cost = 0

    mst_edges = []

    while min_heap:

        weight, vertex = heapq.heappop(min_heap)

        if vertex in visited:

            continue

        visited.add(vertex)

        total_cost += weight

        if weight != 0:

            mst_edges.append((vertex, weight))

        for neighbor, edge_weight in graph[vertex]:

            if neighbor not in visited:

                heapq.heappush(

                    min_heap,

                    (edge_weight, neighbor)

                )

    return mst_edges, total_cost


mst, cost = prim(graph, "A")

print("MST Edges:\n")

for edge in mst:

    print(edge)

print("\nTotal Cost:")

print(cost)