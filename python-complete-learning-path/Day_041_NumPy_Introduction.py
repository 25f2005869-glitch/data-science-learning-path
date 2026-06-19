# ======================================
# Day 041: NumPy Introduction
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to NumPy for Data Science
# and Scientific Computing
# ======================================

print("=" * 50)
print("DAY 041 - NUMPY INTRODUCTION")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is NumPy?

NumPy stands for:

Numerical Python

NumPy is the fundamental package for:

1. Scientific Computing
2. Data Analysis
3. Machine Learning
4. Artificial Intelligence
5. Data Science

Why NumPy?

Python Lists:
- Flexible
- Slower for numerical operations

NumPy Arrays:
- Faster
- Memory Efficient
- Powerful Mathematical Functions

Installation:

pip install numpy

Import:

import numpy as np

Why np?

It is the standard alias used
worldwide by Python developers.
"""

# ======================================
# 1. IMPORTING NUMPY
# ======================================

print("\n1. IMPORTING NUMPY")

import numpy as np

print("NumPy Imported Successfully")

# ======================================
# 2. CHECK NUMPY VERSION
# ======================================

print("\n2. NUMPY VERSION")

print(np.__version__)

# ======================================
# 3. PYTHON LIST
# ======================================

print("\n3. PYTHON LIST")

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(type(numbers))

# ======================================
# 4. NUMPY ARRAY
# ======================================

print("\n4. NUMPY ARRAY")

numbers_array = np.array(
    [10, 20, 30, 40, 50]
)

print(numbers_array)
print(type(numbers_array))

# ======================================
# 5. ARRAY OF STRINGS
# ======================================

print("\n5. ARRAY OF STRINGS")

subjects = np.array(
    [
        "Python",
        "DBMS",
        "Statistics"
    ]
)

print(subjects)

# ======================================
# 6. ARRAY OF FLOATS
# ======================================

print("\n6. ARRAY OF FLOATS")

marks = np.array(
    [92.5, 88.0, 95.5]
)

print(marks)

# ======================================
# 7. ARRAY DIMENSIONS
# ======================================

print("\n7. ARRAY DIMENSIONS")

numbers = np.array(
    [1, 2, 3, 4, 5]
)

print("Dimensions:", numbers.ndim)

# ======================================
# 8. ARRAY SHAPE
# ======================================

print("\n8. ARRAY SHAPE")

print("Shape:", numbers.shape)

# ======================================
# 9. ARRAY SIZE
# ======================================

print("\n9. ARRAY SIZE")

print("Size:", numbers.size)

# ======================================
# 10. ARRAY DATA TYPE
# ======================================

print("\n10. ARRAY DATA TYPE")

print("Data Type:", numbers.dtype)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

user_numbers = input(
    "Enter numbers separated by spaces: "
).split()

user_numbers = np.array(
    user_numbers,
    dtype=int
)

print("Array:", user_numbers)

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT - STUDENT MARKS")

student_marks = np.array(
    [92, 95, 88, 90, 85]
)

print("Marks Array :", student_marks)

print("Total Marks :", np.sum(student_marks))

print("Average     :",
      np.mean(student_marks))

print("Maximum     :",
      np.max(student_marks))

print("Minimum     :",
      np.min(student_marks))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a NumPy array of
five integers.

Exercise 2:
Print:

- Shape
- Size
- Data Type

of the array.

Exercise 3:
Create an array of
student marks and find:

- Sum
- Average
- Maximum
- Minimum

Exercise 4:
Create a NumPy array
containing subject names.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Performance Analyzer.

Store marks of 5 subjects
in a NumPy array.

Calculate:

1. Total Marks
2. Average Marks
3. Highest Marks
4. Lowest Marks
5. Number of Subjects

Display the complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 041 Completed Successfully!")