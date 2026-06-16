# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Bellman-Ford Algorithm
# Day         : 67
# Description : Shortest path with negative weights
#               using Bellman-Ford Algorithm.
# ==========================================================

vertices = ["A", "B", "C"]

edges = [

    ("A", "B", 4),

    ("A", "C", 5),

    ("B", "C", -2)

]

distance = {

    vertex: float("inf")

    for vertex in vertices

}

distance["A"] = 0

for _ in range(len(vertices) - 1):

    for source, destination, weight in edges:

        if (

            distance[source] != float("inf")

            and

            distance[source] + weight

            < distance[destination]

        ):

            distance[destination] = (

                distance[source]

                + weight

            )

print("Shortest Distances From A:\n")

for vertex in vertices:

    print(vertex, ":", distance[vertex])