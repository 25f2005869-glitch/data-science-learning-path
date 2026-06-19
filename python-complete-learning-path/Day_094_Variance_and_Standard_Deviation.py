# ======================================
# Day 094: Variance and Standard Deviation
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Variance and
# Standard Deviation in Statistics
# ======================================

print("=" * 60)
print("DAY 094 - VARIANCE AND STANDARD DEVIATION")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

from statistics import (
    variance,
    stdev,
    mean
)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Variance and Standard Deviation
measure the spread of data.

Questions Answered:

1. How far are values
   from the mean?

2. Is the dataset
   consistent?

Applications:

1. Machine Learning
2. Data Science
3. Risk Analysis
4. Finance
5. Research
"""

# ======================================
# SAMPLE DATASET
# ======================================

marks = [
    92,
    88,
    95,
    81,
    90
]

print("\nDATASET")
print(marks)

# ======================================
# MEAN
# ======================================

print("\nMEAN")

mean_value = mean(
    marks
)

print(
    "Mean:",
    round(
        mean_value,
        2
    )
)

# ======================================
# VARIANCE
# ======================================

print("\nVARIANCE")

variance_value = variance(
    marks
)

print(
    "Variance:",
    round(
        variance_value,
        2
    )
)

# ======================================
# STANDARD DEVIATION
# ======================================

print("\nSTANDARD DEVIATION")

std_value = stdev(
    marks
)

print(
    "Standard Deviation:",
    round(
        std_value,
        2
    )
)

# ======================================
# MANUAL DEVIATIONS
# ======================================

print("\nDEVIATIONS FROM MEAN")

for mark in marks:

    deviation = (
        mark -
        mean_value
    )

    print(
        f"{mark} -> "
        f"{round(deviation,2)}"
    )

# ======================================
# ATTENDANCE DATA
# ======================================

print("\nATTENDANCE DATA")

attendance = [
    95,
    88,
    97,
    82,
    91
]

print(
    "Variance:",
    round(
        variance(attendance),
        2
    )
)

print(
    "Standard Deviation:",
    round(
        stdev(attendance),
        2
    )
)

# ======================================
# SALARY DATA
# ======================================

print("\nSALARY DATA")

salary = [
    25000,
    30000,
    35000,
    40000,
    45000
]

print(
    "Mean Salary:",
    mean(salary)
)

print(
    "Variance:",
    round(
        variance(salary),
        2
    )
)

print(
    "Standard Deviation:",
    round(
        stdev(salary),
        2
    )
)

# ======================================
# LOW VARIANCE DATA
# ======================================

print("\nLOW VARIANCE DATA")

data1 = [
    89,
    90,
    91,
    90,
    89
]

print(data1)

print(
    "Variance:",
    round(
        variance(data1),
        2
    )
)

# ======================================
# HIGH VARIANCE DATA
# ======================================

print("\nHIGH VARIANCE DATA")

data2 = [
    50,
    70,
    90,
    110,
    130
]

print(data2)

print(
    "Variance:",
    round(
        variance(data2),
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
    "Variance:",
    round(
        variance(user_data),
        2
    )
)

print(
    "Standard Deviation:",
    round(
        stdev(user_data),
        2
    )
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

student_scores = [
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
    "Variance:",
    round(
        variance(student_scores),
        2
    )
)

print(
    "Standard Deviation:",
    round(
        stdev(student_scores),
        2
    )
)

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Variance:
Spread of Data

Standard Deviation:
Square Root of Variance

Low Variance:
Data close to Mean

High Variance:
Data far from Mean
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Calculate Variance.

Exercise 2:
Calculate Standard Deviation.

Exercise 3:
Compare two datasets.

Exercise 4:
Identify which dataset
has higher spread.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Variance?

Q2. What is Standard Deviation?

Q3. Why are they important?

Q4. Difference between
Variance and Standard
Deviation?

Q5. What does high
variance indicate?

Q6. What does low
variance indicate?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics System.

Input:

1. Student Marks

Generate:

1. Mean
2. Variance
3. Standard Deviation

Analyze consistency.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 094 Completed Successfully!"
)