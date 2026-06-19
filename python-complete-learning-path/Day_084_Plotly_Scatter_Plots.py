# ======================================
# Day 084: Plotly Scatter Plots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Interactive Scatter Plots
# using Plotly
# ======================================

print("=" * 50)
print("DAY 084 - PLOTLY SCATTER PLOTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import plotly.express as px
import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Scatter Plot?

A Scatter Plot is used to show
the relationship between two
numerical variables.

Plotly Function:

px.scatter()

Applications:

1. Study Hours vs Marks
2. Height vs Weight
3. Sales vs Profit
4. Age vs Salary
5. Machine Learning

Advantages:

1. Interactive Visualization
2. Correlation Analysis
3. Outlier Detection
4. Data Exploration
"""

# ======================================
# STUDY HOURS DATASET
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

print("\nSTUDENT DATASET")
print(student_data)

# ======================================
# 1. BASIC SCATTER PLOT
# ======================================

print("\n1. BASIC SCATTER PLOT")

fig = px.scatter(
    student_data,
    x="Study_Hours",
    y="Marks",
    title="Study Hours vs Marks"
)

fig.show()

# ======================================
# 2. ATTENDANCE VS MARKS
# ======================================

print("\n2. ATTENDANCE VS MARKS")

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

fig = px.scatter(
    attendance_data,
    x="Attendance",
    y="Marks",
    title="Attendance vs Marks"
)

fig.show()

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

fig = px.scatter(
    health_data,
    x="Height",
    y="Weight",
    title="Height vs Weight"
)

fig.show()

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

fig = px.scatter(
    business_data,
    x="Sales",
    y="Profit",
    title="Sales vs Profit"
)

fig.show()

# ======================================
# 5. EXAM PERFORMANCE
# ======================================

print("\n5. EXAM PERFORMANCE")

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

fig = px.scatter(
    exam_data,
    x="Hours",
    y="Scores",
    title="Exam Performance Analysis"
)

fig.show()

# ======================================
# 6. DEPARTMENT ANALYSIS
# ======================================

print("\n6. DEPARTMENT ANALYSIS")

department_data = pd.DataFrame(
    {
        "Students": [
            50, 80, 100,
            120, 150
        ],

        "Average_Marks": [
            72, 78, 82,
            88, 92
        ]
    }
)

fig = px.scatter(
    department_data,
    x="Students",
    y="Average_Marks",
    title="Department Analysis"
)

fig.show()

# ======================================
# 7. CUSTOM LAYOUT
# ======================================

print("\n7. CUSTOM LAYOUT")

fig = px.scatter(
    student_data,
    x="Study_Hours",
    y="Marks"
)

fig.update_layout(
    title="Professional Student Dashboard",
    xaxis_title="Study Hours",
    yaxis_title="Marks"
)

fig.show()

# ======================================
# 8. LEARNING PROGRESS
# ======================================

print("\n8. LEARNING PROGRESS")

progress_data = pd.DataFrame(
    {
        "Practice_Hours": [
            1, 2, 3, 4,
            5, 6, 7, 8
        ],

        "Python_Score": [
            40, 48, 58, 68,
            77, 85, 91, 97
        ]
    }
)

fig = px.scatter(
    progress_data,
    x="Practice_Hours",
    y="Python_Score",
    title="Python Learning Progress"
)

fig.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

fig = px.scatter(
    student_data,
    x="Study_Hours",
    y="Marks"
)

fig.write_html(
    "plotly_scatter_plot.html"
)

print(
    "Chart Saved Successfully"
)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

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
    f"Study Hours: {hours}"
)

print(
    f"Marks: {marks}"
)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT")

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

fig = px.scatter(
    project_data,
    x="Study_Hours",
    y="Marks",
    title="Student Performance Dashboard"
)

fig.show()

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
# IMPORTANT FUNCTIONS
# ======================================

"""
px.scatter()

fig.show()

fig.update_layout()

fig.write_html()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Scatter Plot.

Exercise 2:
Analyze Study Hours vs Marks.

Exercise 3:
Analyze Sales vs Profit.

Exercise 4:
Save chart as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is px.scatter()?

Q2. What is Correlation?

Q3. Why use Scatter Plots?

Q4. How can Scatter Plots
identify outliers?

Q5. What makes Plotly
interactive?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics Dashboard.

Columns:

1. Study Hours
2. Attendance
3. Marks

Generate:

1. Study Hours vs Marks
2. Attendance vs Marks
3. Correlation Analysis

Create an interactive report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 084 Completed Successfully!"
)