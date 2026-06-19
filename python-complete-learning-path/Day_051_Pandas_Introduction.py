# ======================================
# Day 051: Pandas Introduction
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Pandas for Data
# Analysis and Data Science
# ======================================

print("=" * 50)
print("DAY 051 - PANDAS INTRODUCTION")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Pandas?

Pandas is the most popular Python
library for Data Analysis and
Data Manipulation.

Developed By:

Wes McKinney (2008)

Applications:

1. Data Analysis
2. Data Cleaning
3. Data Visualization
4. Machine Learning
5. Business Analytics

Main Data Structures:

1. Series
   (1-Dimensional)

2. DataFrame
   (2-Dimensional)

Installation:

pip install pandas

Import:

import pandas as pd
"""

# ======================================
# IMPORT PANDAS
# ======================================

import pandas as pd

# ======================================
# 1. CHECK PANDAS VERSION
# ======================================

print("\n1. PANDAS VERSION")

print(pd.__version__)

# ======================================
# 2. SIMPLE LIST
# ======================================

print("\n2. PYTHON LIST")

students = [
    "Saloni",
    "Riya",
    "Ankit"
]

print(students)

# ======================================
# 3. CREATE SERIES
# ======================================

print("\n3. PANDAS SERIES")

student_series = pd.Series(
    students
)

print(student_series)

# ======================================
# 4. SERIES WITH NUMBERS
# ======================================

print("\n4. NUMERIC SERIES")

marks = pd.Series(
    [92, 95, 88, 90]
)

print(marks)

# ======================================
# 5. CREATE DATAFRAME
# ======================================

print("\n5. DATAFRAME")

data = {
    "Name": [
        "Saloni",
        "Riya",
        "Ankit"
    ],
    "Marks": [
        92,
        88,
        95
    ]
}

df = pd.DataFrame(data)

print(df)

# ======================================
# 6. DATAFRAME SHAPE
# ======================================

print("\n6. DATAFRAME SHAPE")

print(df.shape)

# ======================================
# 7. DATAFRAME COLUMNS
# ======================================

print("\n7. DATAFRAME COLUMNS")

print(df.columns)

# ======================================
# 8. DATAFRAME INDEX
# ======================================

print("\n8. DATAFRAME INDEX")

print(df.index)

# ======================================
# 9. DATA TYPES
# ======================================

print("\n9. DATA TYPES")

print(df.dtypes)

# ======================================
# 10. BASIC INFORMATION
# ======================================

print("\n10. DATAFRAME INFO")

print(df.info())

# ======================================
# 11. DESCRIPTIVE STATISTICS
# ======================================

print("\n11. DESCRIPTIVE STATISTICS")

print(df.describe())

# ======================================
# 12. HEAD METHOD
# ======================================

print("\n12. HEAD METHOD")

print(df.head())

# ======================================
# 13. TAIL METHOD
# ======================================

print("\n13. TAIL METHOD")

print(df.tail())

# ======================================
# 14. CREATE DATAFRAME
# ======================================

print("\n14. STUDENT DATAFRAME")

student_data = {
    "Name": [
        "Saloni",
        "Riya",
        "Ankit",
        "Rahul"
    ],
    "Math": [
        92,
        88,
        95,
        81
    ],
    "Python": [
        95,
        90,
        89,
        85
    ]
}

students_df = pd.DataFrame(
    student_data
)

print(students_df)

# ======================================
# 15. ACCESS COLUMN
# ======================================

print("\n15. ACCESS COLUMN")

print(
    students_df["Name"]
)

# ======================================
# 16. USER INPUT EXAMPLE
# ======================================

print("\n16. USER INPUT EXAMPLE")

name = input(
    "Enter Student Name: "
)

marks = int(
    input(
        "Enter Marks: "
    )
)

user_df = pd.DataFrame(
    {
        "Name": [name],
        "Marks": [marks]
    }
)

print(user_df)

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT")

student_data = {
    "Name": [
        "Saloni",
        "Riya",
        "Ankit",
        "Rahul",
        "Priya"
    ],
    "Marks": [
        92,
        88,
        95,
        81,
        90
    ]
}

students_df = pd.DataFrame(
    student_data
)

print("\nStudent Data")

print(students_df)

print("\nAverage Marks")

print(
    students_df["Marks"].mean()
)

print("\nHighest Marks")

print(
    students_df["Marks"].max()
)

print("\nLowest Marks")

print(
    students_df["Marks"].min()
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Pandas Series
containing 5 numbers.

Exercise 2:
Create a DataFrame
containing:

- Name
- Age
- City

Exercise 3:
Display:

- Shape
- Columns
- Data Types

Exercise 4:
Calculate:

- Mean
- Maximum
- Minimum
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Management System.

Store:

- Name
- Mathematics Marks
- Python Marks
- DBMS Marks

Using a DataFrame.

Display:

1. Student Records
2. Average Marks
3. Highest Marks
4. Lowest Marks
5. DataFrame Information
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 051 Completed Successfully!")