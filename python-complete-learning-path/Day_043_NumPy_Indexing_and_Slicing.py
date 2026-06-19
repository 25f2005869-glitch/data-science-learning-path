# ======================================
# Day 043: NumPy Indexing and Slicing
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Indexing and Slicing
# Operations in NumPy Arrays
# ======================================

print("=" * 50)
print("DAY 043 - NUMPY INDEXING AND SLICING")
print("=" * 50)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Indexing:

Indexing is used to access
individual elements of an array.

Positive Indexing:

0, 1, 2, 3, ...

Negative Indexing:

-1, -2, -3, ...

--------------------------------------

Slicing:

Used to extract a portion
of an array.

Syntax:

array[start:stop:step]

Important:

start -> inclusive
stop  -> exclusive
step  -> optional
"""

# ======================================
# 1. 1D ARRAY INDEXING
# ======================================

print("\n1. 1D ARRAY INDEXING")

numbers = np.array(
    [10, 20, 30, 40, 50]
)

print("First Element :", numbers[0])
print("Third Element :", numbers[2])
print("Last Element  :", numbers[-1])

# ======================================
# 2. 1D ARRAY SLICING
# ======================================

print("\n2. 1D ARRAY SLICING")

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

# ======================================
# 3. STEP SLICING
# ======================================

print("\n3. STEP SLICING")

array = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8]
)

print(array[::2])
print(array[::3])

# ======================================
# 4. 2D ARRAY
# ======================================

print("\n4. 2D ARRAY")

matrix = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)

print(matrix)

# ======================================
# 5. ACCESSING ELEMENTS IN 2D ARRAY
# ======================================

print("\n5. 2D ARRAY INDEXING")

print(matrix[0, 0])
print(matrix[1, 2])
print(matrix[2, 1])

# ======================================
# 6. ACCESSING ROWS
# ======================================

print("\n6. ACCESSING ROWS")

print("First Row:")
print(matrix[0])

print("Second Row:")
print(matrix[1])

# ======================================
# 7. ACCESSING COLUMNS
# ======================================

print("\n7. ACCESSING COLUMNS")

print("First Column:")
print(matrix[:, 0])

print("Second Column:")
print(matrix[:, 1])

# ======================================
# 8. 2D ARRAY SLICING
# ======================================

print("\n8. 2D ARRAY SLICING")

print(matrix[0:2, 0:2])

# ======================================
# 9. LAST ROW AND COLUMN
# ======================================

print("\n9. LAST ROW AND COLUMN")

print("Last Row:")
print(matrix[-1])

print("Last Column:")
print(matrix[:, -1])

# ======================================
# 10. MODIFYING VALUES
# ======================================

print("\n10. MODIFYING VALUES")

numbers = np.array(
    [10, 20, 30, 40, 50]
)

print("Before:", numbers)

numbers[2] = 100

print("After :", numbers)

# ======================================
# 11. BOOLEAN INDEXING
# ======================================

print("\n11. BOOLEAN INDEXING")

marks = np.array(
    [92, 35, 78, 45, 95, 25]
)

passed_marks = marks[marks >= 40]

print("Passed Marks:")
print(passed_marks)

# ======================================
# 12. FANCY INDEXING
# ======================================

print("\n12. FANCY INDEXING")

numbers = np.array(
    [10, 20, 30, 40, 50]
)

selected = numbers[[0, 2, 4]]

print(selected)

# ======================================
# 13. USER INPUT ARRAY
# ======================================

print("\n13. USER INPUT ARRAY")

user_array = input(
    "Enter numbers separated by spaces: "
).split()

user_array = np.array(
    user_array,
    dtype=int
)

print("Original Array:")
print(user_array)

print("First Three Elements:")
print(user_array[:3])

# ======================================
# 14. MINI PROJECT
# ======================================

print("\n14. MINI PROJECT - MARKS ANALYZER")

marks = np.array(
    [92, 85, 78, 95, 88, 90]
)

print("Marks:", marks)

print("Top Three Marks:")
print(marks[:3])

print("Last Three Marks:")
print(marks[-3:])

print("Alternate Marks:")
print(marks[::2])

print("Passed Marks:")
print(marks[marks >= 40])

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a NumPy array and
access:

- First Element
- Last Element

Exercise 2:
Perform:

- Basic Slicing
- Step Slicing

Exercise 3:
Create a 3x3 matrix and
access:

- First Row
- First Column

Exercise 4:
Use Boolean Indexing to
filter marks above 50.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Performance Analyzer.

Store marks of 10 students
in a NumPy array.

Display:

1. First Five Marks
2. Last Five Marks
3. Alternate Marks
4. Passed Students (>= 40)
5. Highest Marks
6. Lowest Marks

Use:

- Indexing
- Slicing
- Boolean Indexing
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 043 Completed Successfully!")