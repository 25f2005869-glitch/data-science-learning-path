# ======================================
# Day 083: Plotly Bar Charts
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Interactive Bar Charts
# using Plotly
# ======================================

print("=" * 50)
print("DAY 083 - PLOTLY BAR CHARTS")
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
What is a Bar Chart?

A Bar Chart is used to compare
different categories of data.

Plotly Function:

px.bar()

Applications:

1. Student Performance
2. Sales Comparison
3. Department Analysis
4. Business Reports
5. Survey Results

Advantages:

1. Interactive Visualization
2. Easy Comparison
3. Hover Information
4. Professional Dashboards
"""

# ======================================
# STUDENT DATASET
# ======================================

student_data = pd.DataFrame(
    {
        "Student": [
            "Saloni",
            "Riya",
            "Ankit",
            "Rahul",
            "Priya"
        ],

        "Marks": [
            92,
            88,
            95,
            81,
            90
        ]
    }
)

print("\nSTUDENT DATASET")
print(student_data)

# ======================================
# 1. BASIC BAR CHART
# ======================================

print("\n1. BASIC BAR CHART")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks",
    title="Student Performance"
)

fig.show()

# ======================================
# 2. SUBJECT PERFORMANCE
# ======================================

print("\n2. SUBJECT PERFORMANCE")

subject_data = pd.DataFrame(
    {
        "Subject": [
            "Math",
            "Python",
            "DBMS",
            "Statistics",
            "English"
        ],

        "Marks": [
            92,
            95,
            88,
            90,
            85
        ]
    }
)

fig = px.bar(
    subject_data,
    x="Subject",
    y="Marks",
    title="Subject Performance"
)

fig.show()

# ======================================
# 3. SALES COMPARISON
# ======================================

print("\n3. SALES COMPARISON")

sales_data = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],

        "Sales": [
            1000,
            1200,
            1500,
            1300,
            1800
        ]
    }
)

fig = px.bar(
    sales_data,
    x="Month",
    y="Sales",
    title="Monthly Sales"
)

fig.show()

# ======================================
# 4. DEPARTMENT ANALYSIS
# ======================================

print("\n4. DEPARTMENT ANALYSIS")

department_data = pd.DataFrame(
    {
        "Department": [
            "Data Science",
            "Math",
            "Physics",
            "Chemistry"
        ],

        "Students": [
            120,
            95,
            80,
            70
        ]
    }
)

fig = px.bar(
    department_data,
    x="Department",
    y="Students",
    title="Department Strength"
)

fig.show()

# ======================================
# 5. HORIZONTAL BAR CHART
# ======================================

print("\n5. HORIZONTAL BAR CHART")

fig = px.bar(
    subject_data,
    x="Marks",
    y="Subject",
    orientation="h",
    title="Horizontal Bar Chart"
)

fig.show()

# ======================================
# 6. ATTENDANCE ANALYSIS
# ======================================

print("\n6. ATTENDANCE ANALYSIS")

attendance_data = pd.DataFrame(
    {
        "Student": [
            "Saloni",
            "Riya",
            "Ankit",
            "Rahul",
            "Priya"
        ],

        "Attendance": [
            95,
            88,
            97,
            82,
            91
        ]
    }
)

fig = px.bar(
    attendance_data,
    x="Student",
    y="Attendance",
    title="Attendance Analysis"
)

fig.show()

# ======================================
# 7. EXAM RESULTS
# ======================================

print("\n7. EXAM RESULTS")

exam_data = pd.DataFrame(
    {
        "Student": [
            "A",
            "B",
            "C",
            "D"
        ],

        "Marks": [
            85,
            90,
            78,
            95
        ]
    }
)

fig = px.bar(
    exam_data,
    x="Student",
    y="Marks",
    title="Exam Results"
)

fig.show()

# ======================================
# 8. CUSTOM LAYOUT
# ======================================

print("\n8. CUSTOM LAYOUT")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks"
)

fig.update_layout(
    title="Professional Student Dashboard",
    xaxis_title="Students",
    yaxis_title="Marks"
)

fig.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks"
)

fig.write_html(
    "plotly_bar_chart.html"
)

print(
    "Chart Saved Successfully"
)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

student_name = input(
    "Enter Student Name: "
)

student_marks = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"{student_name} scored {student_marks}"
)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT")

project_data = pd.DataFrame(
    {
        "Subject": [
            "Math",
            "Python",
            "DBMS",
            "Statistics",
            "English"
        ],

        "Marks": [
            92,
            95,
            88,
            90,
            85
        ]
    }
)

print(project_data)

fig = px.bar(
    project_data,
    x="Subject",
    y="Marks",
    title="Subject Performance Dashboard"
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
px.bar()

orientation="h"

fig.show()

fig.update_layout()

fig.write_html()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Bar Chart.

Exercise 2:
Create a Horizontal Bar Chart.

Exercise 3:
Analyze Student Marks.

Exercise 4:
Save chart as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is px.bar()?

Q2. Why use Bar Charts?

Q3. Difference between
Vertical and Horizontal Bar Charts?

Q4. Why are Plotly charts interactive?

Q5. What is fig.update_layout()?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a College Dashboard.

Columns:

1. Department
2. Students
3. Average Marks

Generate:

1. Bar Chart
2. Horizontal Bar Chart
3. Department Comparison

Create an interactive report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 083 Completed Successfully!"
)