# Day 73 – Range Sum Query Using Segment Tree

## Objective

The goal of this session is to understand how Segment Trees are used to efficiently answer Range Sum Queries.

---

## What is a Range Sum Query?

A Range Sum Query asks:

Find the sum of elements between two indices.

Example:

Array:

1 3 5 7 9 11

Query:

Sum from index 1 to 4

Calculation:

3 + 5 + 7 + 9

Answer:

24

---

## Problem with Normal Arrays

For every query:

Traverse all elements in the range.

Example:

Query:

[1,4]

Time Complexity:

O(n)

---

If thousands of queries are performed:

Performance becomes slow.

---

## Solution

Use a Segment Tree.

Segment Tree answers range queries efficiently.

Query Time:

O(log n)

---

## Example Array

Array:

1 3 5 7

Indexes:

0 1 2 3

---

## Segment Tree

          16
        /    \
       4      12
      / \    /  \
     1   3  5    7

Root:

16

represents:

1 + 3 + 5 + 7

---

## Range Query Example

Find Sum:

[1,3]

Elements:

3 5 7

Answer:

15

---

## Query Process

Start from Root.

Check segment overlap.

Three cases exist:

---

### Complete Overlap

Current segment lies completely inside query range.

Return stored value.

---

### No Overlap

Current segment lies outside query range.

Return 0.

---

### Partial Overlap

Split query into left and right children.

Combine results.

---

## Example

Array:

1 3 5 7

Query:

[1,3]

Result:

3 + 5 + 7

=

15

---

## Query Algorithm

1. Start at root.
2. Check overlap.
3. Return value for complete overlap.
4. Return 0 for no overlap.
5. Recurse for partial overlap.
6. Combine answers.

---

## Applications

### Competitive Programming

Range Sum Queries

---

### Financial Systems

Transaction Analysis

---

### Gaming

Score Aggregation

---

### Analytics

Large Dataset Queries

---

### Databases

Fast Range Computation

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

O(4n)

approximately

O(n)

---

## Comparison

| Operation | Array | Segment Tree |
|------------|--------|-------------|
| Range Sum Query | O(n) | O(log n) |
| Update | O(1) | O(log n) |

---

## Key Concepts Learned

- Segment Tree
- Range Sum Query
- Complete Overlap
- Partial Overlap
- No Overlap

---

## Summary

Segment Trees answer Range Sum Queries efficiently by dividing the array into segments and storing precomputed information. This reduces query time from O(n) to O(log n).