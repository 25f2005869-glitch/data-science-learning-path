# ==========================================================
# Day 22 : Standard Deviation
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 22")
print("=" * 60)

print("\nStandard Deviation")
print("-" * 30)

print("""
Standard Deviation measures how much
data values deviate from the mean.

It is one of the most important measures
of data spread in Statistics and ML.

Small Standard Deviation:
✓ Data close to mean

Large Standard Deviation:
✓ Data spread far from mean
""")

# ----------------------------------------------------------
# Dataset Example
# ----------------------------------------------------------

print("\nDataset Example")
print("-" * 30)

data = [2, 4, 6, 8, 10]

print("Data =", data)

# ----------------------------------------------------------
# Mean Calculation
# ----------------------------------------------------------

print("\nStep 1 : Calculate Mean")
print("-" * 30)

mean = sum(data) / len(data)

print("Mean =", mean)

# ----------------------------------------------------------
# Deviation Calculation
# ----------------------------------------------------------

print("\nStep 2 : Calculate Deviations")
print("-" * 30)

deviations = []

for value in data:

    deviation = value - mean
    deviations.append(deviation)

print("Deviations =")
print(deviations)

# ----------------------------------------------------------
# Squared Deviations
# ----------------------------------------------------------

print("\nStep 3 : Squared Deviations")
print("-" * 30)

squared_deviations = []

for deviation in deviations:

    squared_deviation = deviation ** 2
    squared_deviations.append(squared_deviation)

print("Squared Deviations =")
print(squared_deviations)

# ----------------------------------------------------------
# Variance Calculation
# ----------------------------------------------------------

print("\nStep 4 : Variance")
print("-" * 30)

variance = (
    sum(squared_deviations) /
    len(data)
)

print("Variance =", variance)

# ----------------------------------------------------------
# Standard Deviation Calculation
# ----------------------------------------------------------

print("\nStep 5 : Standard Deviation")
print("-" * 30)

standard_deviation = variance ** 0.5

print("Standard Deviation =",
      round(standard_deviation, 2))

print("""
Formula:

Standard Deviation = √Variance
""")

# ----------------------------------------------------------
# Standard Deviation Visualization
# ----------------------------------------------------------

# ----------------------------------------------------------
# Example 2 : Student Marks
# ----------------------------------------------------------

print("\nExample 2 : Student Marks")
print("-" * 30)

marks = [60, 65, 70, 75, 80]

mean_marks = sum(marks) / len(marks)

variance_marks = sum(
    (x - mean_marks) ** 2
    for x in marks
) / len(marks)

std_marks = variance_marks ** 0.5

print("Marks =", marks)
print("Mean =", mean_marks)
print("Variance =", round(variance_marks, 2))
print("Standard Deviation =",
      round(std_marks, 2))

# ----------------------------------------------------------
# Low vs High Standard Deviation
# ----------------------------------------------------------

print("\nLow vs High Standard Deviation")
print("-" * 30)

dataset_A = [49, 50, 51, 50, 50]
dataset_B = [10, 30, 50, 70, 90]

mean_A = sum(dataset_A) / len(dataset_A)
mean_B = sum(dataset_B) / len(dataset_B)

std_A = (
    sum((x - mean_A) ** 2
        for x in dataset_A)
    / len(dataset_A)
) ** 0.5

std_B = (
    sum((x - mean_B) ** 2
        for x in dataset_B)
    / len(dataset_B)
) ** 0.5

print("Dataset A SD =", round(std_A, 2))
print("Dataset B SD =", round(std_B, 2))

print("""
Dataset A:
Low Spread

Dataset B:
High Spread
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nStandard Deviation in ML")
print("-" * 30)

applications = [
    "Feature Scaling",
    "Data Analysis",
    "Outlier Detection",
    "Anomaly Detection",
    "Model Evaluation",
    "Data Preprocessing"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Z-Score Introduction
# ----------------------------------------------------------

print("\nIntroduction to Z-Score")
print("-" * 30)

print("""
Z-Score tells us how far
a value is from the mean.

Formula:

Z = (X - Mean) / SD
""")

mean = 70
sd = 10
score = 85

z_score = (score - mean) / sd

print("Score =", score)
print("Mean =", mean)
print("SD =", sd)
print("Z-Score =", round(z_score, 2))

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

temperatures = [28, 30, 31, 29, 32]

avg_temp = (
    sum(temperatures) /
    len(temperatures)
)

variance_temp = sum(
    (x - avg_temp) ** 2
    for x in temperatures
) / len(temperatures)

sd_temp = variance_temp ** 0.5

print("Temperatures =", temperatures)
print("Mean =", round(avg_temp, 2))
print("SD =", round(sd_temp, 2))

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

practice = [1, 2, 3, 4, 5]

mean_p = sum(practice) / len(practice)

variance_p = sum(
    (x - mean_p) ** 2
    for x in practice
) / len(practice)

sd_p = variance_p ** 0.5

print("Standard Deviation =",
      round(sd_p, 2))

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Standard Deviation?

2. What does a low SD indicate?

3. What does a high SD indicate?

4. How is SD related to Variance?

5. Why is SD useful in ML?
""")

print("""
Answers:

1. Measure of data spread
2. Data close to mean
3. Data widely spread
4. SD = √Variance
5. Helps analyze distributions
   and detect anomalies
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 22 Summary")
print("-" * 30)

print("""
1. Standard Deviation measures spread.
2. It is the square root of variance.
3. Low SD means less variability.
4. High SD means more variability.
5. SD is important in ML,
   Statistics, and Data Analysis.
""")

print("\nDay 22 Completed Successfully!")
print("=" * 60)