# ======================================
# Day 085: Plotly Pie Charts
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Interactive Pie Charts
# using Plotly
# ======================================

print("=" * 50)
print("DAY 085 - PLOTLY PIE CHARTS")
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
What is a Pie Chart?

A Pie Chart is used to show
the proportion of different
categories in a dataset.

Plotly Function:

px.pie()

Applications:

1. Budget Analysis
2. Subject Marks Distribution
3. Market Share Analysis
4. Sales Contribution
5. Survey Results

Advantages:

1. Easy Visualization
2. Interactive Display
3. Percentage Analysis
4. Professional Reports
"""

# ======================================
# STUDENT MARKS DATASET
# ======================================

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

print("\nSUBJECT DATASET")
print(subject_data)

# ======================================
# 1. BASIC PIE CHART
# ======================================

print("\n1. BASIC PIE CHART")

fig = px.pie(
    subject_data,
    names="Subject",
    values="Marks",
    title="Subject Marks Distribution"
)

fig.show()

# ======================================
# 2. STUDENT ATTENDANCE
# ======================================

print("\n2. ATTENDANCE DISTRIBUTION")

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

fig = px.pie(
    attendance_data,
    names="Student",
    values="Attendance",
    title="Attendance Distribution"
)

fig.show()

# ======================================
# 3. SALES CONTRIBUTION
# ======================================

print("\n3. SALES CONTRIBUTION")

sales_data = pd.DataFrame(
    {
        "Product": [
            "Laptop",
            "Mobile",
            "Tablet",
            "Monitor"
        ],

        "Sales": [
            45000,
            35000,
            15000,
            10000
        ]
    }
)

fig = px.pie(
    sales_data,
    names="Product",
    values="Sales",
    title="Product Sales Contribution"
)

fig.show()

# ======================================
# 4. EXPENSE ANALYSIS
# ======================================

print("\n4. EXPENSE ANALYSIS")

expense_data = pd.DataFrame(
    {
        "Category": [
            "Food",
            "Rent",
            "Travel",
            "Education",
            "Others"
        ],

        "Amount": [
            5000,
            12000,
            3000,
            4000,
            2000
        ]
    }
)

fig = px.pie(
    expense_data,
    names="Category",
    values="Amount",
    title="Monthly Expense Distribution"
)

fig.show()

# ======================================
# 5. DONUT CHART
# ======================================

print("\n5. DONUT CHART")

fig = px.pie(
    expense_data,
    names="Category",
    values="Amount",
    hole=0.4,
    title="Expense Donut Chart"
)

fig.show()

# ======================================
# 6. EXAM RESULT ANALYSIS
# ======================================

print("\n6. EXAM RESULT ANALYSIS")

result_data = pd.DataFrame(
    {
        "Grade": [
            "A",
            "B",
            "C",
            "D"
        ],

        "Students": [
            40,
            30,
            20,
            10
        ]
    }
)

fig = px.pie(
    result_data,
    names="Grade",
    values="Students",
    title="Grade Distribution"
)

fig.show()

# ======================================
# 7. CUSTOM LAYOUT
# ======================================

print("\n7. CUSTOM LAYOUT")

fig = px.pie(
    subject_data,
    names="Subject",
    values="Marks"
)

fig.update_layout(
    title="Professional Subject Dashboard"
)

fig.show()

# ======================================
# 8. COMPANY DEPARTMENTS
# ======================================

print("\n8. COMPANY DEPARTMENTS")

department_data = pd.DataFrame(
    {
        "Department": [
            "HR",
            "Finance",
            "IT",
            "Marketing"
        ],

        "Employees": [
            25,
            20,
            40,
            15
        ]
    }
)

fig = px.pie(
    department_data,
    names="Department",
    values="Employees",
    title="Employee Distribution"
)

fig.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

fig = px.pie(
    subject_data,
    names="Subject",
    values="Marks"
)

fig.write_html(
    "plotly_pie_chart.html"
)

print(
    "Chart Saved Successfully"
)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

subject = input(
    "Enter Subject Name: "
)

marks = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"{subject}: {marks}"
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

fig = px.pie(
    project_data,
    names="Subject",
    values="Marks",
    hole=0.3,
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
px.pie()

hole=0.4

fig.show()

fig.update_layout()

fig.write_html()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Pie Chart.

Exercise 2:
Create a Donut Chart.

Exercise 3:
Analyze Expense Data.

Exercise 4:
Save chart as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is px.pie()?

Q2. What is a Donut Chart?

Q3. When should Pie Charts
be used?

Q4. Why use Plotly?

Q5. What is hole=0.4?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Budget Dashboard.

Columns:

1. Category
2. Amount

Generate:

1. Pie Chart
2. Donut Chart
3. Expense Analysis

Create an interactive report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 085 Completed Successfully!"
)