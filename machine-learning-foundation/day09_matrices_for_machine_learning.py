# ==========================================================
# Day 09 : Matrices for Machine Learning
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 09")
print("=" * 60)

print("\nMatrices for Machine Learning")
print("-" * 30)

print("""
A Matrix is a rectangular arrangement of numbers
organized into rows and columns.

Matrices are used extensively in Machine Learning
to represent datasets and perform computations.
""")

# ----------------------------------------------------------
# Creating a Matrix
# ----------------------------------------------------------

print("\nCreating a Matrix")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)

# ----------------------------------------------------------
# Rows and Columns
# ----------------------------------------------------------

print("\nRows and Columns")
print("-" * 30)

rows = len(matrix)
columns = len(matrix[0])

print("Number of Rows    :", rows)
print("Number of Columns :", columns)

# ----------------------------------------------------------
# Dataset as a Matrix
# ----------------------------------------------------------

print("\nDataset Representation")
print("-" * 30)

students = [
    [18, 6, 90],
    [19, 8, 95],
    [17, 5, 85],
    [20, 7, 88]
]

print("Age | Study Hours | Attendance")
print("-" * 35)

for student in students:
    print(student)

print("""
Rows    -> Observations
Columns -> Features
""")

# ----------------------------------------------------------
# Accessing Matrix Elements
# ----------------------------------------------------------

print("\nAccessing Elements")
print("-" * 30)

print("First Row:", students[0])
print("First Element:", students[0][0])
print("Second Row, Third Column:", students[1][2])

# ----------------------------------------------------------
# Matrix Dimensions
# ----------------------------------------------------------

print("\nMatrix Dimensions")
print("-" * 30)

print("""
Dimension = Rows × Columns

Example:

4 × 3 Matrix
4 Rows
3 Columns
""")

print("Student Matrix Dimension =", len(students), "x", len(students[0]))

# ----------------------------------------------------------
# Matrix Addition
# ----------------------------------------------------------

print("\nMatrix Addition")
print("-" * 30)

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = []

for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])

    C.append(row)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nA + B:")
for row in C:
    print(row)

# ----------------------------------------------------------
# Scalar Multiplication
# ----------------------------------------------------------

print("\nScalar Multiplication")
print("-" * 30)

scalar = 2

result = []

for row in A:
    new_row = []

    for value in row:
        new_row.append(value * scalar)

    result.append(new_row)

print("2 × A =")

for row in result:
    print(row)

# ----------------------------------------------------------
# Identity Matrix
# ----------------------------------------------------------

print("\nIdentity Matrix")
print("-" * 30)

identity = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

for row in identity:
    print(row)

print("""
An Identity Matrix has:
1s on the diagonal
0s elsewhere
""")

# ----------------------------------------------------------
# Matrix in Machine Learning
# ----------------------------------------------------------

print("\nWhy Matrices Matter in ML")
print("-" * 30)

print("""
Machine Learning datasets are usually stored
as matrices.

Examples:

Student Dataset
House Price Dataset
Customer Dataset
Image Data
Text Data

Most ML algorithms perform matrix operations.
""")

# ----------------------------------------------------------
# Real ML Example
# ----------------------------------------------------------

print("\nReal Machine Learning Example")
print("-" * 30)

house_data = [
    [1000, 2],
    [1200, 3],
    [1500, 3],
    [1800, 4]
]

print("Area | Bedrooms")
print("-" * 20)

for house in house_data:
    print(house)

print("""
Each row represents a house.
Each column represents a feature.
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Matrix?
2. What are Rows?
3. What are Columns?
4. How are datasets represented in ML?
""")

print("""
Answers:
1. Rectangular arrangement of numbers
2. Observations/Records
3. Features/Variables
4. Using matrices
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 09 Summary")
print("-" * 30)

print("""
1. A Matrix is a collection of rows and columns.
2. Datasets are commonly represented as matrices.
3. Rows represent observations.
4. Columns represent features.
5. Matrix Addition combines matrices.
6. Scalar Multiplication scales matrix values.
7. Matrices are fundamental to Machine Learning.
""")

print("\nDay 09 Completed Successfully!")
print("=" * 60)