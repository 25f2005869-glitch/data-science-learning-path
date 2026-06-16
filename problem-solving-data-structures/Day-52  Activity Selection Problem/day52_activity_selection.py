# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Activity Selection Problem
# Day         : 52
# Description : Selecting maximum non-overlapping
#               activities using Greedy Algorithm.
# ==========================================================

activities = [

    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (8, 9),
    (5, 9)

]

# Sort by Finish Time
activities.sort(key=lambda x: x[1])

selected = [activities[0]]

last_finish = activities[0][1]

for start, finish in activities[1:]:

    if start >= last_finish:

        selected.append((start, finish))

        last_finish = finish

print("Selected Activities:\n")

for activity in selected:

    print(activity)

print("\nTotal Activities:")

print(len(selected))