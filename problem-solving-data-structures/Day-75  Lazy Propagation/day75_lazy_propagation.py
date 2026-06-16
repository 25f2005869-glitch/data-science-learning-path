# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Lazy Propagation
# Day         : 75
# Description : Range updates using Lazy Propagation
#               in Segment Trees.
# ==========================================================

arr = [1, 3, 5, 7]

n = len(arr)

segment_tree = [0] * (4 * n)

lazy = [0] * (4 * n)


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


def update_range(

    node,

    start,

    end,

    left,

    right,

    value

):

    if lazy[node] != 0:

        segment_tree[node] += (

            end - start + 1

        ) * lazy[node]

        if start != end:

            lazy[2 * node] += lazy[node]

            lazy[2 * node + 1] += lazy[node]

        lazy[node] = 0

    if start > right or end < left:

        return

    if left <= start and end <= right:

        segment_tree[node] += (

            end - start + 1

        ) * value

        if start != end:

            lazy[2 * node] += value

            lazy[2 * node + 1] += value

        return

    mid = (start + end) // 2

    update_range(

        2 * node,

        start,

        mid,

        left,

        right,

        value

    )

    update_range(

        2 * node + 1,

        mid + 1,

        end,

        left,

        right,

        value

    )

    segment_tree[node] = (

        segment_tree[2 * node]

        + segment_tree[2 * node + 1]

    )


build(1, 0, n - 1)

print("Original Sum:")

print(segment_tree[1])

update_range(

    1,

    0,

    n - 1,

    0,

    3,

    5

)

print("\nUpdated Sum:")

print(segment_tree[1])