📘 Day 47 – Heap Sort
notes.md
Day 47 – Heap Sort
Objective

The goal of this session is to understand Heap Sort and how sorting can be performed using the Heap data structure.

What is Heap Sort?

Heap Sort is a comparison-based sorting algorithm that uses a Binary Heap.

It works by:

Building a Max Heap.
Repeatedly moving the largest element to the end.
Restoring the heap property.
Why Heap Sort?

Heap Sort provides:

Guaranteed O(n log n)

time complexity in all cases.

Unlike Quick Sort:

Worst Case = O(n²)

Heap Sort always remains:

O(n log n)
Example

Unsorted Array:

[4, 10, 3, 5, 1]
Step 1: Build Max Heap
       10
      /  \
     5    3
    / \
   4   1

Array Form:

[10, 5, 3, 4, 1]
Step 2: Move Largest Element

Swap:

10 ↔ 1

Array:

[1, 5, 3, 4, 10]

10 is now in its final sorted position.

Step 3: Heapify Remaining Elements

Restore Max Heap:

      5
     / \
    4   3
   /
  1

Array:

[5, 4, 3, 1, 10]
Continue Process

Repeat until heap size becomes 1.

Final Sorted Array:

[1, 3, 4, 5, 10]
Heapify

Heapify is the process of restoring heap properties after insertion or deletion.

For Max Heap:

Parent ≥ Children
Heap Sort Algorithm
Build Max Heap.
Swap root with last element.
Reduce heap size.
Heapify root.
Repeat until sorted.
Applications
Operating Systems
Priority Scheduling
Database Systems
Embedded Systems
Real-Time Processing
Time Complexity
Case	Complexity
Best	O(n log n)
Average	O(n log n)
Worst	O(n log n)
Space Complexity
O(1)

Heap Sort is an in-place sorting algorithm.

Comparison with Other Sorting Algorithms
Algorithm	Worst Case
Bubble Sort	O(n²)
Selection Sort	O(n²)
Insertion Sort	O(n²)
Merge Sort	O(n log n)
Heap Sort	O(n log n)
Key Concepts Learned
Heap Sort
Max Heap
Heapify
In-Place Sorting
O(n log n)
Summary

Heap Sort uses a Max Heap to repeatedly extract the largest element and place it in its correct position, producing a sorted array efficiently.