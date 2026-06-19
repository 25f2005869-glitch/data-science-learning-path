# ======================================
# Day 070: Matplotlib Revision
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Complete Revision of Matplotlib
# for Data Visualization
# ======================================

print("=" * 60)
print("DAY 070 - MATPLOTLIB REVISION")
print("=" * 60)

# ======================================
# IMPORT LIBRARY
# ======================================

import matplotlib.pyplot as plt

# ======================================
# REVISION NOTES
# ======================================

"""
MATPLOTLIB REVISION CHEAT SHEET

Matplotlib is the most popular
Python library for creating
data visualizations.

Topics Covered:

Day 061 : Introduction
Day 062 : Line Plots
Day 063 : Bar Charts
Day 064 : Histograms
Day 065 : Pie Charts
Day 066 : Scatter Plots
Day 067 : Subplots
Day 068 : Styling
Day 069 : Dashboard Project

Main Library:

import matplotlib.pyplot as plt
"""

# ======================================
# SAMPLE DATA
# ======================================

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

# ======================================
# 1. LINE PLOT REVISION
# ======================================

print("\n1. LINE PLOT")

plt.plot(
    students,
    marks,
    marker="o"
)

plt.title(
    "Line Plot"
)

plt.show()

# ======================================
# 2. BAR CHART REVISION
# ======================================

print("\n2. BAR CHART")

plt.bar(
    students,
    marks
)

plt.title(
    "Bar Chart"
)

plt.show()

# ======================================
# 3. HISTOGRAM REVISION
# ======================================

print("\n3. HISTOGRAM")

plt.hist(
    marks,
    bins=5
)

plt.title(
    "Histogram"
)

plt.show()

# ======================================
# 4. PIE CHART REVISION
# ======================================

print("\n4. PIE CHART")

plt.pie(
    marks,
    labels=students,
    autopct="%1.1f%%"
)

plt.title(
    "Pie Chart"
)

plt.show()

# ======================================
# 5. SCATTER PLOT REVISION
# ======================================

print("\n5. SCATTER PLOT")

study_hours = [
    8,
    6,
    9,
    5,
    7
]

plt.scatter(
    study_hours,
    marks
)

plt.title(
    "Scatter Plot"
)

plt.xlabel(
    "Study Hours"
)

plt.ylabel(
    "Marks"
)

plt.show()

# ======================================
# 6. SUBPLOTS REVISION
# ======================================

print("\n6. SUBPLOTS")

plt.figure(
    figsize=(8, 4)
)

plt.subplot(1, 2, 1)

plt.bar(
    students,
    marks
)

plt.title(
    "Bar Chart"
)

plt.subplot(1, 2, 2)

plt.plot(
    students,
    marks,
    marker="o"
)

plt.title(
    "Line Plot"
)

plt.tight_layout()

plt.show()

# ======================================
# 7. STYLING REVISION
# ======================================

print("\n7. STYLING")

plt.plot(
    students,
    marks,
    marker="o",
    linestyle="--",
    linewidth=2
)

plt.title(
    "Styled Plot"
)

plt.xlabel(
    "Students"
)

plt.ylabel(
    "Marks"
)

plt.grid(True)

plt.show()

# ======================================
# 8. SAVE CHART
# ======================================

print("\n8. SAVE CHART")

plt.plot(
    students,
    marks
)

plt.savefig(
    "revision_chart.png"
)

plt.close()

print(
    "Chart Saved Successfully"
)

# ======================================
# 9. STUDENT ANALYSIS
# ======================================

print("\n9. STUDENT ANALYSIS")

print(
    "Highest Marks:",
    max(marks)
)

print(
    "Lowest Marks:",
    min(marks)
)

print(
    "Average Marks:",
    round(
        sum(marks) /
        len(marks),
        2
    )
)

# ======================================
# 10. MINI PROJECT
# ======================================

print("\n10. MINI PROJECT")

plt.figure(
    figsize=(10, 6)
)

plt.subplot(2, 2, 1)

plt.bar(
    students,
    marks
)

plt.title(
    "Bar Chart"
)

plt.subplot(2, 2, 2)

plt.plot(
    students,
    marks,
    marker="o"
)

plt.title(
    "Line Plot"
)

plt.subplot(2, 2, 3)

plt.hist(
    marks,
    bins=5
)

plt.title(
    "Histogram"
)

plt.subplot(2, 2, 4)

plt.pie(
    marks,
    labels=students,
    autopct="%1.1f%%"
)

plt.title(
    "Pie Chart"
)

plt.tight_layout()

plt.show()

# ======================================
# IMPORTANT FUNCTIONS
# ======================================

"""
plt.plot()       -> Line Plot
plt.bar()        -> Bar Chart
plt.barh()       -> Horizontal Bar
plt.hist()       -> Histogram
plt.pie()        -> Pie Chart
plt.scatter()    -> Scatter Plot

plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.grid()

plt.subplot()
plt.figure()

plt.savefig()
plt.show()
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Matplotlib?

Q2. Difference between
Bar Chart and Histogram?

Q3. What is a Scatter Plot?

Q4. Why use Subplots?

Q5. What is the purpose
of plt.savefig()?

Q6. Difference between
plt.bar() and plt.barh()?

Q7. What is a Pie Chart?

Q8. Why use Grid Lines?
"""

# ======================================
# PRACTICE QUESTIONS
# ======================================

"""
Practice 1:
Create a Line Plot.

Practice 2:
Create a Bar Chart.

Practice 3:
Create a Histogram.

Practice 4:
Create a Pie Chart.

Practice 5:
Create a Scatter Plot.

Practice 6:
Create a Dashboard using
Subplots.
"""

# ======================================
# FINAL CHEAT SHEET
# ======================================

"""
Line Plot      -> Trends
Bar Chart      -> Comparisons
Histogram      -> Distribution
Pie Chart      -> Percentage Share
Scatter Plot   -> Relationships
Subplots       -> Dashboards
Styling        -> Professional Charts
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a College Analytics Dashboard.

Include:

1. Student Marks
2. Attendance
3. Study Hours

Generate:

- Bar Chart
- Line Plot
- Histogram
- Pie Chart
- Scatter Plot

Display all charts in
a professional dashboard.
"""

# ======================================
# END OF FILE
# ======================================

print("\nDay 070 Completed Successfully!")