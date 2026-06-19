# ======================================
# Day 061: Matplotlib Introduction
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Matplotlib for
# Data Visualization
# ======================================

print("=" * 50)
print("DAY 061 - MATPLOTLIB INTRODUCTION")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Matplotlib?

Matplotlib is the most popular
Python library used for creating
graphs, charts, and visualizations.

Developed By:
John D. Hunter

Applications:

1. Data Analysis
2. Data Science
3. Machine Learning
4. Business Analytics
5. Research

Advantages:

1. Easy to Use
2. Highly Customizable
3. Industry Standard
4. Works with NumPy & Pandas

Common Chart Types:

1. Line Plot
2. Bar Chart
3. Histogram
4. Pie Chart
5. Scatter Plot
"""

# ======================================
# 1. SIMPLE LINE PLOT
# ======================================

print("\n1. SIMPLE LINE PLOT")

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# ======================================
# 2. STUDENT MARKS GRAPH
# ======================================

print("\n2. STUDENT MARKS GRAPH")

students = [
    "Saloni",
    "Riya",
    "Ankit",
    "Rahul",
    "Priya"
]

marks = [
    92,
    88,
    95,
    81,
    90
]

plt.plot(
    students,
    marks
)

plt.title(
    "Student Marks"
)

plt.xlabel(
    "Students"
)

plt.ylabel(
    "Marks"
)

plt.show()

# ======================================
# 3. CUSTOM LINE WIDTH
# ======================================

print("\n3. CUSTOM LINE WIDTH")

plt.plot(
    x,
    y,
    linewidth=3
)

plt.title(
    "Custom Line Width"
)

plt.show()

# ======================================
# 4. MULTIPLE LINES
# ======================================

print("\n4. MULTIPLE LINES")

python_marks = [
    95,
    90,
    89,
    85,
    93
]

plt.plot(
    students,
    marks,
    label="Math"
)

plt.plot(
    students,
    python_marks,
    label="Python"
)

plt.legend()

plt.title(
    "Subject Comparison"
)

plt.show()

# ======================================
# 5. GRID
# ======================================

print("\n5. GRID")

plt.plot(
    x,
    y
)

plt.grid(True)

plt.title(
    "Grid Example"
)

plt.show()

# ======================================
# 6. MARKERS
# ======================================

print("\n6. MARKERS")

plt.plot(
    x,
    y,
    marker="o"
)

plt.title(
    "Markers Example"
)

plt.show()

# ======================================
# 7. FIGURE SIZE
# ======================================

print("\n7. FIGURE SIZE")

plt.figure(
    figsize=(8, 4)
)

plt.plot(
    x,
    y
)

plt.title(
    "Custom Figure Size"
)

plt.show()

# ======================================
# 8. SAVE FIGURE
# ======================================

print("\n8. SAVE FIGURE")

plt.plot(
    x,
    y
)

plt.title(
    "Saved Figure"
)

plt.savefig(
    "sample_plot.png"
)

plt.close()

print(
    "Figure Saved Successfully"
)

# ======================================
# 9. SALES ANALYSIS
# ======================================

print("\n9. SALES ANALYSIS")

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

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title(
    "Monthly Sales"
)

plt.xlabel(
    "Months"
)

plt.ylabel(
    "Sales"
)

plt.grid(True)

plt.show()

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

number = int(
    input(
        "How many values? "
    )
)

x_values = list(
    range(
        1,
        number + 1
    )
)

y_values = []

for i in range(number):

    value = int(
        input(
            f"Enter Value {i+1}: "
        )
    )

    y_values.append(
        value
    )

plt.plot(
    x_values,
    y_values,
    marker="o"
)

plt.title(
    "User Data Plot"
)

plt.show()

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT")

student_data = {
    "Students": [
        "A",
        "B",
        "C",
        "D",
        "E"
    ],
    "Marks": [
        85,
        90,
        78,
        95,
        88
    ]
}

plt.figure(
    figsize=(8, 4)
)

plt.plot(
    student_data["Students"],
    student_data["Marks"],
    marker="o"
)

plt.title(
    "Student Performance Analysis"
)

plt.xlabel(
    "Students"
)

plt.ylabel(
    "Marks"
)

plt.grid(True)

plt.show()

print(
    "Average Marks:",
    sum(
        student_data["Marks"]
    ) / len(
        student_data["Marks"]
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a line plot using:

x = [1,2,3,4,5]
y = [5,10,15,20,25]

Exercise 2:
Add:

- Title
- X Label
- Y Label

Exercise 3:
Use markers and grid.

Exercise 4:
Save the chart as PNG.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Result Dashboard.

Display:

1. Student Names
2. Marks
3. Line Plot
4. Average Marks

Generate a complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 061 Completed Successfully!")