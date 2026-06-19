# ======================================
# Day 042: NumPy Arrays
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating and Working with NumPy
# Arrays in Python
# ======================================

print("=" * 50)
print("DAY 042 - NUMPY ARRAYS")
print("=" * 50)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a NumPy Array?

A NumPy array is a collection of
elements stored in contiguous memory.

Advantages:

1. Faster than Python Lists
2. Memory Efficient
3. Supports Vectorized Operations
4. Useful for Data Science

Array Types:

1. 1-D Array
2. 2-D Array
3. 3-D Array
"""

# ======================================
# 1. 1-D ARRAY
# ======================================

print("\n1. ONE-DIMENSIONAL ARRAY")

arr1 = np.array(
    [10, 20, 30, 40, 50]
)

print(arr1)

# ======================================
# 2. 2-D ARRAY
# ======================================

print("\n2. TWO-DIMENSIONAL ARRAY")

arr2 = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

print(arr2)

# ======================================
# 3. 3-D ARRAY
# ======================================

print("\n3. THREE-DIMENSIONAL ARRAY")

arr3 = np.array(
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

print(arr3)

# ======================================
# 4. CHECK DIMENSIONS
# ======================================

print("\n4. ARRAY DIMENSIONS")

print("1D:", arr1.ndim)
print("2D:", arr2.ndim)
print("3D:", arr3.ndim)

# ======================================
# 5. ARRAY SHAPE
# ======================================

print("\n5. ARRAY SHAPE")

print("arr1 Shape:", arr1.shape)
print("arr2 Shape:", arr2.shape)
print("arr3 Shape:", arr3.shape)

# ======================================
# 6. ARRAY SIZE
# ======================================

print("\n6. ARRAY SIZE")

print("arr1 Size:", arr1.size)
print("arr2 Size:", arr2.size)
print("arr3 Size:", arr3.size)

# ======================================
# 7. ARRAY DATA TYPE
# ======================================

print("\n7. ARRAY DATA TYPE")

print(arr1.dtype)

# ======================================
# 8. ZEROS ARRAY
# ======================================

print("\n8. ZEROS ARRAY")

zeros_array = np.zeros((3, 3))

print(zeros_array)

# ======================================
# 9. ONES ARRAY
# ======================================

print("\n9. ONES ARRAY")

ones_array = np.ones((2, 4))

print(ones_array)

# ======================================
# 10. FULL ARRAY
# ======================================

print("\n10. FULL ARRAY")

full_array = np.full(
    (3, 3),
    7
)

print(full_array)

# ======================================
# 11. ARANGE FUNCTION
# ======================================

print("\n11. ARANGE FUNCTION")

numbers = np.arange(
    1,
    11
)

print(numbers)

# ======================================
# 12. LINSPACE FUNCTION
# ======================================

print("\n12. LINSPACE FUNCTION")

values = np.linspace(
    0,
    100,
    5
)

print(values)

# ======================================
# 13. RANDOM ARRAY
# ======================================

print("\n13. RANDOM ARRAY")

random_array = np.random.randint(
    1,
    100,
    size=5
)

print(random_array)

# ======================================
# 14. EMPTY ARRAY
# ======================================

print("\n14. EMPTY ARRAY")

empty_array = np.empty((2, 2))

print(empty_array)

# ======================================
# 15. IDENTITY MATRIX
# ======================================

print("\n15. IDENTITY MATRIX")

identity = np.eye(3)

print(identity)

# ======================================
# 16. USER INPUT ARRAY
# ======================================

print("\n16. USER INPUT ARRAY")

numbers = input(
    "Enter numbers separated by spaces: "
).split()

numbers = np.array(
    numbers,
    dtype=int
)

print(numbers)

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT - STUDENT MARKS")

marks = np.array(
    [92, 95, 88, 90, 85]
)

print("Marks:", marks)

print("Total  :", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest :", np.min(marks))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create:

- 1D Array
- 2D Array
- 3D Array

Exercise 2:
Create:

- Zeros Array
- Ones Array

Exercise 3:
Create arrays using:

- arange()
- linspace()

Exercise 4:
Create a 4x4 Identity Matrix.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Data System.

Store:

- Mathematics Marks
- Python Marks
- DBMS Marks
- Statistics Marks
- English Marks

Using a NumPy Array.

Find:

1. Total
2. Average
3. Highest
4. Lowest
5. Number of Subjects
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 042 Completed Successfully!")