# ======================================
# Day 079: Seaborn Data Visualization Project
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Complete Student Analytics
# Dashboard using Seaborn
# ======================================

print("=" * 60)
print("DAY 079 - SEABORN DATA VISUALIZATION PROJECT")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
PROJECT OBJECTIVE

Build a complete Student Analytics
Dashboard using Seaborn.

Concepts Used:

1. Bar Plot
2. Histogram
3. Box Plot
4. Scatter Plot
5. Heatmap
6. Pairplot
7. Correlation Analysis
8. Dashboard Design

Applications:

1. Education Analytics
2. Data Science
3. Business Analytics
4. Research Projects
5. Machine Learning
"""

# ======================================
# STUDENT DATASET
# ======================================

students = pd.DataFrame(
    {
        "Student": [
            "Saloni",
            "Riya",
            "Ankit",
            "Rahul",
            "Priya"
        ],

        "Math": [
            92,
            88,
            95,
            81,
            90
        ],

        "Python": [
            95,
            90,
            89,
            85,
            93
        ],

        "DBMS": [
            88,
            85,
            91,
            80,
            87
        ],

        "Attendance": [
            95,
            88,
            97,
            82,
            91
        ],

        "Study_Hours": [
            8,
            6,
            9,
            5,
            7
        ]
    }
)

print("\nSTUDENT DATASET")
print(students)

# ======================================
# BASIC ANALYSIS
# ======================================

print("\nSUMMARY REPORT")

print(
    "Average Math Marks:",
    round(
        students["Math"].mean(),
        2
    )
)

print(
    "Average Python Marks:",
    round(
        students["Python"].mean(),
        2
    )
)

print(
    "Average DBMS Marks:",
    round(
        students["DBMS"].mean(),
        2
    )
)

# ======================================
# DASHBOARD SETUP
# ======================================

plt.figure(
    figsize=(14, 10)
)

# ======================================
# 1. BAR PLOT
# ======================================

plt.subplot(2, 2, 1)

sns.barplot(
    data=students,
    x="Student",
    y="Math"
)

plt.title(
    "Math Performance"
)

# ======================================
# 2. HISTOGRAM
# ======================================

plt.subplot(2, 2, 2)

sns.histplot(
    data=students,
    x="Math",
    kde=True
)

plt.title(
    "Math Distribution"
)

# ======================================
# 3. BOX PLOT
# ======================================

plt.subplot(2, 2, 3)

sns.boxplot(
    data=students,
    y="Python"
)

plt.title(
    "Python Marks Distribution"
)

# ======================================
# 4. SCATTER PLOT
# ======================================

plt.subplot(2, 2, 4)

sns.scatterplot(
    data=students,
    x="Study_Hours",
    y="Math"
)

plt.title(
    "Study Hours vs Math"
)

plt.tight_layout()

plt.show()

# ======================================
# CORRELATION ANALYSIS
# ======================================

print("\nCORRELATION MATRIX")

correlation = students[
    [
        "Math",
        "Python",
        "DBMS",
        "Attendance",
        "Study_Hours"
    ]
].corr()

print(correlation)

# ======================================
# HEATMAP
# ======================================

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Correlation Heatmap"
)

plt.show()

# ======================================
# PAIRPLOT
# ======================================

print("\nPAIRPLOT ANALYSIS")

sns.pairplot(
    students[
        [
            "Math",
            "Python",
            "DBMS",
            "Attendance",
            "Study_Hours"
        ]
    ]
)

plt.show()

# ======================================
# TOP STUDENT
# ======================================

print("\nTOP PERFORMER")

top_student = students.loc[
    students["Math"].idxmax()
]

print(
    "Name:",
    top_student["Student"]
)

print(
    "Math Marks:",
    top_student["Math"]
)

# ======================================
# SAVE HEATMAP
# ======================================

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Student Analytics Heatmap"
)

plt.savefig(
    "student_analytics_heatmap.png"
)

plt.close()

print(
    "\nHeatmap Saved Successfully"
)

# ======================================
# USER INPUT ANALYSIS
# ======================================

print("\nUSER INPUT REPORT")

name = input(
    "Enter Student Name: "
)

marks = int(
    input(
        "Enter Marks: "
    )
)

attendance = int(
    input(
        "Enter Attendance (%): "
    )
)

print("\nREPORT")

print(
    "Name:",
    name
)

print(
    "Marks:",
    marks
)

print(
    "Attendance:",
    attendance
)

if marks >= 90:
    print("Grade: A+")

elif marks >= 80:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

else:
    print("Grade: C")

# ======================================
# PROJECT SUMMARY
# ======================================

print("\n" + "=" * 60)

print(
    "PROJECT SUMMARY"
)

print("=" * 60)

print(
    "Total Students:",
    len(students)
)

print(
    "Highest Math Marks:",
    students["Math"].max()
)

print(
    "Lowest Math Marks:",
    students["Math"].min()
)

print(
    "Average Math Marks:",
    round(
        students["Math"].mean(),
        2
    )
)

print("=" * 60)

# ======================================
# CHALLENGE TASK
# ======================================

"""
Project Version 2

Add:

1. CSV Dataset
2. Multiple Departments
3. More Subjects
4. Attendance Tracking
5. Streamlit Dashboard
6. PDF Report
7. Advanced Analytics
8. Machine Learning Insights
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 079 Completed Successfully!"
)