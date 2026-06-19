# ======================================
# Day 086: Plotly Histograms
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Interactive Histograms
# using Plotly
# ======================================

print("=" * 50)
print("DAY 086 - PLOTLY HISTOGRAMS")
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
What is a Histogram?

A Histogram is used to show
the frequency distribution
of numerical data.

Plotly Function:

px.histogram()

Applications:

1. Student Marks Analysis
2. Salary Distribution
3. Sales Analysis
4. Machine Learning
5. Data Exploration

Advantages:

1. Understand Distribution
2. Detect Patterns
3. Identify Outliers
4. Interactive Visualization
"""

# ======================================
# STUDENT MARKS DATASET
# ======================================

marks_data = pd.DataFrame(
    {
        "Marks": [
            92, 88, 95, 81, 90,
            78, 84, 89, 91, 87,
            76, 85, 93, 80, 82
        ]
    }
)

print("\nMARKS DATASET")
print(marks_data)

# ======================================
# 1. BASIC HISTOGRAM
# ======================================

print("\n1. BASIC HISTOGRAM")

fig = px.histogram(
    marks_data,
    x="Marks",
    title="Marks Distribution"
)

fig.show()

# ======================================
# 2. CUSTOM NUMBER OF BINS
# ======================================

print("\n2. CUSTOM BINS")

fig = px.histogram(
    marks_data,
    x="Marks",
    nbins=5,
    title="Histogram with 5 Bins"
)

fig.show()

# ======================================
# 3. SALES DISTRIBUTION
# ======================================

print("\n3. SALES DISTRIBUTION")

sales_data = pd.DataFrame(
    {
        "Sales": [
            1000, 1200, 1500,
            1300, 1800, 2100,
            1700, 1900
        ]
    }
)

fig = px.histogram(
    sales_data,
    x="Sales",
    title="Sales Distribution"
)

fig.show()

# ======================================
# 4. EXAM PERFORMANCE
# ======================================

print("\n4. EXAM PERFORMANCE")

exam_data = pd.DataFrame(
    {
        "Scores": [
            55, 60, 62, 65, 67,
            70, 72, 75, 78, 80,
            82, 85, 88, 90, 92
        ]
    }
)

fig = px.histogram(
    exam_data,
    x="Scores",
    nbins=6,
    title="Exam Score Distribution"
)

fig.show()

# ======================================
# 5. RANDOM DATASET
# ======================================

print("\n5. RANDOM DATASET")

random_data = pd.DataFrame(
    {
        "Values":
        np.random.randint(
            1,
            100,
            100
        )
    }
)

fig = px.histogram(
    random_data,
    x="Values",
    title="Random Data Distribution"
)

fig.show()

# ======================================
# 6. ATTENDANCE ANALYSIS
# ======================================

print("\n6. ATTENDANCE ANALYSIS")

attendance_data = pd.DataFrame(
    {
        "Attendance": [
            60, 65, 70, 75, 80,
            85, 90, 95, 100
        ]
    }
)

fig = px.histogram(
    attendance_data,
    x="Attendance",
    title="Attendance Distribution"
)

fig.show()

# ======================================
# 7. STUDY HOURS ANALYSIS
# ======================================

print("\n7. STUDY HOURS ANALYSIS")

study_data = pd.DataFrame(
    {
        "Study_Hours": [
            1, 2, 2, 3, 4,
            5, 5, 6, 7, 8
        ]
    }
)

fig = px.histogram(
    study_data,
    x="Study_Hours",
    title="Study Hours Distribution"
)

fig.show()

# ======================================
# 8. CUSTOM LAYOUT
# ======================================

print("\n8. CUSTOM LAYOUT")

fig = px.histogram(
    marks_data,
    x="Marks"
)

fig.update_layout(
    title="Professional Marks Dashboard",
    xaxis_title="Marks",
    yaxis_title="Frequency"
)

fig.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

fig = px.histogram(
    marks_data,
    x="Marks"
)

fig.write_html(
    "plotly_histogram.html"
)

print(
    "Chart Saved Successfully"
)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

value = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"Marks Entered: {value}"
)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT")

project_data = pd.DataFrame(
    {
        "Marks": [
            92, 88, 95, 81, 90,
            78, 84, 89, 91, 87,
            76, 85, 93, 80, 82
        ]
    }
)

print(project_data)

fig = px.histogram(
    project_data,
    x="Marks",
    nbins=5,
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
px.histogram()

nbins=5

fig.show()

fig.update_layout()

fig.write_html()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Histogram.

Exercise 2:
Use nbins=5 and nbins=10.

Exercise 3:
Analyze Marks Distribution.

Exercise 4:
Save chart as HTML.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is px.histogram()?

Q2. What is a Histogram?

Q3. What are bins?

Q4. Why use Histograms?

Q5. Difference between
Bar Chart and Histogram?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics Dashboard.

Columns:

1. Marks

Generate:

1. Histogram
2. Distribution Analysis
3. Performance Report

Create an interactive report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 086 Completed Successfully!"
)