# ======================================
# Day 048: NumPy Broadcasting
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Broadcasting in NumPy
# for Efficient Array Operations
# ======================================

print("=" * 50)
print("DAY 048 - NUMPY BROADCASTING")
print("=" * 50)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Broadcasting?

Broadcasting is a NumPy mechanism
that allows arrays of different
shapes to perform arithmetic
operations together.

Without Broadcasting:
Arrays must have the same shape.

With Broadcasting:
NumPy automatically expands
smaller arrays when possible.

Benefits:

1. Faster Computation
2. Less Memory Usage
3. Cleaner Code
4. No Explicit Loops

Broadcasting Rules:

1. Dimensions must be equal
   OR

2. One dimension must be 1
"""

# ======================================
# 1. ARRAY + SCALAR
# ======================================

print("\n1. ARRAY + SCALAR")

numbers = np.array(
    [10, 20, 30, 40, 50]
)

print("Original:")
print(numbers)

print("\nAfter Adding 5:")
print(numbers + 5)

# ======================================
# 2. ARRAY * SCALAR
# ======================================

print("\n2. ARRAY * SCALAR")

print(numbers * 2)

# ======================================
# 3. ARRAY + ARRAY
# ======================================

print("\n3. ARRAY + ARRAY")

array1 = np.array(
    [1, 2, 3]
)

array2 = np.array(
    [10, 20, 30]
)

print(array1 + array2)

# ======================================
# 4. BROADCASTING EXAMPLE
# ======================================

print("\n4. BROADCASTING EXAMPLE")

matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

vector = np.array(
    [10, 20, 30]
)

print("Matrix:")
print(matrix)

print("\nVector:")
print(vector)

print("\nResult:")
print(matrix + vector)

# ======================================
# 5. ROW BROADCASTING
# ======================================

print("\n5. ROW BROADCASTING")

matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

row = np.array(
    [100, 200, 300]
)

print(matrix + row)

# ======================================
# 6. COLUMN BROADCASTING
# ======================================

print("\n6. COLUMN BROADCASTING")

matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

column = np.array(
    [
        [10],
        [20]
    ]
)

print(matrix + column)

# ======================================
# 7. MULTIPLICATION BROADCASTING
# ======================================

print("\n7. MULTIPLICATION")

matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

print(matrix * 10)

# ======================================
# 8. DIVISION BROADCASTING
# ======================================

print("\n8. DIVISION")

numbers = np.array(
    [10, 20, 30, 40, 50]
)

print(numbers / 10)

# ======================================
# 9. 3D BROADCASTING
# ======================================

print("\n9. 3D BROADCASTING")

array_3d = np.array(
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
)

print(array_3d + 5)

# ======================================
# 10. SHAPE CHECKING
# ======================================

print("\n10. SHAPE CHECKING")

matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

vector = np.array(
    [10, 20, 30]
)

print("Matrix Shape:",
      matrix.shape)

print("Vector Shape:",
      vector.shape)

# ======================================
# 11. BONUS MARKS SYSTEM
# ======================================

print("\n11. BONUS MARKS SYSTEM")

marks = np.array(
    [92, 85, 78, 95, 88]
)

bonus_marks = marks + 5

print("Original:")
print(marks)

print("Bonus:")
print(bonus_marks)

# ======================================
# 12. TEMPERATURE CONVERSION
# ======================================

print("\n12. TEMPERATURE CONVERSION")

celsius = np.array(
    [0, 10, 20, 30, 40]
)

fahrenheit = (
    celsius * 9 / 5
) + 32

print(fahrenheit)

# ======================================
# 13. USER INPUT EXAMPLE
# ======================================

print("\n13. USER INPUT EXAMPLE")

numbers = input(
    "Enter numbers separated by spaces: "
).split()

numbers = np.array(
    numbers,
    dtype=int
)

print("Original:")
print(numbers)

print("After Adding 10:")
print(numbers + 10)

# ======================================
# 14. SALES DATA ANALYSIS
# ======================================

print("\n14. SALES DATA ANALYSIS")

sales = np.array(
    [1000, 1500, 1200, 1800]
)

growth = sales * 1.10

print("Current Sales:")
print(sales)

print("Projected Sales:")
print(growth)

# ======================================
# 15. STUDENT MARKS MATRIX
# ======================================

print("\n15. STUDENT MARKS MATRIX")

marks = np.array(
    [
        [92, 85, 78],
        [95, 88, 90],
        [85, 89, 93]
    ]
)

bonus = np.array(
    [5, 5, 5]
)

updated_marks = marks + bonus

print(updated_marks)

# ======================================
# 16. NORMALIZATION
# ======================================

print("\n16. NORMALIZATION")

data = np.array(
    [10, 20, 30, 40, 50]
)

normalized = data / np.max(data)

print(normalized)

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT - STUDENT PERFORMANCE")

marks = np.array(
    [
        [92, 85, 78],
        [95, 88, 90],
        [85, 89, 93]
    ]
)

bonus_marks = marks + 5

print("Original Marks:")
print(marks)

print("\nBonus Marks:")
print(bonus_marks)

print("\nAverage Marks:")
print(
    np.mean(
        bonus_marks,
        axis=1
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create an array and add:

- 10
- 20

using broadcasting.

Exercise 2:
Multiply all values
by 5.

Exercise 3:
Create a matrix and
add a row vector.

Exercise 4:
Create a matrix and
add a column vector.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Marks Analyzer.

Store marks in a matrix.

Apply:

1. Bonus Marks
2. Percentage Increase
3. Average Marks
4. Highest Marks
5. Lowest Marks

Use Broadcasting wherever possible.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 048 Completed Successfully!")