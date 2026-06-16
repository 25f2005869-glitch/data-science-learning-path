# Day 35 – Tree Traversals

## Objective

The goal of this session is to understand the three fundamental tree traversal techniques used to visit every node in a binary tree.

---

## What is Tree Traversal?

Tree Traversal is the process of visiting every node in a tree exactly once in a specific order.

Traversal is important for:

* Searching
* Printing
* Copying Trees
* Expression Evaluation
* Tree Algorithms

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

## 1. Preorder Traversal

Traversal Order:

```text
Root → Left → Right
```

Steps:

```text
A → B → D → E → C → F → G
```

Output:

```text
A B D E C F G
```

---

## 2. Inorder Traversal

Traversal Order:

```text
Left → Root → Right
```

Steps:

```text
D → B → E → A → F → C → G
```

Output:

```text
D B E A F C G
```

For BSTs, Inorder Traversal always produces sorted output.

---

## 3. Postorder Traversal

Traversal Order:

```text
Left → Right → Root
```

Steps:

```text
D → E → B → F → G → C → A
```

Output:

```text
D E B F G C A
```

---

## Comparison

| Traversal | Order               |
| --------- | ------------------- |
| Preorder  | Root → Left → Right |
| Inorder   | Left → Root → Right |
| Postorder | Left → Right → Root |

---

## Applications

### Preorder

* Copying Trees
* Prefix Expressions

### Inorder

* BST Sorted Output

### Postorder

* Deleting Trees
* Postfix Expressions

---

## Time Complexity

For all traversals:

```text
O(n)
```

Every node is visited exactly once.

---

## Key Concepts Learned

* Tree Traversal
* Preorder Traversal
* Inorder Traversal
* Postorder Traversal
* Recursive Traversal

---

## Summary

Tree Traversals provide different ways to visit nodes in a tree and are among the most important concepts in Tree Data Structures.
