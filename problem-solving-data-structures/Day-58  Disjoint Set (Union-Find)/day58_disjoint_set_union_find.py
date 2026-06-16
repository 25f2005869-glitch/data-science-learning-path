# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Disjoint Set (Union-Find)
# Day         : 58
# Description : Basic Union-Find implementation with
#               Path Compression.
# ==========================================================

parent = {}


def make_set(vertex):

    parent[vertex] = vertex


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

    make_set(vertex)

union("A", "B")
union("C", "D")
union("A", "C")

print("Parent Structure:\n")

for vertex in vertices:

    print(vertex, "->", find(vertex))