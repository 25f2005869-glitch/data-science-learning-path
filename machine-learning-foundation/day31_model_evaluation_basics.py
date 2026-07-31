# ==========================================================
# Day 31 : Model Evaluation Basics
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 31")
print("=" * 60)

print("\nModel Evaluation Basics")
print("-" * 30)

print("""
Model Evaluation is the process of measuring
how well a Machine Learning model performs.

After training a model, we must determine:

✓ Is the model accurate?
✓ Is it making good predictions?
✓ Can it generalize to new data?
✓ Is it better than other models?

Model Evaluation helps answer these questions.
""")

# ----------------------------------------------------------
# Why Model Evaluation?
# ----------------------------------------------------------

print("\nWhy Model Evaluation?")
print("-" * 30)

reasons = [
    "Measure Performance",
    "Compare Models",
    "Detect Overfitting",
    "Detect Underfitting",
    "Improve Predictions"
]

for reason in reasons:
    print("✓", reason)

# ----------------------------------------------------------
# Actual vs Predicted Values
# ----------------------------------------------------------

print("\nActual vs Predicted Values")
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

mae = sum(absolute_errors) / len(absolute_errors)

print("Absolute Errors =", absolute_errors)
print("MAE =", round(mae, 2))

print("""
Formula:

MAE = Σ|Actual - Predicted| / n
""")

# ----------------------------------------------------------
# Mean Squared Error (MSE)
# ----------------------------------------------------------

print("\nMean Squared Error (MSE)")
print("-" * 30)

squared_errors = []

for error in errors:
    squared_errors.append(error ** 2)

mse = sum(squared_errors) / len(squared_errors)

print("Squared Errors =", squared_errors)
print("MSE =", round(mse, 2))

print("""
Formula:

MSE = Σ(Actual - Predicted)² / n
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
# Accuracy Concept
# ----------------------------------------------------------

print("\nAccuracy")
print("-" * 30)

print("""
Accuracy is commonly used for
classification problems.

Formula:

Accuracy =
Correct Predictions
-------------------
Total Predictions
""")

correct_predictions = 8
total_predictions = 10

accuracy = (
    correct_predictions /
    total_predictions
) * 100

print("Accuracy =", accuracy, "%")

# ----------------------------------------------------------
# Classification Example
# ----------------------------------------------------------

print("\nClassification Example")
print("-" * 30)

actual_labels = [
    "Pass",
    "Fail",
    "Pass",
    "Pass",
    "Fail"
]

predicted_labels = [
    "Pass",
    "Fail",
    "Pass",
    "Fail",
    "Fail"
]

correct = 0

for a, p in zip(actual_labels, predicted_labels):

    if a == p:
        correct += 1

classification_accuracy = (
    correct /
    len(actual_labels)
) * 100

print("Correct Predictions =", correct)
print("Accuracy =", classification_accuracy, "%")

# ----------------------------------------------------------
# Overfitting Review
# ----------------------------------------------------------

print("\nOverfitting")
print("-" * 30)

print("""
Overfitting occurs when a model
memorizes training data.

Result:

✓ High Training Accuracy
✗ Poor Test Accuracy
""")

# ----------------------------------------------------------
# Underfitting Review
# ----------------------------------------------------------

print("\nUnderfitting")
print("-" * 30)

print("""
Underfitting occurs when a model
fails to learn important patterns.

Result:

✗ Poor Training Accuracy
✗ Poor Test Accuracy
""")

# ----------------------------------------------------------
# Model Comparison Example
# ----------------------------------------------------------

print("\nModel Comparison")
print("-" * 30)

model_A_accuracy = 82
model_B_accuracy = 89

print("Model A Accuracy =", model_A_accuracy, "%")
print("Model B Accuracy =", model_B_accuracy, "%")

if model_B_accuracy > model_A_accuracy:
    print("Model B Performs Better")

# ----------------------------------------------------------
# Machine Learning Workflow
# ----------------------------------------------------------

print("\nEvaluation in ML Workflow")
print("-" * 30)

workflow = [
    "Collect Data",
    "Preprocess Data",
    "Train-Test Split",
    "Train Model",
    "Evaluate Model",
    "Improve Model",
    "Deploy Model"
]

for i, step in enumerate(workflow, start=1):
    print(f"{i}. {step}")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

student_actual = [60, 70, 80, 90]
student_predicted = [58, 72, 78, 92]

total_error = 0

for a, p in zip(student_actual, student_predicted):

    total_error += abs(a - p)

average_error = (
    total_error /
    len(student_actual)
)

print("Average Prediction Error =",
      round(average_error, 2))

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

actual_values = [10, 20, 30]
predicted_values = [12, 18, 29]

errors = []

for a, p in zip(actual_values, predicted_values):
    errors.append(abs(a - p))

practice_mae = sum(errors) / len(errors)

print("MAE =", round(practice_mae, 2))

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Model Evaluation?

2. What is MAE?

3. What is MSE?

4. What is RMSE?

5. Why is model evaluation important?
""")

print("""
Answers:

1. Measuring model performance
2. Mean Absolute Error
3. Mean Squared Error
4. Root Mean Squared Error
5. To determine model quality
   and prediction performance
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 31 Summary")
print("-" * 30)

print("""
1. Model Evaluation measures
   prediction performance.

2. Common metrics:

   ✓ MAE
   ✓ MSE
   ✓ RMSE
   ✓ Accuracy

3. Lower error generally means
   better predictions.

4. Evaluation helps compare models.

5. It is essential before deploying
   a Machine Learning model.
""")

print("\nDay 31 Completed Successfully!")
print("=" * 60)