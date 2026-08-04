# ==========================================================
# Day 34 : Introduction to Supervised Learning
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 34")
print("=" * 60)

print("\nIntroduction to Supervised Learning")
print("-" * 30)

print("""
Supervised Learning is one of the most
important categories of Machine Learning.

In Supervised Learning, the model learns
from labeled data.

Labeled Data means:

Input  → Output

The model learns the relationship
between inputs and outputs.
""")

# ----------------------------------------------------------
# What is Supervised Learning?
# ----------------------------------------------------------

print("\nWhat is Supervised Learning?")
print("-" * 30)

print("""
The model is provided with:

✓ Features (Inputs)
✓ Labels (Outputs)

Goal:

Learn a mapping function that can
predict outputs for new inputs.
""")

# Example

study_hours = [2, 4, 6, 8, 10]
marks = [40, 55, 70, 85, 95]

print("Study Hours =", study_hours)
print("Marks       =", marks)

print("""
The model learns:

Study Hours → Marks
""")

# ----------------------------------------------------------
# Input Features and Labels
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
    40,
    55,
    70,
    85,
    95
]

print("Features =", features)
print("Labels   =", labels)

# ----------------------------------------------------------
# Supervised Learning Workflow
# ----------------------------------------------------------

print("\nSupervised Learning Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Prepare Data",
    "Train Model",
    "Test Model",
    "Evaluate Performance",
    "Make Predictions"
]

for i, step in enumerate(steps, start=1):
    print(f"{i}. {step}")

# ----------------------------------------------------------
# Types of Supervised Learning
# ----------------------------------------------------------

print("\nTypes of Supervised Learning")
print("-" * 30)

print("""
There are two major types:

1. Regression
2. Classification
""")

# ----------------------------------------------------------
# Regression
# ----------------------------------------------------------

print("\n1. Regression")
print("-" * 30)

print("""
Regression predicts continuous values.

Examples:

✓ House Price Prediction
✓ Temperature Prediction
✓ Salary Prediction
✓ Sales Forecasting
""")

house_sizes = [1000, 1200, 1500, 1800]
house_prices = [20, 25, 35, 45]

print("House Sizes  =", house_sizes)
print("House Prices =", house_prices)

print("""
Output is numeric.

This is a Regression problem.
""")

# ----------------------------------------------------------
# Classification
# ----------------------------------------------------------

print("\n2. Classification")
print("-" * 30)

print("""
Classification predicts categories.

Examples:

✓ Spam Detection
✓ Disease Prediction
✓ Pass/Fail Prediction
✓ Sentiment Analysis
""")

emails = [
    "Spam",
    "Not Spam",
    "Spam",
    "Not Spam"
]

print("Email Labels =", emails)

print("""
Output belongs to categories.

This is a Classification problem.
""")

# ----------------------------------------------------------
# Real Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

students = [
    [18, 6, 90, 85],
    [19, 8, 95, 92],
    [17, 5, 80, 75]
]

print("""
Columns:

Age
Study Hours
Attendance
Marks
""")

for row in students:
    print(row)

print("""
Features:
Age, Study Hours, Attendance

Label:
Marks
""")

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
    40,
    55,
    70,
    85
]

print("Training Features =", train_features)
print("Training Labels   =", train_labels)

# ----------------------------------------------------------
# Testing Data
# ----------------------------------------------------------

print("\nTesting Data")
print("-" * 30)

test_features = [[10]]
actual_output = [95]

print("Testing Feature =", test_features)
print("Actual Output   =", actual_output)

print("""
The trained model will try
to predict the output.
""")

# ----------------------------------------------------------
# Why Supervised Learning?
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Easy to Understand",
    "High Predictive Power",
    "Widely Used",
    "Supports Many Applications",
    "Good Performance with Quality Data"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "House Price Prediction",
    "Medical Diagnosis",
    "Spam Detection",
    "Fraud Detection",
    "Recommendation Systems",
    "Customer Churn Prediction"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Machine Learning Algorithms
# ----------------------------------------------------------

print("\nPopular Supervised Learning Algorithms")
print("-" * 30)

algorithms = [
    "Linear Regression",
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "Support Vector Machine",
    "K-Nearest Neighbors"
]

for algorithm in algorithms:
    print("✓", algorithm)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

experience = [1, 2, 3, 4, 5]
salary = [25000, 30000, 40000, 50000, 60000]

print("Experience =", experience)
print("Salary     =", salary)

print("""
The model learns:

Experience → Salary
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Identify the Problem Type:

Input:
House Features

Output:
House Price

Answer:
Regression
""")

print("""
Input:
Email Text

Output:
Spam / Not Spam

Answer:
Classification
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Supervised Learning?

2. What is labeled data?

3. What are the two types of
   Supervised Learning?

4. Give one Regression example.

5. Give one Classification example.
""")

print("""
Answers:

1. Learning from labeled data
2. Data containing inputs and outputs
3. Regression and Classification
4. House Price Prediction
5. Spam Detection
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 34 Summary")
print("-" * 30)

print("""
1. Supervised Learning learns from
   labeled data.

2. Inputs are called Features.

3. Outputs are called Labels.

4. Two major categories:

   ✓ Regression
   ✓ Classification

5. Supervised Learning is widely used
   in real-world Machine Learning systems.

6. It forms the foundation for many
   advanced ML algorithms.
""")

print("\nDay 34 Completed Successfully!")
print("=" * 60)