# Day 19 – Selection Sort

## Objective

The goal of this session is to understand the Selection Sort algorithm and how it sorts elements by repeatedly selecting the smallest element.

---

## What is Selection Sort?

Selection Sort is a sorting algorithm that repeatedly finds the smallest element from the unsorted portion of the array and places it at its correct position.

---

## Example

Unsorted Array:

```text
[50, 20, 40, 10, 30]
```

### Pass 1

Smallest element = 10

Swap 50 and 10

```text
[10, 20, 40, 50, 30]
```

### Pass 2

Smallest element = 20

Already in correct position.

```text
[10, 20, 40, 50, 30]
```

### Pass 3

Smallest element = 30

Swap 40 and 30

```text
[10, 20, 30, 50, 40]
```

### Pass 4

Smallest element = 40

Swap 50 and 40

```text
[10, 20, 30, 40, 50]
```

Array Sorted ✅

---

## Algorithm

1. Find the smallest element.
2. Swap it with the first unsorted position.
3. Move the boundary of the sorted part by one.
4. Repeat until the array is sorted.

---

## Pseudocode

```text
FOR i = 0 TO n-2

    min_index = i

    FOR j = i+1 TO n-1

        IF arr[j] < arr[min_index]

            min_index = j

    SWAP arr[i] and arr[min_index]
```

---

## Time Complexity

### Best Case

```text
O(n²)
```

### Average Case

```text
O(n²)
```

### Worst Case

```text
O(n²)
```

Unlike Bubble Sort, Selection Sort performs the same number of comparisons in all cases.

---

## Space Complexity

```text
O(1)
```

Selection Sort is an in-place sorting algorithm.

---

## Advantages

* Easy to understand
* Requires very little extra memory
* Fewer swaps compared to Bubble Sort

---

## Disadvantages

* Slow for large datasets
* Not suitable for modern applications

---

## Bubble Sort vs Selection Sort

| Feature          | Bubble Sort       | Selection Sort |
| ---------------- | ----------------- | -------------- |
| Method           | Repeated Swapping | Select Minimum |
| Time Complexity  | O(n²)             | O(n²)          |
| Swaps            | More              | Fewer          |
| Space Complexity | O(1)              | O(1)           |

---

## Key Concepts Learned

* Selection Sort
* Minimum Element Selection
* Swapping
* In-Place Sorting
* O(n²) Sorting

---

## Summary

Selection Sort works by repeatedly selecting the smallest element and placing it in its correct position. It is simple to implement and introduces the concept of selection-based sorting.
