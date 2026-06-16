# Day 31 – Binary Search Trees (BST)

## Objective

The goal of this session is to understand Binary Search Trees (BST) and how they improve searching efficiency compared to ordinary binary trees.

---

## What is a Binary Search Tree?

A Binary Search Tree (BST) is a special type of Binary Tree that follows the BST Property:

```text id="bst01"
Left Subtree  <  Root  <  Right Subtree
```

For every node:

* All values in the left subtree are smaller.
* All values in the right subtree are larger.

---

## Example

```text id="bst02"
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

Here:

```text id="bst03"
20 < 30 < 40 < 50 < 60 < 70 < 80
```

BST Property is satisfied.

---

## Why BST?

BST provides efficient:

* Searching
* Insertion
* Deletion

compared to linear structures.

---

## Searching in BST

To search for 60:

```text id="bst04"
Start at 50

60 > 50

Move Right

70

60 < 70

Move Left

60 Found
```

---

## Insertion in BST

Insert 65:

```text id="bst05"
        50
       /  \
     30    70
          / \
         60 80
           \
            65
```

---

## BST Traversal

### Inorder Traversal

```text id="bst06"
Left → Root → Right
```

Output:

```text id="bst07"
20 30 40 50 60 70 80
```

Inorder traversal of a BST always produces sorted output.

---

## Time Complexity

For a Balanced BST:

| Operation | Complexity |
| --------- | ---------- |
| Search    | O(log n)   |
| Insert    | O(log n)   |
| Delete    | O(log n)   |

Worst Case (Skewed Tree):

```text id="bst08"
O(n)
```

---

## Binary Tree vs BST

| Feature       | Binary Tree | BST           |
| ------------- | ----------- | ------------- |
| Ordering Rule | No          | Yes           |
| Search        | O(n)        | O(log n)      |
| Sorted Output | No          | Yes (Inorder) |

---

## Applications

* Database Indexing
* Search Engines
* Dictionaries
* File Systems
* Symbol Tables

---

## Key Concepts Learned

* Binary Search Tree
* BST Property
* Search
* Insert
* Inorder Traversal
* O(log n)

---

## Summary

A Binary Search Tree organizes data in sorted order and provides efficient searching, insertion, and deletion operations.
