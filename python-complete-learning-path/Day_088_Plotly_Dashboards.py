# ======================================
# Day 088: Plotly Dashboards
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Building Interactive Dashboards
# using Plotly
# ======================================

print("=" * 50)
print("DAY 088 - PLOTLY DASHBOARDS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Dashboard?

A Dashboard is a collection of
multiple visualizations displayed
in a single screen.

Why Dashboards?

1. Centralized Analytics
2. Business Reporting
3. Performance Monitoring
4. Data Storytelling
5. Interactive Insights

Plotly Tools:

1. plotly.express
2. plotly.graph_objects
3. plotly.subplots
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
print(student_data)

# ======================================
# DASHBOARD CREATION
# ======================================

print("\nCREATING DASHBOARD")

fig = sp.make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Marks",
        "Attendance",
        "Study Hours",
        "Performance"
    )
)

# ======================================
# BAR CHART
# ======================================

fig.add_trace(
    go.Bar(
        x=student_data["Student"],
        y=student_data["Marks"],
        name="Marks"
    ),
    row=1,
    col=1
)

# ======================================
# LINE CHART
# ======================================

fig.add_trace(
    go.Scatter(
        x=student_data["Student"],
        y=student_data["Attendance"],
        mode="lines+markers",
        name="Attendance"
    ),
    row=1,
    col=2
)

# ======================================
# PIE CHART
# ======================================

fig.add_trace(
    go.Pie(
        labels=student_data["Student"],
        values=student_data["Study_Hours"],
        name="Study Hours"
    ),
    row=2,
    col=1
)

# ======================================
# SCATTER PLOT
# ======================================

fig.add_trace(
    go.Scatter(
        x=student_data["Study_Hours"],
        y=student_data["Marks"],
        mode="markers",
        name="Performance"
    ),
    row=2,
    col=2
)

# ======================================
# DASHBOARD TITLE
# ======================================

fig.update_layout(
    title="Student Analytics Dashboard",
    height=800
)

fig.show()

# ======================================
# SALES DASHBOARD
# ======================================

print("\nSALES DASHBOARD")

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
        ],

        "Profit": [
            200,
            250,
            350,
            300,
            450
        ]
    }
)

fig = sp.make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(
        "Sales",
        "Profit"
    )
)

fig.add_trace(
    go.Bar(
        x=sales_data["Month"],
        y=sales_data["Sales"]
    ),
    row=1,
    col=1
)

fig.add_trace(
    go.Scatter(
        x=sales_data["Month"],
        y=sales_data["Profit"],
        mode="lines+markers"
    ),
    row=1,
    col=2
)

fig.update_layout(
    title="Sales Dashboard"
)

fig.show()

# ======================================
# ATTENDANCE DASHBOARD
# ======================================

print("\nATTENDANCE DASHBOARD")

fig = px.bar(
    student_data,
    x="Student",
    y="Attendance",
    title="Attendance Dashboard"
)

fig.show()

# ======================================
# PERFORMANCE ANALYSIS
# ======================================

print("\nPERFORMANCE ANALYSIS")

print(
    "Highest Marks:",
    student_data["Marks"].max()
)

print(
    "Lowest Marks:",
    student_data["Marks"].min()
)

print(
    "Average Marks:",
    round(
        student_data["Marks"].mean(),
        2
    )
)

# ======================================
# SAVE DASHBOARD
# ======================================

print("\nSAVE DASHBOARD")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks"
)

fig.write_html(
    "plotly_dashboard.html"
)

print(
    "Dashboard Saved Successfully"
)

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

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
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

project_data = pd.DataFrame(
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

print(project_data)

fig = px.bar(
    project_data,
    x="Department",
    y="Students",
    title="Department Dashboard"
)

fig.show()

# ======================================
# IMPORTANT FUNCTIONS
# ======================================

"""
sp.make_subplots()

go.Bar()

go.Scatter()

go.Pie()

fig.add_trace()

fig.update_layout()

fig.write_html()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Dashboard with:

1. Bar Chart
2. Line Chart

Exercise 2:
Add Pie Chart.

Exercise 3:
Add Scatter Plot.

Exercise 4:
Save Dashboard as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is a Dashboard?

Q2. Why use Dashboards?

Q3. What is make_subplots()?

Q4. What is add_trace()?

Q5. Difference between
Plotly Express and
Graph Objects?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a College Dashboard.

Dataset:

1. Student Marks
2. Attendance
3. Study Hours

Generate:

1. Bar Chart
2. Line Chart
3. Pie Chart
4. Scatter Plot

Combine all in one Dashboard.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 088 Completed Successfully!"
)