# ======================================
# Day 052: Pandas Series
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Pandas Series for
# Data Analysis and Data Science
# ======================================

print("=" * 50)
print("DAY 052 - PANDAS SERIES")
print("=" * 50)

# ======================================
# IMPORT PANDAS
# ======================================

import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Pandas Series?

A Series is a one-dimensional
labeled array capable of holding
different types of data.

Characteristics:

1. One-Dimensional
2. Indexed
3. Mutable
4. Fast Data Access

Syntax:

pd.Series(data)

Applications:

- Data Analysis
- Data Cleaning
- Data Manipulation
"""

# ======================================
# 1. CREATE SERIES
# ======================================

print("\n1. CREATE SERIES")

numbers = pd.Series(
    [10, 20, 30, 40, 50]
)

print(numbers)

# ======================================
# 2. SERIES WITH CUSTOM INDEX
# ======================================

print("\n2. CUSTOM INDEX")

marks = pd.Series(
    [92, 95, 88],
    index=[
        "Math",
        "Python",
        "DBMS"
    ]
)

print(marks)

# ======================================
# 3. ACCESS VALUES
# ======================================

print("\n3. ACCESS VALUES")

print(marks["Math"])
print(marks["Python"])

# ======================================
# 4. ACCESS MULTIPLE VALUES
# ======================================

print("\n4. MULTIPLE VALUES")

print(
    marks[
        ["Math", "DBMS"]
    ]
)

# ======================================
# 5. SERIES ATTRIBUTES
# ======================================

print("\n5. SERIES ATTRIBUTES")

print("Size:")
print(marks.size)

print("\nShape:")
print(marks.shape)

print("\nData Type:")
print(marks.dtype)

# ======================================
# 6. SERIES FROM DICTIONARY
# ======================================

print("\n6. SERIES FROM DICTIONARY")

student = {
    "Math": 92,
    "Python": 95,
    "DBMS": 88
}

student_series = pd.Series(
    student
)

print(student_series)

# ======================================
# 7. SERIES MATHEMATICAL OPERATIONS
# ======================================

print("\n7. MATHEMATICAL OPERATIONS")

numbers = pd.Series(
    [1, 2, 3, 4, 5]
)

print(numbers + 10)
print(numbers * 2)

# ======================================
# 8. STATISTICAL FUNCTIONS
# ======================================

print("\n8. STATISTICAL FUNCTIONS")

marks = pd.Series(
    [92, 95, 88, 90, 85]
)

print("Sum     :", marks.sum())
print("Mean    :", marks.mean())
print("Max     :", marks.max())
print("Min     :", marks.min())

# ======================================
# 9. BOOLEAN FILTERING
# ======================================

print("\n9. BOOLEAN FILTERING")

print(
    marks[
        marks >= 90
    ]
)

# ======================================
# 10. CHECK CONDITIONS
# ======================================

print("\n10. CONDITIONS")

print(marks > 90)

# ======================================
# 11. SORT VALUES
# ======================================

print("\n11. SORT VALUES")

print(
    marks.sort_values()
)

# ======================================
# 12. SORT INDEX
# ======================================

print("\n12. SORT INDEX")

subject_marks = pd.Series(
    [95, 88, 92],
    index=[
        "Python",
        "DBMS",
        "Math"
    ]
)

print(
    subject_marks.sort_index()
)

# ======================================
# 13. SERIES HEAD
# ======================================

print("\n13. HEAD")

print(
    marks.head(3)
)

# ======================================
# 14. SERIES TAIL
# ======================================

print("\n14. TAIL")

print(
    marks.tail(2)
)

# ======================================
# 15. VALUE COUNTS
# ======================================

print("\n15. VALUE COUNTS")

data = pd.Series(
    [
        "Python",
        "DBMS",
        "Python",
        "MLF",
        "Python"
    ]
)

print(
    data.value_counts()
)

# ======================================
# 16. USER INPUT EXAMPLE
# ======================================

print("\n16. USER INPUT EXAMPLE")

value1 = int(
    input("Enter Value 1: ")
)

value2 = int(
    input("Enter Value 2: ")
)

value3 = int(
    input("Enter Value 3: ")
)

user_series = pd.Series(
    [value1, value2, value3]
)

print(user_series)

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT")

student_marks = pd.Series(
    {
        "Mathematics": 92,
        "Python": 95,
        "DBMS": 88,
        "Statistics": 90,
        "English": 85
    }
)

print("\nStudent Marks")
print(student_marks)

print("\nTotal Marks")
print(student_marks.sum())

print("\nAverage Marks")
print(round(
    student_marks.mean(),
    2
))

print("\nHighest Marks")
print(student_marks.max())

print("\nLowest Marks")
print(student_marks.min())

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Series with
5 numbers.

Exercise 2:
Create a Series with
custom indexes.

Exercise 3:
Find:

- Sum
- Mean
- Max
- Min

Exercise 4:
Use Boolean Filtering
to display values
greater than 50.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Subject Performance Analyzer.

Store marks of:

- Mathematics
- Python
- DBMS
- Statistics
- English

Using a Series.

Display:

1. Total Marks
2. Average Marks
3. Highest Marks
4. Lowest Marks
5. Subjects Above 90
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 052 Completed Successfully!")