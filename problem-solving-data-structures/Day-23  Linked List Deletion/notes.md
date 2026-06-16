# Day 23 – Linked List Deletion

## Objective

The goal of this session is to understand how nodes are removed from a linked list.

---

## What is Deletion?

Deletion means removing a node from a linked list.

Common deletion operations:

1. Delete from Beginning
2. Delete from End
3. Delete a Specific Node

---

## Initial Linked List

```text id="ll23a"
10 → 20 → 30 → 40 → NULL
```

---

## Deletion from Beginning

Remove the first node.

Before:

```text id="ll23b"
10 → 20 → 30 → 40 → NULL
```

After:

```text id="ll23c"
20 → 30 → 40 → NULL
```

Steps:

1. Move head to the second node.
2. First node is removed.

Time Complexity:

```text id="ll23d"
O(1)
```

---

## Deletion from End

Remove the last node.

Before:

```text id="ll23e"
10 → 20 → 30 → 40 → NULL
```

After:

```text id="ll23f"
10 → 20 → 30 → NULL
```

Steps:

1. Traverse to second last node.
2. Set its next pointer to NULL.

Time Complexity:

```text id="ll23g"
O(n)
```

---

## Deletion of a Specific Node

Remove node containing 30.

Before:

```text id="ll23h"
10 → 20 → 30 → 40 → NULL
```

After:

```text id="ll23i"
10 → 20 → 40 → NULL
```

Steps:

1. Find previous node.
2. Change links.
3. Skip the target node.

Time Complexity:

```text id="ll23j"
O(n)
```

---

## Visualization

Before:

```text id="ll23k"
10 → 20 → 30 → 40 → NULL
```

Delete 30:

```text id="ll23l"
10 → 20 ─────→ 40 → NULL
```

---

## Time Complexity

| Operation           | Complexity |
| ------------------- | ---------- |
| Delete at Beginning | O(1)       |
| Delete at End       | O(n)       |
| Delete by Value     | O(n)       |

---

## Key Concepts Learned

* Linked List Deletion
* Head Pointer Update
* Deleting Last Node
* Deleting Specific Node
* Link Adjustment

---

## Summary

Deletion in linked lists is efficient because nodes can be removed without shifting elements, unlike arrays.
