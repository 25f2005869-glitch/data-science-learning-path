# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Segment Tree Introduction
# Day         : 72
# Description : Building a Segment Tree for range sums.
# ==========================================================

arr = [1, 3, 5, 7]

segment_tree = [0] * 16


def build(node, start, end):

    if start == end:

        segment_tree[node] = arr[start]

        return

    mid = (start + end) // 2

    build(2 * node, start, mid)

    build(2 * node + 1, mid + 1, end)

    segment_tree[node] = (

        segment_tree[2 * node]

        + segment_tree[2 * node + 1]

    )


build(1, 0, len(arr) - 1)

print("Segment Tree:\n")

for value in segment_tree[:8]:

    print(value)