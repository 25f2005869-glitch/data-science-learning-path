# Day 29 – Trees

## Objective

The goal of this session is to understand the Tree data structure and its basic terminology.

---

## What is a Tree?

A Tree is a hierarchical data structure consisting of nodes connected by edges.

Unlike arrays, stacks, and queues, trees organize data in a parent-child relationship.

---

## Real Life Example

```text
Family Tree

      Grandparent
       /      \
   Parent1   Parent2
     /  \
 Child1 Child2
```

---

## Basic Terminology

### Root Node

The topmost node of a tree.

```text
      A
```

A is the Root Node.

---

### Parent Node

A node that has one or more children.

```text
      A
     / \
    B   C
```

A is the parent of B and C.

---

### Child Node

A node connected below another node.

```text
B and C
```

are children of A.

---

### Leaf Node

A node with no children.

```text
      A
     / \
    B   C
       / \
      D   E
```

Leaf Nodes:

```text
B, D, E
```

---

### Edge

A connection between two nodes.

```text
A → B
```

is an edge.

---

### Level

Distance from the root.

```text
Level 0 : A
Level 1 : B, C
Level 2 : D, E
```

---

### Height

The number of edges on the longest path from root to a leaf.

---

## Example Tree

```text
         A
       /   \
      B     C
     / \   / \
    D   E F   G
```

Root:

```text
A
```

Leaf Nodes:

```text
D, E, F, G
```

---

## Why Trees?

Trees are used when data has a hierarchical structure.

Examples:

* File Systems
* Organization Charts
* XML/HTML Documents
* Databases
* Decision Trees

---

## Time Complexity

For balanced trees:

| Operation | Complexity |
| --------- | ---------- |
| Search    | O(log n)   |
| Insert    | O(log n)   |
| Delete    | O(log n)   |

---

## Key Concepts Learned

* Tree
* Node
* Root
* Parent
* Child
* Leaf
* Edge
* Level
* Height

---

## Summary

Trees are hierarchical data structures that provide efficient organization and retrieval of data and form the foundation of many advanced data structures.
