# ======================================
# Day 072: Seaborn Line Plots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Professional Line Plots
# using Seaborn
# ======================================

print("=" * 50)
print("DAY 072 - SEABORN LINE PLOTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Line Plot?

A Line Plot is used to visualize
trends and changes over time.

Applications:

1. Sales Trends
2. Stock Prices
3. Student Progress
4. Population Growth
5. Machine Learning Analysis

Seaborn Function:

sns.lineplot()

Advantages:

1. Attractive Visuals
2. Statistical Confidence
3. Easy Integration with Pandas
4. Less Code
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
# 1. BASIC LINE PLOT
# ======================================

print("\n1. BASIC LINE PLOT")

sns.lineplot(
    data=sales_data,
    x="Month",
    y="Sales"
)

plt.title(
    "Monthly Sales Trend"
)

plt.show()

# ======================================
# 2. LINE PLOT WITH MARKERS
# ======================================

print("\n2. LINE PLOT WITH MARKERS")

sns.lineplot(
    data=sales_data,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title(
    "Sales Trend with Markers"
)

plt.show()

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

sns.lineplot(
    data=student_data,
    x="Test",
    y="Marks",
    marker="o"
)

plt.title(
    "Student Progress"
)

plt.show()

# ======================================
# 4. MULTIPLE LINE PLOTS
# ======================================

print("\n4. MULTIPLE LINE PLOTS")

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

sns.lineplot(
    data=comparison_data,
    x="Month",
    y="Sales",
    marker="o",
    label="Sales"
)

sns.lineplot(
    data=comparison_data,
    x="Month",
    y="Profit",
    marker="s",
    label="Profit"
)

plt.title(
    "Sales vs Profit"
)

plt.legend()

plt.show()

# ======================================
# 5. CUSTOM STYLE
# ======================================

print("\n5. CUSTOM STYLE")

sns.set_style(
    "darkgrid"
)

sns.lineplot(
    data=sales_data,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# 6. DIFFERENT STYLE
# ======================================

print("\n6. WHITEGRID STYLE")

sns.set_style(
    "whitegrid"
)

sns.lineplot(
    data=sales_data,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title(
    "White Grid Style"
)

plt.show()

# ======================================
# 7. ATTENDANCE ANALYSIS
# ======================================

print("\n7. ATTENDANCE ANALYSIS")

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

sns.lineplot(
    data=attendance_data,
    x="Month",
    y="Attendance",
    marker="o"
)

plt.title(
    "Attendance Trend"
)

plt.show()

# ======================================
# 8. EXAM PERFORMANCE
# ======================================

print("\n8. EXAM PERFORMANCE")

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

sns.lineplot(
    data=exam_data,
    x="Exam",
    y="Marks",
    marker="o"
)

plt.title(
    "Exam Performance"
)

plt.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

sns.lineplot(
    data=sales_data,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title(
    "Sales Trend"
)

plt.savefig(
    "seaborn_line_plot.png"
)

plt.close()

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
            "W1",
            "W2",
            "W3",
            "W4",
            "W5"
        ],
        "Python": [
            65,
            72,
            80,
            88,
            95
        ]
    }
)

print(progress_data)

sns.lineplot(
    data=progress_data,
    x="Week",
    y="Python",
    marker="o"
)

plt.title(
    "Python Learning Progress"
)

plt.xlabel(
    "Weeks"
)

plt.ylabel(
    "Performance Score"
)

plt.show()

print(
    "Average Score:",
    progress_data["Python"].mean()
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a line plot
using monthly sales.

Exercise 2:
Add markers.

Exercise 3:
Compare two lines:

- Sales
- Profit

Exercise 4:
Apply different styles.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is sns.lineplot()?

Q2. Why use line plots?

Q3. Difference between
Matplotlib and Seaborn
line plots?

Q4. What is a trend?

Q5. What is the purpose
of markers?
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

Create:

1. Line Plot
2. Trend Analysis
3. Performance Report

Identify growth over time.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 072 Completed Successfully!"
)