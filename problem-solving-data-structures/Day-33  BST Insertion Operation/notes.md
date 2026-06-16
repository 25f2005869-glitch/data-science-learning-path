# Day 33 – BST Insertion Operation

## Objective

The goal of this session is to understand how new nodes are inserted into a Binary Search Tree (BST) while maintaining the BST property.

---

## BST Property

A Binary Search Tree follows:

```text
Left Subtree < Root < Right Subtree
```

Every insertion must preserve this rule.

---

## Example BST

```text
        50
       /  \
     30    70
    / \    /
   20 40  60
```

---

## Insert 80

### Step 1

Start at Root:

```text
50
```

Compare:

```text
80 > 50
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
80 > 70
```

Move Right.

---

### Step 3

Right Child is NULL.

Insert Node.

```text
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

Insertion Complete ✅

---

## BST Insertion Algorithm

1. Start from Root.
2. Compare value with current node.
3. If value is smaller, move Left.
4. If value is larger, move Right.
5. Repeat until NULL position is found.
6. Insert the new node.

---

## Pseudocode

```text
INSERT(root, value)

IF root IS NULL

    RETURN New Node

IF value < root.data

    root.left = INSERT(root.left, value)

ELSE

    root.right = INSERT(root.right, value)

RETURN root
```

---

## Inorder Verification

After insertion:

```text
20 30 40 50 60 70 80
```

The output remains sorted.

---

## Time Complexity

### Balanced BST

```text
O(log n)
```

### Skewed BST

```text
O(n)
```

---

## Applications

* Dynamic Data Storage
* Database Indexing
* Search Systems
* Ordered Data Processing

---

## Key Concepts Learned

* BST Insertion
* Recursive Insertion
* BST Property
* Ordered Data
* O(log n)

---

## Summary

BST Insertion places a new node at the correct position while preserving the Binary Search Tree property.
