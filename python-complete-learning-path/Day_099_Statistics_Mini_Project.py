# ======================================
# Day 099: Statistics Mini Project
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Student Statistics Analysis System
# Mini Project
# ======================================

print("=" * 60)
print("DAY 099 - STATISTICS MINI PROJECT")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

from statistics import (
    mean,
    median,
    mode,
    variance,
    stdev
)

# ======================================
# PROJECT OVERVIEW
# ======================================

"""
PROJECT:

Student Statistics Analysis System

Concepts Used:

1. Mean
2. Median
3. Mode
4. Variance
5. Standard Deviation
6. Range
7. Probability Concept
8. Data Analysis

Goal:

Analyze student performance
using statistical methods.
"""

# ======================================
# DATASET
# ======================================

marks = [
    92,
    88,
    95,
    81,
    90,
    85,
    87,
    91,
    89,
    93
]

print("\nSTUDENT MARKS")
print(marks)

# ======================================
# BASIC STATISTICS
# ======================================

print("\nBASIC STATISTICS")

print(
    "Total Students:",
    len(marks)
)

print(
    "Total Marks:",
    sum(marks)
)

print(
    "Highest Marks:",
    max(marks)
)

print(
    "Lowest Marks:",
    min(marks)
)

# ======================================
# RANGE
# ======================================

range_value = (
    max(marks)
    -
    min(marks)
)

print(
    "Range:",
    range_value
)

# ======================================
# MEAN
# ======================================

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

mode_data = [
    90,
    90,
    88,
    92,
    90,
    85
]

print(
    "Mode Dataset:",
    mode_data
)

print(
    "Mode:",
    mode(
        mode_data
    )
)

# ======================================
# VARIANCE
# ======================================

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
# PERFORMANCE ANALYSIS
# ======================================

print("\nPERFORMANCE ANALYSIS")

if mean_value >= 90:

    print(
        "Excellent Performance"
    )

elif mean_value >= 80:

    print(
        "Good Performance"
    )

else:

    print(
        "Needs Improvement"
    )

# ======================================
# STUDENT GRADES
# ======================================

print("\nGRADE REPORT")

for mark in marks:

    if mark >= 90:
        grade = "A+"

    elif mark >= 80:
        grade = "A"

    elif mark >= 70:
        grade = "B"

    else:
        grade = "C"

    print(
        mark,
        "->",
        grade
    )

# ======================================
# PROBABILITY EXAMPLE
# ======================================

print("\nPROBABILITY EXAMPLE")

above_90 = 0

for mark in marks:

    if mark >= 90:
        above_90 += 1

probability = (
    above_90 /
    len(marks)
)

print(
    "Students >= 90 Marks:",
    above_90
)

print(
    "Probability:",
    round(
        probability,
        2
    )
)

# ======================================
# USER INPUT REPORT
# ======================================

print("\nUSER INPUT REPORT")

student_name = input(
    "Enter Student Name: "
)

student_marks = int(
    input(
        "Enter Marks: "
    )
)

print(
    "\nStudent:",
    student_name
)

print(
    "Marks:",
    student_marks
)

if student_marks >= 90:

    print(
        "Grade: A+"
    )

elif student_marks >= 80:

    print(
        "Grade: A"
    )

elif student_marks >= 70:

    print(
        "Grade: B"
    )

else:

    print(
        "Grade: C"
    )

# ======================================
# PROJECT SUMMARY
# ======================================

print("\n" + "=" * 60)

print(
    "PROJECT SUMMARY"
)

print("=" * 60)

print(
    "Mean:",
    round(
        mean_value,
        2
    )
)

print(
    "Median:",
    median_value
)

print(
    "Variance:",
    round(
        variance_value,
        2
    )
)

print(
    "Standard Deviation:",
    round(
        std_value,
        2
    )
)

print(
    "Range:",
    range_value
)

print("=" * 60)

# ======================================
# IMPORTANT FORMULAS
# ======================================

"""
Mean =
Sum of Values / Count

Range =
Maximum - Minimum

Variance =
Average Squared Deviation

Standard Deviation =
Square Root of Variance
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Change dataset values.

Exercise 2:
Add more students.

Exercise 3:
Create Grade Analysis.

Exercise 4:
Find Probability of
students scoring above 80.
"""

# ======================================
# CHALLENGE VERSION
# ======================================

"""
Version 2 Features:

1. CSV File Support
2. Pandas Analysis
3. Charts
4. Histograms
5. Correlation Analysis
6. Dashboard
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 099 Completed Successfully!"
)