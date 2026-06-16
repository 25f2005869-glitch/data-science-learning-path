# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Segment Tree Update Operation
# Day         : 74
# Description : Updating values in Segment Tree and
#               maintaining correct range sums.
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


def update(

    node,

    start,

    end,

    index,

    value

):

    if start == end:

        arr[index] = value

        segment_tree[node] = value

        return

    mid = (start + end) // 2

    if index <= mid:

        update(

            2 * node,

            start,

            mid,

            index,

            value

        )

    else:

        update(

            2 * node + 1,

            mid + 1,

            end,

            index,

            value

        )

    segment_tree[node] = (

        segment_tree[2 * node]

        + segment_tree[2 * node + 1]

    )


build(1, 0, len(arr) - 1)

print("Original Root Sum:")

print(segment_tree[1])

update(

    1,

    0,

    len(arr) - 1,

    2,

    10

)

print("\nUpdated Root Sum:")

print(segment_tree[1])