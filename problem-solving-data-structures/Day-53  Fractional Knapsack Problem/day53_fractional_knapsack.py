# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Fractional Knapsack Problem
# Day         : 53
# Description : Maximum profit using Fractional Knapsack
#               and Greedy Algorithm.
# ==========================================================

items = [

    (60, 10),   # (value, weight)
    (100, 20),
    (120, 30)

]

capacity = 50

# Sort by value/weight ratio
items.sort(

    key=lambda item: item[0] / item[1],

    reverse=True

)

total_value = 0

for value, weight in items:

    if capacity >= weight:

        total_value += value

        capacity -= weight

    else:

        fraction = capacity / weight

        total_value += value * fraction

        break

print("Maximum Value:")

print(total_value)