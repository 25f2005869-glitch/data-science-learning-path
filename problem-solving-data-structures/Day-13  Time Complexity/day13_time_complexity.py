# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Time Complexity
# Day         : 13
# Description : Examples of O(1), O(n) and O(n²).
# ==========================================================

numbers = [10, 20, 30, 40, 50]

# O(1)
print("First Element:", numbers[0])

# O(n)
print("\nLinear Traversal:")

for item in numbers:
    print(item)

# O(n²)
print("\nNested Loop:")

for i in range(3):
    for j in range(3):
        print(i, j)