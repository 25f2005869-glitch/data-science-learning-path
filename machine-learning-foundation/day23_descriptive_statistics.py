# ==========================================================
# Day 23 : Descriptive Statistics
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 23")
print("=" * 60)

print("\nDescriptive Statistics")
print("-" * 30)

print("""
Descriptive Statistics is used to summarize,
organize, and understand data.

It answers questions like:

✓ What is the average?
✓ What is the middle value?
✓ Which value occurs most often?
✓ How spread out is the data?

Descriptive Statistics is one of the most
important tools in Data Science and ML.
""")

# ----------------------------------------------------------
# Sample Dataset
# ----------------------------------------------------------

print("\nSample Dataset")
print("-" * 30)

data = [10, 20, 20, 30, 40, 50, 50, 50, 60]

print("Data =", data)

# ----------------------------------------------------------
# Mean
# ----------------------------------------------------------

print("\n1. Mean")
print("-" * 30)

mean = sum(data) / len(data)

print("Mean =", round(mean, 2))

print("""
Mean is the average value.

Formula:

Mean = Sum of Values / Number of Values
""")

# ----------------------------------------------------------
# Median
# ----------------------------------------------------------

print("\n2. Median")
print("-" * 30)

sorted_data = sorted(data)

n = len(sorted_data)

median = sorted_data[n // 2]

print("Sorted Data =", sorted_data)
print("Median =", median)

print("""
Median is the middle value
of a sorted dataset.
""")

# ----------------------------------------------------------
# Mode
# ----------------------------------------------------------

print("\n3. Mode")
print("-" * 30)

frequency = {}

for value in data:

    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

mode = max(frequency, key=frequency.get)

print("Mode =", mode)

print("""
Mode is the most frequently
occurring value.
""")

# ----------------------------------------------------------
# Range
# ----------------------------------------------------------

print("\n4. Range")
print("-" * 30)

data_range = max(data) - min(data)

print("Range =", data_range)

print("""
Range = Maximum - Minimum
""")

# ----------------------------------------------------------
# Variance
# ----------------------------------------------------------

print("\n5. Variance")
print("-" * 30)

variance = sum(
    (x - mean) ** 2
    for x in data
) / len(data)

print("Variance =", round(variance, 2))

# Variance Visualization

# ----------------------------------------------------------
# Standard Deviation
# ----------------------------------------------------------

print("\n6. Standard Deviation")
print("-" * 30)

standard_deviation = variance ** 0.5

print("Standard Deviation =",
      round(standard_deviation, 2))

# ----------------------------------------------------------
# Five Number Summary
# ----------------------------------------------------------

print("\n7. Five Number Summary")
print("-" * 30)

minimum = min(data)
maximum = max(data)

print("Minimum =", minimum)
print("Maximum =", maximum)

print("""
Five Number Summary:

✓ Minimum
✓ Q1
✓ Median
✓ Q3
✓ Maximum
""")

# ----------------------------------------------------------
# Dataset Comparison
# ----------------------------------------------------------

print("\nDataset Comparison")
print("-" * 30)

dataset_A = [48, 49, 50, 51, 52]
dataset_B = [10, 30, 50, 70, 90]

mean_A = sum(dataset_A) / len(dataset_A)
mean_B = sum(dataset_B) / len(dataset_B)

print("Mean A =", mean_A)
print("Mean B =", mean_B)

print("""
Both datasets have similar centers,
but different spreads.
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nDescriptive Statistics in ML")
print("-" * 30)

applications = [
    "Data Understanding",
    "Exploratory Data Analysis",
    "Feature Engineering",
    "Data Cleaning",
    "Outlier Detection",
    "Model Preparation"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Student Marks Example
# ----------------------------------------------------------

print("\nStudent Marks Example")
print("-" * 30)

marks = [55, 60, 65, 70, 75, 80, 85]

mean_marks = sum(marks) / len(marks)

print("Marks =", marks)
print("Average Marks =", round(mean_marks, 2))

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

temperatures = [28, 29, 30, 31, 32]

avg_temp = sum(temperatures) / len(temperatures)

print("Temperatures =", temperatures)
print("Average Temperature =", avg_temp)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

practice_data = [5, 10, 15, 20, 25]

practice_mean = (
    sum(practice_data) /
    len(practice_data)
)

practice_range = (
    max(practice_data) -
    min(practice_data)
)

print("Mean =", practice_mean)
print("Range =", practice_range)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Mean?

2. What is Median?

3. What is Mode?

4. What is Range?

5. Why is Descriptive Statistics
   important in ML?
""")

print("""
Answers:

1. Average value
2. Middle value
3. Most frequent value
4. Maximum - Minimum
5. Helps understand and
   summarize data
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 23 Summary")
print("-" * 30)

print("""
1. Descriptive Statistics summarizes data.
2. Mean measures average value.
3. Median measures center value.
4. Mode identifies frequent values.
5. Range measures spread.
6. Variance and SD measure variability.
7. Descriptive Statistics is essential
   for Data Science and Machine Learning.
""")

print("\nDay 23 Completed Successfully!")
print("=" * 60)