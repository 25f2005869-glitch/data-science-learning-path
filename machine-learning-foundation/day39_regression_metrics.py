# ==========================================================
# Day 39 : Regression Metrics
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 39")
print("=" * 60)

print("\nRegression Metrics")
print("-" * 30)

print("""
Regression Metrics are used to evaluate
the performance of Regression Models.

They help us measure:

✓ Prediction Accuracy
✓ Model Quality
✓ Error Magnitude
✓ Model Reliability

Common Regression Metrics:

1. MAE  (Mean Absolute Error)
2. MSE  (Mean Squared Error)
3. RMSE (Root Mean Squared Error)
4. R² Score (Coefficient of Determination)
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

actual = [50, 60, 70, 80, 90]
predicted = [52, 58, 72, 78, 88]

print("Actual Values    =", actual)
print("Predicted Values =", predicted)

# ----------------------------------------------------------
# Prediction Errors
# ----------------------------------------------------------

print("\nPrediction Errors")
print("-" * 30)

errors = []

for a, p in zip(actual, predicted):

    error = a - p

    errors.append(error)

print("Errors =", errors)

# ----------------------------------------------------------
# Mean Absolute Error (MAE)
# ----------------------------------------------------------

print("\nMean Absolute Error (MAE)")
print("-" * 30)

absolute_errors = []

for error in errors:

    absolute_errors.append(abs(error))

mae = (
    sum(absolute_errors) /
    len(absolute_errors)
)

print("Absolute Errors =", absolute_errors)
print("MAE =", round(mae, 2))

print("""
Formula:

MAE =
Σ |Actual - Predicted|
----------------------
Number of Observations
""")

# ----------------------------------------------------------
# Mean Squared Error (MSE)
# ----------------------------------------------------------

print("\nMean Squared Error (MSE)")
print("-" * 30)

squared_errors = []

for error in errors:

    squared_errors.append(error ** 2)

mse = (
    sum(squared_errors) /
    len(squared_errors)
)

print("Squared Errors =", squared_errors)
print("MSE =", round(mse, 2))

print("""
Formula:

MSE =
Σ (Actual - Predicted)^2
-------------------------
Number of Observations
""")

# ----------------------------------------------------------
# Root Mean Squared Error (RMSE)
# ----------------------------------------------------------

print("\nRoot Mean Squared Error (RMSE)")
print("-" * 30)

rmse = mse ** 0.5

print("RMSE =", round(rmse, 2))

print("""
Formula:

RMSE = √MSE
""")

# ----------------------------------------------------------
# Understanding RMSE
# ----------------------------------------------------------

print("\nUnderstanding RMSE")
print("-" * 30)

print("""
RMSE gives error in the same unit
as the target variable.

Lower RMSE:
✓ Better Model

Higher RMSE:
✗ Poor Model
""")

# ----------------------------------------------------------
# R-Squared Score
# ----------------------------------------------------------

print("\nR² Score (Coefficient of Determination)")
print("-" * 30)

mean_actual = (
    sum(actual) /
    len(actual)
)

total_sum_squares = 0

for value in actual:

    total_sum_squares += (
        value - mean_actual
    ) ** 2

residual_sum_squares = 0

for a, p in zip(actual, predicted):

    residual_sum_squares += (
        a - p
    ) ** 2

r_squared = (
    1 -
    (
        residual_sum_squares /
        total_sum_squares
    )
)

print("R² Score =",
      round(r_squared, 4))

print("""
Interpretation:

R² = 1
Perfect Prediction

R² = 0
No Improvement Over Mean

Closer to 1
Better Model
""")

# ----------------------------------------------------------
# Comparing Models
# ----------------------------------------------------------

print("\nModel Comparison")
print("-" * 30)

model_A_rmse = 8.5
model_B_rmse = 4.2

print("Model A RMSE =", model_A_rmse)
print("Model B RMSE =", model_B_rmse)

if model_B_rmse < model_A_rmse:
    print("Model B Performs Better")

# ----------------------------------------------------------
# Regression Metrics Summary Table
# ----------------------------------------------------------

print("\nRegression Metrics Overview")
print("-" * 30)

metrics = [
    "MAE",
    "MSE",
    "RMSE",
    "R² Score"
]

for metric in metrics:
    print("✓", metric)

# ----------------------------------------------------------
# House Price Prediction Example
# ----------------------------------------------------------

print("\nHouse Price Prediction")
print("-" * 30)

actual_prices = [
    20,
    25,
    30,
    35,
    40
]

predicted_prices = [
    21,
    24,
    31,
    34,
    39
]

print("Actual Prices    =", actual_prices)
print("Predicted Prices =", predicted_prices)

print("""
Regression metrics help determine
how accurate these predictions are.
""")

# ----------------------------------------------------------
# Salary Prediction Example
# ----------------------------------------------------------

print("\nSalary Prediction")
print("-" * 30)

actual_salary = [
    25000,
    35000,
    45000
]

predicted_salary = [
    26000,
    34000,
    46000
]

print("Actual Salary    =", actual_salary)
print("Predicted Salary =", predicted_salary)

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nRegression Metrics in ML")
print("-" * 30)

applications = [
    "Linear Regression",
    "Multiple Regression",
    "Forecasting",
    "Sales Prediction",
    "Demand Prediction",
    "Price Prediction"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Good vs Bad Model
# ----------------------------------------------------------

print("\nGood vs Bad Model")
print("-" * 30)

good_rmse = 2
bad_rmse = 15

print("Good Model RMSE =", good_rmse)
print("Bad Model RMSE  =", bad_rmse)

print("""
Lower Error
→ Better Predictions

Higher Error
→ Poor Predictions
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

actual_score = 90
predicted_score = 85

error = abs(
    actual_score -
    predicted_score
)

print("Absolute Error =", error)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

actual_value = 100
predicted_value = 95

absolute_error = abs(
    actual_value -
    predicted_value
)

squared_error = (
    actual_value -
    predicted_value
) ** 2

print("Absolute Error =", absolute_error)
print("Squared Error =", squared_error)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is MAE?

2. What is MSE?

3. What is RMSE?

4. What does R² measure?

5. Which value is preferred:
   High RMSE or Low RMSE?
""")

print("""
Answers:

1. Mean Absolute Error
2. Mean Squared Error
3. Root Mean Squared Error
4. Explained Variance
5. Low RMSE
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 39 Summary")
print("-" * 30)

print("""
1. Regression Metrics evaluate
   regression models.

2. MAE measures average
   absolute error.

3. MSE penalizes larger errors.

4. RMSE provides error in
   original units.

5. R² measures explained variance.

6. Lower MAE, MSE, RMSE
   indicate better models.

7. Higher R² indicates
   better model performance.
""")

print("\nDay 39 Completed Successfully!")
print("=" * 60)