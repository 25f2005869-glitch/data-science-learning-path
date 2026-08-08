# ==========================================================
# Day 37 : Gradient Descent Introduction
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 37")
print("=" * 60)

print("\nGradient Descent Introduction")
print("-" * 30)

print("""
Gradient Descent is one of the most
important optimization algorithms in
Machine Learning.

Its purpose is to minimize the
Cost Function and find the best values
for model parameters.

Applications:

✓ Linear Regression
✓ Logistic Regression
✓ Neural Networks
✓ Deep Learning
✓ Artificial Intelligence
""")

# ----------------------------------------------------------
# Why Gradient Descent?
# ----------------------------------------------------------

print("\nWhy Gradient Descent?")
print("-" * 30)

print("""
In Linear Regression, many possible
lines can fit the data.

We need a method to find the line
with the minimum cost.

Gradient Descent helps us:

✓ Reduce Error
✓ Minimize Cost Function
✓ Improve Predictions
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]

print("Study Hours =", study_hours)
print("Marks       =", marks)

# ----------------------------------------------------------
# Initial Parameters
# ----------------------------------------------------------

print("\nInitial Parameters")
print("-" * 30)

m = 1
b = 0

print("Initial Slope (m)     =", m)
print("Initial Intercept (b) =", b)

print("""
These values are usually random
at the beginning.
""")

# ----------------------------------------------------------
# Prediction Function
# ----------------------------------------------------------

print("\nPrediction Function")
print("-" * 30)

predictions = []

for x in study_hours:

    y_pred = (m * x) + b

    predictions.append(y_pred)

print("Predictions =", predictions)

# ----------------------------------------------------------
# Calculate Errors
# ----------------------------------------------------------

print("\nPrediction Errors")
print("-" * 30)

errors = []

for actual, predicted in zip(
        marks,
        predictions):

    error = actual - predicted

    errors.append(error)

print("Errors =", errors)

# ----------------------------------------------------------
# Cost Function
# ----------------------------------------------------------

print("\nCost Function (MSE)")
print("-" * 30)

squared_errors = []

for error in errors:

    squared_errors.append(
        error ** 2
    )

mse = (
    sum(squared_errors) /
    len(squared_errors)
)

print("MSE =", round(mse, 2))

print("""
A large MSE indicates that
our model is performing poorly.
""")

# ----------------------------------------------------------
# Gradient Descent Concept
# ----------------------------------------------------------

print("\nGradient Descent Concept")
print("-" * 30)

print("""
Imagine standing on top of a hill.

Goal:

Reach the lowest point.

Gradient Descent repeatedly takes
small steps downhill until the
minimum cost is reached.

High Cost
     ↓
Lower Cost
     ↓
Minimum Cost
""")

# ----------------------------------------------------------
# Learning Rate
# ----------------------------------------------------------

print("\nLearning Rate")
print("-" * 30)

learning_rate = 0.01

print("Learning Rate =", learning_rate)

print("""
Learning Rate controls the
size of each step.

Small Learning Rate:
✓ Slow Learning

Large Learning Rate:
✓ Fast Learning
✗ May overshoot minimum
""")

# ----------------------------------------------------------
# Parameter Update Concept
# ----------------------------------------------------------

print("\nParameter Updates")
print("-" * 30)

print("""
Gradient Descent updates:

m = m - LearningRate × Gradient

b = b - LearningRate × Gradient

After every update:

✓ Cost decreases
✓ Predictions improve
""")

# ----------------------------------------------------------
# Simulated Update
# ----------------------------------------------------------

print("\nSimulated Parameter Update")
print("-" * 30)

gradient_m = 5
gradient_b = 2

new_m = (
    m -
    learning_rate * gradient_m
)

new_b = (
    b -
    learning_rate * gradient_b
)

print("Old m =", m)
print("New m =", round(new_m, 4))

print("Old b =", b)
print("New b =", round(new_b, 4))

# ----------------------------------------------------------
# Iterations
# ----------------------------------------------------------

print("\nIterations")
print("-" * 30)

print("""
Gradient Descent runs repeatedly.

Iteration 1
Iteration 2
Iteration 3
...
Iteration N

Until Cost becomes very small.
""")

for iteration in range(1, 6):

    cost = 100 / iteration

    print(
        "Iteration",
        iteration,
        "Cost =",
        round(cost, 2)
    )

# ----------------------------------------------------------
# Types of Gradient Descent
# ----------------------------------------------------------

print("\nTypes of Gradient Descent")
print("-" * 30)

types = [
    "Batch Gradient Descent",
    "Stochastic Gradient Descent",
    "Mini-Batch Gradient Descent"
]

for item in types:
    print("✓", item)

# ----------------------------------------------------------
# Batch Gradient Descent
# ----------------------------------------------------------

print("\nBatch Gradient Descent")
print("-" * 30)

print("""
Uses the entire dataset
for each update.

Advantages:

✓ Stable Updates

Disadvantages:

✗ Slow on large datasets
""")

# ----------------------------------------------------------
# Stochastic Gradient Descent
# ----------------------------------------------------------

print("\nStochastic Gradient Descent")
print("-" * 30)

print("""
Uses one training example
at a time.

Advantages:

✓ Fast Updates

Disadvantages:

✗ More Noise
""")

# ----------------------------------------------------------
# Mini-Batch Gradient Descent
# ----------------------------------------------------------

print("\nMini-Batch Gradient Descent")
print("-" * 30)

print("""
Uses a small group of records.

Advantages:

✓ Faster
✓ Stable
✓ Most Common in Practice
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nGradient Descent in ML")
print("-" * 30)

applications = [
    "Linear Regression",
    "Logistic Regression",
    "Neural Networks",
    "Deep Learning",
    "Computer Vision",
    "Natural Language Processing"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

cost_values = [
    500,
    300,
    180,
    100,
    60,
    35
]

print("Cost Reduction During Training:")

for cost in cost_values:
    print(cost)

print("""
Cost decreases after each update.

This indicates learning.
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

learning_rate = 0.1
parameter = 10
gradient = 4

updated_parameter = (
    parameter -
    learning_rate * gradient
)

print("Updated Parameter =",
      updated_parameter)

print("""
Question:

Parameter = 10
Gradient = 4
Learning Rate = 0.1

New Parameter = 9.6
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Gradient Descent?

2. Why is it used?

3. What is Learning Rate?

4. What happens if Learning Rate
   is too large?

5. Name three types of
   Gradient Descent.
""")

print("""
Answers:

1. Optimization algorithm
2. To minimize cost
3. Step size during updates
4. It may overshoot the minimum
5. Batch, Stochastic,
   Mini-Batch
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 37 Summary")
print("-" * 30)

print("""
1. Gradient Descent minimizes
   the Cost Function.

2. It improves model parameters
   step by step.

3. Learning Rate controls
   update size.

4. Lower Cost means
   better predictions.

5. Gradient Descent is the
   foundation of modern
   Machine Learning and
   Deep Learning.

6. Most ML algorithms use
   some form of optimization.
""")

print("\nDay 37 Completed Successfully!")
print("=" * 60)