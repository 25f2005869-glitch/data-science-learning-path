# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Minimum Spanning Tree (MST)
# Day         : 55
# Description : Simple MST example using sorted edges.
# ==========================================================

edges = [

    ("B", "C", 2),

    ("A", "C", 3),

    ("A", "B", 4)

]

# Sort edges by weight
edges.sort(key=lambda edge: edge[2])

mst_cost = 0

mst_edges = []

for u, v, weight in edges[:2]:

    mst_edges.append((u, v, weight))

    mst_cost += weight

print("MST Edges:\n")

for edge in mst_edges:

    print(edge)

print("\nTotal MST Cost:")

print(mst_cost)