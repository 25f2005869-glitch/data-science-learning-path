# ======================================
# Day 069: Data Visualization Project
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Professional Student Analytics
# Dashboard using Matplotlib
# ======================================

print("=" * 60)
print("DAY 069 - DATA VISUALIZATION PROJECT")
print("STUDENT ANALYTICS DASHBOARD")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Project Objective

Build a complete Student Analytics
Dashboard using all major Matplotlib
visualization techniques learned
from Day 061 to Day 068.

Concepts Used:

1. Line Plot
2. Bar Chart
3. Histogram
4. Pie Chart
5. Scatter Plot
6. Subplots
7. Customization
8. Dashboard Design

Applications:

- Educational Analytics
- Business Dashboards
- Research Reporting
- Data Science Projects
"""

# ======================================
# STUDENT DATASET
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

study_hours = [
    8,
    6,
    9,
    5,
    7
]

attendance = [
    95,
    88,
    97,
    82,
    91
]

# ======================================
# BASIC ANALYSIS
# ======================================

print("\nSTUDENT DATA")

for student, mark in zip(
    students,
    marks
):
    print(
        f"{student}: {mark}"
    )

print("\nSUMMARY")

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
# DASHBOARD
# ======================================

plt.figure(
    figsize=(14, 10)
)

# ======================================
# 1. BAR CHART
# ======================================

plt.subplot(2, 3, 1)

plt.bar(
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

plt.grid(
    axis="y"
)

# ======================================
# 2. LINE PLOT
# ======================================

plt.subplot(2, 3, 2)

plt.plot(
    students,
    marks,
    marker="o",
    linewidth=2
)

plt.title(
    "Marks Trend"
)

plt.xlabel(
    "Students"
)

plt.ylabel(
    "Marks"
)

plt.grid(True)

# ======================================
# 3. HISTOGRAM
# ======================================

plt.subplot(2, 3, 3)

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

# ======================================
# 4. PIE CHART
# ======================================

plt.subplot(2, 3, 4)

plt.pie(
    marks,
    labels=students,
    autopct="%1.1f%%"
)

plt.title(
    "Marks Percentage"
)

# ======================================
# 5. SCATTER PLOT
# ======================================

plt.subplot(2, 3, 5)

plt.scatter(
    study_hours,
    marks
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

# ======================================
# 6. ATTENDANCE ANALYSIS
# ======================================

plt.subplot(2, 3, 6)

plt.scatter(
    attendance,
    marks
)

plt.title(
    "Attendance vs Marks"
)

plt.xlabel(
    "Attendance (%)"
)

plt.ylabel(
    "Marks"
)

plt.grid(True)

# ======================================
# FINAL DASHBOARD
# ======================================

plt.suptitle(
    "Student Analytics Dashboard",
    fontsize=16
)

plt.tight_layout()

plt.show()

# ======================================
# TOP STUDENT
# ======================================

print("\nTOP PERFORMER")

top_index = marks.index(
    max(marks)
)

print(
    "Student:",
    students[top_index]
)

print(
    "Marks:",
    marks[top_index]
)

# ======================================
# LOWEST STUDENT
# ======================================

print("\nLOWEST PERFORMER")

low_index = marks.index(
    min(marks)
)

print(
    "Student:",
    students[low_index]
)

print(
    "Marks:",
    marks[low_index]
)

# ======================================
# SAVE DASHBOARD
# ======================================

plt.figure(
    figsize=(8, 4)
)

plt.bar(
    students,
    marks
)

plt.title(
    "Student Performance Report"
)

plt.savefig(
    "student_dashboard.png"
)

plt.close()

print(
    "\nDashboard Saved Successfully"
)

# ======================================
# USER INPUT SECTION
# ======================================

print("\nUSER INPUT ANALYSIS")

name = input(
    "Enter Student Name: "
)

student_mark = int(
    input(
        "Enter Marks: "
    )
)

print("\nREPORT")

print(
    "Student:",
    name
)

print(
    "Marks:",
    student_mark
)

if student_mark >= 90:
    print("Grade: A+")

elif student_mark >= 80:
    print("Grade: A")

elif student_mark >= 70:
    print("Grade: B")

else:
    print("Grade: C")

# ======================================
# PROJECT SUMMARY
# ======================================

print("\n" + "=" * 60)

print(
    "PROJECT SUMMARY"
)

print("=" * 60)

print(
    "Total Students:",
    len(students)
)

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

print("=" * 60)

# ======================================
# CHALLENGE TASK
# ======================================

"""
Project Version 2

Add:

1. Pandas Integration
2. CSV Dataset
3. Multiple Subjects
4. Department Analysis
5. Group-wise Dashboard
6. NumPy Statistics
7. Streamlit Dashboard
8. PDF Report Generation
"""

# ======================================
# END OF PROJECT
# ======================================

print(
    "\nDay 069 Completed Successfully!"
)