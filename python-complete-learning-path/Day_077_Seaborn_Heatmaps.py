# ======================================
# Day 077: Seaborn Heatmaps
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Heatmaps using
# Seaborn
# ======================================

print("=" * 50)
print("DAY 077 - SEABORN HEATMAPS")
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
What is a Heatmap?

A Heatmap is a graphical
representation of data where
values are represented using colors.

Seaborn Function:

sns.heatmap()

Applications:

1. Correlation Analysis
2. Machine Learning
3. Business Analytics
4. Research Projects
5. Exploratory Data Analysis (EDA)

Advantages:

1. Easy Pattern Detection
2. Correlation Visualization
3. Compact Data Representation
4. Useful for Large Datasets
"""

# ======================================
# SAMPLE MATRIX DATA
# ======================================

matrix_data = pd.DataFrame(
    [
        [10, 20, 30],
        [15, 25, 35],
        [20, 30, 40]
    ],
    columns=[
        "Math",
        "Python",
        "DBMS"
    ]
)

print("\nMATRIX DATA")
print(matrix_data)

# ======================================
# 1. BASIC HEATMAP
# ======================================

print("\n1. BASIC HEATMAP")

sns.heatmap(
    matrix_data
)

plt.title(
    "Basic Heatmap"
)

plt.show()

# ======================================
# 2. HEATMAP WITH VALUES
# ======================================

print("\n2. HEATMAP WITH VALUES")

sns.heatmap(
    matrix_data,
    annot=True
)

plt.title(
    "Heatmap with Annotations"
)

plt.show()

# ======================================
# 3. CUSTOM COLOR MAP
# ======================================

print("\n3. CUSTOM COLOR MAP")

sns.heatmap(
    matrix_data,
    annot=True,
    cmap="YlGnBu"
)

plt.title(
    "Custom Color Map"
)

plt.show()

# ======================================
# 4. STUDENT MARKS HEATMAP
# ======================================

print("\n4. STUDENT MARKS HEATMAP")

student_data = pd.DataFrame(
    {
        "Math": [92, 88, 95],
        "Python": [95, 90, 89],
        "DBMS": [88, 85, 91]
    },
    index=[
        "Saloni",
        "Riya",
        "Ankit"
    ]
)

print(student_data)

sns.heatmap(
    student_data,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Student Marks Heatmap"
)

plt.show()

# ======================================
# 5. CORRELATION MATRIX
# ======================================

print("\n5. CORRELATION MATRIX")

marks_df = pd.DataFrame(
    {
        "Math": [
            92, 88, 95, 81, 90
        ],
        "Python": [
            95, 90, 89, 85, 93
        ],
        "DBMS": [
            88, 85, 91, 80, 87
        ]
    }
)

correlation = (
    marks_df.corr()
)

print(correlation)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Correlation Matrix"
)

plt.show()

# ======================================
# 6. RANDOM DATASET
# ======================================

print("\n6. RANDOM DATASET")

random_data = pd.DataFrame(
    np.random.randint(
        1,
        100,
        size=(5, 5)
    )
)

sns.heatmap(
    random_data,
    annot=True
)

plt.title(
    "Random Data Heatmap"
)

plt.show()

# ======================================
# 7. DARKGRID STYLE
# ======================================

print("\n7. DARKGRID STYLE")

sns.set_style(
    "darkgrid"
)

sns.heatmap(
    matrix_data,
    annot=True
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# 8. SALES ANALYSIS
# ======================================

print("\n8. SALES ANALYSIS")

sales_data = pd.DataFrame(
    {
        "Q1": [1000, 1200, 1500],
        "Q2": [1300, 1600, 1800],
        "Q3": [1700, 1900, 2100],
        "Q4": [2000, 2200, 2500]
    },
    index=[
        "Product A",
        "Product B",
        "Product C"
    ]
)

print(sales_data)

sns.heatmap(
    sales_data,
    annot=True,
    cmap="YlOrRd"
)

plt.title(
    "Quarterly Sales Analysis"
)

plt.show()

# ======================================
# 9. ATTENDANCE ANALYSIS
# ======================================

print("\n9. ATTENDANCE ANALYSIS")

attendance_data = pd.DataFrame(
    {
        "Jan": [85, 90, 88],
        "Feb": [87, 92, 89],
        "Mar": [90, 95, 91]
    },
    index=[
        "Student A",
        "Student B",
        "Student C"
    ]
)

sns.heatmap(
    attendance_data,
    annot=True,
    cmap="Greens"
)

plt.title(
    "Attendance Heatmap"
)

plt.show()

# ======================================
# 10. SAVE HEATMAP
# ======================================

print("\n10. SAVE HEATMAP")

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Saved Heatmap"
)

plt.savefig(
    "seaborn_heatmap.png"
)

plt.close()

print(
    "Heatmap Saved Successfully"
)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

value = int(
    input(
        "Enter Any Number: "
    )
)

print(
    f"You Entered: {value}"
)

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

project_data = pd.DataFrame(
    {
        "Math": [92, 88, 95, 81],
        "Python": [95, 90, 89, 85],
        "DBMS": [88, 85, 91, 80],
        "Statistics": [90, 87, 92, 84]
    }
)

print(project_data)

project_corr = (
    project_data.corr()
)

print("\nCorrelation Matrix")
print(project_corr)

sns.heatmap(
    project_corr,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Student Performance Dashboard"
)

plt.show()

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a basic heatmap.

Exercise 2:
Add annotations.

Exercise 3:
Use different color maps.

Exercise 4:
Create a correlation matrix.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is a Heatmap?

Q2. What is Correlation?

Q3. Why use Heatmaps?

Q4. What is annot=True?

Q5. What is a Correlation Matrix?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics System.

Columns:

1. Math
2. Python
3. DBMS
4. Statistics

Generate:

1. Correlation Matrix
2. Heatmap
3. Performance Analysis

Identify relationships
between subjects.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 077 Completed Successfully!"
)