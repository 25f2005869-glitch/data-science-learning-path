# Day 34 – BST Deletion Operation

## Objective

The goal of this session is to understand how nodes are deleted from a Binary Search Tree (BST) while maintaining the BST property.

---

## Why is BST Deletion Important?

Deletion is the most complex BST operation because the tree structure must remain valid after removing a node.

BST Property:

```text
Left Subtree < Root < Right Subtree
```

This property must always be preserved.

---

## Cases in BST Deletion

There are three possible cases.

---

## Case 1: Deleting a Leaf Node

A leaf node has no children.

Example:

```text
      50
     /  \
   30    70
         /
       60
```

Delete:

```text
60
```

After Deletion:

```text
      50
     /  \
   30    70
```

Time Complexity:

```text
O(log n)
```

(Balanced BST)

---

## Case 2: Deleting a Node with One Child

Example:

```text
      50
     /  \
   30    70
         /
       60
```

Delete:

```text
70
```

After Deletion:

```text
      50
     /  \
   30    60
```

The child replaces the deleted node.

---

## Case 3: Deleting a Node with Two Children

Example:

```text
        50
       /  \
     30    70
          /  \
        60    80
```

Delete:

```text
70
```

Replace with Inorder Successor:

```text
80
```

Result:

```text
        50
       /  \
     30    80
          /
        60
```

---

## Inorder Successor

The Inorder Successor is the smallest value in the right subtree.

Example:

```text
        70
       /  \
      60   80
```

Successor of 70:

```text
80
```

---

## BST Deletion Algorithm

1. Find the node.
2. Check deletion case.
3. Remove node.
4. Reconnect tree.
5. Preserve BST property.

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

* Dynamic Databases
* Search Systems
* Index Management
* Ordered Data Storage

---

## Key Concepts Learned

* BST Deletion
* Leaf Node Deletion
* One Child Deletion
* Two Child Deletion
* Inorder Successor

---

## Summary

BST Deletion removes nodes while maintaining the BST property. It is one of the most important BST operations and a common interview topic.
