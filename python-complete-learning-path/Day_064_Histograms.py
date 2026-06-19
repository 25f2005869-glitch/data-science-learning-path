# ======================================
# Day 064: Histograms
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Histograms using
# Matplotlib
# ======================================

print("=" * 50)
print("DAY 064 - HISTOGRAMS")
print("=" * 50)

# ======================================
# IMPORT LIBRARY
# ======================================

import matplotlib.pyplot as plt
import random

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Histogram?

A Histogram is used to display
the distribution of numerical data.

Unlike Bar Charts:

Bar Chart:
- Compares categories

Histogram:
- Shows frequency distribution

Applications:

1. Student Marks Analysis
2. Salary Distribution
3. Population Analysis
4. Data Science
5. Machine Learning

Function:

plt.hist()
"""

# ======================================
# 1. BASIC HISTOGRAM
# ======================================

print("\n1. BASIC HISTOGRAM")

marks = [
    45, 50, 55, 60, 65,
    70, 75, 80, 85, 90,
    95, 78, 82, 88, 91
]

plt.hist(marks)

plt.title(
    "Basic Histogram"
)

plt.xlabel(
    "Marks"
)

plt.ylabel(
    "Frequency"
)

plt.show()

# ======================================
# 2. CUSTOM BINS
# ======================================

print("\n2. CUSTOM BINS")

plt.hist(
    marks,
    bins=5
)

plt.title(
    "Histogram with 5 Bins"
)

plt.show()

# ======================================
# 3. STUDENT MARKS DISTRIBUTION
# ======================================

print("\n3. MARKS DISTRIBUTION")

student_marks = [
    92, 88, 95, 81, 90,
    78, 84, 89, 91, 87,
    76, 85, 93, 80, 82
]

plt.hist(
    student_marks,
    bins=6
)

plt.title(
    "Student Marks Distribution"
)

plt.xlabel(
    "Marks"
)

plt.ylabel(
    "Number of Students"
)

plt.show()

# ======================================
# 4. RANDOM DATA
# ======================================

print("\n4. RANDOM DATA")

random_data = [
    random.randint(
        1,
        100
    )
    for _ in range(100)
]

plt.hist(
    random_data,
    bins=10
)

plt.title(
    "Random Data Distribution"
)

plt.show()

# ======================================
# 5. GRID
# ======================================

print("\n5. GRID")

plt.hist(
    student_marks,
    bins=6
)

plt.grid(True)

plt.title(
    "Histogram with Grid"
)

plt.show()

# ======================================
# 6. EXAM SCORE ANALYSIS
# ======================================

print("\n6. EXAM SCORE ANALYSIS")

exam_scores = [
    55, 60, 62, 65, 67,
    70, 72, 75, 78, 80,
    82, 85, 88, 90, 92,
    95, 97
]

plt.hist(
    exam_scores,
    bins=7
)

plt.title(
    "Exam Score Distribution"
)

plt.xlabel(
    "Scores"
)

plt.ylabel(
    "Frequency"
)

plt.show()

# ======================================
# 7. SALES DATA
# ======================================

print("\n7. SALES DATA")

sales = [
    1000, 1200, 1300, 1500,
    1600, 1800, 1900, 2000,
    2200, 2500
]

plt.hist(
    sales,
    bins=5
)

plt.title(
    "Sales Distribution"
)

plt.show()

# ======================================
# 8. LARGE DATASET
# ======================================

print("\n8. LARGE DATASET")

large_data = [
    random.randint(
        40,
        100
    )
    for _ in range(500)
]

plt.hist(
    large_data,
    bins=12
)

plt.title(
    "Large Dataset Histogram"
)

plt.show()

# ======================================
# 9. SAVE HISTOGRAM
# ======================================

print("\n9. SAVE HISTOGRAM")

plt.hist(
    student_marks,
    bins=6
)

plt.title(
    "Saved Histogram"
)

plt.savefig(
    "histogram.png"
)

plt.close()

print(
    "Histogram Saved Successfully"
)

# ======================================
# 10. FREQUENCY ANALYSIS
# ======================================

print("\n10. FREQUENCY ANALYSIS")

marks = [
    92, 88, 95, 81, 90,
    78, 84, 89, 91, 87
]

print(
    "Highest Marks:",
    max(marks)
)

print(
    "Lowest Marks:",
    min(marks)
)

print(
    "Average Marks:",
    sum(marks) / len(marks)
)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

n = int(
    input(
        "Enter Number of Values: "
    )
)

values = []

for i in range(n):

    value = int(
        input(
            f"Value {i+1}: "
        )
    )

    values.append(
        value
    )

plt.hist(
    values,
    bins=5
)

plt.title(
    "User Data Histogram"
)

plt.show()

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

student_scores = [
    92, 88, 95, 81, 90,
    78, 84, 89, 91, 87,
    76, 85, 93, 80, 82,
    96, 77, 86, 94, 83
]

plt.figure(
    figsize=(8, 4)
)

plt.hist(
    student_scores,
    bins=8
)

plt.title(
    "Student Performance Distribution"
)

plt.xlabel(
    "Marks"
)

plt.ylabel(
    "Frequency"
)

plt.grid(True)

plt.show()

print(
    "Average Marks:",
    round(
        sum(student_scores)
        /
        len(student_scores),
        2
    )
)

print(
    "Highest Marks:",
    max(student_scores)
)

print(
    "Lowest Marks:",
    min(student_scores)
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Histogram
using student marks.

Exercise 2:
Use different bins:

- 5
- 10
- 15

Exercise 3:
Add:

- Title
- Labels
- Grid

Exercise 4:
Save histogram as PNG.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create an Exam Analysis System.

Store marks of
50 students.

Display:

1. Histogram
2. Average Marks
3. Highest Marks
4. Lowest Marks
5. Marks Distribution

Generate complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 064 Completed Successfully!")