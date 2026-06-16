# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Lists
# Day         : 07
# Description : Understanding list creation, access,
#               modification and traversal.
# ==========================================================

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Second Element:", numbers[1])

# Modifying an element
numbers[2] = 35

print("Modified List:", numbers)

# Adding an element
numbers.append(60)

print("After Append:", numbers)

# Removing an element
numbers.remove(20)

print("After Remove:", numbers)

# Length of list
print("Length:", len(numbers))

# Traversing list
print("List Elements:")

for item in numbers:
    print(item)