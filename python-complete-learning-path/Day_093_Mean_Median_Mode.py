# ======================================
# Day 093: Mean, Median, Mode
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Mean, Median,
# and Mode in Statistics
# ======================================

print("=" * 60)
print("DAY 093 - MEAN, MEDIAN, MODE")
print("=" * 60)

# ======================================
# IMPORT LIBRARY
# ======================================

from statistics import (
    mean,
    median,
    mode
)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Measures of Central Tendency

1. Mean
2. Median
3. Mode

These measures represent
the center of a dataset.

Applications:

1. Data Science
2. Machine Learning
3. Business Analytics
4. Research
5. Economics
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
# MEDIAN
# ======================================

print("\nMEDIAN")

median_value = median(
    marks
)

print(
    "Median:",
    median_value
)

# ======================================
# MODE
# ======================================

print("\nMODE")

mode_data = [
    90,
    85,
    90,
    88,
    90,
    92
]

print(
    "Mode Dataset:",
    mode_data
)

mode_value = mode(
    mode_data
)

print(
    "Mode:",
    mode_value
)

# ======================================
# MANUAL MEAN
# ======================================

print("\nMANUAL MEAN")

manual_mean = (
    sum(marks) /
    len(marks)
)

print(
    "Manual Mean:",
    round(
        manual_mean,
        2
    )
)

# ======================================
# ODD DATASET MEDIAN
# ======================================

print("\nODD DATASET")

odd_data = [
    10,
    20,
    30,
    40,
    50
]

print(
    "Median:",
    median(
        odd_data
    )
)

# ======================================
# EVEN DATASET MEDIAN
# ======================================

print("\nEVEN DATASET")

even_data = [
    10,
    20,
    30,
    40
]

print(
    "Median:",
    median(
        even_data
    )
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
    "Mean Attendance:",
    round(
        mean(attendance),
        2
    )
)

print(
    "Median Attendance:",
    median(attendance)
)

# ======================================
# SALARY EXAMPLE
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
    "Median Salary:",
    median(salary)
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

print(
    "Median:",
    median(user_data)
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
    95,
    90,
    90
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
    "Median:",
    median(student_scores)
)

print(
    "Mode:",
    mode(student_scores)
)

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Mean:
Average Value

Median:
Middle Value

Mode:
Most Frequent Value
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Find Mean.

Exercise 2:
Find Median.

Exercise 3:
Find Mode.

Exercise 4:
Compare all three
measures.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Mean?

Q2. What is Median?

Q3. What is Mode?

Q4. Difference between
Mean and Median?

Q5. When is Mode useful?

Q6. What are Measures
of Central Tendency?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Statistics System.

Input:

1. Student Marks

Generate:

1. Mean
2. Median
3. Mode

Display Report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 093 Completed Successfully!"
)