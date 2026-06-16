# Day 74 – Segment Tree Update Operation

## Objective

The goal of this session is to understand how updates are performed efficiently in a Segment Tree.

---

## Why Updates Matter?

Consider an array:

1 3 5 7

Suppose:

Index 2 changes from:

5

to

10

Updated Array:

1 3 10 7

Now all future range queries must use the updated value.

---

## Problem with Normal Arrays

Updating an element:

O(1)

But recalculating range sums repeatedly can be expensive.

For large datasets:

Performance decreases.

---

## Segment Tree Solution

Segment Tree updates only the affected nodes.

Instead of rebuilding the entire tree:

Update only one path from leaf to root.

---

## Example Array

Array:

1 3 5 7

Segment Tree:

          16
        /    \
       4      12
      / \    /  \
     1   3  5    7

---

## Update Operation

Change:

arr[2]

from

5

to

10

---

## Step 1

Locate Leaf Node

          16
        /    \
       4      12
      / \    /  \
     1   3  5    7
             ↑

Update:

5 → 10

---

## Step 2

Update Parent

Old:

12

=

5 + 7

---

New:

17

=

10 + 7

---

## Step 3

Update Root

Old:

16

=

4 + 12

---

New:

21

=

4 + 17

---

## Updated Tree

          21
        /    \
       4      17
      / \    /  \
     1   3 10    7

---

## Key Idea

Only nodes on the update path are modified.

Other nodes remain unchanged.

---

## Update Algorithm

1. Locate target index.
2. Update leaf node.
3. Move upward.
4. Recalculate parent nodes.
5. Continue until root.

---

## Applications

### Live Score Systems

Real-time updates.

---

### Financial Systems

Stock value updates.

---

### Gaming Systems

Score modifications.

---

### Database Analytics

Dynamic range calculations.

---

### Competitive Programming

Range updates and queries.

---

## Time Complexity

### Build Tree

O(n)

---

### Range Query

O(log n)

---

### Update

O(log n)

---

## Space Complexity

O(n)

---

## Comparison

| Operation | Array | Segment Tree |
|------------|--------|-------------|
| Update | O(1) | O(log n) |
| Range Query | O(n) | O(log n) |

---

## Example

Original Array:

1 3 5 7

Update:

Index 2 → 10

Updated Array:

1 3 10 7

Range Sum [1,3]:

3 + 10 + 7

=

20

---

## Key Concepts Learned

- Segment Tree
- Point Update
- Range Query
- Tree Recalculation
- Efficient Updates

---

## Summary

Segment Tree Update Operation modifies only the affected nodes from leaf to root, allowing updates and queries to be performed efficiently in logarithmic time.