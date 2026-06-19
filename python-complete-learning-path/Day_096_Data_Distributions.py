# ======================================
# Day 096: Data Distributions
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Data Distributions
# in Statistics and Data Science
# ======================================

print("=" * 60)
print("DAY 096 - DATA DISTRIBUTIONS")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import random
from statistics import mean

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Data Distribution?

A Data Distribution describes
how data values are spread
across a dataset.

Why Important?

1. Understand Patterns
2. Detect Outliers
3. Prepare ML Models
4. Analyze Data Behavior

Common Distributions:

1. Uniform Distribution
2. Normal Distribution
3. Skewed Distribution
"""

# ======================================
# SAMPLE DATASET
# ======================================

marks = [
    78,
    82,
    85,
    88,
    90,
    92,
    95
]

print("\nDATASET")
print(marks)

# ======================================
# MEAN
# ======================================

print("\nMEAN")

average = mean(marks)

print(
    "Mean:",
    round(
        average,
        2
    )
)

# ======================================
# MINIMUM AND MAXIMUM
# ======================================

print("\nMINIMUM AND MAXIMUM")

print(
    "Minimum:",
    min(marks)
)

print(
    "Maximum:",
    max(marks)
)

# ======================================
# RANGE
# ======================================

print("\nRANGE")

range_value = (
    max(marks) -
    min(marks)
)

print(
    "Range:",
    range_value
)

# ======================================
# UNIFORM DISTRIBUTION
# ======================================

print("\nUNIFORM DISTRIBUTION")

uniform_data = [
    10,
    20,
    30,
    40,
    50
]

print(
    uniform_data
)

print(
    "Mean:",
    mean(uniform_data)
)

# ======================================
# NORMAL-LIKE DISTRIBUTION
# ======================================

print("\nNORMAL-LIKE DISTRIBUTION")

normal_data = [
    60,
    70,
    75,
    80,
    82,
    85,
    90,
    95,
    100
]

print(
    normal_data
)

print(
    "Mean:",
    round(
        mean(normal_data),
        2
    )
)

# ======================================
# RIGHT SKEWED DATA
# ======================================

print("\nRIGHT SKEWED DATA")

right_skewed = [
    10,
    12,
    15,
    18,
    20,
    50
]

print(
    right_skewed
)

# ======================================
# LEFT SKEWED DATA
# ======================================

print("\nLEFT SKEWED DATA")

left_skewed = [
    5,
    40,
    42,
    45,
    48,
    50
]

print(
    left_skewed
)

# ======================================
# RANDOM DATA GENERATION
# ======================================

print("\nRANDOM DATA")

random_data = []

for i in range(10):

    random_data.append(
        random.randint(
            1,
            100
        )
    )

print(
    random_data
)

# ======================================
# DISTRIBUTION ANALYSIS
# ======================================

print("\nDISTRIBUTION ANALYSIS")

print(
    "Count:",
    len(random_data)
)

print(
    "Minimum:",
    min(random_data)
)

print(
    "Maximum:",
    max(random_data)
)

print(
    "Mean:",
    round(
        mean(random_data),
        2
    )
)

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

num1 = int(
    input(
        "Enter Number 1: "
    )
)

num2 = int(
    input(
        "Enter Number 2: "
    )
)

num3 = int(
    input(
        "Enter Number 3: "
    )
)

user_data = [
    num1,
    num2,
    num3
]

print(
    "Mean:",
    round(
        mean(user_data),
        2
    )
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

student_scores = [
    65,
    70,
    75,
    80,
    85,
    90,
    95
]

print(
    "Scores:",
    student_scores
)

print(
    "Mean:",
    round(
        mean(student_scores),
        2
    )
)

print(
    "Range:",
    max(student_scores)
    -
    min(student_scores)
)

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Distribution

Uniform Distribution

Normal Distribution

Skewed Distribution

Outlier
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create Uniform Data.

Exercise 2:
Create Normal-like Data.

Exercise 3:
Create Right Skewed Data.

Exercise 4:
Find Range and Mean.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is a Distribution?

Q2. Why are Distributions
important?

Q3. What is Uniform
Distribution?

Q4. What is Normal
Distribution?

Q5. What is Skewness?

Q6. What is an Outlier?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analysis System.

Input:

1. Student Marks

Generate:

1. Mean
2. Minimum
3. Maximum
4. Range

Identify Distribution Pattern.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 096 Completed Successfully!"
)