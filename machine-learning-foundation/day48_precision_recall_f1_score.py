# ==========================================================
# Day 48 : Precision, Recall and F1 Score
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 48")
print("=" * 60)

print("\nPrecision, Recall and F1 Score")
print("-" * 30)

print("""
Precision, Recall, and F1 Score are
important evaluation metrics for
Classification Models.

These metrics are calculated using
the Confusion Matrix.

They provide deeper insights than
Accuracy alone.
""")

# ----------------------------------------------------------
# Confusion Matrix Recap
# ----------------------------------------------------------

print("\nConfusion Matrix Recap")
print("-" * 30)

print("""
                 Predicted

              Positive  Negative

Actual Positive    TP        FN

Actual Negative    FP        TN
""")

tp = 80
fp = 10
fn = 20
tn = 90

print("TP =", tp)
print("FP =", fp)
print("FN =", fn)
print("TN =", tn)

# ----------------------------------------------------------
# Why Not Accuracy Alone?
# ----------------------------------------------------------

print("\nWhy Not Accuracy Alone?")
print("-" * 30)

print("""
Accuracy can be misleading,
especially for imbalanced datasets.

Example:

990 Negative Cases
10 Positive Cases

A model predicting everything
as Negative achieves:

99% Accuracy

But it completely fails to
identify Positive cases.
""")

# ----------------------------------------------------------
# Precision
# ----------------------------------------------------------

print("\nPrecision")
print("-" * 30)

print("""
Precision measures how many
predicted Positive cases were
actually Positive.

Formula:

Precision =
TP
-----------
TP + FP
""")

precision = tp / (tp + fp)

print("Precision =",
      round(precision, 4))

# ----------------------------------------------------------
# Precision Interpretation
# ----------------------------------------------------------

print("\nPrecision Interpretation")
print("-" * 30)

print("""
High Precision:

✓ Few False Positives

Low Precision:

✗ Many False Positives

Question Answered:

Of all predicted positives,
how many were actually positive?
""")

# ----------------------------------------------------------
# Recall
# ----------------------------------------------------------

print("\nRecall")
print("-" * 30)

print("""
Recall measures how many
actual Positive cases were
correctly identified.

Formula:

Recall =
TP
-----------
TP + FN
""")

recall = tp / (tp + fn)

print("Recall =",
      round(recall, 4))

# ----------------------------------------------------------
# Recall Interpretation
# ----------------------------------------------------------

print("\nRecall Interpretation")
print("-" * 30)

print("""
High Recall:

✓ Few False Negatives

Low Recall:

✗ Many False Negatives

Question Answered:

Of all actual positives,
how many did we detect?
""")

# ----------------------------------------------------------
# F1 Score
# ----------------------------------------------------------

print("\nF1 Score")
print("-" * 30)

print("""
F1 Score combines Precision
and Recall into a single metric.

Formula:

F1 =
2 × Precision × Recall
------------------------
 Precision + Recall
""")

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

# ----------------------------------------------------------
# F1 Score Interpretation
# ----------------------------------------------------------

print("\nF1 Score Interpretation")
print("-" * 30)

print("""
F1 Score provides balance between:

✓ Precision
✓ Recall

Useful when both metrics
are equally important.
""")

# ----------------------------------------------------------
# Complete Example
# ----------------------------------------------------------

print("\nComplete Example")
print("-" * 30)

tp = 50
fp = 5
fn = 10
tn = 35

precision = tp / (tp + fp)

recall = tp / (tp + fn)

f1_score = (
    2 *
    precision *
    recall
) / (
    precision +
    recall
)

print("Precision =", round(precision, 4))
print("Recall    =", round(recall, 4))
print("F1 Score  =", round(f1_score, 4))

# ----------------------------------------------------------
# Medical Diagnosis Example
# ----------------------------------------------------------

print("\nMedical Diagnosis")
print("-" * 30)

print("""
In disease prediction:

High Recall is important.

Reason:

Missing a disease patient
(False Negative) can be dangerous.

Goal:

Detect as many positive
patients as possible.
""")

# ----------------------------------------------------------
# Spam Detection Example
# ----------------------------------------------------------

print("\nSpam Detection")
print("-" * 30)

print("""
In spam detection:

High Precision is important.

Reason:

Important emails should not
be marked as Spam.

Goal:

Reduce False Positives.
""")

# ----------------------------------------------------------
# Fraud Detection Example
# ----------------------------------------------------------

print("\nFraud Detection")
print("-" * 30)

print("""
Fraud detection requires:

✓ High Precision
✓ High Recall

Therefore:

F1 Score becomes very important.
""")

# ----------------------------------------------------------
# Accuracy vs Precision vs Recall
# ----------------------------------------------------------

print("\nMetric Comparison")
print("-" * 30)

print("""
Accuracy:

Overall Correct Predictions

Precision:

Correct Positive Predictions

Recall:

Detected Actual Positives

F1 Score:

Balance Between Precision
and Recall
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nStudent Pass/Fail Example")
print("-" * 30)

actual = [
    "Pass",
    "Pass",
    "Pass",
    "Fail",
    "Fail"
]

predicted = [
    "Pass",
    "Pass",
    "Fail",
    "Fail",
    "Fail"
]

print("Actual    =", actual)
print("Predicted =", predicted)

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Medical Diagnosis",
    "Fraud Detection",
    "Spam Detection",
    "Face Recognition",
    "Sentiment Analysis",
    "Customer Churn Prediction"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

tp = 90
fp = 15
fn = 10

precision = tp / (tp + fp)

recall = tp / (tp + fn)

print("Precision =",
      round(precision, 4))

print("Recall =",
      round(recall, 4))

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

tp = 40
fp = 10

precision = tp / (tp + fp)

print("""
Question:

TP = 40
FP = 10

Find Precision.
""")

print("Answer =",
      round(precision, 2))

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Precision?

2. What is Recall?

3. What is F1 Score?

4. Which metric focuses on
   False Positives?

5. Which metric focuses on
   False Negatives?
""")

print("""
Answers:

1. Positive Prediction Accuracy
2. Positive Detection Rate
3. Balance of Precision and Recall
4. Precision
5. Recall
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 48 Summary")
print("-" * 30)

print("""
1. Precision measures the quality
   of positive predictions.

2. Recall measures the ability
   to find positive cases.

3. F1 Score balances Precision
   and Recall.

4. These metrics are derived
   from the Confusion Matrix.

5. They are more informative
   than Accuracy alone.

6. Different applications require
   different evaluation priorities.

7. Precision, Recall, and F1 Score
   are essential classification metrics.
""")

print("\nDay 48 Completed Successfully!")
print("=" * 60)