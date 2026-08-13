# ==========================================================
# Day 40 : Introduction to Classification
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 40")
print("=" * 60)

print("\nIntroduction to Classification")
print("-" * 30)

print("""
Classification is a Supervised Learning
technique used to predict categories
or class labels.

Unlike Regression, which predicts
continuous numerical values,
Classification predicts discrete classes.

Examples:

✓ Spam or Not Spam
✓ Pass or Fail
✓ Disease or No Disease
✓ Fraud or Not Fraud
✓ Positive or Negative Review
""")

# ----------------------------------------------------------
# What is Classification?
# ----------------------------------------------------------

print("\nWhat is Classification?")
print("-" * 30)

print("""
Classification learns from labeled data
and assigns observations to predefined
categories.

Input  → Features

Output → Class Label

Goal:

Predict the correct class for new data.
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
result = [
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

print("Study Hours =", study_hours)
print("Result      =", result)

print("""
The model learns:

Study Hours → Pass/Fail
""")

# ----------------------------------------------------------
# Classification vs Regression
# ----------------------------------------------------------

print("\nClassification vs Regression")
print("-" * 30)

print("""
Regression:

Predicts numerical values.

Examples:
✓ Salary Prediction
✓ House Price Prediction

Classification:

Predicts categories.

Examples:
✓ Spam Detection
✓ Disease Prediction
""")

# ----------------------------------------------------------
# Binary Classification
# ----------------------------------------------------------

print("\nBinary Classification")
print("-" * 30)

print("""
Binary Classification has
only two classes.

Examples:

✓ Yes / No
✓ Pass / Fail
✓ Spam / Not Spam
✓ Fraud / Not Fraud
""")

binary_labels = [
    "Pass",
    "Fail"
]

print("Classes =", binary_labels)

# ----------------------------------------------------------
# Multi-Class Classification
# ----------------------------------------------------------

print("\nMulti-Class Classification")
print("-" * 30)

print("""
Multi-Class Classification has
more than two classes.

Examples:

✓ Grade A
✓ Grade B
✓ Grade C
✓ Grade D
""")

grades = [
    "A",
    "B",
    "C",
    "D"
]

print("Classes =", grades)

# ----------------------------------------------------------
# Features and Labels
# ----------------------------------------------------------

print("\nFeatures and Labels")
print("-" * 30)

features = [
    [2],
    [4],
    [6],
    [8],
    [10]
]

labels = [
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

print("Features =", features)
print("Labels   =", labels)

# ----------------------------------------------------------
# Training Data
# ----------------------------------------------------------

print("\nTraining Data")
print("-" * 30)

train_features = [
    [2],
    [4],
    [6],
    [8]
]

train_labels = [
    "Fail",
    "Fail",
    "Pass",
    "Pass"
]

print("Training Features =", train_features)
print("Training Labels   =", train_labels)

# ----------------------------------------------------------
# Testing Data
# ----------------------------------------------------------

print("\nTesting Data")
print("-" * 30)

test_feature = [[10]]

print("Testing Feature =", test_feature)

print("""
The model predicts:

Pass or Fail
""")

# ----------------------------------------------------------
# Real-World Example
# ----------------------------------------------------------

print("\nEmail Spam Detection")
print("-" * 30)

emails = [
    "Win a Lottery",
    "Meeting Schedule",
    "Free Gift Offer",
    "Project Update"
]

labels = [
    "Spam",
    "Not Spam",
    "Spam",
    "Not Spam"
]

for email, label in zip(emails, labels):

    print(email, "→", label)

# ----------------------------------------------------------
# Disease Prediction Example
# ----------------------------------------------------------

print("\nDisease Prediction")
print("-" * 30)

patients = [
    ["Fever", "Cough"],
    ["Headache"],
    ["Fever", "Fatigue"]
]

labels = [
    "Disease",
    "Healthy",
    "Disease"
]

for patient, label in zip(patients, labels):

    print(patient, "→", label)

# ----------------------------------------------------------
# Classification Workflow
# ----------------------------------------------------------

print("\nClassification Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Preprocess Data",
    "Train Model",
    "Predict Classes",
    "Evaluate Model",
    "Deploy Model"
]

for i, step in enumerate(steps, start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Popular Classification Algorithms
# ----------------------------------------------------------

print("\nClassification Algorithms")
print("-" * 30)

algorithms = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "K-Nearest Neighbors",
    "Naive Bayes",
    "Support Vector Machine"
]

for algorithm in algorithms:

    print("✓", algorithm)

# ----------------------------------------------------------
# Accuracy Example
# ----------------------------------------------------------

print("\nClassification Accuracy")
print("-" * 30)

actual = [
    "Pass",
    "Fail",
    "Pass",
    "Pass",
    "Fail"
]

predicted = [
    "Pass",
    "Fail",
    "Pass",
    "Fail",
    "Fail"
]

correct = 0

for a, p in zip(actual, predicted):

    if a == p:
        correct += 1

accuracy = (
    correct /
    len(actual)
) * 100

print("Correct Predictions =", correct)
print("Accuracy =", accuracy, "%")

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Spam Detection",
    "Medical Diagnosis",
    "Fraud Detection",
    "Sentiment Analysis",
    "Image Recognition",
    "Customer Churn Prediction"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

attendance = 90

if attendance >= 75:

    prediction = "Pass"

else:

    prediction = "Fail"

print("Attendance =", attendance)
print("Predicted Class =", prediction)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Problem:

Predict whether an email is
Spam or Not Spam.

Question:

Regression or Classification?

Answer:

Classification
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Classification?

2. What type of output does it predict?

3. What is Binary Classification?

4. What is Multi-Class Classification?

5. Give one real-world application.
""")

print("""
Answers:

1. Predicting categories
2. Class labels
3. Two-class classification
4. More than two classes
5. Spam Detection
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 40 Summary")
print("-" * 30)

print("""
1. Classification is a Supervised
   Learning technique.

2. It predicts class labels.

3. Binary Classification has
   two classes.

4. Multi-Class Classification has
   more than two classes.

5. Classification is widely used
   in real-world applications.

6. Popular algorithms include:

   ✓ Logistic Regression
   ✓ Decision Tree
   ✓ Random Forest
   ✓ KNN
   ✓ Naive Bayes

7. Classification forms the foundation
   of many AI systems.
""")

print("\nDay 40 Completed Successfully!")
print("=" * 60)