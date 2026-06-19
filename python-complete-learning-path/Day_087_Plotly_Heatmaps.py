# ======================================
# Day 087: Plotly Heatmaps
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Interactive Heatmaps
# using Plotly
# ======================================

print("=" * 50)
print("DAY 087 - PLOTLY HEATMAPS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import plotly.express as px
import pandas as pd
import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Heatmap?

A Heatmap is a visualization
that represents data values
using colors.

Plotly Function:

px.imshow()

Applications:

1. Correlation Analysis
2. Machine Learning
3. Business Analytics
4. Research Projects
5. Exploratory Data Analysis

Advantages:

1. Easy Pattern Detection
2. Correlation Visualization
3. Interactive Exploration
4. Compact Data Representation
"""

# ======================================
# STUDENT MARKS DATASET
# ======================================

student_data = pd.DataFrame(
    {
        "Math": [
            92, 88, 95, 81, 90
        ],

        "Python": [
            95, 90, 89, 85, 93
        ],

        "DBMS": [
            88, 85, 91, 80, 87
        ],

        "Statistics": [
            90, 87, 92, 84, 89
        ]
    }
)

print("\nSTUDENT DATASET")
print(student_data)

# ======================================
# 1. CORRELATION MATRIX
# ======================================

print("\n1. CORRELATION MATRIX")

correlation = student_data.corr()

print(correlation)

# ======================================
# 2. BASIC HEATMAP
# ======================================

print("\n2. BASIC HEATMAP")

fig = px.imshow(
    correlation,
    text_auto=True,
    title="Correlation Heatmap"
)

fig.show()

# ======================================
# 3. CUSTOM COLOR SCALE
# ======================================

print("\n3. CUSTOM COLOR SCALE")

fig = px.imshow(
    correlation,
    text_auto=True,
    color_continuous_scale="RdBu",
    title="Custom Heatmap"
)

fig.show()

# ======================================
# 4. SALES DATA ANALYSIS
# ======================================

print("\n4. SALES ANALYSIS")

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

fig = px.imshow(
    sales_data,
    text_auto=True,
    title="Quarterly Sales Heatmap"
)

fig.show()

# ======================================
# 5. ATTENDANCE DATA
# ======================================

print("\n5. ATTENDANCE ANALYSIS")

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

fig = px.imshow(
    attendance_data,
    text_auto=True,
    title="Attendance Heatmap"
)

fig.show()

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

fig = px.imshow(
    random_data,
    text_auto=True,
    title="Random Data Heatmap"
)

fig.show()

# ======================================
# 7. EXAM PERFORMANCE
# ======================================

print("\n7. EXAM PERFORMANCE")

exam_data = pd.DataFrame(
    {
        "Math": [70, 82, 88],
        "Python": [75, 85, 90],
        "DBMS": [72, 80, 87]
    },
    index=[
        "Student A",
        "Student B",
        "Student C"
    ]
)

fig = px.imshow(
    exam_data,
    text_auto=True,
    title="Exam Performance Heatmap"
)

fig.show()

# ======================================
# 8. CUSTOM LAYOUT
# ======================================

print("\n8. CUSTOM LAYOUT")

fig = px.imshow(
    correlation,
    text_auto=True
)

fig.update_layout(
    title="Professional Correlation Dashboard"
)

fig.show()

# ======================================
# 9. SAVE HEATMAP
# ======================================

print("\n9. SAVE HEATMAP")

fig = px.imshow(
    correlation,
    text_auto=True
)

fig.write_html(
    "plotly_heatmap.html"
)

print(
    "Heatmap Saved Successfully"
)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

value = int(
    input(
        "Enter Any Number: "
    )
)

print(
    f"You Entered: {value}"
)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT")

project_data = pd.DataFrame(
    {
        "Math": [92, 88, 95, 81],
        "Python": [95, 90, 89, 85],
        "DBMS": [88, 85, 91, 80],
        "Statistics": [90, 87, 92, 84]
    }
)

print(project_data)

project_corr = project_data.corr()

print("\nCorrelation Matrix")
print(project_corr)

fig = px.imshow(
    project_corr,
    text_auto=True,
    color_continuous_scale="Viridis",
    title="Student Analytics Dashboard"
)

fig.show()

# ======================================
# IMPORTANT FUNCTIONS
# ======================================

"""
px.imshow()

text_auto=True

color_continuous_scale=

fig.show()

fig.update_layout()

fig.write_html()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Heatmap.

Exercise 2:
Create a Correlation Matrix.

Exercise 3:
Use Different Color Scales.

Exercise 4:
Save chart as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is a Heatmap?

Q2. What is Correlation?

Q3. Why use Heatmaps?

Q4. What is px.imshow()?

Q5. What is text_auto=True?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics Dashboard.

Columns:

1. Math
2. Python
3. DBMS
4. Statistics

Generate:

1. Correlation Matrix
2. Heatmap
3. Performance Analysis

Create an interactive report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 087 Completed Successfully!"
)