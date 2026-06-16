# Day 58 – Disjoint Set (Union-Find)

## Objective

The goal of this session is to understand the Disjoint Set (Union-Find) data structure and how it efficiently manages groups of connected elements.

---

## What is a Disjoint Set?

A Disjoint Set is a data structure that keeps track of elements divided into non-overlapping sets.

Each element belongs to exactly one set.

Example:

Set 1:

A B C

Set 2:

D E

These sets are independent.

---

## Why Do We Need It?

Disjoint Set helps answer questions like:

Are two elements in the same group?

Can two groups be merged?

This is heavily used in:

- Kruskal's Algorithm
- Network Connectivity
- Social Networks
- Connected Components
- Cycle Detection

---

## Core Operations

### Make Set

Create a separate set for each element.

Example:

A

B

C

Initially:

A → A

B → B

C → C

---

### Find

Find the representative (root) of a set.

Example:

A → A

B → A

C → A

Find(C)

Output:

A

---

### Union

Merge two sets into one set.

Example:

Before:

A     B

After Union(A,B):

A

|

B

---

## Tree Representation

Initially:

A

B

C

D

After Union(A,B):

    A
    |
    B

After Union(C,D):

    C
    |
    D

After Union(A,C):

        A
       / \
      B   C
           \
            D

---

## Path Compression

Optimization used during Find.

Without Compression:

D → C → A

Find(D)

travels through all nodes.

After Compression:

D → A

Future operations become faster.

---

## Union by Rank

Attach smaller tree under larger tree.

This keeps the tree shallow and improves performance.

---

## Algorithm

MakeSet(x)

Find(x)

Union(x, y)

---

## Applications

### Kruskal's Algorithm

Detect cycles while building MST.

### Social Networks

Check whether users belong to the same community.

### Network Connectivity

Determine connected computers.

### Image Processing

Connected region detection.

---

## Time Complexity

With Path Compression
and Union by Rank:

Find:

O(α(n))

Union:

O(α(n))

Where:

α(n) = Inverse Ackermann Function

Practically:

Almost O(1)

---

## Space Complexity

O(n)

---

## Key Concepts Learned

- Disjoint Set
- Union-Find
- Make Set
- Find
- Union
- Path Compression
- Union by Rank

---

## Summary

Disjoint Set (Union-Find) is an efficient data structure used to manage groups of connected elements. It is a key component of Kruskal's Algorithm and many graph-based applications.