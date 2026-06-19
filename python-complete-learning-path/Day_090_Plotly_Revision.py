# ======================================
# Day 090: Plotly Revision
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Complete Revision of Plotly
# Interactive Data Visualization
# ======================================

print("=" * 60)
print("DAY 090 - PLOTLY REVISION")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import pandas as pd
import plotly.express as px

# ======================================
# REVISION NOTES
# ======================================

"""
PLOTLY REVISION CHEAT SHEET

Plotly is an interactive
data visualization library.

Topics Covered:

Day 081 : Introduction
Day 082 : Line Charts
Day 083 : Bar Charts
Day 084 : Scatter Plots
Day 085 : Pie Charts
Day 086 : Histograms
Day 087 : Heatmaps
Day 088 : Dashboards
Day 089 : Data Visualization Project

Main Modules:

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

print("\nDATASET")
print(student_data)

# ======================================
# 1. BAR CHART REVISION
# ======================================

print("\n1. BAR CHART")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks",
    title="Student Marks"
)

fig.show()

# ======================================
# 2. LINE CHART REVISION
# ======================================

print("\n2. LINE CHART")

fig = px.line(
    student_data,
    x="Student",
    y="Marks",
    markers=True,
    title="Marks Trend"
)

fig.show()

# ======================================
# 3. SCATTER PLOT REVISION
# ======================================

print("\n3. SCATTER PLOT")

fig = px.scatter(
    student_data,
    x="Study_Hours",
    y="Marks",
    title="Study Hours vs Marks"
)

fig.show()

# ======================================
# 4. PIE CHART REVISION
# ======================================

print("\n4. PIE CHART")

fig = px.pie(
    student_data,
    names="Student",
    values="Attendance",
    title="Attendance Distribution"
)

fig.show()

# ======================================
# 5. HISTOGRAM REVISION
# ======================================

print("\n5. HISTOGRAM")

fig = px.histogram(
    student_data,
    x="Marks",
    title="Marks Distribution"
)

fig.show()

# ======================================
# 6. HEATMAP REVISION
# ======================================

print("\n6. HEATMAP")

correlation = student_data[
    [
        "Marks",
        "Attendance",
        "Study_Hours"
    ]
].corr()

heatmap = px.imshow(
    correlation,
    text_auto=True,
    title="Correlation Heatmap"
)

heatmap.show()

# ======================================
# 7. PERFORMANCE ANALYSIS
# ======================================

print("\n7. PERFORMANCE ANALYSIS")

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
# 8. SAVE CHART
# ======================================

print("\n8. SAVE CHART")

fig = px.bar(
    student_data,
    x="Student",
    y="Marks"
)

fig.write_html(
    "plotly_revision_chart.html"
)

print(
    "Chart Saved Successfully"
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
px.imshow()

fig.show()
fig.write_html()
fig.update_layout()
"""

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
    title="Subject Performance"
)

fig.show()

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Plotly?

Q2. Difference between
Matplotlib and Plotly?

Q3. What is px.bar()?

Q4. What is px.line()?

Q5. What is px.scatter()?

Q6. What is px.pie()?

Q7. What is px.histogram()?

Q8. What is px.imshow()?

Q9. Why use Dashboards?

Q10. Why is Plotly Interactive?
"""

# ======================================
# PRACTICE QUESTIONS
# ======================================

"""
Practice 1:
Create a Bar Chart.

Practice 2:
Create a Line Chart.

Practice 3:
Create a Scatter Plot.

Practice 4:
Create a Pie Chart.

Practice 5:
Create a Histogram.

Practice 6:
Create a Heatmap.

Practice 7:
Build a Dashboard.
"""

# ======================================
# FINAL CHEAT SHEET
# ======================================

"""
Bar Chart     -> Comparison

Line Chart    -> Trends

Scatter Plot  -> Relationships

Pie Chart     -> Proportions

Histogram     -> Distribution

Heatmap       -> Correlation

Dashboard     -> Multiple Charts

Plotly        -> Interactive
                 Visualization
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a College Analytics Dashboard.

Dataset:

1. Marks
2. Attendance
3. Study Hours

Generate:

1. Bar Chart
2. Line Chart
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Heatmap
7. Dashboard

Perform complete EDA.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 090 Completed Successfully!"
)