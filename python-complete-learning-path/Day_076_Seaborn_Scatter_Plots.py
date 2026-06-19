# ======================================
# Day 076: Seaborn Scatter Plots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Scatter Plots using
# Seaborn
# ======================================

print("=" * 50)
print("DAY 076 - SEABORN SCATTER PLOTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Scatter Plot?

A Scatter Plot is used to show
the relationship between two
numerical variables.

Seaborn Function:

sns.scatterplot()

Applications:

1. Study Hours vs Marks
2. Height vs Weight
3. Sales vs Profit
4. Age vs Salary
5. Machine Learning

Advantages:

1. Detect Relationships
2. Find Correlations
3. Identify Outliers
4. Data Exploration
"""

# ======================================
# SAMPLE DATA
# ======================================

student_data = pd.DataFrame(
    {
        "Study_Hours": [
            1, 2, 3, 4, 5,
            6, 7, 8
        ],
        "Marks": [
            45, 52, 60, 68,
            75, 82, 88, 95
        ]
    }
)

print("\nSTUDENT DATA")
print(student_data)

# ======================================
# 1. BASIC SCATTER PLOT
# ======================================

print("\n1. BASIC SCATTER PLOT")

sns.scatterplot(
    data=student_data,
    x="Study_Hours",
    y="Marks"
)

plt.title(
    "Study Hours vs Marks"
)

plt.show()

# ======================================
# 2. SCATTER WITH GRID
# ======================================

print("\n2. SCATTER WITH GRID")

sns.scatterplot(
    data=student_data,
    x="Study_Hours",
    y="Marks"
)

plt.grid(True)

plt.title(
    "Scatter Plot with Grid"
)

plt.show()

# ======================================
# 3. HEIGHT VS WEIGHT
# ======================================

print("\n3. HEIGHT VS WEIGHT")

health_data = pd.DataFrame(
    {
        "Height": [
            150, 155, 160,
            165, 170, 175, 180
        ],
        "Weight": [
            45, 50, 55,
            60, 68, 72, 80
        ]
    }
)

sns.scatterplot(
    data=health_data,
    x="Height",
    y="Weight"
)

plt.title(
    "Height vs Weight"
)

plt.show()

# ======================================
# 4. SALES VS PROFIT
# ======================================

print("\n4. SALES VS PROFIT")

business_data = pd.DataFrame(
    {
        "Sales": [
            1000, 2000, 3000,
            4000, 5000
        ],
        "Profit": [
            100, 250, 400,
            550, 700
        ]
    }
)

sns.scatterplot(
    data=business_data,
    x="Sales",
    y="Profit"
)

plt.title(
    "Sales vs Profit"
)

plt.show()

# ======================================
# 5. ATTENDANCE VS MARKS
# ======================================

print("\n5. ATTENDANCE VS MARKS")

attendance_data = pd.DataFrame(
    {
        "Attendance": [
            60, 65, 70, 75,
            80, 85, 90, 95
        ],
        "Marks": [
            50, 58, 65, 72,
            80, 86, 92, 98
        ]
    }
)

sns.scatterplot(
    data=attendance_data,
    x="Attendance",
    y="Marks"
)

plt.title(
    "Attendance vs Marks"
)

plt.show()

# ======================================
# 6. RANDOM DATASET
# ======================================

print("\n6. RANDOM DATASET")

random_data = pd.DataFrame(
    {
        "X":
        np.random.randint(
            1,
            100,
            50
        ),

        "Y":
        np.random.randint(
            1,
            100,
            50
        )
    }
)

sns.scatterplot(
    data=random_data,
    x="X",
    y="Y"
)

plt.title(
    "Random Data Scatter Plot"
)

plt.show()

# ======================================
# 7. DARKGRID STYLE
# ======================================

print("\n7. DARKGRID STYLE")

sns.set_style(
    "darkgrid"
)

sns.scatterplot(
    data=student_data,
    x="Study_Hours",
    y="Marks"
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# 8. WHITEGRID STYLE
# ======================================

print("\n8. WHITEGRID STYLE")

sns.set_style(
    "whitegrid"
)

sns.scatterplot(
    data=student_data,
    x="Study_Hours",
    y="Marks"
)

plt.title(
    "White Grid Style"
)

plt.show()

# ======================================
# 9. EXAM PERFORMANCE
# ======================================

print("\n9. EXAM PERFORMANCE")

exam_data = pd.DataFrame(
    {
        "Hours": [
            2, 3, 4, 5,
            6, 7, 8
        ],
        "Scores": [
            50, 58, 67,
            75, 82, 90, 96
        ]
    }
)

sns.scatterplot(
    data=exam_data,
    x="Hours",
    y="Scores"
)

plt.title(
    "Exam Performance Analysis"
)

plt.show()

# ======================================
# 10. SAVE SCATTER PLOT
# ======================================

print("\n10. SAVE SCATTER PLOT")

sns.scatterplot(
    data=student_data,
    x="Study_Hours",
    y="Marks"
)

plt.title(
    "Saved Scatter Plot"
)

plt.savefig(
    "seaborn_scatter_plot.png"
)

plt.close()

print(
    "Scatter Plot Saved Successfully"
)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

hours = int(
    input(
        "Enter Study Hours: "
    )
)

marks = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"Hours: {hours}"
)

print(
    f"Marks: {marks}"
)

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

project_data = pd.DataFrame(
    {
        "Study_Hours": [
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10
        ],

        "Marks": [
            42, 50, 57, 64, 70,
            78, 84, 89, 94, 98
        ]
    }
)

print(project_data)

sns.scatterplot(
    data=project_data,
    x="Study_Hours",
    y="Marks"
)

plt.title(
    "Student Performance Dashboard"
)

plt.xlabel(
    "Study Hours"
)

plt.ylabel(
    "Marks"
)

plt.grid(True)

plt.show()

print(
    "Highest Marks:",
    project_data["Marks"].max()
)

print(
    "Lowest Marks:",
    project_data["Marks"].min()
)

print(
    "Average Marks:",
    round(
        project_data["Marks"].mean(),
        2
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a scatter plot
using height and weight.

Exercise 2:
Create a scatter plot
using attendance and marks.

Exercise 3:
Apply:

- darkgrid
- whitegrid

Exercise 4:
Save chart as PNG.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is sns.scatterplot()?

Q2. Why use scatter plots?

Q3. What is correlation?

Q4. How are outliers detected?

Q5. Difference between
Line Plot and Scatter Plot?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics System.

Columns:

1. Study Hours
2. Attendance
3. Marks

Generate:

1. Study Hours vs Marks
2. Attendance vs Marks
3. Correlation Analysis
4. Performance Report

Identify patterns in data.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 076 Completed Successfully!"
)