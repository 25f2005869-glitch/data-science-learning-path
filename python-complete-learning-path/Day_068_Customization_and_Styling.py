# ======================================
# Day 068: Customization and Styling
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Customizing and Styling Charts
# using Matplotlib
# ======================================

print("=" * 50)
print("DAY 068 - CUSTOMIZATION AND STYLING")
print("=" * 50)

# ======================================
# IMPORT LIBRARY
# ======================================

import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Customization?

Customization means modifying
the appearance of charts to
make them more readable and
professional.

Benefits:

1. Better Presentation
2. Improved Readability
3. Professional Dashboards
4. Better Data Interpretation

Common Customizations:

1. Titles
2. Axis Labels
3. Legends
4. Grid
5. Figure Size
6. Markers
7. Line Styles
8. Axis Limits
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

# ======================================
# 1. CHART TITLE
# ======================================

print("\n1. CHART TITLE")

plt.plot(months, sales)

plt.title(
    "Monthly Sales Report"
)

plt.show()

# ======================================
# 2. AXIS LABELS
# ======================================

print("\n2. AXIS LABELS")

plt.plot(months, sales)

plt.title(
    "Monthly Sales"
)

plt.xlabel(
    "Months"
)

plt.ylabel(
    "Sales Amount"
)

plt.show()

# ======================================
# 3. LINE STYLE
# ======================================

print("\n3. LINE STYLE")

plt.plot(
    months,
    sales,
    linestyle="--"
)

plt.title(
    "Dashed Line"
)

plt.show()

# ======================================
# 4. LINE WIDTH
# ======================================

print("\n4. LINE WIDTH")

plt.plot(
    months,
    sales,
    linewidth=3
)

plt.title(
    "Custom Line Width"
)

plt.show()

# ======================================
# 5. MARKERS
# ======================================

print("\n5. MARKERS")

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title(
    "Markers Example"
)

plt.show()

# ======================================
# 6. GRID
# ======================================

print("\n6. GRID")

plt.plot(
    months,
    sales,
    marker="o"
)

plt.grid(True)

plt.title(
    "Chart with Grid"
)

plt.show()

# ======================================
# 7. LEGEND
# ======================================

print("\n7. LEGEND")

profits = [
    200,
    250,
    350,
    300,
    450
]

plt.plot(
    months,
    sales,
    label="Sales"
)

plt.plot(
    months,
    profits,
    label="Profit"
)

plt.legend()

plt.title(
    "Sales vs Profit"
)

plt.show()

# ======================================
# 8. FIGURE SIZE
# ======================================

print("\n8. FIGURE SIZE")

plt.figure(
    figsize=(8, 4)
)

plt.plot(
    months,
    sales
)

plt.title(
    "Custom Figure Size"
)

plt.show()

# ======================================
# 9. AXIS LIMITS
# ======================================

print("\n9. AXIS LIMITS")

plt.plot(
    months,
    sales
)

plt.ylim(
    500,
    2000
)

plt.title(
    "Axis Limits"
)

plt.show()

# ======================================
# 10. ROTATE LABELS
# ======================================

print("\n10. ROTATE LABELS")

long_months = [
    "January",
    "February",
    "March",
    "April",
    "May"
]

plt.plot(
    long_months,
    sales,
    marker="o"
)

plt.xticks(
    rotation=45
)

plt.title(
    "Rotated Labels"
)

plt.show()

# ======================================
# 11. BAR CHART STYLING
# ======================================

print("\n11. BAR CHART STYLING")

plt.bar(
    months,
    sales
)

plt.title(
    "Styled Bar Chart"
)

plt.xlabel(
    "Months"
)

plt.ylabel(
    "Sales"
)

plt.grid(
    axis="y"
)

plt.show()

# ======================================
# 12. HISTOGRAM STYLING
# ======================================

print("\n12. HISTOGRAM STYLING")

marks = [
    92, 88, 95, 81, 90,
    78, 84, 89, 91, 87
]

plt.hist(
    marks,
    bins=5
)

plt.title(
    "Marks Distribution"
)

plt.xlabel(
    "Marks"
)

plt.ylabel(
    "Frequency"
)

plt.show()

# ======================================
# 13. SCATTER PLOT STYLING
# ======================================

print("\n13. SCATTER PLOT STYLING")

study_hours = [
    1, 2, 3, 4, 5,
    6, 7, 8
]

student_marks = [
    45, 52, 60, 68,
    75, 82, 88, 95
]

plt.scatter(
    study_hours,
    student_marks
)

plt.title(
    "Study Hours vs Marks"
)

plt.xlabel(
    "Study Hours"
)

plt.ylabel(
    "Marks"
)

plt.grid(True)

plt.show()

# ======================================
# 14. SAVE STYLED CHART
# ======================================

print("\n14. SAVE STYLED CHART")

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title(
    "Saved Styled Chart"
)

plt.grid(True)

plt.savefig(
    "styled_chart.png"
)

plt.close()

print(
    "Chart Saved Successfully"
)

# ======================================
# 15. USER INPUT EXAMPLE
# ======================================

print("\n15. USER INPUT EXAMPLE")

value1 = int(
    input(
        "Enter Value 1: "
    )
)

value2 = int(
    input(
        "Enter Value 2: "
    )
)

plt.bar(
    ["A", "B"],
    [value1, value2]
)

plt.title(
    "User Data"
)

plt.show()

# ======================================
# 16. MINI PROJECT
# ======================================

print("\n16. MINI PROJECT")

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

plt.plot(
    subjects,
    marks,
    marker="o",
    linewidth=2
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

plt.grid(True)

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
Create a chart with:

- Title
- Labels
- Grid

Exercise 2:
Use:

- Markers
- Line Width
- Line Style

Exercise 3:
Rotate X-axis labels.

Exercise 4:
Save chart as PNG.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Professional
Student Dashboard.

Include:

1. Line Plot
2. Bar Chart
3. Histogram

Apply:

- Titles
- Labels
- Grid
- Figure Size
- Axis Limits

Generate a professional report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 068 Completed Successfully!")