# ==========================================================
# Day 12 : Determinants and Inverse
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 12")
print("=" * 60)

print("\nDeterminants and Inverse")
print("-" * 30)

print("""
Determinants and Matrix Inverses are important
concepts in Linear Algebra.

Applications in Machine Learning:

✓ Linear Regression
✓ Solving Linear Equations
✓ Optimization
✓ Matrix Transformations
✓ Data Analysis
""")

# ----------------------------------------------------------
# Matrix Example
# ----------------------------------------------------------

print("\nExample Matrix")
print("-" * 30)

A = [
    [4, 7],
    [2, 6]
]

for row in A:
    print(row)

# ----------------------------------------------------------
# Determinant of 2x2 Matrix
# ----------------------------------------------------------

print("\nDeterminant")
print("-" * 30)

print("""
For a 2×2 Matrix:

|a  b|
|c  d|

Determinant = (a × d) - (b × c)
""")

a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]

determinant = (a * d) - (b * c)

print("Determinant =", determinant)

# ----------------------------------------------------------
# Interpretation of Determinant
# ----------------------------------------------------------

print("\nWhy Determinant Matters")
print("-" * 30)

print("""
If Determinant = 0
→ Matrix is Singular
→ Inverse does NOT exist

If Determinant ≠ 0
→ Matrix is Non-Singular
→ Inverse exists
""")

if determinant != 0:
    print("Inverse Exists")
else:
    print("Inverse Does Not Exist")

# ----------------------------------------------------------
# Inverse of a 2x2 Matrix
# ----------------------------------------------------------

print("\nInverse Matrix")
print("-" * 30)

print("""
Formula:

A⁻¹ = 1/det(A)

| d  -b |
| -c  a |
""")

if determinant != 0:

    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]

    print("Inverse Matrix:")

    for row in inverse:
        print(row)

else:
    print("Inverse Cannot Be Calculated")

# ----------------------------------------------------------
# Verification
# ----------------------------------------------------------

print("\nVerification")
print("-" * 30)

print("""
If:

A × A⁻¹ = I

Then the inverse is correct.

I = Identity Matrix
""")

identity = [
    [1, 0],
    [0, 1]
]

print("Identity Matrix:")

for row in identity:
    print(row)

# ----------------------------------------------------------
# Singular Matrix Example
# ----------------------------------------------------------

print("\nSingular Matrix Example")
print("-" * 30)

B = [
    [2, 4],
    [1, 2]
]

for row in B:
    print(row)

det_B = (B[0][0] * B[1][1]) - (B[0][1] * B[1][0])

print("Determinant =", det_B)

if det_B == 0:
    print("Matrix is Singular")
    print("Inverse Does Not Exist")

# ----------------------------------------------------------
# Machine Learning Example
# ----------------------------------------------------------

print("\nMachine Learning Connection")
print("-" * 30)

print("""
In Linear Regression:

β = (XᵀX)⁻¹ XᵀY

Here:

X  = Feature Matrix
Xᵀ = Transpose Matrix
(XᵀX)⁻¹ = Inverse Matrix

The inverse matrix helps find
optimal model parameters.
""")

# ----------------------------------------------------------
# Practical Dataset Example
# ----------------------------------------------------------

print("\nFeature Matrix Example")
print("-" * 30)

features = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for row in features:
    print(row)

print("""
Rows    -> Observations
Columns -> Features

Many ML calculations involve
determinants and inverses.
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

C = [
    [5, 3],
    [2, 1]
]

for row in C:
    print(row)

det_C = (C[0][0] * C[1][1]) - (C[0][1] * C[1][0])

print("Determinant =", det_C)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a determinant?

2. When does a matrix have an inverse?

3. What is a singular matrix?

4. Why are inverses useful in ML?
""")

print("""
Answers:

1. A value computed from a square matrix
2. When determinant ≠ 0
3. A matrix with determinant = 0
4. They help solve matrix equations and
   optimize machine learning models
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 12 Summary")
print("-" * 30)

print("""
1. Determinants are computed from square matrices.
2. Determinant helps determine invertibility.
3. If determinant = 0, inverse does not exist.
4. Matrix inverse is important in Linear Regression.
5. Determinants and inverses are core concepts
   in Machine Learning mathematics.
""")

print("\nDay 12 Completed Successfully!")
print("=" * 60)