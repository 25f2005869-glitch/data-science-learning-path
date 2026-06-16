# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Selection Sort
# Day         : 19
# Description : Sorting an array using Selection Sort.
# ==========================================================

numbers = [50, 20, 40, 10, 30]

print("Original Array:", numbers)

n = len(numbers)

for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):

        if numbers[j] < numbers[min_index]:

            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted Array:", numbers)