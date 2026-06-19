# ======================================
# Day 046: NumPy Linear Algebra
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Linear Algebra using
# NumPy for Data Science and ML
# ======================================

print("=" * 50)
print("DAY 046 - NUMPY LINEAR ALGEBRA")
print("=" * 50)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Linear Algebra?

Linear Algebra is the branch of
mathematics that deals with:

1. Vectors
2. Matrices
3. Determinants
4. Eigenvalues
5. Linear Equations

Applications:

1. Machine Learning
2. Artificial Intelligence
3. Computer Vision
4. Data Science
5. Deep Learning

NumPy Linear Algebra Module:

np.linalg
"""

# ======================================
# 1. VECTOR CREATION
# ======================================

print("\n1. VECTOR CREATION")

vector = np.array(
    [10, 20, 30]
)

print(vector)

# ======================================
# 2. MATRIX CREATION
# ======================================

print("\n2. MATRIX CREATION")

matrix = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

print(matrix)

# ======================================
# 3. MATRIX ADDITION
# ======================================

print("\n3. MATRIX ADDITION")

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

print(matrix1 + matrix2)

# ======================================
# 4. MATRIX SUBTRACTION
# ======================================

print("\n4. MATRIX SUBTRACTION")

print(matrix2 - matrix1)

# ======================================
# 5. MATRIX MULTIPLICATION
# ======================================

print("\n5. MATRIX MULTIPLICATION")

result = np.matmul(
    matrix1,
    matrix2
)

print(result)

# ======================================
# 6. DOT PRODUCT
# ======================================

print("\n6. DOT PRODUCT")

vector1 = np.array(
    [1, 2, 3]
)

vector2 = np.array(
    [4, 5, 6]
)

print(
    np.dot(
        vector1,
        vector2
    )
)

# ======================================
# 7. MATRIX TRANSPOSE
# ======================================

print("\n7. MATRIX TRANSPOSE")

matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

print(matrix.T)

# ======================================
# 8. DETERMINANT
# ======================================

print("\n8. DETERMINANT")

matrix = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

print(
    np.linalg.det(
        matrix
    )
)

# ======================================
# 9. MATRIX INVERSE
# ======================================

print("\n9. MATRIX INVERSE")

matrix = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

print(
    np.linalg.inv(
        matrix
    )
)

# ======================================
# 10. MATRIX RANK
# ======================================

print("\n10. MATRIX RANK")

matrix = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

print(
    np.linalg.matrix_rank(
        matrix
    )
)

# ======================================
# 11. EIGENVALUES & EIGENVECTORS
# ======================================

print("\n11. EIGENVALUES")

matrix = np.array(
    [
        [4, 2],
        [1, 3]
    ]
)

eigenvalues, eigenvectors = (
    np.linalg.eig(matrix)
)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# ======================================
# 12. SOLVING LINEAR EQUATIONS
# ======================================

print("\n12. LINEAR EQUATIONS")

A = np.array(
    [
        [2, 1],
        [1, 3]
    ]
)

B = np.array(
    [8, 13]
)

solution = np.linalg.solve(
    A,
    B
)

print(solution)

# ======================================
# 13. TRACE OF MATRIX
# ======================================

print("\n13. TRACE")

matrix = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

print(np.trace(matrix))

# ======================================
# 14. IDENTITY MATRIX
# ======================================

print("\n14. IDENTITY MATRIX")

identity = np.eye(3)

print(identity)

# ======================================
# 15. MATRIX POWER
# ======================================

print("\n15. MATRIX POWER")

matrix = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

print(
    np.linalg.matrix_power(
        matrix,
        2
    )
)

# ======================================
# 16. USER INPUT VECTOR
# ======================================

print("\n16. USER INPUT VECTOR")

numbers = input(
    "Enter numbers separated by spaces: "
).split()

vector = np.array(
    numbers,
    dtype=int
)

print("Vector:")
print(vector)

print("Sum:",
      np.sum(vector))

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT - STUDENT MARKS MATRIX")

marks = np.array(
    [
        [92, 95, 90],
        [88, 91, 87],
        [85, 89, 93]
    ]
)

print("Marks Matrix:")
print(marks)

print("\nRow-wise Total:")
print(
    np.sum(
        marks,
        axis=1
    )
)

print("\nColumn-wise Average:")
print(
    np.mean(
        marks,
        axis=0
    )
)

print("\nOverall Average:")
print(
    np.mean(
        marks
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create two matrices and perform:

- Addition
- Subtraction
- Multiplication

Exercise 2:
Find:

- Determinant
- Inverse
- Rank

of a matrix.

Exercise 3:
Create a matrix and find:

- Transpose
- Trace

Exercise 4:
Solve a system of
linear equations.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Marks Matrix.

Rows:
Students

Columns:
Subjects

Calculate:

1. Student-wise Total
2. Student-wise Average
3. Subject-wise Average
4. Highest Marks
5. Lowest Marks
6. Overall Average

Display a complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 046 Completed Successfully!")