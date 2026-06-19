# ======================================
# Day 073: Seaborn Bar Plots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Professional Bar Plots
# using Seaborn
# ======================================

print("=" * 50)
print("DAY 073 - SEABORN BAR PLOTS")
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
What is a Bar Plot?

A Bar Plot is used to compare
different categories of data.

Seaborn Function:

sns.barplot()

Applications:

1. Student Marks Analysis
2. Sales Comparison
3. Department Performance
4. Business Analytics
5. Survey Analysis

Advantages:

1. Easy Comparison
2. Attractive Design
3. Statistical Aggregation
4. Works with DataFrames
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

print("\nSTUDENT DATA")
print(student_data)

# ======================================
# 1. BASIC BAR PLOT
# ======================================

print("\n1. BASIC BAR PLOT")

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Student Marks"
)

plt.show()

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

print(subject_data)

sns.barplot(
    data=subject_data,
    x="Subject",
    y="Marks"
)

plt.title(
    "Subject Performance"
)

plt.show()

# ======================================
# 3. SALES ANALYSIS
# ======================================

print("\n3. SALES ANALYSIS")

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

sns.barplot(
    data=sales_data,
    x="Month",
    y="Sales"
)

plt.title(
    "Monthly Sales"
)

plt.show()

# ======================================
# 4. DEPARTMENT ANALYSIS
# ======================================

print("\n4. DEPARTMENT ANALYSIS")

department_data = pd.DataFrame(
    {
        "Department": [
            "DS",
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

sns.barplot(
    data=department_data,
    x="Department",
    y="Students"
)

plt.title(
    "Department Strength"
)

plt.show()

# ======================================
# 5. HORIZONTAL BAR PLOT
# ======================================

print("\n5. HORIZONTAL BAR PLOT")

sns.barplot(
    data=subject_data,
    x="Marks",
    y="Subject"
)

plt.title(
    "Horizontal Bar Plot"
)

plt.show()

# ======================================
# 6. STYLE SETTINGS
# ======================================

print("\n6. DARKGRID STYLE")

sns.set_style(
    "darkgrid"
)

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# 7. WHITEGRID STYLE
# ======================================

print("\n7. WHITEGRID STYLE")

sns.set_style(
    "whitegrid"
)

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "White Grid Style"
)

plt.show()

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

sns.barplot(
    data=attendance_data,
    x="Student",
    y="Attendance"
)

plt.title(
    "Attendance Analysis"
)

plt.show()

# ======================================
# 9. MULTIPLE CATEGORY DATA
# ======================================

print("\n9. MULTIPLE CATEGORY DATA")

result_data = pd.DataFrame(
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

sns.barplot(
    data=result_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Result Analysis"
)

plt.show()

# ======================================
# 10. SAVE BAR PLOT
# ======================================

print("\n10. SAVE BAR PLOT")

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Saved Bar Plot"
)

plt.savefig(
    "seaborn_bar_plot.png"
)

plt.close()

print(
    "Chart Saved Successfully"
)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

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
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

performance_data = pd.DataFrame(
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

print(performance_data)

sns.barplot(
    data=performance_data,
    x="Subject",
    y="Marks"
)

plt.title(
    "Subject Performance Dashboard"
)

plt.xlabel(
    "Subjects"
)

plt.ylabel(
    "Marks"
)

plt.show()

print(
    "Highest Marks:",
    performance_data["Marks"].max()
)

print(
    "Lowest Marks:",
    performance_data["Marks"].min()
)

print(
    "Average Marks:",
    performance_data["Marks"].mean()
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Bar Plot
using student marks.

Exercise 2:
Create a Horizontal
Bar Plot.

Exercise 3:
Apply:

- darkgrid
- whitegrid

Exercise 4:
Save chart as PNG.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is sns.barplot()?

Q2. Why use bar plots?

Q3. Difference between
Bar Plot and Histogram?

Q4. What is category data?

Q5. What is a horizontal
bar plot?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a College Report System.

Columns:

1. Department
2. Students
3. Average Marks

Create:

1. Department Comparison
2. Student Strength Analysis
3. Performance Report

Generate complete dashboard.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 073 Completed Successfully!"
)