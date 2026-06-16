# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Sets
# Day         : 11
# Description : Understanding set creation, operations,
#               and unique element storage.
# ==========================================================

# Creating a set
numbers = {10, 20, 20, 30, 30, 40}

print("Set:", numbers)

# Adding an element
numbers.add(50)

print("After Add:", numbers)

# Removing an element
numbers.remove(20)

print("After Remove:", numbers)

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

# Traversing a set
print("Set Elements:")

for item in numbers:
    print(item)