# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Space Complexity
# Day         : 14
# Description : Understanding O(1), O(n) and O(n²)
#               space complexity.
# ==========================================================

# O(1) Space
a = 10
b = 20

sum_result = a + b

print("Sum =", sum_result)

# O(n) Space
numbers = []

for i in range(5):
    numbers.append(i)

print("List:", numbers)

# O(n²) Space
matrix = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(0)

    matrix.append(row)

print("Matrix:")

for row in matrix:
    print(row)