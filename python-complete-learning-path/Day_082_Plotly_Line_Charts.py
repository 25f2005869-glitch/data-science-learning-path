# ======================================
# Day 082: Plotly Line Charts
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Interactive Line Charts
# using Plotly
# ======================================

print("=" * 50)
print("DAY 082 - PLOTLY LINE CHARTS")
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
What is a Line Chart?

A Line Chart is used to visualize
trends and changes over time.

Plotly Function:

px.line()

Applications:

1. Sales Trends
2. Stock Prices
3. Student Progress
4. Population Growth
5. Business Analytics

Advantages:

1. Interactive Visualization
2. Hover Information
3. Zoom and Pan
4. Professional Appearance
"""

# ======================================
# SAMPLE DATASET
# ======================================

sales_data = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],

        "Sales": [
            1000,
            1200,
            1500,
            1300,
            1800,
            2100
        ]
    }
)

print("\nSALES DATASET")
print(sales_data)

# ======================================
# 1. BASIC LINE CHART
# ======================================

print("\n1. BASIC LINE CHART")

fig = px.line(
    sales_data,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend"
)

fig.show()

# ======================================
# 2. LINE CHART WITH MARKERS
# ======================================

print("\n2. LINE CHART WITH MARKERS")

fig = px.line(
    sales_data,
    x="Month",
    y="Sales",
    markers=True,
    title="Sales Trend with Markers"
)

fig.show()

# ======================================
# 3. STUDENT PERFORMANCE
# ======================================

print("\n3. STUDENT PERFORMANCE")

student_data = pd.DataFrame(
    {
        "Test": [
            "Test1",
            "Test2",
            "Test3",
            "Test4",
            "Test5"
        ],

        "Marks": [
            72,
            78,
            85,
            89,
            94
        ]
    }
)

print(student_data)

fig = px.line(
    student_data,
    x="Test",
    y="Marks",
    markers=True,
    title="Student Progress"
)

fig.show()

# ======================================
# 4. MULTIPLE LINES
# ======================================

print("\n4. MULTIPLE LINE CHART")

comparison_data = pd.DataFrame(
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

fig = px.line(
    comparison_data,
    x="Month",
    y=[
        "Sales",
        "Profit"
    ],
    markers=True,
    title="Sales vs Profit"
)

fig.show()

# ======================================
# 5. ATTENDANCE TREND
# ======================================

print("\n5. ATTENDANCE TREND")

attendance_data = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],

        "Attendance": [
            80,
            85,
            88,
            92,
            95
        ]
    }
)

fig = px.line(
    attendance_data,
    x="Month",
    y="Attendance",
    markers=True,
    title="Attendance Trend"
)

fig.show()

# ======================================
# 6. EXAM PERFORMANCE
# ======================================

print("\n6. EXAM PERFORMANCE")

exam_data = pd.DataFrame(
    {
        "Exam": [
            "Unit Test",
            "Midterm",
            "Practical",
            "Final"
        ],

        "Marks": [
            70,
            82,
            88,
            94
        ]
    }
)

fig = px.line(
    exam_data,
    x="Exam",
    y="Marks",
    markers=True,
    title="Exam Performance"
)

fig.show()

# ======================================
# 7. CUSTOM LAYOUT
# ======================================

print("\n7. CUSTOM LAYOUT")

fig = px.line(
    sales_data,
    x="Month",
    y="Sales",
    markers=True
)

fig.update_layout(
    title="Professional Sales Dashboard",
    xaxis_title="Month",
    yaxis_title="Sales Amount"
)

fig.show()

# ======================================
# 8. SALES DASHBOARD
# ======================================

print("\n8. SALES DASHBOARD")

sales_dashboard = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],

        "Revenue": [
            5000,
            5500,
            6200,
            6100,
            7000,
            7800
        ]
    }
)

fig = px.line(
    sales_dashboard,
    x="Month",
    y="Revenue",
    markers=True,
    title="Revenue Trend"
)

fig.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

fig = px.line(
    sales_data,
    x="Month",
    y="Sales"
)

fig.write_html(
    "plotly_line_chart.html"
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

progress_data = pd.DataFrame(
    {
        "Week": [
            "Week1",
            "Week2",
            "Week3",
            "Week4",
            "Week5"
        ],

        "Python_Score": [
            65,
            72,
            80,
            88,
            95
        ]
    }
)

print(progress_data)

fig = px.line(
    progress_data,
    x="Week",
    y="Python_Score",
    markers=True,
    title="Python Learning Progress"
)

fig.show()

print(
    "Average Score:",
    round(
        progress_data[
            "Python_Score"
        ].mean(),
        2
    )
)

# ======================================
# IMPORTANT FUNCTIONS
# ======================================

"""
px.line()

fig.show()

fig.update_layout()

fig.write_html()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Line Chart
using monthly sales.

Exercise 2:
Add markers.

Exercise 3:
Compare Sales and Profit.

Exercise 4:
Save chart as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is px.line()?

Q2. Why use Line Charts?

Q3. What are markers?

Q4. What is an interactive chart?

Q5. Why use Plotly?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Progress Tracker.

Columns:

1. Month
2. Study Hours
3. Marks

Generate:

1. Line Chart
2. Trend Analysis
3. Progress Report

Identify growth over time.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 082 Completed Successfully!"
)