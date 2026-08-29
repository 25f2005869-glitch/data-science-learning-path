# ==========================================================
# Day 52 : Principal Component Analysis (PCA)
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 52")
print("=" * 60)

print("\nPrincipal Component Analysis (PCA)")
print("-" * 30)

print("""
Principal Component Analysis (PCA)
is one of the most important
Dimensionality Reduction techniques
in Machine Learning.

Goal:

✓ Reduce Number of Features
✓ Preserve Important Information
✓ Remove Redundancy
✓ Improve Efficiency

PCA is widely used in:

✓ Data Science
✓ Machine Learning
✓ Computer Vision
✓ Image Processing
""")

# ----------------------------------------------------------
# What is PCA?
# ----------------------------------------------------------

print("\nWhat is PCA?")
print("-" * 30)

print("""
PCA transforms a dataset containing
many features into a smaller set of
new features called:

Principal Components

These components capture the
maximum variance in the data.
""")

# ----------------------------------------------------------
# Why PCA?
# ----------------------------------------------------------

print("\nWhy PCA?")
print("-" * 30)

print("""
Real-world datasets often contain:

✓ Many Features
✓ Correlated Variables
✓ Redundant Information

Problems:

✗ Slow Training
✗ High Memory Usage
✗ Difficult Visualization

PCA solves these problems.
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

students = [
    [80, 82, 85],
    [75, 78, 80],
    [90, 92, 95],
    [65, 68, 70]
]

print("""
Columns:

Math Marks
Physics Marks
Chemistry Marks
""")

for row in students:
    print(row)

# ----------------------------------------------------------
# Dimensionality Reduction Concept
# ----------------------------------------------------------

print("\nDimensionality Reduction")
print("-" * 30)

print("""
Original Features:

Math
Physics
Chemistry

After PCA:

Principal Component 1
Principal Component 2

3 Features → 2 Features
""")

# ----------------------------------------------------------
# Variance Concept
# ----------------------------------------------------------

print("\nVariance")
print("-" * 30)

print("""
Variance measures how much
data values spread out.

Higher Variance:

✓ More Information

Lower Variance:

✗ Less Information

PCA keeps directions with
maximum variance.
""")

# Example

values = [10, 20, 30, 40, 50]

mean = sum(values) / len(values)

variance = 0

for value in values:

    variance += (
        value - mean
    ) ** 2

variance = variance / len(values)

print("Variance =", variance)

# ----------------------------------------------------------
# Principal Components
# ----------------------------------------------------------

print("\nPrincipal Components")
print("-" * 30)

print("""
Principal Components are
new variables created from
the original features.

Properties:

✓ Uncorrelated
✓ Capture Maximum Information
✓ Ranked by Importance
""")

pc1 = "Principal Component 1"
pc2 = "Principal Component 2"

print(pc1)
print(pc2)

# ----------------------------------------------------------
# PCA Workflow
# ----------------------------------------------------------

print("\nPCA Workflow")
print("-" * 30)

steps = [
    "Standardize Data",
    "Compute Covariance Matrix",
    "Calculate Eigenvalues",
    "Calculate Eigenvectors",
    "Select Principal Components",
    "Transform Data"
]

for i, step in enumerate(
        steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Covariance Matrix
# ----------------------------------------------------------

print("\nCovariance Matrix")
print("-" * 30)

print("""
PCA uses a Covariance Matrix
to understand relationships
between features.

Example Matrix:

      M   P   C

M    10   8   7
P     8  12   9
C     7   9  11
""")

# ----------------------------------------------------------
# Eigenvalues
# ----------------------------------------------------------

print("\nEigenvalues")
print("-" * 30)

print("""
Eigenvalues indicate the amount
of variance captured by a
Principal Component.

Higher Eigenvalue:

✓ More Important Component

Lower Eigenvalue:

✗ Less Important Component
""")

eigenvalues = [
    25.4,
    4.2,
    0.8
]

print("Eigenvalues =", eigenvalues)

# ----------------------------------------------------------
# Eigenvectors
# ----------------------------------------------------------

print("\nEigenvectors")
print("-" * 30)

print("""
Eigenvectors determine the
direction of Principal Components.

Together:

Eigenvalues → Importance

Eigenvectors → Direction
""")

eigenvector_1 = [0.58, 0.57, 0.58]

print("Example Eigenvector =",
      eigenvector_1)

# ----------------------------------------------------------
# Selecting Components
# ----------------------------------------------------------

print("\nSelecting Components")
print("-" * 30)

print("""
Suppose:

PC1 explains 85%
PC2 explains 12%
PC3 explains 3%

We may keep:

✓ PC1
✓ PC2

and discard PC3.
""")

# ----------------------------------------------------------
# Explained Variance
# ----------------------------------------------------------

print("\nExplained Variance")
print("-" * 30)

total_variance = (
    25.4 + 4.2 + 0.8
)

pc1_variance = (
    25.4 / total_variance
) * 100

print("PC1 Explained Variance =",
      round(pc1_variance, 2),
      "%")

# ----------------------------------------------------------
# 2D Visualization Example
# ----------------------------------------------------------

print("\nVisualization Example")
print("-" * 30)

print("""
Original Data:

Math
Physics
Chemistry

After PCA:

PC1
PC2

This allows easier
visualization of data.
""")

# ----------------------------------------------------------
# Image Compression
# ----------------------------------------------------------

print("\nImage Compression")
print("-" * 30)

print("""
PCA can reduce image size
while preserving important
visual information.

Applications:

✓ Face Recognition
✓ Image Compression
✓ Medical Imaging
""")

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Reduces Dimensions",
    "Removes Redundancy",
    "Speeds Up Training",
    "Improves Visualization",
    "Reduces Noise"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Loss of Information",
    "Reduced Interpretability",
    "Sensitive to Scaling",
    "Linear Technique"
]

for item in limitations:
    print("✗", item)

# ----------------------------------------------------------
# Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Data Compression",
    "Image Processing",
    "Face Recognition",
    "Finance",
    "Bioinformatics",
    "Machine Learning Preprocessing"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

features_before = 10
features_after = 3

print("Original Features =", features_before)
print("Reduced Features  =", features_after)

print("""
PCA reduced the number
of features significantly.
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

What does PCA stand for?

Answer:

Principal Component Analysis
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is PCA?

2. Why is PCA used?

3. What is a Principal Component?

4. What do Eigenvalues represent?

5. Give one application of PCA.
""")

print("""
Answers:

1. Dimensionality Reduction Technique
2. Reduce Features
3. New Feature Created by PCA
4. Amount of Variance Captured
5. Image Compression
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 52 Summary")
print("-" * 30)

print("""
1. PCA is a Dimensionality
   Reduction technique.

2. It reduces the number
   of features.

3. Principal Components capture
   maximum variance.

4. PCA uses:

   ✓ Covariance Matrix
   ✓ Eigenvalues
   ✓ Eigenvectors

5. It improves efficiency
   and visualization.

6. PCA is widely used in
   Machine Learning and
   Data Science.

7. It is one of the most important
   preprocessing techniques.
""")

print("\nDay 52 Completed Successfully!")
print("=" * 60)