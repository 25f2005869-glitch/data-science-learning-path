# ==========================================================
# Day 43 : Random Forest
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 43")
print("=" * 60)

print("\nRandom Forest")
print("-" * 30)

print("""
Random Forest is an Ensemble Learning
algorithm that combines multiple
Decision Trees.

Instead of relying on a single tree,
Random Forest uses many trees and
combines their predictions.

Goal:

✓ Improve Accuracy
✓ Reduce Overfitting
✓ Increase Reliability
""")

# ----------------------------------------------------------
# What is Random Forest?
# ----------------------------------------------------------

print("\nWhat is Random Forest?")
print("-" * 30)

print("""
Random Forest is a collection
of Decision Trees.

Each tree makes its own prediction.

Final Prediction:

Classification:
Majority Voting

Regression:
Average Prediction
""")

# ----------------------------------------------------------
# Why Random Forest?
# ----------------------------------------------------------

print("\nWhy Random Forest?")
print("-" * 30)

print("""
A single Decision Tree may overfit.

Random Forest reduces overfitting by
combining predictions from multiple trees.

Benefits:

✓ Better Generalization
✓ Higher Accuracy
✓ Robust Predictions
""")

# ----------------------------------------------------------
# Example Decision Trees
# ----------------------------------------------------------

print("\nExample Predictions")
print("-" * 30)

tree_1 = "Pass"
tree_2 = "Pass"
tree_3 = "Fail"
tree_4 = "Pass"
tree_5 = "Pass"

print("Tree 1 Prediction =", tree_1)
print("Tree 2 Prediction =", tree_2)
print("Tree 3 Prediction =", tree_3)
print("Tree 4 Prediction =", tree_4)
print("Tree 5 Prediction =", tree_5)

# ----------------------------------------------------------
# Majority Voting
# ----------------------------------------------------------

print("\nMajority Voting")
print("-" * 30)

predictions = [
    tree_1,
    tree_2,
    tree_3,
    tree_4,
    tree_5
]

pass_votes = predictions.count("Pass")
fail_votes = predictions.count("Fail")

print("Pass Votes =", pass_votes)
print("Fail Votes =", fail_votes)

if pass_votes > fail_votes:
    final_prediction = "Pass"
else:
    final_prediction = "Fail"

print("Final Prediction =", final_prediction)

# ----------------------------------------------------------
# Forest Structure
# ----------------------------------------------------------

print("\nForest Structure")
print("-" * 30)

print("""
                Random Forest
                      |
     ----------------------------------
     |        |        |        |      |
   Tree1    Tree2    Tree3    Tree4  Tree5
     |        |        |        |      |
   Pred     Pred     Pred     Pred   Pred

Final Output = Combined Prediction
""")

# ----------------------------------------------------------
# Bootstrap Sampling
# ----------------------------------------------------------

print("\nBootstrap Sampling")
print("-" * 30)

print("""
Each tree receives a random sample
of the training dataset.

This process is called:

Bootstrap Sampling

Different trees see different
parts of the data.
""")

dataset = [1, 2, 3, 4, 5, 6, 7, 8]

tree_sample = [1, 2, 4, 4, 6, 7]

print("Original Dataset =", dataset)
print("Bootstrap Sample =", tree_sample)

# ----------------------------------------------------------
# Feature Randomness
# ----------------------------------------------------------

print("\nFeature Randomness")
print("-" * 30)

print("""
Random Forest also selects
random subsets of features.

This creates diversity among trees.

Example Features:

✓ Age
✓ Salary
✓ Experience
✓ Education

Each tree may use different features.
""")

# ----------------------------------------------------------
# Classification Example
# ----------------------------------------------------------

print("\nClassification Example")
print("-" * 30)

print("""
Problem:

Email Spam Detection

Trees Predict:

Tree 1 → Spam
Tree 2 → Spam
Tree 3 → Not Spam
Tree 4 → Spam

Final Prediction:

Spam
""")

# ----------------------------------------------------------
# Regression Example
# ----------------------------------------------------------

print("\nRegression Example")
print("-" * 30)

predictions = [
    45000,
    47000,
    46000,
    48000,
    47000
]

average_prediction = (
    sum(predictions) /
    len(predictions)
)

print("Tree Predictions =", predictions)

print("Final Prediction =",
      average_prediction)

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "High Accuracy",
    "Reduces Overfitting",
    "Works for Classification",
    "Works for Regression",
    "Handles Large Datasets",
    "Robust Performance"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "More Computational Cost",
    "Slower Training",
    "Less Interpretable",
    "Large Memory Usage"
]

for item in limitations:
    print("✗", item)

# ----------------------------------------------------------
# Decision Tree vs Random Forest
# ----------------------------------------------------------

print("\nDecision Tree vs Random Forest")
print("-" * 30)

print("""
Decision Tree:

✓ Simple
✓ Easy to Interpret
✗ Can Overfit

Random Forest:

✓ More Accurate
✓ Less Overfitting
✗ More Complex
""")

# ----------------------------------------------------------
# Real World Example
# ----------------------------------------------------------

print("\nLoan Approval Example")
print("-" * 30)

tree_predictions = [
    "Approved",
    "Approved",
    "Rejected",
    "Approved",
    "Approved"
]

approved_votes = tree_predictions.count(
    "Approved"
)

rejected_votes = tree_predictions.count(
    "Rejected"
)

if approved_votes > rejected_votes:
    decision = "Approved"
else:
    decision = "Rejected"

print("Final Loan Decision =", decision)

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Fraud Detection",
    "Medical Diagnosis",
    "Loan Approval",
    "Customer Churn Prediction",
    "Stock Analysis",
    "Recommendation Systems"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nRandom Forest Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Create Bootstrap Samples",
    "Build Multiple Trees",
    "Generate Predictions",
    "Combine Predictions",
    "Evaluate Model"
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

scores = [
    "Pass",
    "Pass",
    "Fail",
    "Pass"
]

pass_count = scores.count("Pass")

if pass_count >= 3:
    result = "Pass"
else:
    result = "Fail"

print("Final Result =", result)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

salary_predictions = [
    30000,
    32000,
    31000,
    33000
]

average_salary = (
    sum(salary_predictions) /
    len(salary_predictions)
)

print("Predicted Salary =",
      average_salary)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Random Forest?

2. How does it make predictions?

3. What is Majority Voting?

4. Why is Random Forest better than
   a single Decision Tree?

5. Give one application.
""")

print("""
Answers:

1. Collection of Decision Trees
2. Combines tree predictions
3. Most common class wins
4. Reduces overfitting
5. Fraud Detection
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 43 Summary")
print("-" * 30)

print("""
1. Random Forest is an
   Ensemble Learning algorithm.

2. It combines multiple
   Decision Trees.

3. Classification uses
   Majority Voting.

4. Regression uses
   Average Prediction.

5. It reduces overfitting and
   improves accuracy.

6. Random Forest is one of the
   most powerful ML algorithms.

7. It is widely used in
   industry applications.
""")

print("\nDay 43 Completed Successfully!")
print("=" * 60)