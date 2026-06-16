# Day 20 – Insertion Sort

## Objective

The goal of this session is to understand the Insertion Sort algorithm and how elements are inserted into their correct positions.

---

## What is Insertion Sort?

Insertion Sort builds the sorted array one element at a time.

It works similarly to arranging playing cards in your hand.

Each new element is inserted into its correct position among the already sorted elements.

---

## Example

Unsorted Array:

```text id="is01"
[50, 20, 40, 10, 30]
```

### Pass 1

Insert 20 before 50

```text id="is02"
[20, 50, 40, 10, 30]
```

### Pass 2

Insert 40 between 20 and 50

```text id="is03"
[20, 40, 50, 10, 30]
```

### Pass 3

Insert 10 at beginning

```text id="is04"
[10, 20, 40, 50, 30]
```

### Pass 4

Insert 30 between 20 and 40

```text id="is05"
[10, 20, 30, 40, 50]
```

Array Sorted ✅

---

## Algorithm

1. Start from the second element.
2. Compare it with previous elements.
3. Shift larger elements to the right.
4. Insert the current element in its correct position.
5. Repeat until the array is sorted.

---

## Pseudocode

```text id="is06"
FOR i = 1 TO n-1

    key = arr[i]

    j = i - 1

    WHILE j >= 0 AND arr[j] > key

        arr[j + 1] = arr[j]

        j = j - 1

    arr[j + 1] = key
```

---

## Time Complexity

### Best Case (Already Sorted)

```text id="is07"
O(n)
```

### Average Case

```text id="is08"
O(n²)
```

### Worst Case (Reverse Sorted)

```text id="is09"
O(n²)
```

---

## Space Complexity

```text id="is10"
O(1)
```

Insertion Sort is an in-place sorting algorithm.

---

## Advantages

* Easy to implement
* Efficient for small datasets
* Works well for nearly sorted arrays
* Stable sorting algorithm

---

## Disadvantages

* Slow for large datasets
* Not suitable for very large inputs

---

## Comparison of Basic Sorting Algorithms

| Algorithm      | Best Case | Average Case | Worst Case |
| -------------- | --------- | ------------ | ---------- |
| Bubble Sort    | O(n)      | O(n²)        | O(n²)      |
| Selection Sort | O(n²)     | O(n²)        | O(n²)      |
| Insertion Sort | O(n)      | O(n²)        | O(n²)      |

---

## Key Concepts Learned

* Insertion Sort
* Shifting Elements
* Sorted and Unsorted Portions
* Stable Sorting
* O(n²) Sorting

---

## Summary

Insertion Sort places each element into its correct position within the sorted portion of the array. It is simple, intuitive, and performs well on small or nearly sorted datasets.
