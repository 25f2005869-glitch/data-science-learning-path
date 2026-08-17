# ==========================================================
# Day 44 : K-Nearest Neighbors (KNN)
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 44")
print("=" * 60)

print("\nK-Nearest Neighbors (KNN)")
print("-" * 30)

print("""
K-Nearest Neighbors (KNN) is a simple
and powerful Supervised Learning algorithm.

It can be used for:

✓ Classification
✓ Regression

KNN makes predictions based on the
nearest data points in the dataset.
""")

# ----------------------------------------------------------
# What is KNN?
# ----------------------------------------------------------

print("\nWhat is KNN?")
print("-" * 30)

print("""
KNN stands for:

K → Number of Neighbors
NN → Nearest Neighbors

Idea:

Find the K nearest data points.

Use their values or labels
to make a prediction.
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]

results = [
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

for hour, result in zip(
        study_hours,
        results):

    print(hour, "Hours →", result)

# ----------------------------------------------------------
# New Student Prediction
# ----------------------------------------------------------

print("\nNew Student")
print("-" * 30)

new_student_hours = 7

print("Study Hours =", new_student_hours)

print("""
Goal:

Predict Pass or Fail
using nearest neighbors.
""")

# ----------------------------------------------------------
# Distance Calculation
# ----------------------------------------------------------

print("\nDistance Calculation")
print("-" * 30)

distances = []

for hour in study_hours:

    distance = abs(
        new_student_hours - hour
    )

    distances.append(distance)

print("Distances =", distances)

# ----------------------------------------------------------
# Nearest Neighbors
# ----------------------------------------------------------

print("\nNearest Neighbors")
print("-" * 30)

neighbor_data = []

for hour, result in zip(
        study_hours,
        results):

    distance = abs(
        new_student_hours - hour
    )

    neighbor_data.append(
        (distance, result)
    )

neighbor_data.sort()

print("Sorted Neighbors:")

for item in neighbor_data:

    print(item)

# ----------------------------------------------------------
# K = 3 Example
# ----------------------------------------------------------

print("\nK = 3")
print("-" * 30)

k = 3

nearest_neighbors = neighbor_data[:k]

print("Nearest Neighbors:")

for item in nearest_neighbors:

    print(item)

# ----------------------------------------------------------
# Majority Voting
# ----------------------------------------------------------

print("\nMajority Voting")
print("-" * 30)

votes = []

for item in nearest_neighbors:

    votes.append(item[1])

pass_votes = votes.count("Pass")
fail_votes = votes.count("Fail")

print("Pass Votes =", pass_votes)
print("Fail Votes =", fail_votes)

if pass_votes > fail_votes:

    prediction = "Pass"

else:

    prediction = "Fail"

print("Predicted Class =", prediction)

# ----------------------------------------------------------
# Understanding K
# ----------------------------------------------------------

print("\nChoosing K")
print("-" * 30)

print("""
Small K:

✓ Sensitive to Noise
✓ More Flexible

Large K:

✓ More Stable
✓ May Ignore Details

Common Choices:

K = 3
K = 5
K = 7
""")

# ----------------------------------------------------------
# Classification Example
# ----------------------------------------------------------

print("\nClassification Example")
print("-" * 30)

print("""
Problem:

Pass / Fail Prediction

KNN finds nearest students
and predicts the majority class.
""")

# ----------------------------------------------------------
# Regression Example
# ----------------------------------------------------------

print("\nRegression Example")
print("-" * 30)

neighbor_prices = [
    200000,
    220000,
    210000
]

average_price = (
    sum(neighbor_prices) /
    len(neighbor_prices)
)

print("Neighbor Prices =", neighbor_prices)

print("Predicted Price =",
      average_price)

# ----------------------------------------------------------
# Euclidean Distance
# ----------------------------------------------------------

print("\nEuclidean Distance")
print("-" * 30)

print("""
Most common distance metric.

Formula:

Distance =
√((x2 - x1)^2 + (y2 - y1)^2)

Used to measure similarity
between points.
""")

# Example

x1 = 2
y1 = 3

x2 = 5
y2 = 7

distance = (
    ((x2 - x1) ** 2) +
    ((y2 - y1) ** 2)
) ** 0.5

print("Distance =",
      round(distance, 2))

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Easy to Understand",
    "Simple Implementation",
    "No Training Phase",
    "Works for Classification",
    "Works for Regression"
]

for item in advantages:

    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Slow for Large Datasets",
    "Sensitive to Noise",
    "Requires Feature Scaling",
    "Memory Intensive"
]

for item in limitations:

    print("✗", item)

# ----------------------------------------------------------
# Feature Scaling Importance
# ----------------------------------------------------------

print("\nFeature Scaling")
print("-" * 30)

print("""
KNN relies on distances.

Features with larger values
can dominate distance calculations.

Therefore:

✓ Normalization
✓ Standardization

are important before using KNN.
""")

# ----------------------------------------------------------
# Real World Example
# ----------------------------------------------------------

print("\nMovie Recommendation")
print("-" * 30)

print("""
Users with similar preferences
are considered neighbors.

KNN recommends movies liked
by similar users.
""")

# ----------------------------------------------------------
# Medical Diagnosis Example
# ----------------------------------------------------------

print("\nMedical Diagnosis")
print("-" * 30)

print("""
Patients with similar symptoms
can help predict diseases.

KNN compares new patients with
previous patient records.
""")

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Recommendation Systems",
    "Medical Diagnosis",
    "Image Recognition",
    "Pattern Recognition",
    "Fraud Detection",
    "Customer Segmentation"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nKNN Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Choose K",
    "Calculate Distances",
    "Find Nearest Neighbors",
    "Vote or Average",
    "Make Prediction"
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

neighbor_marks = [
    75,
    80,
    85
]

predicted_marks = (
    sum(neighbor_marks) /
    len(neighbor_marks)
)

print("Predicted Marks =",
      predicted_marks)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

k = 5

print("""
Question:

What does K represent?

Answer:

Number of Nearest Neighbors
""")

print("K =", k)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What does KNN stand for?

2. Is KNN used for Classification,
   Regression, or Both?

3. What is K?

4. Which distance metric is most common?

5. Give one application of KNN.
""")

print("""
Answers:

1. K-Nearest Neighbors
2. Both
3. Number of Neighbors
4. Euclidean Distance
5. Recommendation Systems
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 44 Summary")
print("-" * 30)

print("""
1. KNN is a Supervised Learning algorithm.

2. It works for:

   ✓ Classification
   ✓ Regression

3. Predictions are based on
   nearest neighbors.

4. K determines the number of
   neighbors considered.

5. Euclidean Distance is commonly used.

6. Feature Scaling is important.

7. KNN is simple, intuitive,
   and widely used.
""")

print("\nDay 44 Completed Successfully!")
print("=" * 60)