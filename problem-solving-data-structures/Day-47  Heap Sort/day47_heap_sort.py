# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Heap Sort
# Day         : 47
# Description : Sorting an array using Heap Sort.
# ==========================================================

def heapify(arr, n, i):

    largest = i

    left = 2 * i + 1

    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:

        largest = left

    if right < n and arr[right] > arr[largest]:

        largest = right

    if largest != i:

        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):

        heapify(arr, n, i)

    # Extract Elements
    for i in range(n - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)


numbers = [4, 10, 3, 5, 1]

print("Original Array:")

print(numbers)

heap_sort(numbers)

print("\nSorted Array:")

print(numbers)