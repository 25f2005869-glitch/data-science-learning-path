# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Linear Search
# Day         : 16
# Description : Searching an element in an array using
#               Linear Search.
# ==========================================================

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter element to search: "))

found = False

for index in range(len(numbers)):

    if numbers[index] == target:

        print("Element Found at Index", index)

        found = True

        break

if not found:

    print("Element Not Found")