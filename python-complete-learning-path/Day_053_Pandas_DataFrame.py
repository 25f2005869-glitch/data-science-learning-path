# ======================================
# Day 053: Pandas DataFrame
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Pandas DataFrame for
# Data Analysis and Data Science
# ======================================

print("=" * 50)
print("DAY 053 - PANDAS DATAFRAME")
print("=" * 50)

# ======================================
# IMPORT PANDAS
# ======================================

import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a DataFrame?

A DataFrame is a two-dimensional
tabular data structure consisting
of rows and columns.

It is the most important data
structure in Pandas.

Examples:

| Name   | Marks |
|---------|--------|
| Saloni | 92     |
| Riya   | 88     |

Features:

1. Rows and Columns
2. Labeled Axes
3. Different Data Types
4. Easy Data Analysis

Applications:

- Data Cleaning
- Data Analysis
- Machine Learning
- Business Analytics
"""

# ======================================
# 1. CREATE DATAFRAME
# ======================================

print("\n1. CREATE DATAFRAME")

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
# 2. DATAFRAME SHAPE
# ======================================

print("\n2. DATAFRAME SHAPE")

print(df.shape)

# ======================================
# 3. DATAFRAME COLUMNS
# ======================================

print("\n3. DATAFRAME COLUMNS")

print(df.columns)

# ======================================
# 4. DATAFRAME INDEX
# ======================================

print("\n4. DATAFRAME INDEX")

print(df.index)

# ======================================
# 5. DATA TYPES
# ======================================

print("\n5. DATA TYPES")

print(df.dtypes)

# ======================================
# 6. DATAFRAME INFO
# ======================================

print("\n6. DATAFRAME INFO")

df.info()

# ======================================
# 7. DESCRIBE METHOD
# ======================================

print("\n7. DESCRIBE METHOD")

print(df.describe())

# ======================================
# 8. HEAD METHOD
# ======================================

print("\n8. HEAD METHOD")

print(df.head())

# ======================================
# 9. TAIL METHOD
# ======================================

print("\n9. TAIL METHOD")

print(df.tail())

# ======================================
# 10. ACCESS SINGLE COLUMN
# ======================================

print("\n10. SINGLE COLUMN")

print(df["Name"])

# ======================================
# 11. ACCESS MULTIPLE COLUMNS
# ======================================

print("\n11. MULTIPLE COLUMNS")

print(
    df[
        ["Name", "Marks"]
    ]
)

# ======================================
# 12. ADD NEW COLUMN
# ======================================

print("\n12. ADD NEW COLUMN")

df["Grade"] = [
    "A",
    "B",
    "A+"
]

print(df)

# ======================================
# 13. ROW ACCESS USING loc
# ======================================

print("\n13. ROW ACCESS")

print(df.loc[0])

# ======================================
# 14. ROW ACCESS USING iloc
# ======================================

print("\n14. ILOC")

print(df.iloc[1])

# ======================================
# 15. FILTERING DATA
# ======================================

print("\n15. FILTERING")

print(
    df[
        df["Marks"] > 90
    ]
)

# ======================================
# 16. SORT VALUES
# ======================================

print("\n16. SORT VALUES")

print(
    df.sort_values(
        by="Marks",
        ascending=False
    )
)

# ======================================
# 17. CREATE STUDENT DATAFRAME
# ======================================

print("\n17. STUDENT DATAFRAME")

student_data = {
    "Name": [
        "Saloni",
        "Riya",
        "Ankit",
        "Rahul",
        "Priya"
    ],
    "Math": [
        92,
        88,
        95,
        81,
        90
    ],
    "Python": [
        95,
        90,
        89,
        85,
        93
    ]
}

students_df = pd.DataFrame(
    student_data
)

print(students_df)

# ======================================
# 18. ADD TOTAL COLUMN
# ======================================

print("\n18. TOTAL COLUMN")

students_df["Total"] = (
    students_df["Math"] +
    students_df["Python"]
)

print(students_df)

# ======================================
# 19. ADD AVERAGE COLUMN
# ======================================

print("\n19. AVERAGE COLUMN")

students_df["Average"] = (
    students_df["Total"] / 2
)

print(students_df)

# ======================================
# 20. USER INPUT EXAMPLE
# ======================================

print("\n20. USER INPUT EXAMPLE")

name = input(
    "Enter Name: "
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
# 21. MINI PROJECT
# ======================================

print("\n21. MINI PROJECT")

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

print("\nStudent Records")
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
Create a DataFrame with:

- Name
- Age
- City

Exercise 2:
Display:

- Shape
- Columns
- Data Types

Exercise 3:
Add a new column.

Exercise 4:
Filter students having
marks greater than 80.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Management System.

Store:

- Name
- Mathematics
- Python
- DBMS

Calculate:

1. Total Marks
2. Average Marks
3. Highest Marks
4. Lowest Marks

Display complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 053 Completed Successfully!")