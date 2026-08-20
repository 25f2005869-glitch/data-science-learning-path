# ==========================================================
# Day 47 : Confusion Matrix
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 47")
print("=" * 60)

print("\nConfusion Matrix")
print("-" * 30)

print("""
A Confusion Matrix is a table used to
evaluate Classification Models.

It compares:

✓ Actual Values
✓ Predicted Values

The Confusion Matrix helps us understand
how well a classification model performs.
""")

# ----------------------------------------------------------
# Why Confusion Matrix?
# ----------------------------------------------------------

print("\nWhy Confusion Matrix?")
print("-" * 30)

print("""
Accuracy alone is not always enough.

A Confusion Matrix provides:

✓ Detailed Evaluation
✓ Error Analysis
✓ Class-wise Performance
✓ Better Understanding
""")

# ----------------------------------------------------------
# Binary Classification Example
# ----------------------------------------------------------

print("\nBinary Classification Example")
print("-" * 30)

print("""
Disease Prediction

Actual:

Positive
Negative

Predicted:

Positive
Negative
""")

# ----------------------------------------------------------
# Confusion Matrix Structure
# ----------------------------------------------------------

print("\nConfusion Matrix Structure")
print("-" * 30)

print("""
                     Predicted

                Positive   Negative

Actual Positive     TP         FN

Actual Negative     FP         TN
""")

# ----------------------------------------------------------
# Understanding Terms
# ----------------------------------------------------------

print("\nConfusion Matrix Terms")
print("-" * 30)

print("""
TP = True Positive
FP = False Positive

TN = True Negative
FN = False Negative
""")

# ----------------------------------------------------------
# True Positive
# ----------------------------------------------------------

print("\nTrue Positive (TP)")
print("-" * 30)

print("""
Model predicts Positive.

Actual class is also Positive.

Example:

Disease Present
Predicted Disease Present

Correct Prediction.
""")

tp = 40

print("TP =", tp)

# ----------------------------------------------------------
# True Negative
# ----------------------------------------------------------

print("\nTrue Negative (TN)")
print("-" * 30)

print("""
Model predicts Negative.

Actual class is also Negative.

Example:

No Disease
Predicted No Disease

Correct Prediction.
""")

tn = 50

print("TN =", tn)

# ----------------------------------------------------------
# False Positive
# ----------------------------------------------------------

print("\nFalse Positive (FP)")
print("-" * 30)

print("""
Model predicts Positive.

Actual class is Negative.

Example:

Healthy Person
Predicted Disease

Incorrect Prediction.

Also called:

Type-I Error
""")

fp = 5

print("FP =", fp)

# ----------------------------------------------------------
# False Negative
# ----------------------------------------------------------

print("\nFalse Negative (FN)")
print("-" * 30)

print("""
Model predicts Negative.

Actual class is Positive.

Example:

Disease Present
Predicted Healthy

Incorrect Prediction.

Also called:

Type-II Error
""")

fn = 5

print("FN =", fn)

# ----------------------------------------------------------
# Example Confusion Matrix
# ----------------------------------------------------------

print("\nExample Confusion Matrix")
print("-" * 30)

print("""
                 Predicted

              Positive  Negative

Actual Positive    40        5

Actual Negative     5       50
""")

# ----------------------------------------------------------
# Accuracy
# ----------------------------------------------------------

print("\nAccuracy")
print("-" * 30)

accuracy = (
    (tp + tn) /
    (tp + tn + fp + fn)
)

print("Accuracy =",
      round(accuracy * 100, 2),
      "%")

print("""
Formula:

(TP + TN)
-----------
Total Samples
""")

# ----------------------------------------------------------
# Precision
# ----------------------------------------------------------

print("\nPrecision")
print("-" * 30)

precision = (
    tp /
    (tp + fp)
)

print("Precision =",
      round(precision, 4))

print("""
Formula:

TP
------
TP + FP

Precision answers:

Of all predicted positives,
how many were actually positive?
""")

# ----------------------------------------------------------
# Recall
# ----------------------------------------------------------

print("\nRecall")
print("-" * 30)

recall = (
    tp /
    (tp + fn)
)

print("Recall =",
      round(recall, 4))

print("""
Formula:

TP
------
TP + FN

Recall answers:

Of all actual positives,
how many were detected?
""")

# ----------------------------------------------------------
# F1 Score
# ----------------------------------------------------------

print("\nF1 Score")
print("-" * 30)

f1_score = (
    2 *
    precision *
    recall
) / (
    precision +
    recall
)

print("F1 Score =",
      round(f1_score, 4))

print("""
F1 Score balances:

✓ Precision
✓ Recall
""")

# ----------------------------------------------------------
# Classification Example
# ----------------------------------------------------------

print("\nStudent Pass/Fail Example")
print("-" * 30)

actual = [
    "Pass",
    "Pass",
    "Fail",
    "Pass",
    "Fail"
]

predicted = [
    "Pass",
    "Fail",
    "Fail",
    "Pass",
    "Fail"
]

correct = 0

for a, p in zip(actual, predicted):

    if a == p:

        correct += 1

print("Correct Predictions =",
      correct)

# ----------------------------------------------------------
# Medical Diagnosis Example
# ----------------------------------------------------------

print("\nMedical Diagnosis")
print("-" * 30)

print("""
Confusion Matrix is extremely important
in healthcare.

False Negatives can be dangerous.

A patient with disease should
not be classified as healthy.
""")

# ----------------------------------------------------------
# Spam Detection Example
# ----------------------------------------------------------

print("\nSpam Detection")
print("-" * 30)

print("""
False Positive:

Important Email
classified as Spam.

False Negative:

Spam Email reaches inbox.
""")

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Medical Diagnosis",
    "Fraud Detection",
    "Spam Detection",
    "Image Classification",
    "Sentiment Analysis",
    "Customer Churn Prediction"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Model Evaluation Workflow
# ----------------------------------------------------------

print("\nEvaluation Workflow")
print("-" * 30)

steps = [
    "Train Model",
    "Make Predictions",
    "Create Confusion Matrix",
    "Calculate Metrics",
    "Analyze Errors",
    "Improve Model"
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

tp = 80
tn = 90
fp = 10
fn = 20

accuracy = (
    (tp + tn) /
    (tp + tn + fp + fn)
)

print("Accuracy =",
      round(accuracy * 100, 2),
      "%")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

tp = 30
fp = 10

precision = tp / (tp + fp)

print("Precision =",
      round(precision, 2))

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Confusion Matrix?

2. What is TP?

3. What is FP?

4. What is Recall?

5. Why is Confusion Matrix useful?
""")

print("""
Answers:

1. Classification evaluation table
2. True Positive
3. False Positive
4. Ability to detect positives
5. Provides detailed model analysis
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 47 Summary")
print("-" * 30)

print("""
1. Confusion Matrix evaluates
   classification models.

2. Four important terms:

   ✓ TP
   ✓ TN
   ✓ FP
   ✓ FN

3. Important metrics:

   ✓ Accuracy
   ✓ Precision
   ✓ Recall
   ✓ F1 Score

4. It helps analyze model errors.

5. It is widely used in
   classification problems.

6. Confusion Matrix provides more
   information than accuracy alone.
""")

print("\nDay 47 Completed Successfully!")
print("=" * 60)