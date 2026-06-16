# Day 18 – Bubble Sort

## Objective

The goal of this session is to understand the Bubble Sort algorithm and how elements are arranged in sorted order.

---

## What is Sorting?

Sorting is the process of arranging data in a specific order.

Common orders:

* Ascending Order
* Descending Order

Example:

Unsorted Array:

```text
[50, 20, 40, 10, 30]
```

Sorted Array:

```text
[10, 20, 30, 40, 50]
```

---

## What is Bubble Sort?

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

After each pass, the largest element moves to its correct position.

---

## Example

Array:

```text
[5, 3, 8, 2]
```

Pass 1:

```text
5 3 → Swap

[3, 5, 8, 2]

8 2 → Swap

[3, 5, 2, 8]
```

Largest element (8) reaches its correct position.

---

## Algorithm

1. Compare adjacent elements.
2. Swap if left element is greater than right element.
3. Continue until the end of the array.
4. Repeat for remaining elements.
5. Stop when the array becomes sorted.

---

## Pseudocode

```text
FOR i = 0 TO n-1

    FOR j = 0 TO n-i-2

        IF arr[j] > arr[j+1]

            SWAP arr[j] and arr[j+1]
```

---

## Time Complexity

### Best Case

Already sorted array:

```text
O(n)
```

(Optimized Bubble Sort)

### Average Case

```text
O(n²)
```

### Worst Case

```text
O(n²)
```

---

## Space Complexity

```text
O(1)
```

Bubble Sort is an in-place sorting algorithm.

---

## Advantages

* Easy to understand
* Easy to implement

---

## Disadvantages

* Slow for large datasets
* Not suitable for efficient sorting

---

## Key Concepts Learned

* Sorting
* Bubble Sort
* Swapping
* Passes
* O(n²)

---

## Summary

Bubble Sort is one of the simplest sorting algorithms and helps in understanding the basic idea of sorting through repeated comparisons and swaps.
