# ==========================================================
# Day 41 : Logistic Regression Introduction
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 41")
print("=" * 60)

print("\nLogistic Regression Introduction")
print("-" * 30)

print("""
Logistic Regression is one of the most
important Classification Algorithms.

Despite its name, Logistic Regression
is used for Classification problems,
not Regression problems.

It predicts probabilities and assigns
data points to classes.

Examples:

✓ Spam Detection
✓ Disease Prediction
✓ Pass/Fail Prediction
✓ Fraud Detection
✓ Customer Churn Prediction
""")

# ----------------------------------------------------------
# What is Logistic Regression?
# ----------------------------------------------------------

print("\nWhat is Logistic Regression?")
print("-" * 30)

print("""
Logistic Regression is a Supervised
Machine Learning Algorithm used for
Classification tasks.

Input:
Features

Output:
Probability of belonging to a class

Example:

Study Hours → Pass or Fail
""")

# ----------------------------------------------------------
# Classification Problem Example
# ----------------------------------------------------------

print("\nClassification Example")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]

results = [
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

print("Study Hours =", study_hours)
print("Results     =", results)

# ----------------------------------------------------------
# Why Not Linear Regression?
# ----------------------------------------------------------

print("\nWhy Not Linear Regression?")
print("-" * 30)

print("""
Linear Regression can produce
values less than 0 or greater than 1.

Example:

Predicted Probability = 1.5

This is not valid.

Probabilities must always
remain between 0 and 1.
""")

# ----------------------------------------------------------
# Logistic Regression Solution
# ----------------------------------------------------------

print("\nLogistic Regression Solution")
print("-" * 30)

print("""
Logistic Regression uses a
Sigmoid Function.

The Sigmoid Function converts
any number into a value
between 0 and 1.
""")

# ----------------------------------------------------------
# Sigmoid Function
# ----------------------------------------------------------

print("\nSigmoid Function")
print("-" * 30)

print("""
Formula:

P = 1 / (1 + e^(-z))

Where:

P = Probability
e = Euler's Number
z = Linear Combination
""")

# ----------------------------------------------------------
# Example Sigmoid Calculation
# ----------------------------------------------------------

print("\nExample Sigmoid Output")
print("-" * 30)

z_values = [-4, -2, 0, 2, 4]

for z in z_values:

    probability = (
        1 /
        (1 + (2.71828 ** (-z)))
    )

    print(
        "z =",
        z,
        "| Probability =",
        round(probability, 4)
    )

# ----------------------------------------------------------
# Probability Interpretation
# ----------------------------------------------------------

print("\nProbability Interpretation")
print("-" * 30)

print("""
Probability > 0.5

→ Positive Class

Probability < 0.5

→ Negative Class
""")

# ----------------------------------------------------------
# Pass/Fail Example
# ----------------------------------------------------------

print("\nPass/Fail Prediction")
print("-" * 30)

probability_pass = 0.82

print("Probability =", probability_pass)

if probability_pass >= 0.5:

    prediction = "Pass"

else:

    prediction = "Fail"

print("Prediction =", prediction)

# ----------------------------------------------------------
# Binary Classification
# ----------------------------------------------------------

print("\nBinary Classification")
print("-" * 30)

print("""
Logistic Regression is mainly used
for Binary Classification.

Examples:

0 → No
1 → Yes

0 → Fail
1 → Pass

0 → Spam
1 → Not Spam
""")

# ----------------------------------------------------------
# Multi-Class Classification
# ----------------------------------------------------------

print("\nMulti-Class Classification")
print("-" * 30)

print("""
Logistic Regression can also be
extended to Multi-Class problems.

Examples:

Grade A
Grade B
Grade C
Grade D
""")

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
    0,
    0,
    1,
    1,
    1
]

print("Features =", features)
print("Labels   =", labels)

print("""
0 = Fail
1 = Pass
""")

# ----------------------------------------------------------
# Logistic Regression Workflow
# ----------------------------------------------------------

print("\nWorkflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Preprocess Data",
    "Train Model",
    "Calculate Probabilities",
    "Assign Classes",
    "Evaluate Performance"
]

for i, step in enumerate(steps, start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Real World Example
# ----------------------------------------------------------

print("\nEmail Spam Detection")
print("-" * 30)

emails = [
    "Win Money",
    "Meeting Reminder",
    "Free Gift",
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
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Simple and Fast",
    "Easy to Interpret",
    "Works Well for Binary Classification",
    "Probability Output",
    "Computationally Efficient"
]

for item in advantages:

    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Assumes Linear Decision Boundary",
    "Sensitive to Outliers",
    "May Underperform on Complex Data"
]

for item in limitations:

    print("✗", item)

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Spam Detection",
    "Fraud Detection",
    "Medical Diagnosis",
    "Customer Churn Prediction",
    "Marketing Analytics",
    "Risk Assessment"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

probability = 0.73

if probability >= 0.5:

    prediction = "Positive"

else:

    prediction = "Negative"

print("Probability =", probability)
print("Predicted Class =", prediction)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

probability = 0.35

if probability >= 0.5:

    result = "Pass"

else:

    result = "Fail"

print("Probability =", probability)
print("Result =", result)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Logistic Regression?

2. Is Logistic Regression used for
   Regression or Classification?

3. What does the Sigmoid Function do?

4. What is Binary Classification?

5. Give one application of
   Logistic Regression.
""")

print("""
Answers:

1. Classification Algorithm
2. Classification
3. Converts values into probabilities
4. Two-class prediction problem
5. Spam Detection
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 41 Summary")
print("-" * 30)

print("""
1. Logistic Regression is a
   Classification Algorithm.

2. It predicts probabilities.

3. The Sigmoid Function maps
   values between 0 and 1.

4. It is mainly used for
   Binary Classification.

5. Outputs are converted into classes
   using a threshold (usually 0.5).

6. Logistic Regression is one of the
   most widely used ML algorithms.

7. It forms the foundation of many
   classification systems.
""")

print("\nDay 41 Completed Successfully!")
print("=" * 60)