# ======================================
# Day 067: Subplots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Multiple Charts in a
# Single Figure using Matplotlib
# ======================================

print("=" * 50)
print("DAY 067 - SUBPLOTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARY
# ======================================

import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What are Subplots?

Subplots allow multiple charts
to be displayed in a single figure.

Advantages:

1. Compare Multiple Datasets
2. Better Visualization
3. Dashboard Creation
4. Professional Reporting

Functions:

plt.subplot()

Syntax:

plt.subplot(rows, columns, position)

Applications:

1. Student Analytics
2. Business Dashboards
3. Data Science Reports
4. Research Projects
"""

# ======================================
# SAMPLE DATA
# ======================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    1000,
    1200,
    1500,
    1300,
    1800
]

profits = [
    200,
    250,
    350,
    300,
    450
]

# ======================================
# 1. TWO SUBPLOTS
# ======================================

print("\n1. TWO SUBPLOTS")

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales")

plt.subplot(1, 2, 2)

plt.plot(
    months,
    profits,
    marker="o"
)

plt.title("Profit")

plt.tight_layout()

plt.show()

# ======================================
# 2. FOUR SUBPLOTS
# ======================================

print("\n2. FOUR SUBPLOTS")

plt.figure(figsize=(8, 6))

plt.subplot(2, 2, 1)

plt.plot(
    months,
    sales
)

plt.title("Line Plot")

plt.subplot(2, 2, 2)

plt.bar(
    months,
    sales
)

plt.title("Bar Chart")

plt.subplot(2, 2, 3)

plt.hist(
    sales,
    bins=5
)

plt.title("Histogram")

plt.subplot(2, 2, 4)

plt.scatter(
    sales,
    profits
)

plt.title("Scatter Plot")

plt.tight_layout()

plt.show()

# ======================================
# 3. STUDENT DASHBOARD
# ======================================

print("\n3. STUDENT DASHBOARD")

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

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)

plt.bar(
    subjects,
    marks
)

plt.title("Marks")

plt.subplot(2, 2, 2)

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Percentage")

plt.subplot(2, 2, 3)

plt.plot(
    subjects,
    marks,
    marker="o"
)

plt.title("Trend")

plt.subplot(2, 2, 4)

plt.hist(
    marks,
    bins=4
)

plt.title("Distribution")

plt.tight_layout()

plt.show()

# ======================================
# 4. VERTICAL SUBPLOTS
# ======================================

print("\n4. VERTICAL SUBPLOTS")

plt.figure(figsize=(6, 6))

plt.subplot(2, 1, 1)

plt.plot(
    months,
    sales
)

plt.title("Sales")

plt.subplot(2, 1, 2)

plt.plot(
    months,
    profits
)

plt.title("Profit")

plt.tight_layout()

plt.show()

# ======================================
# 5. HORIZONTAL SUBPLOTS
# ======================================

print("\n5. HORIZONTAL SUBPLOTS")

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)

plt.bar(
    months,
    sales
)

plt.title("Sales")

plt.subplot(1, 2, 2)

plt.bar(
    months,
    profits
)

plt.title("Profit")

plt.tight_layout()

plt.show()

# ======================================
# 6. ATTENDANCE ANALYSIS
# ======================================

print("\n6. ATTENDANCE ANALYSIS")

attendance = [
    75,
    80,
    85,
    90,
    95
]

marks = [
    70,
    75,
    82,
    90,
    96
]

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)

plt.plot(
    attendance,
    marks
)

plt.title(
    "Attendance Trend"
)

plt.subplot(1, 2, 2)

plt.scatter(
    attendance,
    marks
)

plt.title(
    "Attendance vs Marks"
)

plt.tight_layout()

plt.show()

# ======================================
# 7. SALES DASHBOARD
# ======================================

print("\n7. SALES DASHBOARD")

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)

plt.plot(
    months,
    sales
)

plt.title("Sales Trend")

plt.subplot(2, 2, 2)

plt.bar(
    months,
    sales
)

plt.title("Sales Comparison")

plt.subplot(2, 2, 3)

plt.hist(
    sales
)

plt.title("Sales Distribution")

plt.subplot(2, 2, 4)

plt.pie(
    sales,
    labels=months,
    autopct="%1.1f%%"
)

plt.title("Sales Share")

plt.tight_layout()

plt.show()

# ======================================
# 8. USER INPUT EXAMPLE
# ======================================

print("\n8. USER INPUT EXAMPLE")

value1 = int(
    input(
        "Enter First Value: "
    )
)

value2 = int(
    input(
        "Enter Second Value: "
    )
)

plt.figure(figsize=(6, 3))

plt.subplot(1, 2, 1)

plt.bar(
    ["A"],
    [value1]
)

plt.title("Value 1")

plt.subplot(1, 2, 2)

plt.bar(
    ["B"],
    [value2]
)

plt.title("Value 2")

plt.tight_layout()

plt.show()

# ======================================
# 9. MINI PROJECT
# ======================================

print("\n9. MINI PROJECT")

students = [
    "A",
    "B",
    "C",
    "D",
    "E"
]

marks = [
    85,
    92,
    78,
    95,
    88
]

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)

plt.bar(
    students,
    marks
)

plt.title(
    "Student Marks"
)

plt.subplot(2, 2, 2)

plt.plot(
    students,
    marks,
    marker="o"
)

plt.title(
    "Performance Trend"
)

plt.subplot(2, 2, 3)

plt.hist(
    marks,
    bins=5
)

plt.title(
    "Marks Distribution"
)

plt.subplot(2, 2, 4)

plt.pie(
    marks,
    labels=students,
    autopct="%1.1f%%"
)

plt.title(
    "Marks Share"
)

plt.tight_layout()

plt.show()

print(
    "Average Marks:",
    round(
        sum(marks) / len(marks),
        2
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create two subplots.

Exercise 2:
Create a 2x2 dashboard.

Exercise 3:
Combine:

- Line Plot
- Bar Chart
- Histogram
- Pie Chart

Exercise 4:
Use tight_layout().
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Analytics Dashboard.

Display:

1. Bar Chart
2. Line Plot
3. Histogram
4. Pie Chart

Show all charts in a
single figure using subplots.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 067 Completed Successfully!")