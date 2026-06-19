# ======================================
# Day 065: Pie Charts
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Pie Charts using
# Matplotlib
# ======================================

print("=" * 50)
print("DAY 065 - PIE CHARTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARY
# ======================================

import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Pie Chart?

A Pie Chart is used to show
proportions or percentages
of a whole.

Applications:

1. Budget Analysis
2. Market Share Analysis
3. Subject Marks Distribution
4. Business Reports
5. Survey Results

Function:

plt.pie()

Important Parameters:

1. labels
2. autopct
3. startangle
4. explode
"""

# ======================================
# 1. BASIC PIE CHART
# ======================================

print("\n1. BASIC PIE CHART")

subjects = [
    "Math",
    "Python",
    "DBMS",
    "Statistics"
]

marks = [
    92,
    95,
    88,
    90
]

plt.pie(marks)

plt.title(
    "Basic Pie Chart"
)

plt.show()

# ======================================
# 2. PIE CHART WITH LABELS
# ======================================

print("\n2. LABELS")

plt.pie(
    marks,
    labels=subjects
)

plt.title(
    "Subject Distribution"
)

plt.show()

# ======================================
# 3. PERCENTAGES
# ======================================

print("\n3. PERCENTAGES")

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title(
    "Subject Percentage"
)

plt.show()

# ======================================
# 4. START ANGLE
# ======================================

print("\n4. START ANGLE")

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Start Angle Example"
)

plt.show()

# ======================================
# 5. EXPLODE EFFECT
# ======================================

print("\n5. EXPLODE EFFECT")

explode = (
    0,
    0.1,
    0,
    0
)

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    explode=explode
)

plt.title(
    "Exploded Pie Chart"
)

plt.show()

# ======================================
# 6. STUDENT MARKS ANALYSIS
# ======================================

print("\n6. STUDENT ANALYSIS")

students = [
    "Saloni",
    "Riya",
    "Ankit",
    "Rahul",
    "Priya"
]

student_marks = [
    92,
    88,
    95,
    81,
    90
]

plt.pie(
    student_marks,
    labels=students,
    autopct="%1.1f%%"
)

plt.title(
    "Student Marks Distribution"
)

plt.show()

# ======================================
# 7. MONTHLY EXPENSES
# ======================================

print("\n7. MONTHLY EXPENSES")

expenses = [
    "Food",
    "Transport",
    "Books",
    "Internet",
    "Others"
]

amounts = [
    3000,
    1500,
    2000,
    1000,
    500
]

plt.pie(
    amounts,
    labels=expenses,
    autopct="%1.1f%%"
)

plt.title(
    "Monthly Expenses"
)

plt.show()

# ======================================
# 8. MARKET SHARE
# ======================================

print("\n8. MARKET SHARE")

companies = [
    "A",
    "B",
    "C",
    "D"
]

share = [
    40,
    30,
    20,
    10
]

plt.pie(
    share,
    labels=companies,
    autopct="%1.1f%%"
)

plt.title(
    "Market Share Analysis"
)

plt.show()

# ======================================
# 9. SAVE PIE CHART
# ======================================

print("\n9. SAVE PIE CHART")

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title(
    "Saved Pie Chart"
)

plt.savefig(
    "pie_chart.png"
)

plt.close()

print(
    "Pie Chart Saved Successfully"
)

# ======================================
# 10. DISPLAY LEGEND
# ======================================

print("\n10. LEGEND")

plt.pie(
    marks
)

plt.legend(
    subjects
)

plt.title(
    "Pie Chart with Legend"
)

plt.show()

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

n = int(
    input(
        "Enter Number of Categories: "
    )
)

labels = []
values = []

for i in range(n):

    label = input(
        f"Category {i+1}: "
    )

    value = int(
        input(
            f"Value {i+1}: "
        )
    )

    labels.append(label)
    values.append(value)

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title(
    "User Data Pie Chart"
)

plt.show()

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

subjects = [
    "Math",
    "Python",
    "DBMS",
    "Statistics",
    "English"
]

marks = [
    92,
    95,
    88,
    90,
    85
]

plt.figure(
    figsize=(6, 6)
)

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title(
    "Subject Marks Distribution"
)

plt.show()

total_marks = sum(marks)

print(
    "Total Marks:",
    total_marks
)

print(
    "Average Marks:",
    round(
        total_marks / len(marks),
        2
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Pie Chart
using subject marks.

Exercise 2:
Display percentages.

Exercise 3:
Use explode effect.

Exercise 4:
Save chart as PNG.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Budget Analysis System.

Categories:

1. Food
2. Education
3. Travel
4. Internet
5. Others

Display:

1. Pie Chart
2. Percentages
3. Total Budget

Generate complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 065 Completed Successfully!")