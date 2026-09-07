# ==========================================================
# Day 57 : Regularization (L1 & L2)
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 57")
print("=" * 60)

print("\nRegularization (L1 & L2)")
print("-" * 30)

print("""
Regularization is a technique used to
reduce Overfitting in Machine Learning.

Goal:

✓ Improve Generalization
✓ Reduce Model Complexity
✓ Prevent Overfitting
✓ Improve Performance on New Data

Regularization adds a penalty
to the model's cost function.
""")

# ----------------------------------------------------------
# Why Regularization?
# ----------------------------------------------------------

print("\nWhy Regularization?")
print("-" * 30)

print("""
Complex models may memorize
training data.

This causes:

✗ Overfitting
✗ Poor Generalization

Regularization discourages
very large model coefficients.
""")

# ----------------------------------------------------------
# Example of Overfitting
# ----------------------------------------------------------

print("\nOverfitting Example")
print("-" * 30)

training_accuracy = 99
testing_accuracy = 72

print("Training Accuracy =", training_accuracy, "%")
print("Testing Accuracy  =", testing_accuracy, "%")

print("""
Large gap between training and
testing performance indicates
possible overfitting.
""")

# ----------------------------------------------------------
# Regression Equation
# ----------------------------------------------------------

print("\nLinear Regression Equation")
print("-" * 30)

print("""
y = b0 + b1x1 + b2x2 + ...

Where:

b0 = Intercept
b1, b2 = Coefficients

Regularization penalizes
large coefficient values.
""")

# ----------------------------------------------------------
# What is Regularization?
# ----------------------------------------------------------

print("\nWhat is Regularization?")
print("-" * 30)

print("""
Regularization modifies the
original cost function.

New Cost Function:

Cost =
Original Error
+
Penalty Term

Penalty controls
model complexity.
""")

# ----------------------------------------------------------
# Types of Regularization
# ----------------------------------------------------------

print("\nTypes of Regularization")
print("-" * 30)

types = [
    "L1 Regularization (Lasso)",
    "L2 Regularization (Ridge)"
]

for item in types:
    print("✓", item)

# ----------------------------------------------------------
# L1 Regularization
# ----------------------------------------------------------

print("\nL1 Regularization (Lasso)")
print("-" * 30)

print("""
L1 adds the absolute values
of coefficients as a penalty.

Formula:

Penalty =
|b1| + |b2| + |b3| + ...

L1 can force some coefficients
to become exactly zero.
""")

# Example

coefficients = [10, 5, 0, 2]

print("Coefficients =", coefficients)

l1_penalty = 0

for coefficient in coefficients:

    l1_penalty += abs(coefficient)

print("L1 Penalty =", l1_penalty)

# ----------------------------------------------------------
# Feature Selection
# ----------------------------------------------------------

print("\nFeature Selection with L1")
print("-" * 30)

print("""
L1 Regularization can remove
unimportant features.

Example:

Feature A = 10
Feature B = 0
Feature C = 5

Feature B may be removed.

This makes the model simpler.
""")

# ----------------------------------------------------------
# L2 Regularization
# ----------------------------------------------------------

print("\nL2 Regularization (Ridge)")
print("-" * 30)

print("""
L2 adds squared coefficient values
as a penalty.

Formula:

Penalty =
b1² + b2² + b3² + ...

L2 reduces coefficient sizes
but usually does not make
them exactly zero.
""")

# Example

coefficients = [10, 5, 2]

l2_penalty = 0

for coefficient in coefficients:

    l2_penalty += coefficient ** 2

print("Coefficients =", coefficients)
print("L2 Penalty =", l2_penalty)

# ----------------------------------------------------------
# L1 vs L2
# ----------------------------------------------------------

print("\nL1 vs L2")
print("-" * 30)

print("""
L1 Regularization:

✓ Feature Selection
✓ Sparse Models
✓ Some Coefficients Become Zero

L2 Regularization:

✓ Shrinks Coefficients
✓ Keeps All Features
✓ Stable Solutions
""")

# ----------------------------------------------------------
# Lambda Parameter
# ----------------------------------------------------------

print("\nLambda (λ)")
print("-" * 30)

print("""
Lambda controls the strength
of regularization.

Small Lambda:

✓ Less Penalty

Large Lambda:

✓ More Penalty

Choosing the right value
is important.
""")

lambda_value = 0.1

print("Lambda =", lambda_value)

# ----------------------------------------------------------
# Cost Function with L1
# ----------------------------------------------------------

print("\nL1 Cost Function")
print("-" * 30)

print("""
Cost Function:

Error
+
λ × Σ|Coefficient|

This encourages sparse models.
""")

# ----------------------------------------------------------
# Cost Function with L2
# ----------------------------------------------------------

print("\nL2 Cost Function")
print("-" * 30)

print("""
Cost Function:

Error
+
λ × Σ(Coefficient²)

This discourages large
coefficient values.
""")

# ----------------------------------------------------------
# Practical Coefficient Example
# ----------------------------------------------------------

print("\nCoefficient Shrinkage")
print("-" * 30)

original_coefficients = [
    15,
    12,
    8,
    5
]

regularized_coefficients = [
    10,
    8,
    5,
    3
]

print("Original Coefficients =",
      original_coefficients)

print("Regularized Coefficients =",
      regularized_coefficients)

# ----------------------------------------------------------
# Advantages of Regularization
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Reduces Overfitting",
    "Improves Generalization",
    "Controls Complexity",
    "Better Predictions",
    "Feature Selection (L1)"
]

for item in advantages:

    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Requires Parameter Tuning",
    "May Cause Underfitting",
    "Extra Computation",
    "Lambda Selection Required"
]

for item in limitations:

    print("✗", item)

# ----------------------------------------------------------
# Real-World Example
# ----------------------------------------------------------

print("\nHouse Price Prediction")
print("-" * 30)

print("""
Features:

✓ Area
✓ Bedrooms
✓ Location
✓ Age
✓ Parking

Regularization helps identify
the most useful features and
reduces overfitting.
""")

# ----------------------------------------------------------
# Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Linear Regression",
    "Logistic Regression",
    "Finance",
    "Healthcare",
    "Marketing Analytics",
    "Machine Learning Models"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nRegularization Workflow")
print("-" * 30)

steps = [
    "Train Model",
    "Detect Overfitting",
    "Apply Regularization",
    "Tune Lambda",
    "Evaluate Model",
    "Deploy Model"
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

coefficients = [12, 9, 6]

print("Before Regularization =",
      coefficients)

new_coefficients = [
    8,
    6,
    4
]

print("After Regularization =",
      new_coefficients)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

Which regularization method
can set coefficients to zero?

Answer:

L1 Regularization (Lasso)
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Regularization?

2. Why is Regularization used?

3. What is L1 Regularization?

4. What is L2 Regularization?

5. Which technique performs
   feature selection?
""")

print("""
Answers:

1. Overfitting reduction technique
2. Improve generalization
3. Lasso Regularization
4. Ridge Regularization
5. L1 Regularization
""")

# ----------------------------------------------------------
# Summary
#