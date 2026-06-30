# ==========================================================
# Day 15 : Math Foundations Practice
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 15")
print("=" * 60)

print("\nMathematical Foundations Practice")
print("-" * 30)

print("""
This lesson revises all important mathematical
concepts learned in Days 06–14.

Topics Covered:

✓ Sets
✓ Functions
✓ Vectors
✓ Vector Operations
✓ Matrices
✓ Matrix Operations
✓ Matrix Multiplication
✓ Determinants
✓ Matrix Inverse
✓ Eigenvalues & Eigenvectors
""")

# ----------------------------------------------------------
# Practice 1 : Sets
# ----------------------------------------------------------

print("\nPractice 1 : Sets")
print("-" * 30)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A =", A)
print("Set B =", B)

print("Union =", A.union(B))
print("Intersection =", A.intersection(B))
print("Difference (A-B) =", A.difference(B))

# ----------------------------------------------------------
# Practice 2 : Functions
# ----------------------------------------------------------

print("\nPractice 2 : Functions")
print("-" * 30)

def cube(x):
    return x ** 3

number = 4

print("Input =", number)
print("Cube =", cube(number))

# ----------------------------------------------------------
# Practice 3 : Vector Addition
# ----------------------------------------------------------

print("\nPractice 3 : Vector Addition")
print("-" * 30)

v1 = [2, 4, 6]
v2 = [1, 3, 5]

addition = []

for a, b in zip(v1, v2):
    addition.append(a + b)

print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", addition)

# ----------------------------------------------------------
# Practice 4 : Vector Subtraction
# ----------------------------------------------------------

print("\nPractice 4 : Vector Subtraction")
print("-" * 30)

subtraction = []

for a, b in zip(v1, v2):
    subtraction.append(a - b)

print("v1 - v2 =", subtraction)

# ----------------------------------------------------------
# Practice 5 : Dot Product
# ----------------------------------------------------------

print("\nPractice 5 : Dot Product")
print("-" * 30)

dot_product = 0

for a, b in zip(v1, v2):
    dot_product += a * b

print("Dot Product =", dot_product)

# ----------------------------------------------------------
# Practice 6 : Vector Magnitude
# ----------------------------------------------------------

print("\nPractice 6 : Vector Magnitude")
print("-" * 30)

vector = [3, 4]

magnitude = (
    vector[0] ** 2 +
    vector[1] ** 2
) ** 0.5

print("Vector =", vector)
print("Magnitude =", magnitude)

# ----------------------------------------------------------
# Practice 7 : Matrix Addition
# ----------------------------------------------------------

print("\nPractice 7 : Matrix Addition")
print("-" * 30)

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

matrix_add = []

for i in range(len(A)):

    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])

    matrix_add.append(row)

for row in matrix_add:
    print(row)

# ----------------------------------------------------------
# Practice 8 : Matrix Transpose
# ----------------------------------------------------------

print("\nPractice 8 : Matrix Transpose")
print("-" * 30)

transpose = []

for col in range(len(A[0])):

    row = []

    for r in range(len(A)):
        row.append(A[r][col])

    transpose.append(row)

for row in transpose:
    print(row)

# ----------------------------------------------------------
# Practice 9 : Matrix Multiplication
# ----------------------------------------------------------

print("\nPractice 9 : Matrix Multiplication")
print("-" * 30)

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
# Practice 10 : Determinant
# ----------------------------------------------------------

print("\nPractice 10 : Determinant")
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
# Practice 11 : Matrix Inverse
# ----------------------------------------------------------

print("\nPractice 11 : Matrix Inverse")
print("-" * 30)

if determinant != 0:

    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]

    for row in inverse:
        print(row)

else:
    print("Inverse Does Not Exist")

# ----------------------------------------------------------
# Practice 12 : Eigenvalues
# ----------------------------------------------------------

print("\nPractice 12 : Eigenvalues")
print("-" * 30)

print("""
Matrix:

[5 0]
[0 2]

Eigenvalues:

λ₁ = 5
λ₂ = 2
""")

# ----------------------------------------------------------
# Machine Learning Dataset Example
# ----------------------------------------------------------

print("\nPractice 13 : ML Dataset Matrix")
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
# Formula Revision Sheet
# ----------------------------------------------------------

print("\nFormula Revision Sheet")
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
# Final Practice Quiz
# ----------------------------------------------------------

print("\nFinal Practice Quiz")
print("-" * 30)

questions = [
    "What is a set?",
    "What is a vector?",
    "What is a matrix?",
    "When does an inverse exist?",
    "What does PCA use extensively?"
]

for i, question in enumerate(questions, start=1):
    print(f"{i}. {question}")

print("""
Answers:

1. Collection of unique elements
2. Ordered collection of numbers
3. Rectangular arrangement of numbers
4. When determinant ≠ 0
5. Eigenvalues and Eigenvectors
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 15 Summary")
print("-" * 30)

print("""
1. Revised all mathematical foundations.
2. Practiced vector operations.
3. Practiced matrix operations.
4. Calculated determinants and inverses.
5. Reviewed eigenvalues and eigenvectors.
6. Strengthened Linear Algebra concepts.
7. Ready to begin Probability for ML.
""")

print("\nMathematics Foundation Module Completed!")
print("Day 15 Completed Successfully!")
print("=" * 60)