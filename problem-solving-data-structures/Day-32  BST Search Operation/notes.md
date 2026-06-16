# Day 32 – BST Search Operation

## Objective

The goal of this session is to understand how searching is performed efficiently in a Binary Search Tree (BST).

---

## Searching in BST

A Binary Search Tree follows:

```text
Left Subtree < Root < Right Subtree
```

This property allows us to eliminate half of the tree at every step.

---

## Example BST

```text
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

---

## Search Example

Search for:

```text
60
```

### Step 1

Current Node:

```text
50
```

Compare:

```text
60 > 50
```

Move Right.

---

### Step 2

Current Node:

```text
70
```

Compare:

```text
60 < 70
```

Move Left.

---

### Step 3

Current Node:

```text
60
```

Match Found ✅

---

## Search Algorithm

1. Start from Root.
2. Compare target with current node.
3. If equal, return Found.
4. If smaller, move Left.
5. If larger, move Right.
6. Repeat until node becomes NULL.

---

## Pseudocode

```text
SEARCH(root, key)

IF root IS NULL

    RETURN False

IF key == root.data

    RETURN True

IF key < root.data

    SEARCH(root.left, key)

ELSE

    SEARCH(root.right, key)
```

---

## Time Complexity

### Balanced BST

```text
O(log n)
```

---

### Skewed BST

```text
O(n)
```

Example:

```text
10
 \
  20
   \
    30
     \
      40
```

---

## Applications

* Fast Searching
* Database Indexing
* Symbol Tables
* File Systems

---

## Key Concepts Learned

* BST Search
* Recursive Search
* Tree Traversal
* O(log n)
* Balanced BST

---

## Summary

BST Search uses the BST property to efficiently locate elements by reducing the search space at every step.
