# Day 17 – Binary Search

## Objective

The goal of this session is to understand Binary Search and how it improves searching efficiency in sorted arrays.

---

## What is Binary Search?

Binary Search is a searching algorithm that repeatedly divides a sorted array into two halves until the target element is found.

Unlike Linear Search, it does not check every element one by one.

---

## Requirement

Binary Search works only on a **sorted array**.

Example:

```text id="bs01"
[10, 20, 30, 40, 50, 60, 70]
```

---

## Idea Behind Binary Search

Instead of checking every element:

1. Find the middle element.
2. Compare it with the target.
3. If target is smaller, search the left half.
4. If target is larger, search the right half.
5. Repeat until found.

---

## Example

Array:

```text id="bs02"
[10, 20, 30, 40, 50, 60, 70]
```

Target:

```text id="bs03"
60
```

Process:

```text id="bs04"
Middle = 40

60 > 40

Search Right Half

Middle = 60

Found
```

---

## Algorithm

1. Set low = 0
2. Set high = n - 1
3. Find middle element
4. Compare middle with target
5. Adjust low or high
6. Repeat until found or search space becomes empty

---

## Pseudocode

```text id="bs05"
LOW = 0
HIGH = n - 1

WHILE LOW <= HIGH

    MID = (LOW + HIGH) // 2

    IF ARRAY[MID] == TARGET
        FOUND

    ELSE IF TARGET < ARRAY[MID]
        HIGH = MID - 1

    ELSE
        LOW = MID + 1
```

---

## Time Complexity

### Best Case

Target found at middle.

```text id="bs06"
O(1)
```

### Worst Case

```text id="bs07"
O(log n)
```

### Average Case

```text id="bs08"
O(log n)
```

---

## Space Complexity

Iterative Binary Search:

```text id="bs09"
O(1)
```

---

## Advantages

* Very fast
* Efficient for large datasets
* Better than Linear Search

---

## Limitations

* Requires sorted data
* More complex than Linear Search

---

## Key Concepts Learned

* Binary Search
* Sorted Array
* Low, High, Mid
* Divide and Conquer
* O(log n)

---

## Summary

Binary Search reduces the search space by half in each step, making it one of the most efficient searching algorithms.
