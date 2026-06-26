# ==========================================================
# Day 11 : Matrix Multiplication
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 11")
print("=" * 60)

print("\nMatrix Multiplication")
print("-" * 30)

print("""
Matrix Multiplication is one of the most
important operations in Machine Learning.

Applications:
✓ Linear Regression
✓ Neural Networks
✓ Deep Learning
✓ Computer Vision
✓ Natural Language Processing
""")

# ----------------------------------------------------------
# Matrix Multiplication Rule
# ----------------------------------------------------------

print("\nMatrix Multiplication Rule")
print("-" * 30)

print("""
For A × B:

(Number of Columns in A)
            =
(Number of Rows in B)

If A is m × n
and B is n × p

Then Result is m × p
""")

# ----------------------------------------------------------
# Example Matrices
# ----------------------------------------------------------

print("\nExample Matrices")
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
# Matrix Multiplication
# ----------------------------------------------------------

print("\nPerforming Matrix Multiplication")
print("-" * 30)

rows_A = len(A)
cols_A = len(A[0])

rows_B = len(B)
cols_B = len(B[0])

result = []

for i in range(rows_A):

    row = []

    for j in range(cols_B):

        value = 0

        for k in range(cols_A):
            value += A[i][k] * B[k][j]

        row.append(value)

    result.append(row)

print("A × B =")

for row in result:
    print(row)

# ----------------------------------------------------------
# Manual Calculation
# ----------------------------------------------------------

print("\nManual Calculation")
print("-" * 30)

print("""
First Element:

(1 × 5) + (2 × 7)
= 5 + 14
= 19

Second Element:

(1 × 6) + (2 × 8)
= 6 + 16
= 22
""")

# ----------------------------------------------------------
# Matrix Dimensions
# ----------------------------------------------------------

print("\nDimension Check")
print("-" * 30)

print("Matrix A Dimension =", rows_A, "x", cols_A)
print("Matrix B Dimension =", rows_B, "x", cols_B)
print("Result Dimension   =", rows_A, "x", cols_B)

# ----------------------------------------------------------
# Dataset Example
# ----------------------------------------------------------

print("\nMachine Learning Example")
print("-" * 30)

features = [
    [2, 3],
    [4, 5],
    [6, 7]
]

weights = [
    [0.5],
    [1.0]
]

print("Feature Matrix:")
for row in features:
    print(row)

print("\nWeight Matrix:")
for row in weights:
    print(row)

# ----------------------------------------------------------
# Prediction Calculation
# ----------------------------------------------------------

predictions = []

for i in range(len(features)):

    total = 0

    for j in range(len(weights)):
        total += features[i][j] * weights[j][0]

    predictions.append(total)

print("\nPredictions:")

for prediction in predictions:
    print(prediction)

# ----------------------------------------------------------
# Why Matrix Multiplication Matters
# ----------------------------------------------------------

print("\nWhy Matrix Multiplication Matters")
print("-" * 30)

print("""
Most Machine Learning algorithms can be
expressed using matrix multiplication.

Examples:

Input Data Matrix
        ×
Weight Matrix
        =
Predictions

This idea forms the basis of:

✓ Linear Regression
✓ Logistic Regression
✓ Neural Networks
✓ Deep Learning
""")

# ----------------------------------------------------------
# Identity Matrix Property
# ----------------------------------------------------------

print("\nIdentity Matrix Property")
print("-" * 30)

identity = [
    [1, 0],
    [0, 1]
]

print("Identity Matrix:")

for row in identity:
    print(row)

print("""
A × I = A

Multiplying by an identity matrix
does not change the matrix.
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

X = [
    [1, 2],
    [3, 4]
]

Y = [
    [2, 0],
    [1, 2]
]

practice_result = []

for i in range(len(X)):

    row = []

    for j in range(len(Y[0])):

        value = 0

        for k in range(len(Y)):
            value += X[i][k] * Y[k][j]

        row.append(value)

    practice_result.append(row)

print("X × Y =")

for row in practice_result:
    print(row)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What condition is required for
   matrix multiplication?

2. If A is 3×2 and B is 2×4,
   what is the dimension of A×B?

3. Why is matrix multiplication
   important in ML?
""")

print("""
Answers:

1. Columns of A must equal Rows of B
2. 3 × 4
3. It is used in almost all ML algorithms
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 11 Summary")
print("-" * 30)

print("""
1. Matrix multiplication combines rows and columns.
2. Columns(A) must equal Rows(B).
3. Result dimension = Rows(A) × Columns(B).
4. Matrix multiplication is used for predictions.
5. Neural Networks rely heavily on matrix multiplication.
6. It is one of the most important operations in ML.
""")

print("\nDay 11 Completed Successfully!")
print("=" * 60)