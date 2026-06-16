# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Range Sum Query Using Segment Tree
# Day         : 73
# Description : Efficient range sum queries using
#               Segment Tree.
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


def range_sum(

    node,

    start,

    end,

    left,

    right

):

    if right < start or end < left:

        return 0

    if left <= start and end <= right:

        return segment_tree[node]

    mid = (start + end) // 2

    left_sum = range_sum(

        2 * node,

        start,

        mid,

        left,

        right

    )

    right_sum = range_sum(

        2 * node + 1,

        mid + 1,

        end,

        left,

        right

    )

    return left_sum + right_sum


build(1, 0, len(arr) - 1)

result = range_sum(

    1,

    0,

    len(arr) - 1,

    1,

    3

)

print("Range Sum [1,3]:")

print(result)