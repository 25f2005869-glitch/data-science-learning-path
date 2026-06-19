# ======================================
# Day 081: Plotly Introduction
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Plotly for
# Interactive Data Visualization
# ======================================

print("=" * 50)
print("DAY 081 - PLOTLY INTRODUCTION")
print("=" * 50)

# ======================================
# INSTALLATION NOTE
# ======================================

"""
Install Plotly:

pip install plotly
"""

# ======================================
# IMPORT LIBRARIES
# ======================================

import plotly.express as px
import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Plotly?

Plotly is a Python library used
for creating interactive charts
and dashboards.

Developer:

Plotly Technologies Inc.

Why Plotly?

1. Interactive Charts
2. Professional Dashboards
3. Zoom & Pan Features
4. Hover Information
5. Web-based Visualization

Applications:

1. Data Science
2. Business Analytics
3. Research Projects
4. Dashboard Development
5. Machine Learning

Main Modules:

1. plotly.express
2. plotly.graph_objects

Import:

import plotly.express as px
"""

# ======================================
# SAMPLE DATASET
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
# 1. FIRST PLOTLY CHART
# ======================================

print("\n1. FIRST PLOTLY CHART")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks",
    title="Student Performance"
)

fig.show()

# ======================================
# 2. LINE CHART
# ======================================

print("\n2. LINE CHART")

fig = px.line(
    student_data,
    x="Student",
    y="Marks",
    title="Student Marks Trend"
)

fig.show()

# ======================================
# 3. SCATTER CHART
# ======================================

print("\n3. SCATTER CHART")

fig = px.scatter(
    student_data,
    x="Student",
    y="Marks",
    title="Scatter Plot Example"
)

fig.show()

# ======================================
# 4. PIE CHART
# ======================================

print("\n4. PIE CHART")

fig = px.pie(
    student_data,
    names="Student",
    values="Marks",
    title="Marks Distribution"
)

fig.show()

# ======================================
# 5. HISTOGRAM
# ======================================

print("\n5. HISTOGRAM")

fig = px.histogram(
    student_data,
    x="Marks",
    title="Marks Distribution"
)

fig.show()

# ======================================
# 6. CUSTOM TITLES
# ======================================

print("\n6. CUSTOM TITLES")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks"
)

fig.update_layout(
    title="Custom Student Dashboard"
)

fig.show()

# ======================================
# 7. SALES DATA EXAMPLE
# ======================================

print("\n7. SALES DATA")

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

fig = px.line(
    sales_data,
    x="Month",
    y="Sales",
    title="Monthly Sales"
)

fig.show()

# ======================================
# 8. ATTENDANCE ANALYSIS
# ======================================

print("\n8. ATTENDANCE ANALYSIS")

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
# 9. SAVE CHART AS HTML
# ======================================

print("\n9. SAVE CHART")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks"
)

fig.write_html(
    "student_dashboard.html"
)

print(
    "Chart Saved Successfully"
)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

name = input(
    "Enter Student Name: "
)

marks = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"{name} scored {marks}"
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
px.line()
px.scatter()
px.pie()
px.histogram()

fig.show()
fig.write_html()

fig.update_layout()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Install Plotly.

Exercise 2:
Create a Bar Chart.

Exercise 3:
Create a Line Chart.

Exercise 4:
Save chart as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Plotly?

Q2. Why use Plotly?

Q3. Difference between
Matplotlib and Plotly?

Q4. What is plotly.express?

Q5. Why are Plotly charts
interactive?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Dashboard.

Columns:

1. Student
2. Marks
3. Attendance

Generate:

1. Bar Chart
2. Line Chart
3. Pie Chart

Create an interactive report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 081 Completed Successfully!"
)