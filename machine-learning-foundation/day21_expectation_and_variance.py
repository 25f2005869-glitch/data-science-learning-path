# ==========================================================
# Day 21 : Expectation and Variance
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 21")
print("=" * 60)

print("\nExpectation and Variance")
print("-" * 30)

print("""
Expectation and Variance are two of the most
important concepts in Probability and Statistics.

Expectation:
✓ Average Outcome

Variance:
✓ Spread of Data Around the Mean

These concepts are widely used in:

✓ Machine Learning
✓ Data Science
✓ Statistics
✓ Risk Analysis
""")

# ----------------------------------------------------------
# Expectation
# ----------------------------------------------------------

print("\nExpectation (Expected Value)")
print("-" * 30)

print("""
Expectation represents the average outcome
of a random variable over many repetitions.

Formula:

E(X) = Σ [X × P(X)]
""")

# ----------------------------------------------------------
# Dice Example
# ----------------------------------------------------------

print("\nExample 1 : Fair Die")
print("-" * 30)

distribution = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

expected_value = 0

for value, probability in distribution.items():
    expected_value += value * probability

print("Expected Value =", round(expected_value, 2))

# ----------------------------------------------------------
# Student Marks Example
# ----------------------------------------------------------

print("\nExample 2 : Student Marks")
print("-" * 30)

marks_distribution = {
    50: 0.10,
    60: 0.20,
    70: 0.30,
    80: 0.25,
    90: 0.15
}

expected_marks = 0

for mark, probability in marks_distribution.items():
    expected_marks += mark * probability

print("Expected Marks =", round(expected_marks, 2))

# ----------------------------------------------------------
# Variance
# ----------------------------------------------------------

print("\nVariance")
print("-" * 30)

print("""
Variance measures how far values
are spread from the mean.

Small Variance:
✓ Data close to mean

Large Variance:
✓ Data widely spread
""")

# Variance Concept Visualization

# ----------------------------------------------------------
# Variance Example
# ----------------------------------------------------------

print("\nExample 3 : Variance Calculation")
print("-" * 30)

data = [2, 4, 6, 8, 10]

mean = sum(data) / len(data)

print("Data =", data)
print("Mean =", mean)

squared_deviations = []

for value in data:

    deviation = value - mean
    squared_deviation = deviation ** 2

    squared_deviations.append(squared_deviation)

print("Squared Deviations =")
print(squared_deviations)

variance = sum(squared_deviations) / len(data)

print("Variance =", variance)

# ----------------------------------------------------------
# Standard Deviation
# ----------------------------------------------------------

print("\nStandard Deviation")
print("-" * 30)

standard_deviation = variance ** 0.5

print("Standard Deviation =",
      round(standard_deviation, 2))

print("""
Standard Deviation is simply
the square root of Variance.
""")

# ----------------------------------------------------------
# Compare Two Datasets
# ----------------------------------------------------------

print("\nExample 4 : Comparing Variance")
print("-" * 30)

dataset_A = [48, 49, 50, 51, 52]
dataset_B = [20, 35, 50, 65, 80]

mean_A = sum(dataset_A) / len(dataset_A)
mean_B = sum(dataset_B) / len(dataset_B)

variance_A = sum(
    (x - mean_A) ** 2
    for x in dataset_A
) / len(dataset_A)

variance_B = sum(
    (x - mean_B) ** 2
    for x in dataset_B
) / len(dataset_B)

print("Dataset A Variance =", variance_A)
print("Dataset B Variance =", variance_B)

print("""
Dataset B has larger variance.

Therefore,
Dataset B is more spread out.
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nExpectation and Variance in ML")
print("-" * 30)

applications = [
    "Feature Analysis",
    "Data Preprocessing",
    "Anomaly Detection",
    "Model Evaluation",
    "Risk Analysis",
    "Statistical Learning"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Practical Dataset Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

student_scores = [60, 70, 75, 80, 90]

average_score = (
    sum(student_scores) /
    len(student_scores)
)

print("Scores =", student_scores)
print("Average =", average_score)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

practice_data = [1, 2, 3, 4, 5]

practice_mean = (
    sum(practice_data) /
    len(practice_data)
)

practice_variance = sum(
    (x - practice_mean) ** 2
    for x in practice_data
) / len(practice_data)

print("Mean =", practice_mean)
print("Variance =", practice_variance)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Expectation?

2. What is Variance?

3. What does high variance indicate?

4. What is Standard Deviation?

5. Why are Expectation and Variance
   important in ML?
""")

print("""
Answers:

1. Average outcome
2. Spread of data around mean
3. Data is widely spread
4. Square root of variance
5. They help understand
   data distribution
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 21 Summary")
print("-" * 30)

print("""
1. Expectation represents average outcome.
2. Variance measures spread around the mean.
3. Standard Deviation is the square root
   of Variance.
4. High Variance means greater spread.
5. These concepts are fundamental
   in Machine Learning and Statistics.
""")

print("\nDay 21 Completed Successfully!")
print("=" * 60)