# ======================================
# Day 092: Descriptive Statistics
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Descriptive Statistics
# in Data Science
# ======================================

print("=" * 60)
print("DAY 092 - DESCRIPTIVE STATISTICS")
print("=" * 60)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Descriptive Statistics?

Descriptive Statistics is used
to summarize, organize, and
describe a dataset.

Goals:

1. Understand Data
2. Summarize Data
3. Find Patterns
4. Present Information

Common Measures:

1. Mean
2. Median
3. Mode
4. Range
5. Variance
6. Standard Deviation
"""

# ======================================
# SAMPLE DATASET
# ======================================

marks = [
    92,
    88,
    95,
    81,
    90
]

print("\nDATASET")
print(marks)

# ======================================
# TOTAL OBSERVATIONS
# ======================================

print("\nTOTAL OBSERVATIONS")

total_students = len(
    marks
)

print(
    "Total Students:",
    total_students
)

# ======================================
# SUM OF VALUES
# ======================================

print("\nSUM OF VALUES")

total_marks = sum(
    marks
)

print(
    "Total Marks:",
    total_marks
)

# ======================================
# MINIMUM VALUE
# ======================================

print("\nMINIMUM VALUE")

minimum_marks = min(
    marks
)

print(
    "Minimum Marks:",
    minimum_marks
)

# ======================================
# MAXIMUM VALUE
# ======================================

print("\nMAXIMUM VALUE")

maximum_marks = max(
    marks
)

print(
    "Maximum Marks:",
    maximum_marks
)

# ======================================
# RANGE
# ======================================

print("\nRANGE")

range_value = (
    maximum_marks -
    minimum_marks
)

print(
    "Range:",
    range_value
)

# ======================================
# AVERAGE (MEAN PREVIEW)
# ======================================

print("\nAVERAGE")

average_marks = (
    total_marks /
    total_students
)

print(
    "Average Marks:",
    round(
        average_marks,
        2
    )
)

# ======================================
# SORTED DATA
# ======================================

print("\nSORTED DATA")

sorted_marks = sorted(
    marks
)

print(
    sorted_marks
)

# ======================================
# DATA CLASSIFICATION
# ======================================

print("\nDATA CLASSIFICATION")

print(
    """
Qualitative Data:
- Gender
- City
- Department

Quantitative Data:
- Marks
- Salary
- Age
"""
)

# ======================================
# REAL WORLD EXAMPLE
# ======================================

print("\nREAL WORLD EXAMPLE")

attendance = [
    95,
    88,
    97,
    82,
    91
]

print(
    "Attendance Data:",
    attendance
)

print(
    "Highest Attendance:",
    max(attendance)
)

print(
    "Lowest Attendance:",
    min(attendance)
)

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

student_name = input(
    "Enter Student Name: "
)

student_marks = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"{student_name} scored "
    f"{student_marks}"
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

scores = [
    75,
    80,
    85,
    90,
    95
]

print(
    "Scores:",
    scores
)

print(
    "Total Scores:",
    sum(scores)
)

print(
    "Highest Score:",
    max(scores)
)

print(
    "Lowest Score:",
    min(scores)
)

print(
    "Range:",
    max(scores) - min(scores)
)

print(
    "Average Score:",
    round(
        sum(scores) /
        len(scores),
        2
    )
)

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Observation

Dataset

Mean

Median

Mode

Range

Variance

Standard Deviation
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Find Maximum Value.

Exercise 2:
Find Minimum Value.

Exercise 3:
Find Range.

Exercise 4:
Find Average.

Exercise 5:
Sort Data.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Descriptive Statistics?

Q2. Why is it important?

Q3. What is Range?

Q4. Difference between
Qualitative and
Quantitative Data?

Q5. What is an Observation?

Q6. What is a Dataset?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Report System.

Input:

1. Student Name
2. Marks

Generate:

1. Total Marks
2. Maximum Marks
3. Minimum Marks
4. Range
5. Average

Display Final Report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 092 Completed Successfully!"
)