# ======================================
# Day 062: Line Plots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Creating Professional Line Plots
# using Matplotlib
# ======================================

print("=" * 50)
print("DAY 062 - LINE PLOTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARY
# ======================================

import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Line Plot?

A Line Plot is used to show
trends and changes over time.

Applications:

1. Sales Analysis
2. Stock Prices
3. Population Growth
4. Temperature Analysis
5. Student Performance

Function:

plt.plot()

Advantages:

1. Easy Trend Analysis
2. Simple Visualization
3. Useful for Time Series Data
"""

# ======================================
# 1. BASIC LINE PLOT
# ======================================

print("\n1. BASIC LINE PLOT")

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.title("Basic Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# ======================================
# 2. LINE PLOT WITH MARKERS
# ======================================

print("\n2. LINE PLOT WITH MARKERS")

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

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# ======================================
# 3. CUSTOM LINE STYLE
# ======================================

print("\n3. CUSTOM LINE STYLE")

plt.plot(
    x,
    y,
    linestyle="--",
    linewidth=3
)

plt.title("Custom Line Style")

plt.show()

# ======================================
# 4. MULTIPLE LINE PLOTS
# ======================================

print("\n4. MULTIPLE LINE PLOTS")

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

students = [
    "Saloni",
    "Riya",
    "Ankit",
    "Rahul",
    "Priya"
]

plt.plot(
    students,
    math_marks,
    marker="o",
    label="Math"
)

plt.plot(
    students,
    python_marks,
    marker="s",
    label="Python"
)

plt.title("Subject Comparison")

plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()

plt.show()

# ======================================
# 5. GRID
# ======================================

print("\n5. GRID")

plt.plot(
    months,
    sales,
    marker="o"
)

plt.grid(True)

plt.title("Sales with Grid")

plt.show()

# ======================================
# 6. FIGURE SIZE
# ======================================

print("\n6. FIGURE SIZE")

plt.figure(
    figsize=(8, 4)
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Custom Figure Size")

plt.show()

# ======================================
# 7. SALES TREND ANALYSIS
# ======================================

print("\n7. SALES TREND")

sales_data = [
    1000,
    1200,
    1500,
    1300,
    1800,
    2000,
    2200
]

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul"
]

plt.plot(
    months,
    sales_data,
    marker="o"
)

plt.title("Sales Trend Analysis")

plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.show()

# ======================================
# 8. STUDENT PERFORMANCE
# ======================================

print("\n8. STUDENT PERFORMANCE")

tests = [
    "Test1",
    "Test2",
    "Test3",
    "Test4",
    "Test5"
]

marks = [
    75,
    80,
    85,
    90,
    95
]

plt.plot(
    tests,
    marks,
    marker="o"
)

plt.title("Student Performance")

plt.xlabel("Tests")
plt.ylabel("Marks")

plt.show()

# ======================================
# 9. SAVE LINE PLOT
# ======================================

print("\n9. SAVE LINE PLOT")

plt.plot(
    tests,
    marks,
    marker="o"
)

plt.title("Saved Plot")

plt.savefig(
    "line_plot.png"
)

plt.close()

print("Plot Saved Successfully")

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

n = int(
    input(
        "Enter Number of Values: "
    )
)

values = []

for i in range(n):

    value = int(
        input(
            f"Enter Value {i+1}: "
        )
    )

    values.append(value)

x_values = list(
    range(
        1,
        n + 1
    )
)

plt.plot(
    x_values,
    values,
    marker="o"
)

plt.title("User Data")

plt.show()

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT")

student_names = [
    "A",
    "B",
    "C",
    "D",
    "E"
]

student_marks = [
    85,
    92,
    78,
    95,
    88
]

plt.figure(
    figsize=(8, 4)
)

plt.plot(
    student_names,
    student_marks,
    marker="o"
)

plt.title(
    "Student Performance Dashboard"
)

plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid(True)

plt.show()

average_marks = (
    sum(student_marks)
    /
    len(student_marks)
)

print(
    "Average Marks:",
    average_marks
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a line plot
using monthly sales.

Exercise 2:
Add:

- Markers
- Grid
- Labels

Exercise 3:
Plot two subjects
on the same graph.

Exercise 4:
Save the graph as PNG.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Progress Tracker.

Store marks of 5 tests.

Display:

1. Line Plot
2. Average Marks
3. Highest Marks
4. Lowest Marks

Generate complete analysis.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 062 Completed Successfully!")