# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Insertion Sort
# Day         : 20
# Description : Sorting an array using Insertion Sort.
# ==========================================================

numbers = [50, 20, 40, 10, 30]

print("Original Array:", numbers)

for i in range(1, len(numbers)):

    key = numbers[i]

    j = i - 1

    while j >= 0 and numbers[j] > key:

        numbers[j + 1] = numbers[j]

        j -= 1

    numbers[j + 1] = key

print("Sorted Array:", numbers)