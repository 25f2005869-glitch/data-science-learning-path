# ======================================
# Day 059: Data Visualization with Pandas
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Data Visualization using Pandas
# and Matplotlib
# ======================================

print("=" * 50)
print("DAY 059 - DATA VISUALIZATION WITH PANDAS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Data Visualization?

Data Visualization is the graphical
representation of data.

Benefits:

1. Better Understanding
2. Trend Analysis
3. Pattern Recognition
4. Business Insights
5. Decision Making

Common Charts:

1. Line Chart
2. Bar Chart
3. Histogram
4. Pie Chart
5. Scatter Plot

Libraries:

1. Matplotlib
2. Pandas
3. Seaborn
4. Plotly
"""

# ======================================
# SAMPLE DATAFRAME
# ======================================

student_data = {
    "Name": [
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

df = pd.DataFrame(student_data)

print("\nSTUDENT DATA")
print(df)

# ======================================
# 1. LINE CHART
# ======================================

print("\n1. LINE CHART")

df.plot(
    x="Name",
    y="Marks",
    kind="line",
    title="Student Marks"
)

plt.show()

# ======================================
# 2. BAR CHART
# ======================================

print("\n2. BAR CHART")

df.plot(
    x="Name",
    y="Marks",
    kind="bar",
    title="Student Marks Bar Chart"
)

plt.show()

# ======================================
# 3. HISTOGRAM
# ======================================

print("\n3. HISTOGRAM")

df["Marks"].plot(
    kind="hist",
    bins=5,
    title="Marks Distribution"
)

plt.show()

# ======================================
# 4. PIE CHART
# ======================================

print("\n4. PIE CHART")

df.set_index(
    "Name"
)["Marks"].plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Marks Percentage"
)

plt.ylabel("")
plt.show()

# ======================================
# 5. SCATTER PLOT
# ======================================

print("\n5. SCATTER PLOT")

student_scores = pd.DataFrame(
    {
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
        ]
    }
)

student_scores.plot(
    x="Math",
    y="Python",
    kind="scatter",
    title="Math vs Python"
)

plt.show()

# ======================================
# 6. MULTIPLE COLUMN LINE CHART
# ======================================

print("\n6. MULTIPLE COLUMN CHART")

student_scores.plot(
    kind="line",
    title="Subject Comparison"
)

plt.show()

# ======================================
# 7. CUSTOM FIGURE SIZE
# ======================================

print("\n7. CUSTOM FIGURE SIZE")

plt.figure(
    figsize=(8, 4)
)

df.plot(
    x="Name",
    y="Marks",
    kind="bar"
)

plt.show()

# ======================================
# 8. SALES DATA VISUALIZATION
# ======================================

print("\n8. SALES DATA")

sales_df = pd.DataFrame(
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

print(sales_df)

sales_df.plot(
    x="Month",
    y="Sales",
    kind="line",
    title="Monthly Sales"
)

plt.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

sales_df.plot(
    x="Month",
    y="Sales",
    kind="line"
)

plt.savefig(
    "sales_chart.png"
)

plt.close()

print("Chart Saved")

# ======================================
# 10. BOX PLOT
# ======================================

print("\n10. BOX PLOT")

df["Marks"].plot(
    kind="box",
    title="Marks Box Plot"
)

plt.show()

# ======================================
# 11. AREA CHART
# ======================================

print("\n11. AREA CHART")

sales_df.plot(
    x="Month",
    y="Sales",
    kind="area",
    title="Sales Area Chart"
)

plt.show()

# ======================================
# 12. STACKED BAR CHART
# ======================================

print("\n12. STACKED BAR CHART")

subjects = pd.DataFrame(
    {
        "Math": [90, 85, 88],
        "Python": [92, 89, 91]
    },
    index=[
        "Student1",
        "Student2",
        "Student3"
    ]
)

subjects.plot(
    kind="bar",
    stacked=True,
    title="Stacked Subject Marks"
)

plt.show()

# ======================================
# 13. DATA SUMMARY
# ======================================

print("\n13. DATA SUMMARY")

print(df.describe())

# ======================================
# 14. USER INPUT EXAMPLE
# ======================================

print("\n14. USER INPUT EXAMPLE")

name = input(
    "Enter Student Name: "
)

marks = int(
    input(
        "Enter Marks: "
    )
)

user_df = pd.DataFrame(
    {
        "Name": [name],
        "Marks": [marks]
    }
)

print(user_df)

# ======================================
# 15. MINI PROJECT
# ======================================

print("\n15. MINI PROJECT")

result_df = pd.DataFrame(
    {
        "Student": [
            "A",
            "B",
            "C",
            "D",
            "E"
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

print(result_df)

result_df.plot(
    x="Student",
    y="Marks",
    kind="bar",
    title="Student Performance Report"
)

plt.show()

print(
    "Average Marks:",
    result_df["Marks"].mean()
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Line Chart
using student marks.

Exercise 2:
Create a Bar Chart.

Exercise 3:
Create a Histogram.

Exercise 4:
Create a Pie Chart.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Dashboard.

Display:

1. Line Chart
2. Bar Chart
3. Pie Chart
4. Histogram

Generate complete analysis report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 059 Completed Successfully!")