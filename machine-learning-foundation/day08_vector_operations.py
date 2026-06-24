# ==========================================================
# Day 08 : Vector Operations
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 08")
print("=" * 60)

print("\nVector Operations")
print("-" * 30)

print("""
Vector operations are fundamental in
Machine Learning because data is usually
represented as vectors.

Common Operations:
✓ Addition
✓ Subtraction
✓ Scalar Multiplication
✓ Dot Product
✓ Magnitude
✓ Distance Calculation
""")

# ----------------------------------------------------------
# Vector Creation
# ----------------------------------------------------------

print("\nCreating Vectors")
print("-" * 30)

A = [2, 4, 6]
B = [1, 3, 5]

print("Vector A =", A)
print("Vector B =", B)

# ----------------------------------------------------------
# Vector Addition
# ----------------------------------------------------------

print("\nVector Addition")
print("-" * 30)

addition = []

for a, b in zip(A, B):
    addition.append(a + b)

print("A + B =", addition)

# ----------------------------------------------------------
# Vector Subtraction
# ----------------------------------------------------------

print("\nVector Subtraction")
print("-" * 30)

subtraction = []

for a, b in zip(A, B):
    subtraction.append(a - b)

print("A - B =", subtraction)

# ----------------------------------------------------------
# Scalar Multiplication
# ----------------------------------------------------------

print("\nScalar Multiplication")
print("-" * 30)

scalar = 3

scalar_result = []

for value in A:
    scalar_result.append(value * scalar)

print("Scalar =", scalar)
print("3 × A =", scalar_result)

# ----------------------------------------------------------
# Dot Product
# ----------------------------------------------------------

print("\nDot Product")
print("-" * 30)

dot_product = 0

for a, b in zip(A, B):
    dot_product += a * b

print("A =", A)
print("B =", B)
print("Dot Product =", dot_product)

print("""
Formula:

A · B = Σ(ai × bi)
""")

# ----------------------------------------------------------
# Vector Magnitude
# ----------------------------------------------------------

print("\nVector Magnitude")
print("-" * 30)

vector = [3, 4]

magnitude = (vector[0]**2 + vector[1]**2) ** 0.5

print("Vector =", vector)
print("Magnitude =", magnitude)

print("""
Formula:

||V|| = √(x² + y²)
""")

# ----------------------------------------------------------
# Euclidean Distance
# ----------------------------------------------------------

print("\nEuclidean Distance")
print("-" * 30)

point1 = [2, 3]
point2 = [5, 7]

distance = (
    (point2[0] - point1[0])**2 +
    (point2[1] - point1[1])**2
) ** 0.5

print("Point 1 =", point1)
print("Point 2 =", point2)
print("Distance =", round(distance, 2))

print("""
Distance measures similarity between points.

Smaller Distance → More Similar
Larger Distance  → Less Similar
""")

# ----------------------------------------------------------
# Cosine Similarity Concept
# ----------------------------------------------------------

print("\nCosine Similarity Concept")
print("-" * 30)

print("""
Cosine Similarity measures the angle
between two vectors.

Applications:
✓ Recommendation Systems
✓ Search Engines
✓ Text Analysis
✓ NLP
""")

# ----------------------------------------------------------
# Feature Vector Example
# ----------------------------------------------------------

print("\nFeature Vector Example")
print("-" * 30)

student1 = [18, 6, 90]
student2 = [19, 8, 95]
student3 = [17, 5, 85]

print("Student 1 =", student1)
print("Student 2 =", student2)
print("Student 3 =", student3)

print("""
Features:
[Age, Study Hours, Attendance]

Each student is represented as a vector.
""")

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nVector Operations in ML")
print("-" * 30)

applications = [
    "Linear Regression",
    "Logistic Regression",
    "Neural Networks",
    "Recommendation Systems",
    "Computer Vision",
    "Natural Language Processing"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

X = [4, 8]
Y = [1, 2]

practice_dot = 0

for x, y in zip(X, Y):
    practice_dot += x * y

print("Vector X =", X)
print("Vector Y =", Y)
print("Dot Product =", practice_dot)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Dot Product?
2. What is Vector Magnitude?
3. What does Euclidean Distance measure?
4. Why are vectors important in ML?
""")

print("""
Answers:
1. Sum of element-wise multiplication
2. Length of a vector
3. Distance between two points
4. ML data is represented using vectors
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 08 Summary")
print("-" * 30)

print("""
1. Vector Addition combines vectors.
2. Vector Subtraction finds differences.
3. Scalar Multiplication scales vectors.
4. Dot Product measures vector interaction.
5. Magnitude represents vector length.
6. Euclidean Distance measures similarity.
7. Vector operations are used throughout ML.
""")

print("\nDay 08 Completed Successfully!")
print("=" * 60)