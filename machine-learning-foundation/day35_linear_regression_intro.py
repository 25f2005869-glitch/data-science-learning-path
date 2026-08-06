# ==========================================================
# Day 35 : Linear Regression Introduction
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 35")
print("=" * 60)

print("\nIntroduction to Linear Regression")
print("-" * 30)

print("""
Linear Regression is one of the simplest
and most important Machine Learning algorithms.

It is used to predict continuous numerical values.

Examples:

✓ House Price Prediction
✓ Salary Prediction
✓ Sales Forecasting
✓ Temperature Prediction
✓ Demand Forecasting

Linear Regression finds a relationship
between input variables and output variables.
""")

# ----------------------------------------------------------
# What is Linear Regression?
# ----------------------------------------------------------

print("\nWhat is Linear Regression?")
print("-" * 30)

print("""
Linear Regression fits a straight line
through data points.

The objective is to predict future values.

Relationship:

Input (X) → Output (Y)

Example:

Study Hours → Marks
Experience → Salary
Area → House Price
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
# Linear Regression Equation
# ----------------------------------------------------------

print("\nLinear Regression Equation")
print("-" * 30)

print("""
Equation:

Y = mX + b

Where:

Y = Predicted Value
X = Input Feature
m = Slope
b = Intercept
""")

# ----------------------------------------------------------
# Understanding Slope
# ----------------------------------------------------------

print("\nUnderstanding Slope")
print("-" * 30)

x1 = 2
y1 = 40

x2 = 10
y2 = 95

slope = (y2 - y1) / (x2 - x1)

print("Slope =", round(slope, 2))

print("""
Slope indicates how much Y changes
when X increases by one unit.
""")

# ----------------------------------------------------------
# Calculating Intercept
# ----------------------------------------------------------

print("\nCalculating Intercept")
print("-" * 30)

intercept = y1 - (slope * x1)

print("Intercept =", round(intercept, 2))

# ----------------------------------------------------------
# Regression Equation
# ----------------------------------------------------------

print("\nRegression Equation")
print("-" * 30)

print(
    "Predicted Marks =",
    round(slope, 2),
    "* Study Hours +",
    round(intercept, 2)
)

# ----------------------------------------------------------
# Making Predictions
# ----------------------------------------------------------

print("\nMaking Predictions")
print("-" * 30)

new_hours = 7

predicted_marks = (
    slope * new_hours +
    intercept
)

print("Study Hours =", new_hours)
print("Predicted Marks =",
      round(predicted_marks, 2))

# ----------------------------------------------------------
# Actual vs Predicted
# ----------------------------------------------------------

print("\nActual vs Predicted")
print("-" * 30)

actual_marks = [40, 50, 65, 80, 95]

predicted_values = []

for hour in study_hours:

    prediction = (
        slope * hour +
        intercept
    )

    predicted_values.append(
        round(prediction, 2)
    )

print("Actual Marks    =", actual_marks)
print("Predicted Marks =", predicted_values)

# ----------------------------------------------------------
# Error Calculation
# ----------------------------------------------------------

print("\nPrediction Error")
print("-" * 30)

errors = []

for actual, predicted in zip(
        actual_marks,
        predicted_values):

    error = actual - predicted

    errors.append(
        round(error, 2)
    )

print("Errors =", errors)

# ----------------------------------------------------------
# Why Linear Regression?
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Simple to Understand",
    "Easy to Implement",
    "Fast Training",
    "Interpretable Results",
    "Good Baseline Model"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Assumptions
# ----------------------------------------------------------

print("\nAssumptions")
print("-" * 30)

print("""
Linear Regression assumes:

✓ Linear Relationship
✓ Independent Observations
✓ Constant Variance
✓ Minimal Outliers
""")

# ----------------------------------------------------------
# Real World Example
# ----------------------------------------------------------

print("\nSalary Prediction Example")
print("-" * 30)

experience = [1, 2, 3, 4, 5]
salary = [
    25000,
    30000,
    40000,
    50000,
    60000
]

print("Experience =", experience)
print("Salary     =", salary)

print("""
Goal:

Predict Salary from Experience
using Linear Regression.
""")

# ----------------------------------------------------------
# House Price Prediction Example
# ----------------------------------------------------------

print("\nHouse Price Prediction")
print("-" * 30)

house_area = [
    1000,
    1200,
    1500,
    1800
]

house_price = [
    20,
    25,
    35,
    45
]

print("Area  =", house_area)
print("Price =", house_price)

print("""
Goal:

Predict house prices
from house area.
""")

# ----------------------------------------------------------
# Machine Learning Workflow
# ----------------------------------------------------------

print("\nLinear Regression Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Preprocess Data",
    "Train Model",
    "Find Best Fit Line",
    "Make Predictions",
    "Evaluate Model"
]

for i, step in enumerate(steps, start=1):
    print(f"{i}. {step}")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

x = 5
m = 10
b = 20

y = (m * x) + b

print("Y =", y)

print("""
Question:

If X = 5,
m = 10,
b = 20

Find Y.

Answer = 70
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Linear Regression?

2. What type of output does it predict?

3. What is the equation of a line?

4. What does slope represent?

5. Give one real-world application.
""")

print("""
Answers:

1. A supervised learning algorithm
2. Continuous numerical values
3. Y = mX + b
4. Rate of change
5. House Price Prediction
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 35 Summary")
print("-" * 30)

print("""
1. Linear Regression predicts
   continuous values.

2. It is a supervised learning algorithm.

3. It models relationships using:

   Y = mX + b

4. m represents slope.

5. b represents intercept.

6. It is widely used for prediction
   and forecasting problems.

7. Linear Regression is one of the
   most important ML algorithms.
""")

print("\nDay 35 Completed Successfully!")
print("=" * 60)