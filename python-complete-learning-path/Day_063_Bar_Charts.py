# ======================================
# Day 063: Bar Charts
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Professional Bar Charts
# using Matplotlib
# ======================================

print("=" * 50)
print("DAY 063 - BAR CHARTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARY
# ======================================

import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Bar Chart?

A Bar Chart is used to compare
different categories of data.

Applications:

1. Student Marks Analysis
2. Sales Comparison
3. Population Comparison
4. Product Performance
5. Business Reports

Function:

plt.bar()

Advantages:

1. Easy Comparison
2. Clear Visualization
3. Suitable for Categories
"""

# ======================================
# 1. BASIC BAR CHART
# ======================================

print("\n1. BASIC BAR CHART")

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

plt.bar(
    subjects,
    marks
)

plt.title(
    "Subject Marks"
)

plt.xlabel(
    "Subjects"
)

plt.ylabel(
    "Marks"
)

plt.show()

# ======================================
# 2. STUDENT MARKS
# ======================================

print("\n2. STUDENT MARKS")

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

plt.bar(
    students,
    student_marks
)

plt.title(
    "Student Performance"
)

plt.xlabel(
    "Students"
)

plt.ylabel(
    "Marks"
)

plt.show()

# ======================================
# 3. BAR WIDTH
# ======================================

print("\n3. BAR WIDTH")

plt.bar(
    students,
    student_marks,
    width=0.5
)

plt.title(
    "Bar Width Example"
)

plt.show()

# ======================================
# 4. SALES COMPARISON
# ======================================

print("\n4. SALES COMPARISON")

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

plt.bar(
    months,
    sales
)

plt.title(
    "Monthly Sales"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Sales"
)

plt.show()

# ======================================
# 5. HORIZONTAL BAR CHART
# ======================================

print("\n5. HORIZONTAL BAR CHART")

plt.barh(
    students,
    student_marks
)

plt.title(
    "Horizontal Bar Chart"
)

plt.xlabel(
    "Marks"
)

plt.ylabel(
    "Students"
)

plt.show()

# ======================================
# 6. MULTIPLE BAR CHARTS
# ======================================

print("\n6. MULTIPLE BAR CHARTS")

math_marks = [
    92,
    88,
    95,
    81,
    90
]

python_marks = [
    95,
    90,
    89,
    85,
    93
]

x = range(
    len(students)
)

plt.bar(
    x,
    math_marks,
    width=0.4,
    label="Math"
)

plt.bar(
    [i + 0.4 for i in x],
    python_marks,
    width=0.4,
    label="Python"
)

plt.xticks(
    [i + 0.2 for i in x],
    students
)

plt.legend()

plt.title(
    "Subject Comparison"
)

plt.show()

# ======================================
# 7. DISPLAY VALUES
# ======================================

print("\n7. DISPLAY VALUES")

bars = plt.bar(
    students,
    student_marks
)

for bar in bars:

    height = bar.get_height()

    plt.text(
        bar.get_x() +
        bar.get_width()/2,
        height,
        str(height),
        ha="center"
    )

plt.title(
    "Marks with Labels"
)

plt.show()

# ======================================
# 8. GRID
# ======================================

print("\n8. GRID")

plt.bar(
    students,
    student_marks
)

plt.grid(
    axis="y"
)

plt.title(
    "Bar Chart with Grid"
)

plt.show()

# ======================================
# 9. SAVE CHART
# ======================================

print("\n9. SAVE CHART")

plt.bar(
    students,
    student_marks
)

plt.title(
    "Saved Bar Chart"
)

plt.savefig(
    "bar_chart.png"
)

plt.close()

print(
    "Chart Saved Successfully"
)

# ======================================
# 10. DEPARTMENT ANALYSIS
# ======================================

print("\n10. DEPARTMENT ANALYSIS")

departments = [
    "DS",
    "Math",
    "Physics",
    "Chemistry"
]

students_count = [
    120,
    95,
    80,
    70
]

plt.bar(
    departments,
    students_count
)

plt.title(
    "Department Strength"
)

plt.xlabel(
    "Department"
)

plt.ylabel(
    "Students"
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

categories = []
values = []

for i in range(n):

    category = input(
        f"Category {i+1}: "
    )

    value = int(
        input(
            f"Value {i+1}: "
        )
    )

    categories.append(
        category
    )

    values.append(
        value
    )

plt.bar(
    categories,
    values
)

plt.title(
    "User Data Bar Chart"
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
    figsize=(8, 4)
)

bars = plt.bar(
    subjects,
    marks
)

for bar in bars:

    plt.text(
        bar.get_x() +
        bar.get_width()/2,
        bar.get_height(),
        str(
            bar.get_height()
        ),
        ha="center"
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

plt.grid(
    axis="y"
)

plt.show()

print(
    "Average Marks:",
    sum(marks) / len(marks)
)

print(
    "Highest Marks:",
    max(marks)
)

print(
    "Lowest Marks:",
    min(marks)
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Bar Chart
using student marks.

Exercise 2:
Create a Horizontal
Bar Chart.

Exercise 3:
Display values
on bars.

Exercise 4:
Save chart as PNG.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Result Dashboard.

Display:

1. Subject-wise Marks
2. Bar Chart
3. Average Marks
4. Highest Marks
5. Lowest Marks

Generate complete analysis.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 063 Completed Successfully!")