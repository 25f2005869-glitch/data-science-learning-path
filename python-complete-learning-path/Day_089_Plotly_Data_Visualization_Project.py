# ======================================
# Day 089: Plotly Data Visualization Project
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Complete Student Analytics Dashboard
# using Plotly
# ======================================

print("=" * 60)
print("DAY 089 - PLOTLY DATA VISUALIZATION PROJECT")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ======================================
# PROJECT OVERVIEW
# ======================================

"""
PROJECT:
Student Analytics Dashboard

Objectives:

1. Analyze Student Performance
2. Analyze Attendance
3. Analyze Study Habits
4. Generate Interactive Charts
5. Build Dashboard

Tools Used:

1. Pandas
2. Plotly Express
3. Plotly Graph Objects
4. Plotly Subplots
"""

# ======================================
# DATASET
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

students["Average"] = (
    students[
        [
            "Math",
            "Python",
            "DBMS"
        ]
    ].mean(axis=1)
)

print(
    students[
        [
            "Student",
            "Average"
        ]
    ]
)

# ======================================
# TOP PERFORMER
# ======================================

top_student = students.loc[
    students["Average"].idxmax()
]

print("\nTOP PERFORMER")

print(
    "Name:",
    top_student["Student"]
)

print(
    "Average:",
    round(
        top_student["Average"],
        2
    )
)

# ======================================
# DASHBOARD CREATION
# ======================================

fig = make_subplots(
    rows=2,
    cols=2,
    specs=[
        [
            {"type": "bar"},
            {"type": "scatter"}
        ],
        [
            {"type": "pie"},
            {"type": "bar"}
        ]
    ],
    subplot_titles=(
        "Average Marks",
        "Study Hours vs Average",
        "Attendance Share",
        "Python Performance"
    )
)

# ======================================
# BAR CHART
# ======================================

fig.add_trace(
    go.Bar(
        x=students["Student"],
        y=students["Average"],
        name="Average Marks"
    ),
    row=1,
    col=1
)

# ======================================
# SCATTER PLOT
# ======================================

fig.add_trace(
    go.Scatter(
        x=students["Study_Hours"],
        y=students["Average"],
        mode="markers+lines",
        name="Performance"
    ),
    row=1,
    col=2
)

# ======================================
# PIE CHART
# ======================================

fig.add_trace(
    go.Pie(
        labels=students["Student"],
        values=students["Attendance"],
        name="Attendance"
    ),
    row=2,
    col=1
)

# ======================================
# BAR CHART
# ======================================

fig.add_trace(
    go.Bar(
        x=students["Student"],
        y=students["Python"],
        name="Python"
    ),
    row=2,
    col=2
)

# ======================================
# LAYOUT
# ======================================

fig.update_layout(
    title="Student Analytics Dashboard",
    height=800,
    width=1000
)

fig.show()

# ======================================
# CORRELATION ANALYSIS
# ======================================

print("\nCORRELATION ANALYSIS")

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

heatmap = px.imshow(
    correlation,
    text_auto=True,
    title="Correlation Heatmap"
)

heatmap.show()

# ======================================
# SUBJECT PERFORMANCE
# ======================================

subject_average = pd.DataFrame(
    {
        "Subject": [
            "Math",
            "Python",
            "DBMS"
        ],

        "Average_Marks": [
            students["Math"].mean(),
            students["Python"].mean(),
            students["DBMS"].mean()
        ]
    }
)

print("\nSUBJECT PERFORMANCE")
print(subject_average)

subject_chart = px.bar(
    subject_average,
    x="Subject",
    y="Average_Marks",
    title="Subject Performance"
)

subject_chart.show()

# ======================================
# ATTENDANCE ANALYSIS
# ======================================

attendance_chart = px.pie(
    students,
    names="Student",
    values="Attendance",
    title="Attendance Distribution"
)

attendance_chart.show()

# ======================================
# SAVE DASHBOARD
# ======================================

fig.write_html(
    "student_analytics_dashboard.html"
)

print(
    "\nDashboard Saved Successfully"
)

# ======================================
# USER INPUT REPORT
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
        "Enter Attendance: "
    )
)

print("\nSTUDENT REPORT")

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

print("PROJECT SUMMARY")

print("=" * 60)

print(
    "Total Students:",
    len(students)
)

print(
    "Highest Average:",
    round(
        students["Average"].max(),
        2
    )
)

print(
    "Lowest Average:",
    round(
        students["Average"].min(),
        2
    )
)

print(
    "Overall Average:",
    round(
        students["Average"].mean(),
        2
    )
)

print("=" * 60)

# ======================================
# CHALLENGE VERSION
# ======================================

"""
Project Version 2

Add:

1. CSV Dataset
2. Streamlit Dashboard
3. Student Ranking
4. Multiple Subjects
5. Export Reports
6. Department Analytics
7. Performance Prediction
8. Machine Learning Model
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 089 Completed Successfully!"
)