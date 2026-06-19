# ======================================
# Day 066: Scatter Plots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Scatter Plots using
# Matplotlib
# ======================================

print("=" * 50)
print("DAY 066 - SCATTER PLOTS")
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
What is a Scatter Plot?

A Scatter Plot is used to show
the relationship between two
numerical variables.

Applications:

1. Height vs Weight
2. Study Hours vs Marks
3. Sales vs Profit
4. Age vs Income
5. Machine Learning

Function:

plt.scatter()

Advantages:

1. Detect Relationships
2. Find Patterns
3. Identify Outliers
4. Correlation Analysis
"""

# ======================================
# 1. BASIC SCATTER PLOT
# ======================================

print("\n1. BASIC SCATTER PLOT")

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.scatter(x, y)

plt.title(
    "Basic Scatter Plot"
)

plt.xlabel(
    "X Values"
)

plt.ylabel(
    "Y Values"
)

plt.show()

# ======================================
# 2. STUDY HOURS VS MARKS
# ======================================

print("\n2. STUDY HOURS VS MARKS")

study_hours = [
    1, 2, 3, 4, 5,
    6, 7, 8
]

marks = [
    45, 52, 60, 68,
    75, 82, 88, 95
]

plt.scatter(
    study_hours,
    marks
)

plt.title(
    "Study Hours vs Marks"
)

plt.xlabel(
    "Study Hours"
)

plt.ylabel(
    "Marks"
)

plt.show()

# ======================================
# 3. HEIGHT VS WEIGHT
# ======================================

print("\n3. HEIGHT VS WEIGHT")

heights = [
    150, 155, 160, 165,
    170, 175, 180
]

weights = [
    45, 50, 55, 60,
    68, 72, 80
]

plt.scatter(
    heights,
    weights
)

plt.title(
    "Height vs Weight"
)

plt.xlabel(
    "Height (cm)"
)

plt.ylabel(
    "Weight (kg)"
)

plt.show()

# ======================================
# 4. SALES VS PROFIT
# ======================================

print("\n4. SALES VS PROFIT")

sales = [
    1000, 2000, 3000,
    4000, 5000
]

profit = [
    100, 250, 400,
    550, 700
]

plt.scatter(
    sales,
    profit
)

plt.title(
    "Sales vs Profit"
)

plt.xlabel(
    "Sales"
)

plt.ylabel(
    "Profit"
)

plt.show()

# ======================================
# 5. RANDOM DATA
# ======================================

print("\n5. RANDOM DATA")

x_random = [
    random.randint(1, 100)
    for _ in range(50)
]

y_random = [
    random.randint(1, 100)
    for _ in range(50)
]

plt.scatter(
    x_random,
    y_random
)

plt.title(
    "Random Scatter Plot"
)

plt.show()

# ======================================
# 6. GRID
# ======================================

print("\n6. GRID")

plt.scatter(
    study_hours,
    marks
)

plt.grid(True)

plt.title(
    "Scatter Plot with Grid"
)

plt.show()

# ======================================
# 7. STUDENT PERFORMANCE
# ======================================

print("\n7. STUDENT PERFORMANCE")

attendance = [
    60, 65, 70, 75,
    80, 85, 90, 95
]

marks = [
    50, 58, 65, 72,
    80, 86, 92, 98
]

plt.scatter(
    attendance,
    marks
)

plt.title(
    "Attendance vs Marks"
)

plt.xlabel(
    "Attendance (%)"
)

plt.ylabel(
    "Marks"
)

plt.show()

# ======================================
# 8. CUSTOM MARKER
# ======================================

print("\n8. CUSTOM MARKER")

plt.scatter(
    study_hours,
    marks,
    marker="s"
)

plt.title(
    "Custom Marker"
)

plt.show()

# ======================================
# 9. SAVE SCATTER PLOT
# ======================================

print("\n9. SAVE SCATTER PLOT")

plt.scatter(
    study_hours,
    marks
)

plt.title(
    "Saved Scatter Plot"
)

plt.savefig(
    "scatter_plot.png"
)

plt.close()

print(
    "Scatter Plot Saved Successfully"
)

# ======================================
# 10. CORRELATION EXAMPLE
# ======================================

print("\n10. CORRELATION EXAMPLE")

hours = [
    2, 3, 4, 5,
    6, 7, 8
]

scores = [
    50, 58, 67,
    75, 82, 90, 96
]

plt.scatter(
    hours,
    scores
)

plt.title(
    "Positive Correlation"
)

plt.xlabel(
    "Hours Studied"
)

plt.ylabel(
    "Scores"
)

plt.show()

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

n = int(
    input(
        "Enter Number of Points: "
    )
)

x_values = []
y_values = []

for i in range(n):

    x = int(
        input(
            f"X{i+1}: "
        )
    )

    y = int(
        input(
            f"Y{i+1}: "
        )
    )

    x_values.append(x)
    y_values.append(y)

plt.scatter(
    x_values,
    y_values
)

plt.title(
    "User Scatter Plot"
)

plt.show()

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

study_hours = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

exam_marks = [
    42, 50, 57, 64, 70,
    78, 84, 89, 94, 98
]

plt.figure(
    figsize=(8, 4)
)

plt.scatter(
    study_hours,
    exam_marks
)

plt.title(
    "Study Hours Analysis"
)

plt.xlabel(
    "Study Hours"
)

plt.ylabel(
    "Exam Marks"
)

plt.grid(True)

plt.show()

print(
    "Highest Marks:",
    max(exam_marks)
)

print(
    "Lowest Marks:",
    min(exam_marks)
)

print(
    "Average Marks:",
    round(
        sum(exam_marks)
        /
        len(exam_marks),
        2
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Scatter Plot
using height and weight.

Exercise 2:
Create a Scatter Plot
using study hours and marks.

Exercise 3:
Add:

- Title
- Labels
- Grid

Exercise 4:
Save Scatter Plot as PNG.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Analytics System.

Store:

1. Study Hours
2. Attendance
3. Marks

Display:

1. Study Hours vs Marks
2. Attendance vs Marks
3. Highest Marks
4. Average Marks

Generate complete analysis.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 066 Completed Successfully!")