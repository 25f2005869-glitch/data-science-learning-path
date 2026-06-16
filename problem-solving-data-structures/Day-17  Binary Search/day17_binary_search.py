# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Binary Search
# Day         : 17
# Description : Searching an element in a sorted array
#               using Binary Search.
# ==========================================================

numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter element to search: "))

low = 0
high = len(numbers) - 1

found = False

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:

        print("Element Found at Index", mid)

        found = True

        break

    elif target < numbers[mid]:

        high = mid - 1

    else:

        low = mid + 1

if not found:

    print("Element Not Found")