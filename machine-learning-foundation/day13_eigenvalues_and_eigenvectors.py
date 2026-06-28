# ==========================================================
# Day 13 : Eigenvalues and Eigenvectors
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 13")
print("=" * 60)

print("\nEigenvalues and Eigenvectors")
print("-" * 30)

print("""
Eigenvalues and Eigenvectors are important concepts
in Linear Algebra and Machine Learning.

Applications:

✓ Principal Component Analysis (PCA)
✓ Dimensionality Reduction
✓ Face Recognition
✓ Image Compression
✓ Recommendation Systems
✓ Deep Learning
""")

# ----------------------------------------------------------
# Introduction
# ----------------------------------------------------------

print("\nWhat are Eigenvalues and Eigenvectors?")
print("-" * 30)

print("""
For a square matrix A:

A × v = λ × v

where:

A = Matrix
v = Eigenvector
λ = Eigenvalue

The eigenvector keeps its direction
after transformation.

Only its magnitude changes.
""")

# ----------------------------------------------------------
# Example Matrix
# ----------------------------------------------------------

print("\nExample Matrix")
print("-" * 30)

A = [
    [2, 0],
    [0, 3]
]

for row in A:
    print(row)

print("""
For this matrix:

Eigenvalues:
λ₁ = 2
λ₂ = 3

Eigenvectors:
v₁ = [1, 0]
v₂ = [0, 1]
""")

# ----------------------------------------------------------
# Understanding Transformation
# ----------------------------------------------------------

print("\nUnderstanding Transformation")
print("-" * 30)

vector1 = [1, 0]
vector2 = [0, 1]

print("Original Vector 1 =", vector1)
print("Original Vector 2 =", vector2)

transformed_v1 = [2, 0]
transformed_v2 = [0, 3]

print("Transformed Vector 1 =", transformed_v1)
print("Transformed Vector 2 =", transformed_v2)

print("""
Direction remains same.

Only scaling changes.

This is the key idea behind
eigenvectors and eigenvalues.
""")

# ----------------------------------------------------------
# Characteristic Equation
# ----------------------------------------------------------

print("\nCharacteristic Equation")
print("-" * 30)

print("""
Eigenvalues are obtained from:

det(A - λI) = 0

where:

A = Matrix
I = Identity Matrix
λ = Eigenvalue
det = Determinant
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

# ----------------------------------------------------------
# Simple Scaling Example
# ----------------------------------------------------------

print("\nScaling Example")
print("-" * 30)

eigenvector = [2, 1]
eigenvalue = 4

scaled_vector = [
    eigenvector[0] * eigenvalue,
    eigenvector[1] * eigenvalue
]

print("Eigenvector =", eigenvector)
print("Eigenvalue =", eigenvalue)
print("Scaled Vector =", scaled_vector)

print("""
The vector direction remains unchanged.
Only the size increases by factor 4.
""")

# ----------------------------------------------------------
# Machine Learning Example
# ----------------------------------------------------------

print("\nMachine Learning Connection")
print("-" * 30)

print("""
Suppose a dataset contains:

✓ Age
✓ Income
✓ Spending Score

Some features may carry more information
than others.

PCA uses eigenvalues and eigenvectors
to identify the most important directions
in the data.
""")

# ----------------------------------------------------------
# PCA Concept
# ----------------------------------------------------------

print("\nPrincipal Component Analysis (PCA)")
print("-" * 30)

print("""
PCA reduces dimensions while preserving
maximum information.

Steps:

1. Create Covariance Matrix
2. Compute Eigenvalues
3. Compute Eigenvectors
4. Select Largest Eigenvalues
5. Reduce Dimensions

Result:
Less Data + More Information
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nFeature Matrix Example")
print("-" * 30)

data = [
    [18, 30000],
    [20, 35000],
    [22, 40000],
    [24, 45000]
]

print("Age | Income")

for row in data:
    print(row)

print("""
PCA can transform this dataset
into fewer dimensions while
retaining important information.
""")

# ----------------------------------------------------------
# Why Eigenvalues Matter
# ----------------------------------------------------------

print("\nWhy Eigenvalues Matter")
print("-" * 30)

print("""
Large Eigenvalue:
✓ Important Direction

Small Eigenvalue:
✓ Less Important Direction

PCA keeps directions with
largest eigenvalues.
""")

# ----------------------------------------------------------
# Real-World Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Principal Component Analysis",
    "Face Recognition",
    "Image Compression",
    "Data Visualization",
    "Recommendation Systems",
    "Deep Learning"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

matrix = [
    [5, 0],
    [0, 2]
]

for row in matrix:
    print(row)

print("""
Identify the Eigenvalues:

Answer:
λ₁ = 5
λ₂ = 2
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is an Eigenvalue?

2. What is an Eigenvector?

3. Which ML technique uses
   Eigenvalues extensively?

4. Why are Eigenvalues important?
""")

print("""
Answers:

1. Scaling factor of an eigenvector
2. A vector whose direction remains unchanged
3. PCA
4. They identify important directions in data
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 13 Summary")
print("-" * 30)

print("""
1. Eigenvectors maintain their direction
   after transformation.
2. Eigenvalues represent scaling factors.
3. They are obtained using:
   det(A - λI) = 0
4. PCA relies heavily on Eigenvalues
   and Eigenvectors.
5. They help reduce dimensions and
   preserve important information.
""")

print("\nDay 13 Completed Successfully!")
print("=" * 60)