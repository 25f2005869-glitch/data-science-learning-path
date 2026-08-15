# ==========================================================
# Day 42 : Decision Trees
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 42")
print("=" * 60)

print("\nDecision Trees")
print("-" * 30)

print("""
Decision Tree is one of the most popular
Supervised Machine Learning algorithms.

It can be used for:

✓ Classification
✓ Regression

A Decision Tree makes predictions by
asking a series of questions and
following decision paths.

It works similarly to human decision making.
""")

# ----------------------------------------------------------
# What is a Decision Tree?
# ----------------------------------------------------------

print("\nWhat is a Decision Tree?")
print("-" * 30)

print("""
A Decision Tree is a tree-like structure.

Components:

✓ Root Node
✓ Internal Nodes
✓ Branches
✓ Leaf Nodes

The model splits data into smaller
groups until a prediction is made.
""")

# ----------------------------------------------------------
# Simple Example
# ----------------------------------------------------------

print("\nSimple Example")
print("-" * 30)

print("""
Question:

Is Attendance >= 75?

          Attendance?
              |
        ----------------
        |              |
      Yes             No
        |              |
      Pass           Fail

This is a Decision Tree.
""")

# ----------------------------------------------------------
# Student Dataset
# ----------------------------------------------------------

print("\nStudent Dataset")
print("-" * 30)

students = [
    [90, "Pass"],
    [85, "Pass"],
    [80, "Pass"],
    [70, "Fail"],
    [60, "Fail"]
]

print("Attendance | Result")

for row in students:

    print(row[0], "       |", row[1])

# ----------------------------------------------------------
# Root Node
# ----------------------------------------------------------

print("\nRoot Node")
print("-" * 30)

print("""
The Root Node is the first
decision point in the tree.

Example:

Attendance >= 75?

The root node contains
the most important question.
""")

# ----------------------------------------------------------
# Internal Nodes
# ----------------------------------------------------------

print("\nInternal Nodes")
print("-" * 30)

print("""
Internal Nodes contain
additional decision rules.

Example:

Attendance >= 75?

Then:

Study Hours >= 5?

These nodes help further
split the dataset.
""")

# ----------------------------------------------------------
# Leaf Nodes
# ----------------------------------------------------------

print("\nLeaf Nodes")
print("-" * 30)

print("""
Leaf Nodes contain
final predictions.

Examples:

✓ Pass
✓ Fail
✓ Spam
✓ Not Spam

No further splitting occurs.
""")

# ----------------------------------------------------------
# Classification Example
# ----------------------------------------------------------

print("\nClassification Example")
print("-" * 30)

attendance = 85

if attendance >= 75:

    prediction = "Pass"

else:

    prediction = "Fail"

print("Attendance =", attendance)
print("Prediction =", prediction)

# ----------------------------------------------------------
# Regression Example
# ----------------------------------------------------------

print("\nRegression Example")
print("-" * 30)

print("""
Decision Trees can also predict
continuous values.

Example:

House Price Prediction
Salary Prediction
Sales Forecasting
""")

house_area = 1500

if house_area < 1200:

    price = 20

elif house_area < 1800:

    price = 35

else:

    price = 50

print("Predicted Price =", price)

# ----------------------------------------------------------
# Why Decision Trees?
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Easy to Understand",
    "Easy to Visualize",
    "Works for Classification",
    "Works for Regression",
    "Requires Less Data Preparation"
]

for item in advantages:

    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Can Overfit",
    "Sensitive to Noise",
    "May Create Complex Trees",
    "Lower Accuracy on Some Problems"
]

for item in limitations:

    print("✗", item)

# ----------------------------------------------------------
# Tree Depth
# ----------------------------------------------------------

print("\nTree Depth")
print("-" * 30)

print("""
Tree Depth is the number of levels
from root to leaf.

Small Depth:

✓ Simpler Model

Large Depth:

✓ More Complex Model
✗ May Overfit
""")

# ----------------------------------------------------------
# Splitting Criteria
# ----------------------------------------------------------

print("\nSplitting Criteria")
print("-" * 30)

print("""
Decision Trees choose the best split
using measures such as:

✓ Gini Impurity
✓ Entropy
✓ Information Gain
""")

# ----------------------------------------------------------
# Gini Impurity Example
# ----------------------------------------------------------

print("\nGini Impurity")
print("-" * 30)

print("""
Gini measures how mixed
the classes are.

Lower Gini:

✓ Better Split

Higher Gini:

✗ Poor Split
""")

gini = 0.20

print("Example Gini =", gini)

# ----------------------------------------------------------
# Entropy Example
# ----------------------------------------------------------

print("\nEntropy")
print("-" * 30)

print("""
Entropy measures uncertainty.

Lower Entropy:

✓ More Pure Groups

Higher Entropy:

✗ More Uncertainty
""")

entropy = 0.35

print("Example Entropy =", entropy)

# ----------------------------------------------------------
# Real World Example
# ----------------------------------------------------------

print("\nLoan Approval Example")
print("-" * 30)

income = 60000

if income >= 50000:

    loan_status = "Approved"

else:

    loan_status = "Rejected"

print("Income =", income)
print("Loan Status =", loan_status)

# ----------------------------------------------------------
# Email Spam Detection
# ----------------------------------------------------------

print("\nSpam Detection")
print("-" * 30)

contains_offer = True

if contains_offer:

    email_type = "Spam"

else:

    email_type = "Not Spam"

print("Email Type =", email_type)

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Loan Approval",
    "Fraud Detection",
    "Medical Diagnosis",
    "Customer Churn Prediction",
    "Spam Detection",
    "Risk Assessment"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Decision Tree Workflow
# ----------------------------------------------------------

print("\nWorkflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Choose Best Split",
    "Create Nodes",
    "Grow Tree",
    "Make Predictions",
    "Evaluate Model"
]

for i, step in enumerate(steps, start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

study_hours = 7

if study_hours >= 5:

    result = "Pass"

else:

    result = "Fail"

print("Study Hours =", study_hours)
print("Prediction =", result)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

age = 25

if age >= 18:

    status = "Adult"

else:

    status = "Minor"

print("Status =", status)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Decision Tree?

2. What are Leaf Nodes?

3. What is Tree Depth?

4. Name one splitting criterion.

5. Give one application of
   Decision Trees.
""")

print("""
Answers:

1. Tree-based ML algorithm
2. Final prediction nodes
3. Number of levels in tree
4. Gini or Entropy
5. Loan Approval
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 42 Summary")
print("-" * 30)

print("""
1. Decision Trees are supervised
   learning algorithms.

2. They can perform:

   ✓ Classification
   ✓ Regression

3. Trees consist of:

   ✓ Root Nodes
   ✓ Internal Nodes
   ✓ Leaf Nodes

4. Common split measures:

   ✓ Gini Impurity
   ✓ Entropy

5. Decision Trees are easy to
   understand and visualize.

6. Large trees may overfit.

7. They are widely used in
   real-world ML applications.
""")

print("\nDay 42 Completed Successfully!")
print("=" * 60)