# ==========================================================
# Day 46 : Support Vector Machines (SVM)
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 46")
print("=" * 60)

print("\nSupport Vector Machines (SVM)")
print("-" * 30)

print("""
Support Vector Machine (SVM) is a powerful
Supervised Machine Learning algorithm used
for both Classification and Regression.

It is especially effective for:

✓ Classification Problems
✓ High-Dimensional Data
✓ Text Classification
✓ Image Recognition

Main Goal:

Find the best boundary that separates
different classes.
""")

# ----------------------------------------------------------
# What is SVM?
# ----------------------------------------------------------

print("\nWhat is SVM?")
print("-" * 30)

print("""
SVM finds an optimal boundary
between classes.

This boundary is called a:

Hyperplane

The best hyperplane maximizes the
distance between classes.
""")

# ----------------------------------------------------------
# Simple Example
# ----------------------------------------------------------

print("\nSimple Example")
print("-" * 30)

print("""
Pass Class       |      Fail Class

      ●                  ○

      ●                  ○

      ●                  ○

------------------------------
        Hyperplane

The hyperplane separates
the two classes.
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nStudent Dataset")
print("-" * 30)

study_hours = [2, 3, 4, 8, 9, 10]

results = [
    "Fail",
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

for hour, result in zip(
        study_hours,
        results):

    print(hour, "Hours →", result)

# ----------------------------------------------------------
# Hyperplane
# ----------------------------------------------------------

print("\nHyperplane")
print("-" * 30)

print("""
A Hyperplane is a decision boundary.

In 2D:
A line

In 3D:
A plane

In Higher Dimensions:
A hyperplane

SVM searches for the best hyperplane.
""")

# ----------------------------------------------------------
# Support Vectors
# ----------------------------------------------------------

print("\nSupport Vectors")
print("-" * 30)

print("""
Support Vectors are the data points
closest to the hyperplane.

These points are extremely important.

They determine the position of the
decision boundary.
""")

support_vectors = [
    (4, "Fail"),
    (8, "Pass")
]

print("Example Support Vectors:")

for point in support_vectors:

    print(point)

# ----------------------------------------------------------
# Margin
# ----------------------------------------------------------

print("\nMargin")
print("-" * 30)

print("""
Margin is the distance between
the hyperplane and support vectors.

Larger Margin:

✓ Better Generalization
✓ Better Classification

SVM tries to maximize the margin.
""")

margin = 4

print("Example Margin =", margin)

# ----------------------------------------------------------
# Why Maximum Margin?
# ----------------------------------------------------------

print("\nMaximum Margin Principle")
print("-" * 30)

print("""
Among many possible boundaries,
SVM chooses the one with the
largest margin.

Reason:

✓ Better Performance
✓ Less Overfitting
✓ Better Generalization
""")

# ----------------------------------------------------------
# Linear SVM
# ----------------------------------------------------------

print("\nLinear SVM")
print("-" * 30)

print("""
Linear SVM is used when
classes can be separated
using a straight line.

Example:

Pass and Fail students
separated by study hours.
""")

# ----------------------------------------------------------
# Non-Linear Data
# ----------------------------------------------------------

print("\nNon-Linear Data")
print("-" * 30)

print("""
Sometimes classes cannot be
separated using a straight line.

In such cases:

SVM uses Kernel Functions.
""")

# ----------------------------------------------------------
# Kernel Trick
# ----------------------------------------------------------

print("\nKernel Trick")
print("-" * 30)

print("""
Kernel Functions transform data
into higher dimensions where
separation becomes easier.

Popular Kernels:

✓ Linear Kernel
✓ Polynomial Kernel
✓ RBF Kernel
✓ Sigmoid Kernel
""")

# ----------------------------------------------------------
# Linear Kernel
# ----------------------------------------------------------

print("\nLinear Kernel")
print("-" * 30)

print("""
Used when data is linearly separable.

Advantages:

✓ Fast
✓ Simple
✓ Efficient
""")

# ----------------------------------------------------------
# Polynomial Kernel
# ----------------------------------------------------------

print("\nPolynomial Kernel")
print("-" * 30)

print("""
Used when relationships
are more complex.

Can create curved decision boundaries.
""")

# ----------------------------------------------------------
# RBF Kernel
# ----------------------------------------------------------

print("\nRBF Kernel")
print("-" * 30)

print("""
RBF = Radial Basis Function

Most commonly used kernel.

Advantages:

✓ Handles Complex Patterns
✓ High Accuracy
""")

# ----------------------------------------------------------
# Classification Example
# ----------------------------------------------------------

print("\nClassification Example")
print("-" * 30)

attendance = 90

if attendance >= 75:

    prediction = "Pass"

else:

    prediction = "Fail"

print("Attendance =", attendance)
print("Prediction =", prediction)

# ----------------------------------------------------------
# Regression with SVM
# ----------------------------------------------------------

print("\nSupport Vector Regression (SVR)")
print("-" * 30)

print("""
SVM can also be used for Regression.

This version is called:

SVR

Applications:

✓ House Price Prediction
✓ Sales Forecasting
✓ Demand Prediction
""")

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Effective in High Dimensions",
    "Works Well with Small Data",
    "Powerful Classification",
    "Flexible with Kernels",
    "Good Generalization"
]

for item in advantages:

    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Slow on Large Datasets",
    "Kernel Selection Can Be Difficult",
    "Less Interpretable",
    "Higher Computational Cost"
]

for item in limitations:

    print("✗", item)

# ----------------------------------------------------------
# Real World Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Image Recognition",
    "Face Detection",
    "Spam Detection",
    "Medical Diagnosis",
    "Text Classification",
    "Handwriting Recognition"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Machine Learning Workflow
# ----------------------------------------------------------

print("\nSVM Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Preprocess Data",
    "Select Kernel",
    "Train SVM",
    "Find Hyperplane",
    "Evaluate Model",
    "Make Predictions"
]

for i, step in enumerate(
        steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

marks = 82

if marks >= 50:

    result = "Pass"

else:

    result = "Fail"

print("Marks =", marks)
print("Prediction =", result)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

support_vector_count = 2

print("""
Question:

What are Support Vectors?

Answer:

Data points closest to
the hyperplane.
""")

print("Support Vectors =",
      support_vector_count)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What does SVM stand for?

2. What is a Hyperplane?

3. What are Support Vectors?

4. What is a Kernel?

5. Give one application of SVM.
""")

print("""
Answers:

1. Support Vector Machine
2. Decision Boundary
3. Closest points to boundary
4. Function used for
   higher-dimensional mapping
5. Image Recognition
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 46 Summary")
print("-" * 30)

print("""
1. SVM is a powerful Supervised
   Learning algorithm.

2. It is mainly used for
   Classification tasks.

3. SVM finds the optimal hyperplane.

4. Support Vectors determine
   the decision boundary.

5. SVM maximizes the margin.

6. Kernels help handle
   non-linear data.

7. SVM is widely used in
   image processing,
   text classification,
   and medical diagnosis.
""")

print("\nDay 46 Completed Successfully!")
print("=" * 60)