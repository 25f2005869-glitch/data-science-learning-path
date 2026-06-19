# ======================================
# Day 044: NumPy Array Operations
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Performing Mathematical Operations
# on NumPy Arrays
# ======================================

print("=" * 50)
print("DAY 044 - NUMPY ARRAY OPERATIONS")
print("=" * 50)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
NumPy supports vectorized operations.

This means operations are performed
on entire arrays without using loops.

Advantages:

1. Faster Execution
2. Less Code
3. Better Performance
4. Essential for Data Science

Common Operations:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponentiation
7. Comparison Operations
"""

# ======================================
# 1. ARRAY CREATION
# ======================================

print("\n1. ARRAY CREATION")

array1 = np.array(
    [10, 20, 30, 40, 50]
)

array2 = np.array(
    [1, 2, 3, 4, 5]
)

print("Array 1:", array1)
print("Array 2:", array2)

# ======================================
# 2. ADDITION
# ======================================

print("\n2. ADDITION")

result = array1 + array2

print(result)

# ======================================
# 3. SUBTRACTION
# ======================================

print("\n3. SUBTRACTION")

result = array1 - array2

print(result)

# ======================================
# 4. MULTIPLICATION
# ======================================

print("\n4. MULTIPLICATION")

result = array1 * array2

print(result)

# ======================================
# 5. DIVISION
# ======================================

print("\n5. DIVISION")

result = array1 / array2

print(result)

# ======================================
# 6. MODULUS
# ======================================

print("\n6. MODULUS")

result = array1 % array2

print(result)

# ======================================
# 7. EXPONENTIATION
# ======================================

print("\n7. EXPONENTIATION")

result = array2 ** 2

print(result)

# ======================================
# 8. SCALAR OPERATIONS
# ======================================

print("\n8. SCALAR OPERATIONS")

print(array1 + 10)
print(array1 * 2)

# ======================================
# 9. COMPARISON OPERATIONS
# ======================================

print("\n9. COMPARISON OPERATIONS")

print(array1 > 25)
print(array1 == 30)

# ======================================
# 10. AGGREGATE FUNCTIONS
# ======================================

print("\n10. AGGREGATE FUNCTIONS")

print("Sum     :", np.sum(array1))
print("Mean    :", np.mean(array1))
print("Maximum :", np.max(array1))
print("Minimum :", np.min(array1))

# ======================================
# 11. SQUARE ROOT
# ======================================

print("\n11. SQUARE ROOT")

numbers = np.array(
    [1, 4, 9, 16, 25]
)

print(np.sqrt(numbers))

# ======================================
# 12. ABSOLUTE VALUES
# ======================================

print("\n12. ABSOLUTE VALUES")

values = np.array(
    [-10, -20, 30, -40]
)

print(np.abs(values))

# ======================================
# 13. ROUND VALUES
# ======================================

print("\n13. ROUND VALUES")

decimal_values = np.array(
    [3.14159, 2.71828, 1.41421]
)

print(np.round(decimal_values, 2))

# ======================================
# 14. SORT ARRAY
# ======================================

print("\n14. SORT ARRAY")

numbers = np.array(
    [45, 12, 78, 23, 9]
)

print(np.sort(numbers))

# ======================================
# 15. USER INPUT ARRAY
# ======================================

print("\n15. USER INPUT ARRAY")

user_numbers = input(
    "Enter numbers separated by spaces: "
).split()

user_numbers = np.array(
    user_numbers,
    dtype=int
)

print("Array:", user_numbers)

print("Squared Values:")
print(user_numbers ** 2)

# ======================================
# 16. 2D ARRAY OPERATIONS
# ======================================

print("\n16. 2D ARRAY OPERATIONS")

matrix1 = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

matrix2 = np.array(
    [
        [5, 6],
        [7, 8]
    ]
)

print("Addition:")
print(matrix1 + matrix2)

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT - MARKS ANALYZER")

marks = np.array(
    [92, 85, 78, 95, 88]
)

print("Marks:", marks)

print("Total   :", np.sum(marks))
print("Average :", np.mean(marks))
print("Highest :", np.max(marks))
print("Lowest  :", np.min(marks))

print("Bonus Marks:")
print(marks + 5)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create two arrays and perform:

- Addition
- Subtraction
- Multiplication
- Division

Exercise 2:
Find:

- Sum
- Mean
- Maximum
- Minimum

Exercise 3:
Calculate square roots
of array elements.

Exercise 4:
Sort an array.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Marks System.

Store marks in a NumPy array.

Perform:

1. Add 5 Bonus Marks
2. Calculate Total Marks
3. Calculate Average Marks
4. Find Highest Marks
5. Find Lowest Marks
6. Square All Marks

Display complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 044 Completed Successfully!")