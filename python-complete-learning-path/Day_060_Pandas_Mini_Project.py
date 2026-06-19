# ======================================
# Day 060: Pandas Mini Project
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Student Performance Analytics System
# using Pandas
# ======================================

print("=" * 60)
print("DAY 060 - PANDAS MINI PROJECT")
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Project Objectives

This project combines:

1. DataFrame Operations
2. Data Cleaning
3. GroupBy & Aggregation
4. Data Analysis
5. Data Visualization
6. Reporting

Scenario:

Analyze student performance
across different departments.
"""

# ======================================
# CREATE DATASET
# ======================================

student_data = {
    "Student_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110
    ],

    "Name": [
        "Saloni",
        "Riya",
        "Ankit",
        "Rahul",
        "Priya",
        "Aman",
        "Neha",
        "Vikas",
        "Pooja",
        "Arjun"
    ],

    "Department": [
        "Data Science",
        "Data Science",
        "Mathematics",
        "Mathematics",
        "Data Science",
        "Mathematics",
        "Data Science",
        "Mathematics",
        "Data Science",
        "Mathematics"
    ],

    "Math": [
        92, 88, 95, 81, 90,
        85, 87, 89, 91, 84
    ],

    "Python": [
        95, 90, 89, 85, 93,
        80, 92, 82, 94, 79
    ]
}

df = pd.DataFrame(student_data)

print("\nORIGINAL DATASET")
print(df)

# ======================================
# DATA CLEANING
# ======================================

print("\nDATA CLEANING")

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

print("\nDuplicates Removed")

# ======================================
# TOTAL & AVERAGE
# ======================================

print("\nTOTAL & AVERAGE")

df["Total"] = (
    df["Math"] +
    df["Python"]
)

df["Average"] = (
    df["Total"] / 2
)

print(df)

# ======================================
# GRADE ASSIGNMENT
# ======================================

print("\nGRADE ASSIGNMENT")

def assign_grade(avg):

    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    else:
        return "F"

df["Grade"] = (
    df["Average"]
    .apply(assign_grade)
)

print(df)

# ======================================
# TOP STUDENT
# ======================================

print("\nTOP STUDENT")

top_student = df.loc[
    df["Total"].idxmax()
]

print(top_student)

# ======================================
# LOWEST STUDENT
# ======================================

print("\nLOWEST STUDENT")

lowest_student = df.loc[
    df["Total"].idxmin()
]

print(lowest_student)

# ======================================
# OVERALL STATISTICS
# ======================================

print("\nOVERALL STATISTICS")

print(
    "Average Marks:",
    round(
        df["Average"].mean(),
        2
    )
)

print(
    "Highest Total:",
    df["Total"].max()
)

print(
    "Lowest Total:",
    df["Total"].min()
)

# ======================================
# GROUPBY ANALYSIS
# ======================================

print("\nDEPARTMENT REPORT")

department_report = (
    df.groupby("Department")
    ["Total"]
    .agg(
        [
            "count",
            "mean",
            "max",
            "min"
        ]
    )
)

print(department_report)

# ======================================
# GRADE DISTRIBUTION
# ======================================

print("\nGRADE DISTRIBUTION")

print(
    df["Grade"]
    .value_counts()
)

# ======================================
# SORT STUDENTS
# ======================================

print("\nRANKING")

ranking = (
    df.sort_values(
        by="Total",
        ascending=False
    )
)

print(
    ranking[
        [
            "Name",
            "Total",
            "Grade"
        ]
    ]
)

# ======================================
# VISUALIZATION 1
# ======================================

print("\nBAR CHART")

ranking.plot(
    x="Name",
    y="Total",
    kind="bar",
    title="Student Total Marks"
)

plt.show()

# ======================================
# VISUALIZATION 2
# ======================================

print("\nPIE CHART")

df["Grade"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Grade Distribution"
)

plt.ylabel("")
plt.show()

# ======================================
# VISUALIZATION 3
# ======================================

print("\nLINE CHART")

df.plot(
    x="Name",
    y="Average",
    kind="line",
    title="Average Marks"
)

plt.show()

# ======================================
# SAVE REPORT
# ======================================

print("\nSAVE REPORT")

df.to_csv(
    "student_report.csv",
    index=False
)

print(
    "student_report.csv saved"
)

# ======================================
# USER INPUT SECTION
# ======================================

print("\nUSER INPUT")

student_name = input(
    "Enter Student Name: "
)

math_marks = int(
    input(
        "Enter Math Marks: "
    )
)

python_marks = int(
    input(
        "Enter Python Marks: "
    )
)

user_total = (
    math_marks +
    python_marks
)

user_average = (
    user_total / 2
)

print("\nSTUDENT REPORT")

print("Name    :", student_name)
print("Total   :", user_total)
print("Average :", user_average)

# ======================================
# FINAL PROJECT SUMMARY
# ======================================

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print(
    "Total Students :",
    len(df)
)

print(
    "Highest Total  :",
    df["Total"].max()
)

print(
    "Lowest Total   :",
    df["Total"].min()
)

print(
    "Average Marks  :",
    round(
        df["Average"].mean(),
        2
    )
)

print("=" * 60)

# ======================================
# CHALLENGE TASK
# ======================================

"""
Enhance this project by adding:

1. DBMS Marks
2. Statistics Marks
3. Attendance Percentage
4. Student Ranking
5. Excel Report Export
6. Dashboard Creation
7. Streamlit Web App

(Project Version 2)
"""

# ======================================
# END OF PROJECT
# ======================================

print("\nDay 060 Completed Successfully!")