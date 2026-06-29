# ==========================================================
# Day 14 : Linear Algebra Revision
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 14")
print("=" * 60)

print("\nLinear Algebra Revision")
print("-" * 30)

print("""
In the previous lessons we studied:

✓ Sets and Functions
✓ Vectors
✓ Vector Operations
✓ Matrices
✓ Matrix Operations
✓ Matrix Multiplication
✓ Determinants
✓ Matrix Inverse
✓ Eigenvalues and Eigenvectors

Today we will revise all important concepts.
""")

# ----------------------------------------------------------
# Sets Revision
# ----------------------------------------------------------

print("\n1. Sets Revision")
print("-" * 30)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A =", A)
print("Set B =", B)

print("Union =", A.union(B))
print("Intersection =", A.intersection(B))
print("Difference =", A.difference(B))

# ----------------------------------------------------------
# Functions Revision
# ----------------------------------------------------------

print("\n2. Functions Revision")
print("-" * 30)

def square(x):
    return x * x

number = 5

print("Input =", number)
print("Output =", square(number))

print("""
Function:
Input → Output
""")

# ----------------------------------------------------------
# Vectors Revision
# ----------------------------------------------------------

print("\n3. Vectors Revision")
print("-" * 30)

vector = [2, 4, 6]

print("Vector =", vector)
print("Dimension =", len(vector))

# ----------------------------------------------------------
# Vector Addition
# ----------------------------------------------------------

print("\nVector Addition")

v1 = [1, 2, 3]
v2 = [4, 5, 6]

addition = []

for a, b in zip(v1, v2):
    addition.append(a + b)

print("v1 + v2 =", addition)

# ----------------------------------------------------------
# Dot Product
# ----------------------------------------------------------

print("\nDot Product")

dot_product = 0

for a, b in zip(v1, v2):
    dot_product += a * b

print("Dot Product =", dot_product)

# ----------------------------------------------------------
# Magnitude
# ----------------------------------------------------------

print("\nVector Magnitude")

vector_mag = [3, 4]

magnitude = (
    vector_mag[0]**2 +
    vector_mag[1]**2
) ** 0.5

print("Magnitude =", magnitude)

# ----------------------------------------------------------
# Matrices Revision
# ----------------------------------------------------------

print("\n4. Matrices Revision")
print("-" * 30)

matrix = [
    [1, 2],
    [3, 4]
]

for row in matrix:
    print(row)

rows = len(matrix)
cols = len(matrix[0])

print("Dimension =", rows, "x", cols)

# ----------------------------------------------------------
# Matrix Addition
# ----------------------------------------------------------

print("\nMatrix Addition")

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(A)):

    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])

    result.append(row)

for row in result:
    print(row)

# ----------------------------------------------------------
# Matrix Transpose
# ----------------------------------------------------------

print("\nMatrix Transpose")

transpose = []

for col in range(len(A[0])):

    row = []

    for r in range(len(A)):
        row.append(A[r][col])

    transpose.append(row)

for row in transpose:
    print(row)

# ----------------------------------------------------------
# Matrix Multiplication
# ----------------------------------------------------------

print("\nMatrix Multiplication")

result = [
    [0, 0],
    [0, 0]
]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)

# ----------------------------------------------------------
# Determinant Revision
# ----------------------------------------------------------

print("\n5. Determinant Revision")
print("-" * 30)

matrix_det = [
    [4, 7],
    [2, 6]
]

a = matrix_det[0][0]
b = matrix_det[0][1]
c = matrix_det[1][0]
d = matrix_det[1][1]

determinant = (a * d) - (b * c)

print("Determinant =", determinant)

# ----------------------------------------------------------
# Inverse Revision
# ----------------------------------------------------------

print("\n6. Matrix Inverse Revision")
print("-" * 30)

if determinant != 0:

    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]

    print("Inverse Matrix:")

    for row in inverse:
        print(row)

else:
    print("Inverse Does Not Exist")

# ----------------------------------------------------------
# Eigenvalues Revision
# ----------------------------------------------------------

print("\n7. Eigenvalues & Eigenvectors Revision")
print("-" * 30)

print("""
For Matrix:

[2 0]
[0 3]

Eigenvalues:
λ₁ = 2
λ₂ = 3

Eigenvectors:
[1,0]
[0,1]
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\n8. Linear Algebra in Machine Learning")
print("-" * 30)

applications = [
    "Linear Regression",
    "Logistic Regression",
    "Neural Networks",
    "Deep Learning",
    "Computer Vision",
    "Natural Language Processing",
    "Recommendation Systems",
    "Principal Component Analysis (PCA)"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Quick Formula Sheet
# ----------------------------------------------------------

print("\n9. Quick Formula Sheet")
print("-" * 30)

print("""
Vector Magnitude:
||v|| = √(x² + y²)

Dot Product:
A · B = Σ(ai × bi)

Determinant:
ad - bc

Inverse:
A⁻¹ = (1/det(A))
      [ d  -b ]
      [ -c  a ]

Eigenvalue Equation:
Av = λv

Characteristic Equation:
det(A - λI) = 0
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\n10. Revision Quiz")
print("-" * 30)

print("""
1. What is a vector?

2. What is a matrix?

3. What condition is required
   for matrix multiplication?

4. When does an inverse exist?

5. Which ML technique uses
   Eigenvalues extensively?
""")

print("""
Answers:

1. Ordered collection of numbers
2. Rows and columns of numbers
3. Columns(A) = Rows(B)
4. Determinant ≠ 0
5. PCA
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 14 Summary")
print("-" * 30)

print("""
1. Linear Algebra is the mathematical
   foundation of Machine Learning.

2. Vectors represent features.

3. Matrices represent datasets.

4. Matrix multiplication powers
   many ML algorithms.

5. Determinants and inverses help
   solve matrix equations.

6. Eigenvalues and Eigenvectors are
   important for PCA and dimensionality reduction.

7. Strong Linear Algebra skills make
   advanced ML concepts easier to understand.
""")

print("\nDay 14 Completed Successfully!")
print("=" * 60)