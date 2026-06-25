# ==========================================================
# Day 10 : Matrix Operations
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 10")
print("=" * 60)

print("\nMatrix Operations")
print("-" * 30)

print("""
Matrix operations are essential in Machine Learning.

Most ML algorithms internally use matrix
calculations for training and prediction.

Common Operations:
✓ Matrix Addition
✓ Matrix Subtraction
✓ Scalar Multiplication
✓ Matrix Transpose
✓ Matrix Multiplication
""")

# ----------------------------------------------------------
# Creating Matrices
# ----------------------------------------------------------

print("\nCreating Matrices")
print("-" * 30)

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

# ----------------------------------------------------------
# Matrix Addition
# ----------------------------------------------------------

print("\nMatrix Addition")
print("-" * 30)

addition = []

for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])

    addition.append(row)

print("A + B =")

for row in addition:
    print(row)

# ----------------------------------------------------------
# Matrix Subtraction
# ----------------------------------------------------------

print("\nMatrix Subtraction")
print("-" * 30)

subtraction = []

for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])

    subtraction.append(row)

print("A - B =")

for row in subtraction:
    print(row)

# ----------------------------------------------------------
# Scalar Multiplication
# ----------------------------------------------------------

print("\nScalar Multiplication")
print("-" * 30)

scalar = 2

scalar_result = []

for row in A:
    new_row = []

    for value in row:
        new_row.append(value * scalar)

    scalar_result.append(new_row)

print("2 × A =")

for row in scalar_result:
    print(row)

# ----------------------------------------------------------
# Matrix Transpose
# ----------------------------------------------------------

print("\nMatrix Transpose")
print("-" * 30)

transpose = []

for column in range(len(A[0])):
    row = []

    for r in range(len(A)):
        row.append(A[r][column])

    transpose.append(row)

print("Transpose of A:")

for row in transpose:
    print(row)

# ----------------------------------------------------------
# Matrix Multiplication
# ----------------------------------------------------------

print("\nMatrix Multiplication")
print("-" * 30)

result = [
    [0, 0],
    [0, 0]
]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("A × B =")

for row in result:
    print(row)

print("""
Matrix Multiplication Rule:

(Number of Columns in A)
        =
(Number of Rows in B)
""")

# ----------------------------------------------------------
# Identity Matrix
# ----------------------------------------------------------

print("\nIdentity Matrix")
print("-" * 30)

identity = [
    [1, 0],
    [0, 1]
]

for row in identity:
    print(row)

print("""
Multiplying a matrix by an identity matrix
does not change the matrix.
""")

# ----------------------------------------------------------
# Matrix Operations in ML
# ----------------------------------------------------------

print("\nApplications in Machine Learning")
print("-" * 30)

applications = [
    "Linear Regression",
    "Logistic Regression",
    "Neural Networks",
    "Computer Vision",
    "Recommendation Systems",
    "Natural Language Processing"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Dataset Example
# ----------------------------------------------------------

print("\nDataset as Matrix")
print("-" * 30)

students = [
    [18, 6, 90],
    [19, 8, 95],
    [17, 5, 85]
]

print("Age | Study Hours | Attendance")

for row in students:
    print(row)

print("""
Rows    -> Observations
Columns -> Features
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

X = [
    [2, 3],
    [4, 5]
]

Y = [
    [1, 1],
    [1, 1]
]

practice_add = []

for i in range(len(X)):
    row = []

    for j in range(len(X[0])):
        row.append(X[i][j] + Y[i][j])

    practice_add.append(row)

print("X + Y =")

for row in practice_add:
    print(row)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Matrix Addition?
2. What is a Matrix Transpose?
3. What is Matrix Multiplication?
4. Why are matrices important in ML?
""")

print("""
Answers:
1. Adding corresponding elements
2. Rows become columns
3. Row-column multiplication process
4. Datasets and ML computations use matrices
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 10 Summary")
print("-" * 30)

print("""
1. Matrix Addition combines matrices.
2. Matrix Subtraction finds differences.
3. Scalar Multiplication scales values.
4. Transpose swaps rows and columns.
5. Matrix Multiplication is a core ML operation.
6. Identity Matrix preserves matrix values.
7. Most Machine Learning algorithms rely on
   matrix operations.
""")

print("\nDay 10 Completed Successfully!")
print("=" * 60)