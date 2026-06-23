# ==========================================================
# Day 07 : Vectors for Machine Learning
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 07")
print("=" * 60)

print("\nVectors for Machine Learning")
print("-" * 30)

print("""
A Vector is an ordered collection of numbers.

Vectors are used to represent data in Machine Learning.

Examples:
✓ Student Marks
✓ House Features
✓ Customer Information
✓ Image Pixels
""")

# ----------------------------------------------------------
# Creating a Vector
# ----------------------------------------------------------

print("\nCreating a Vector")
print("-" * 30)

vector = [2, 4, 6, 8]

print("Vector =", vector)

# ----------------------------------------------------------
# Vector Representation
# ----------------------------------------------------------

print("\nVector Representation")
print("-" * 30)

print("""
A vector can be written as:

v = [2, 4, 6, 8]

Dimension = Number of Elements

Here,
Dimension = 4
""")

dimension = len(vector)

print("Dimension of Vector =", dimension)

# ----------------------------------------------------------
# Feature Vector Example
# ----------------------------------------------------------

print("\nFeature Vector Example")
print("-" * 30)

print("""
Suppose we want to represent a student.

Features:
Age = 18
Study Hours = 6
Attendance = 90

Vector:
[18, 6, 90]
""")

student_vector = [18, 6, 90]

print("Student Feature Vector =", student_vector)

# ----------------------------------------------------------
# Vector Addition
# ----------------------------------------------------------

print("\nVector Addition")
print("-" * 30)

A = [1, 2, 3]
B = [4, 5, 6]

C = []

for a, b in zip(A, B):
    C.append(a + b)

print("Vector A =", A)
print("Vector B =", B)
print("A + B =", C)

# ----------------------------------------------------------
# Vector Subtraction
# ----------------------------------------------------------

print("\nVector Subtraction")
print("-" * 30)

D = []

for a, b in zip(A, B):
    D.append(a - b)

print("A - B =", D)

# ----------------------------------------------------------
# Scalar Multiplication
# ----------------------------------------------------------

print("\nScalar Multiplication")
print("-" * 30)

scalar = 3

result = []

for value in A:
    result.append(scalar * value)

print("Vector A =", A)
print("Scalar =", scalar)
print("Result =", result)

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

||v|| = √(x² + y²)
""")

# ----------------------------------------------------------
# Dot Product
# ----------------------------------------------------------

print("\nDot Product")
print("-" * 30)

A = [1, 2, 3]
B = [4, 5, 6]

dot_product = 0

for a, b in zip(A, B):
    dot_product += a * b

print("Vector A =", A)
print("Vector B =", B)
print("Dot Product =", dot_product)

print("""
Formula:

A · B = Σ(ai × bi)
""")

# ----------------------------------------------------------
# Why Vectors Matter in ML
# ----------------------------------------------------------

print("\nWhy Vectors Matter in Machine Learning")
print("-" * 30)

print("""
Machine Learning algorithms work with vectors.

Examples:

Student Data:
[Age, Study Hours, Attendance]

House Data:
[Area, Bedrooms, Bathrooms]

Customer Data:
[Income, Spending Score, Age]

Images:
Thousands of pixel values stored as vectors.
""")

# ----------------------------------------------------------
# Real ML Dataset Example
# ----------------------------------------------------------

print("\nReal Dataset Example")
print("-" * 30)

student1 = [18, 6, 90]
student2 = [19, 8, 95]
student3 = [18, 4, 80]

print("Student 1 =", student1)
print("Student 2 =", student2)
print("Student 3 =", student3)

print("""
Each row is a feature vector.

Rows  -> Observations
Columns -> Features
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Vector?
2. What is the dimension of [5, 10, 15]?
3. What is a Dot Product?
4. Why are vectors important in ML?
""")

print("""
Answers:
1. Ordered collection of numbers
2. 3
3. Sum of element-wise multiplication
4. Data is represented using vectors
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 07 Summary")
print("-" * 30)

print("""
1. A vector is an ordered collection of numbers.
2. Vectors represent features in ML.
3. Dimension = Number of elements.
4. Common operations:
   ✓ Addition
   ✓ Subtraction
   ✓ Scalar Multiplication
   ✓ Dot Product
5. Almost all ML algorithms use vectors internally.
""")

print("\nDay 07 Completed Successfully!")
print("=" * 60)