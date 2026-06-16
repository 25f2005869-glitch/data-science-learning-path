# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Floyd-Warshall Algorithm
# Day         : 68
# Description : All-Pairs Shortest Path using
#               Floyd-Warshall Algorithm.
# ==========================================================

INF = float("inf")

graph = [

    [0, 4, 11],

    [INF, 0, 2],

    [INF, INF, 0]

]

vertices = len(graph)

distance = [row[:] for row in graph]

for k in range(vertices):

    for i in range(vertices):

        for j in range(vertices):

            distance[i][j] = min(

                distance[i][j],

                distance[i][k] + distance[k][j]

            )

print("Shortest Distance Matrix:\n")

for row in distance:

    print(row)