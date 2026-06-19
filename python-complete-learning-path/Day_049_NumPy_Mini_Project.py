# ======================================
# Day 049: NumPy Mini Project
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Student Performance Analysis System
# using NumPy
# ======================================

print("=" * 60)
print("DAY 049 - NUMPY MINI PROJECT")
print("STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 60)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Project Objectives

This project combines:

1. NumPy Arrays
2. Indexing & Slicing
3. Array Operations
4. Statistical Functions
5. Random Module
6. Broadcasting
7. Data Analysis

Scenario:

Analyze marks of students
across multiple subjects.
"""

# ======================================
# SUBJECTS
# ======================================

subjects = np.array(
    [
        "Mathematics",
        "Python",
        "DBMS",
        "Statistics",
        "English"
    ]
)

# ======================================
# GENERATE STUDENT DATA
# ======================================

np.random.seed(42)

marks = np.random.randint(
    40,
    101,
    size=(10, 5)
)

# ======================================
# DISPLAY DATA
# ======================================

print("\nSUBJECTS")
print("-" * 40)
print(subjects)

print("\nMARKS MATRIX")
print("-" * 40)
print(marks)

# ======================================
# STUDENT TOTAL MARKS
# ======================================

print("\nSTUDENT TOTAL MARKS")
print("-" * 40)

student_totals = np.sum(
    marks,
    axis=1
)

print(student_totals)

# ======================================
# STUDENT AVERAGE MARKS
# ======================================

print("\nSTUDENT AVERAGE MARKS")
print("-" * 40)

student_average = np.mean(
    marks,
    axis=1
)

print(
    np.round(
        student_average,
        2
    )
)

# ======================================
# SUBJECT-WISE AVERAGE
# ======================================

print("\nSUBJECT-WISE AVERAGE")
print("-" * 40)

subject_average = np.mean(
    marks,
    axis=0
)

for subject, average in zip(
    subjects,
    subject_average
):

    print(
        f"{subject:<12} : "
        f"{average:.2f}"
    )

# ======================================
# HIGHEST MARKS
# ======================================

print("\nHIGHEST MARKS")
print("-" * 40)

print(np.max(marks))

# ======================================
# LOWEST MARKS
# ======================================

print("\nLOWEST MARKS")
print("-" * 40)

print(np.min(marks))

# ======================================
# TOP PERFORMER
# ======================================

print("\nTOP PERFORMER")
print("-" * 40)

top_student_index = np.argmax(
    student_totals
)

print(
    "Student Number:",
    top_student_index + 1
)

print(
    "Total Marks:",
    student_totals[top_student_index]
)

# ======================================
# BONUS MARKS USING BROADCASTING
# ======================================

print("\nBONUS MARKS (+5)")
print("-" * 40)

bonus_marks = marks + 5

print(bonus_marks)

# ======================================
# PASS / FAIL ANALYSIS
# ======================================

print("\nPASS / FAIL ANALYSIS")
print("-" * 40)

pass_status = marks >= 40

print(pass_status)

# ======================================
# SUBJECT HIGHEST MARKS
# ======================================

print("\nSUBJECT HIGHEST MARKS")
print("-" * 40)

highest_subject_marks = np.max(
    marks,
    axis=0
)

for subject, highest in zip(
    subjects,
    highest_subject_marks
):

    print(
        f"{subject:<12} : {highest}"
    )

# ======================================
# SUBJECT LOWEST MARKS
# ======================================

print("\nSUBJECT LOWEST MARKS")
print("-" * 40)

lowest_subject_marks = np.min(
    marks,
    axis=0
)

for subject, lowest in zip(
    subjects,
    lowest_subject_marks
):

    print(
        f"{subject:<12} : {lowest}"
    )

# ======================================
# STANDARD DEVIATION
# ======================================

print("\nSTANDARD DEVIATION")
print("-" * 40)

print(
    np.round(
        np.std(marks),
        2
    )
)

# ======================================
# VARIANCE
# ======================================

print("\nVARIANCE")
print("-" * 40)

print(
    np.round(
        np.var(marks),
        2
    )
)

# ======================================
# OVERALL STATISTICS
# ======================================

print("\nOVERALL STATISTICS")
print("-" * 40)

print(
    "Total Students :",
    marks.shape[0]
)

print(
    "Total Subjects :",
    marks.shape[1]
)

print(
    "Overall Average:",
    round(
        np.mean(marks),
        2
    )
)

# ======================================
# GRADE ASSIGNMENT
# ======================================

print("\nGRADE ASSIGNMENT")
print("-" * 40)

for index, average in enumerate(
    student_average
):

    if average >= 90:
        grade = "A+"

    elif average >= 80:
        grade = "A"

    elif average >= 70:
        grade = "B"

    elif average >= 60:
        grade = "C"

    elif average >= 40:
        grade = "D"

    else:
        grade = "F"

    print(
        f"Student {index + 1}"
        f" -> {grade}"
    )

# ======================================
# FINAL REPORT
# ======================================

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print(
    "Highest Marks :",
    np.max(marks)
)

print(
    "Lowest Marks  :",
    np.min(marks)
)

print(
    "Average Marks :",
    round(
        np.mean(marks),
        2
    )
)

print(
    "Top Student   :",
    top_student_index + 1
)

print("=" * 60)

# ======================================
# END OF PROJECT
# ======================================

print("\nDay 049 Completed Successfully!")