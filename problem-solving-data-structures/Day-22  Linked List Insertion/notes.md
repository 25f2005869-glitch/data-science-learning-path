# Day 22 – Linked List Insertion

## Objective

The goal of this session is to understand how new nodes are inserted into a linked list.

---

## What is Insertion?

Insertion means adding a new node to a linked list.

Common insertion operations:

1. Insertion at Beginning
2. Insertion at End
3. Insertion at a Specific Position

---

## Initial Linked List

```text
10 → 20 → 30 → NULL
```

---

## Insertion at Beginning

Insert 5 before the head node.

```text
5 → 10 → 20 → 30 → NULL
```

Steps:

1. Create a new node.
2. Point new node to current head.
3. Update head.

Time Complexity:

```text
O(1)
```

---

## Insertion at End

Insert 40 at the end.

```text
10 → 20 → 30 → 40 → NULL
```

Steps:

1. Traverse to last node.
2. Connect last node to new node.

Time Complexity:

```text
O(n)
```

---

## Insertion After a Node

Insert 25 after 20.

```text
10 → 20 → 25 → 30 → NULL
```

Steps:

1. Create new node.
2. Point new node to next node.
3. Update current node link.

Time Complexity:

```text
O(1)
```

(if node reference is available)

---

## Visualization

Before:

```text
10 → 20 → 30 → NULL
```

After inserting 25:

```text
10 → 20 → 25 → 30 → NULL
```

---

## Time Complexity

| Operation           | Complexity |
| ------------------- | ---------- |
| Insert at Beginning | O(1)       |
| Insert at End       | O(n)       |
| Insert After Node   | O(1)       |

---

## Key Concepts Learned

* Linked List Insertion
* Head Pointer
* Node Creation
* Insert at Beginning
* Insert at End
* Insert After Node

---

## Summary

Insertion is one of the biggest advantages of linked lists because nodes can be added without shifting existing elements.
