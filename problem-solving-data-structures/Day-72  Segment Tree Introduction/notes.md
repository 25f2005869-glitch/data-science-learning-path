# Day 72 – Segment Tree Introduction

## Objective

The goal of this session is to understand the Segment Tree data structure and how it efficiently handles range queries and updates.

---

## What is a Segment Tree?

A Segment Tree is a tree-based data structure used for:

- Range Queries
- Range Sum Queries
- Range Minimum Queries
- Range Maximum Queries
- Efficient Updates

---

## Why Do We Need Segment Trees?

Consider an array:

1 3 5 7 9 11

Query:

Find sum from index 1 to 4

Traditional Approach:

3 + 5 + 7 + 9

Time Complexity:

O(n)

---

If thousands of queries arrive:

Performance becomes slow.

Segment Tree reduces query time to:

O(log n)

---

## Basic Idea

Divide the array into segments.

Store useful information for every segment.

Example:

Array:

1 3 5 7

Tree:

          16
        /    \
       4      12
      / \    /  \
     1   3  5    7

Root stores:

Total Sum

---

## Segment Representation

Array:

1 3 5 7 9 11

Indexes:

0 1 2 3 4 5

Root Represents:

[0,5]

Children:

[0,2]

[3,5]

Further divided until:

Single Elements

---

## Building the Tree

Step 1:

Create leaf nodes.

Step 2:

Combine child values.

Step 3:

Store result in parent.

Continue until root is built.

---

## Range Sum Query

Example:

Find Sum:

[1,4]

Array:

1 3 5 7 9 11

Result:

3 + 5 + 7 + 9

=

24

Segment Tree avoids visiting every element.

---

## Range Update

Example:

Change:

Index 2

From:

5

To:

10

Update only affected nodes.

Time Complexity:

O(log n)

---

## Applications

### Competitive Programming

Fast query processing.

---

### Database Systems

Range aggregation.

---

### Financial Systems

Stock price analysis.

---

### Gaming

Score calculations.

---

### Analytics

Large dataset processing.

---

## Operations

| Operation | Complexity |
|------------|------------|
| Build Tree | O(n) |
| Range Query | O(log n) |
| Update | O(log n) |

---

## Comparison

| Structure | Query | Update |
|------------|--------|--------|
| Array | O(n) | O(1) |
| Segment Tree | O(log n) | O(log n) |

---

## Tree Example

Array:

1 3 5 7

Segment Tree:

          16
        /    \
       4      12
      / \    /  \
     1   3  5    7

---

## Applications in Interviews

Frequently asked topics:

- Range Sum Query
- Range Minimum Query
- Lazy Propagation
- Dynamic Range Updates

---

## Key Concepts Learned

- Segment Tree
- Range Query
- Range Sum
- Tree Construction
- Efficient Updates

---

## Summary

A Segment Tree is a powerful data structure that allows efficient range queries and updates in logarithmic time. It is widely used in competitive programming, databases, analytics, and advanced algorithmic problems.