# ==========================================================
# Day 36 : Best Fit Line and Cost Function
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 36")
print("=" * 60)

print("\nBest Fit Line and Cost Function")
print("-" * 30)

print("""
In Linear Regression, the goal is to find
the Best Fit Line that represents the
relationship between input and output data.

A Best Fit Line minimizes prediction errors.

To measure these errors, we use a
Cost Function.
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
actual_marks = [40, 50, 65, 80, 95]

print("Study Hours =", study_hours)
print("Actual Marks =", actual_marks)

# ----------------------------------------------------------
# Linear Regression Equation
# ----------------------------------------------------------

print("\nLinear Regression Equation")
print("-" * 30)

print("""
The Best Fit Line follows:

Y = mX + b

Where:

Y = Predicted Output
X = Input Feature
m = Slope
b = Intercept
""")

# ----------------------------------------------------------
# Example Best Fit Line
# ----------------------------------------------------------

print("\nExample Best Fit Line")
print("-" * 30)

m = 6.875
b = 26.25

print("Slope (m)     =", m)
print("Intercept (b) =", b)

print("Equation:")
print("Y =", m, "* X +", b)

# ----------------------------------------------------------
# Predictions
# ----------------------------------------------------------

print("\nPredicted Values")
print("-" * 30)

predicted_marks = []

for hour in study_hours:

    prediction = (
        m * hour +
        b
    )

    predicted_marks.append(
        round(prediction, 2)
    )

print("Predicted Marks =", predicted_marks)

# ----------------------------------------------------------
# Actual vs Predicted
# ----------------------------------------------------------

print("\nActual vs Predicted")
print("-" * 30)

for actual, predicted in zip(
        actual_marks,
        predicted_marks):

    print(
        "Actual =",
        actual,
        "| Predicted =",
        predicted
    )

# ----------------------------------------------------------
# Error Calculation
# ----------------------------------------------------------

print("\nPrediction Errors")
print("-" * 30)

errors = []

for actual, predicted in zip(
        actual_marks,
        predicted_marks):

    error = actual - predicted

    errors.append(
        round(error, 2)
    )

print("Errors =", errors)

# ----------------------------------------------------------
# Why Errors Matter
# ----------------------------------------------------------

print("\nWhy Errors Matter?")
print("-" * 30)

print("""
A good regression line should
produce small prediction errors.

Smaller Error
→ Better Model

Larger Error
→ Poor Model
""")

# ----------------------------------------------------------
# Cost Function
# ----------------------------------------------------------

print("\nCost Function")
print("-" * 30)

print("""
A Cost Function measures
how wrong the predictions are.

The most common cost function
for Linear Regression is:

Mean Squared Error (MSE)
""")

# ----------------------------------------------------------
# Squared Errors
# ----------------------------------------------------------

print("\nSquared Errors")
print("-" * 30)

squared_errors = []

for error in errors:

    squared_error = error ** 2

    squared_errors.append(
        round(squared_error, 2)
    )

print("Squared Errors =", squared_errors)

# ----------------------------------------------------------
# Mean Squared Error
# ----------------------------------------------------------

print("\nMean Squared Error (MSE)")
print("-" * 30)

mse = (
    sum(squared_errors) /
    len(squared_errors)
)

print("MSE =", round(mse, 2))

print("""
Formula:

MSE =
Σ(Actual - Predicted)^2
-----------------------
Number of Observations
""")

# ----------------------------------------------------------
# Good vs Bad Model
# ----------------------------------------------------------

print("\nGood Model vs Bad Model")
print("-" * 30)

good_model_mse = 12
bad_model_mse = 150

print("Good Model MSE =", good_model_mse)
print("Bad Model MSE  =", bad_model_mse)

print("""
Lower MSE is better.

The objective is to minimize
the cost function.
""")

# ----------------------------------------------------------
# Best Fit Line Concept
# ----------------------------------------------------------

print("\nBest Fit Line")
print("-" * 30)

print("""
Many possible lines can fit the data.

The Best Fit Line is the line
with the lowest cost.

Goal:

Minimum Cost Function
→ Best Fit Line
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nBest Fit Line in ML")
print("-" * 30)

applications = [
    "Linear Regression",
    "House Price Prediction",
    "Sales Forecasting",
    "Demand Prediction",
    "Salary Prediction",
    "Trend Analysis"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# House Price Example
# ----------------------------------------------------------

print("\nHouse Price Prediction")
print("-" * 30)

house_area = [1000, 1200, 1500, 1800]
house_price = [20, 25, 35, 45]

print("Area  =", house_area)
print("Price =", house_price)

print("""
Linear Regression tries to find
the Best Fit Line connecting
area and house price.
""")

# ----------------------------------------------------------
# Sales Forecast Example
# ----------------------------------------------------------

print("\nSales Forecast Example")
print("-" * 30)

advertising = [10, 20, 30, 40, 50]
sales = [100, 150, 200, 250, 300]

print("Advertising =", advertising)
print("Sales       =", sales)

print("""
Best Fit Line can predict
future sales from advertising budget.
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

hours = 7

predicted_score = (
    m * hours +
    b
)

print("Study Hours =", hours)
print("Predicted Score =",
      round(predicted_score, 2))

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

actual = 80
predicted = 75

error = actual - predicted

squared_error = error ** 2

print("Error =", error)
print("Squared Error =", squared_error)

print("""
Question:

Actual = 80
Predicted = 75

Find Squared Error.

Answer = 25
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Best Fit Line?

2. What is a Cost Function?

3. What does MSE stand for?

4. Why do we square errors?

5. What is the goal of
   Linear Regression?
""")

print("""
Answers:

1. Line with minimum prediction error
2. Measure of model error
3. Mean Squared Error
4. To penalize large mistakes
5. Find the Best Fit Line
   with minimum cost
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 36 Summary")
print("-" * 30)

print("""
1. Linear Regression finds
   the Best Fit Line.

2. The line follows:

   Y = mX + b

3. Prediction errors measure
   model performance.

4. Cost Function quantifies errors.

5. MSE is the most common
   cost function.

6. Lower Cost Function values
   indicate better models.

7. The objective is to minimize
   prediction error.
""")

print("\nDay 36 Completed Successfully!")
print("=" * 60)