# Day 16 – Linear Search

## Objective

The goal of this session is to understand how to search for an element in an array using Linear Search.

---

## What is Searching?

Searching is the process of finding whether a particular element exists in a collection of data.

---

## What is Linear Search?

Linear Search checks each element one by one until the target element is found or the array ends.

It is the simplest searching technique.

---

## Example

Array:

```text
[10, 20, 30, 40, 50]
```

Target:

```text
40
```

Search Process:

```text
10 ✗
20 ✗
30 ✗
40 ✓
```

Element found at index 3.

---

## Algorithm

1. Start from the first element.
2. Compare each element with the target.
3. If a match is found, return the index.
4. If the end of the array is reached, return "Not Found".

---

## Pseudocode

```text
START

FOR each element in array

    IF element == target

        PRINT Found

        STOP

PRINT Not Found

END
```

---

## Time Complexity

### Best Case

Element found at first position.

```text
O(1)
```

### Worst Case

Element found at last position or not present.

```text
O(n)
```

### Average Case

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

No extra memory is required.

---

## Advantages

* Easy to implement
* Works on unsorted data
* No preprocessing required

---

## Disadvantages

* Slow for large datasets
* Checks elements one by one

---

## Key Concepts Learned

* Searching
* Linear Search
* Best Case
* Worst Case
* Time Complexity O(n)
* Space Complexity O(1)

---

## Summary

Linear Search is the simplest searching algorithm and serves as the foundation for understanding more advanced searching techniques.
