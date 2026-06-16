# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Bubble Sort
# Day         : 18
# Description : Sorting an array using Bubble Sort.
# ==========================================================

numbers = [50, 20, 40, 10, 30]

print("Original Array:", numbers)

n = len(numbers)

for i in range(n):

    for j in range(0, n - i - 1):

        if numbers[j] > numbers[j + 1]:

            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted Array:", numbers)