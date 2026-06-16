# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Arrays
# Day         : 15
# Description : Understanding array operations using Python
#               lists.
# ==========================================================

# Creating an array
numbers = [10, 20, 30, 40, 50]

print("Array:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Third Element:", numbers[2])

# Updating an element
numbers[1] = 25

print("Updated Array:", numbers)

# Traversing the array
print("Array Elements:")

for item in numbers:
    print(item)

# Searching for an element
target = 40

found = False

for item in numbers:
    if item == target:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")