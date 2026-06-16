# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Traveling Salesman Problem (TSP)
# Day         : 80
# Description : TSP using Bitmask Dynamic Programming.
# ==========================================================

from functools import lru_cache

distance = [

    [0, 10, 15, 20],

    [10, 0, 35, 25],

    [15, 35, 0, 30],

    [20, 25, 30, 0]

]

n = len(distance)


@lru_cache(None)
def tsp(mask, city):

    if mask == (1 << n) - 1:

        return distance[city][0]

    minimum_cost = float("inf")

    for next_city in range(n):

        if not (mask & (1 << next_city)):

            cost = (

                distance[city][next_city]

                + tsp(

                    mask | (1 << next_city),

                    next_city

                )

            )

            minimum_cost = min(

                minimum_cost,

                cost

            )

    return minimum_cost


result = tsp(1, 0)

print("Minimum Tour Cost:")

print(result)