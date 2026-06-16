# Day 30 – Binary Trees

## Objective

The goal of this session is to understand Binary Trees and their basic properties.

---

## What is a Binary Tree?

A Binary Tree is a tree data structure in which each node can have at most two children.

These children are called:

* Left Child
* Right Child

---

## Structure

```text
        A
       / \
      B   C
```

A is the root node.

B is the left child.

C is the right child.

---

## Why Binary Trees?

Binary Trees are widely used because they provide efficient searching, insertion, and deletion operations.

Applications include:

* File Systems
* Expression Trees
* Binary Search Trees
* Heaps
* Decision Trees

---

## Terminology

### Root Node

The topmost node.

```text
A
```

---

### Internal Node

A node having at least one child.

```text
A, B, C
```

---

### Leaf Node

A node with no children.

```text
D, E, F, G
```

---

### Subtree

Any tree formed from a node and its descendants.

Example:

```text
      B
     / \
    D   E
```

---

## Example Binary Tree

```text
         A
       /   \
      B     C
     / \   / \
    D   E F   G
```

---

## Types of Binary Trees

### Full Binary Tree

Every node has either 0 or 2 children.

### Complete Binary Tree

All levels are completely filled except possibly the last.

### Perfect Binary Tree

All internal nodes have 2 children and all leaf nodes are at the same level.

### Balanced Binary Tree

Height difference between left and right subtrees remains small.

---

## Binary Tree Traversals

### Preorder

```text
Root → Left → Right
```

Example:

```text
A B D E C F G
```

---

### Inorder

```text
Left → Root → Right
```

Example:

```text
D B E A F C G
```

---

### Postorder

```text
Left → Right → Root
```

Example:

```text
D E B F G C A
```

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Traversal | O(n)       |
| Search    | O(n)       |
| Insert    | O(n)       |
| Delete    | O(n)       |

---

## Key Concepts Learned

* Binary Tree
* Root Node
* Internal Node
* Leaf Node
* Subtree
* Preorder Traversal
* Inorder Traversal
* Postorder Traversal

---

## Summary

A Binary Tree is a hierarchical data structure where each node has at most two children. It serves as the foundation for Binary Search Trees, Heaps, AVL Trees, and many advanced data structures.
