# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Tuples
# Day         : 09
# Description : Understanding tuple creation, indexing,
#               traversal and immutability.
# ==========================================================

# Creating a tuple
numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Second Element:", numbers[1])

# Length of tuple
print("Length:", len(numbers))

# Traversing tuple
print("Tuple Elements:")

for item in numbers:
    print(item)

# Tuple concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)

result = tuple1 + tuple2

print("Concatenated Tuple:", result)