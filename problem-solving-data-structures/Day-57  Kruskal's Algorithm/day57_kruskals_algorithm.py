# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Kruskal's Algorithm
# Day         : 57
# Description : Minimum Spanning Tree using Kruskal's
#               Algorithm and Union-Find.
# ==========================================================

parent = {}


def find(vertex):

    if parent[vertex] != vertex:

        parent[vertex] = find(parent[vertex])

    return parent[vertex]


def union(vertex1, vertex2):

    root1 = find(vertex1)

    root2 = find(vertex2)

    if root1 != root2:

        parent[root2] = root1


vertices = ["A", "B", "C", "D"]

for vertex in vertices:

    parent[vertex] = vertex


edges = [

    (1, "B", "D"),

    (2, "A", "B"),

    (3, "A", "C"),

    (4, "C", "D")

]

edges.sort()

mst = []

total_cost = 0

for weight, u, v in edges:

    if find(u) != find(v):

        union(u, v)

        mst.append((u, v, weight))

        total_cost += weight


print("MST Edges:\n")

for edge in mst:

    print(edge)

print("\nTotal Cost:")

print(total_cost)