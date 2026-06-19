# ======================================
# Day 057: Merging and Joining
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Merging and Joining
# DataFrames in Pandas
# ======================================

print("=" * 50)
print("DAY 057 - MERGING AND JOINING")
print("=" * 50)

# ======================================
# IMPORT PANDAS
# ======================================

import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Merging?

Merging combines multiple DataFrames
based on common columns.

Similar to SQL JOIN operations.

Types of Joins:

1. Inner Join
2. Left Join
3. Right Join
4. Outer Join

Important Functions:

1. merge()
2. join()
3. concat()

Applications:

- Data Integration
- Database Operations
- Business Analytics
- Machine Learning
"""

# ======================================
# DATAFRAME 1
# ======================================

students = pd.DataFrame(
    {
        "Student_ID": [1, 2, 3, 4],
        "Name": [
            "Saloni",
            "Riya",
            "Ankit",
            "Rahul"
        ]
    }
)

print("\nSTUDENTS DATAFRAME")
print(students)

# ======================================
# DATAFRAME 2
# ======================================

marks = pd.DataFrame(
    {
        "Student_ID": [1, 2, 3, 5],
        "Marks": [
            92,
            88,
            95,
            80
        ]
    }
)

print("\nMARKS DATAFRAME")
print(marks)

# ======================================
# 1. INNER JOIN
# ======================================

print("\n1. INNER JOIN")

inner_join = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="inner"
)

print(inner_join)

# ======================================
# 2. LEFT JOIN
# ======================================

print("\n2. LEFT JOIN")

left_join = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="left"
)

print(left_join)

# ======================================
# 3. RIGHT JOIN
# ======================================

print("\n3. RIGHT JOIN")

right_join = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="right"
)

print(right_join)

# ======================================
# 4. OUTER JOIN
# ======================================

print("\n4. OUTER JOIN")

outer_join = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="outer"
)

print(outer_join)

# ======================================
# 5. MULTIPLE DATAFRAMES
# ======================================

print("\n5. THIRD DATAFRAME")

departments = pd.DataFrame(
    {
        "Student_ID": [1, 2, 3, 4],
        "Department": [
            "Data Science",
            "Math",
            "Data Science",
            "Math"
        ]
    }
)

print(departments)

# ======================================
# 6. MERGE THREE TABLES
# ======================================

print("\n6. MERGE THREE DATAFRAMES")

merged_df = pd.merge(
    inner_join,
    departments,
    on="Student_ID"
)

print(merged_df)

# ======================================
# 7. CONCAT ROWS
# ======================================

print("\n7. CONCAT ROWS")

df1 = pd.DataFrame(
    {
        "Name": [
            "Saloni",
            "Riya"
        ]
    }
)

df2 = pd.DataFrame(
    {
        "Name": [
            "Ankit",
            "Rahul"
        ]
    }
)

row_concat = pd.concat(
    [df1, df2]
)

print(row_concat)

# ======================================
# 8. CONCAT COLUMNS
# ======================================

print("\n8. CONCAT COLUMNS")

df3 = pd.DataFrame(
    {
        "Marks": [
            92,
            88
        ]
    }
)

column_concat = pd.concat(
    [df1, df3],
    axis=1
)

print(column_concat)

# ======================================
# 9. JOIN METHOD
# ======================================

print("\n9. JOIN METHOD")

left = pd.DataFrame(
    {
        "Name": [
            "Saloni",
            "Riya"
        ]
    },
    index=[1, 2]
)

right = pd.DataFrame(
    {
        "Marks": [
            92,
            88
        ]
    },
    index=[1, 2]
)

joined = left.join(right)

print(joined)

# ======================================
# 10. MERGE ON DIFFERENT COLUMN NAMES
# ======================================

print("\n10. DIFFERENT COLUMN NAMES")

df_a = pd.DataFrame(
    {
        "ID": [1, 2, 3],
        "Name": [
            "Saloni",
            "Riya",
            "Ankit"
        ]
    }
)

df_b = pd.DataFrame(
    {
        "Student_ID": [1, 2, 3],
        "Marks": [
            92,
            88,
            95
        ]
    }
)

result = pd.merge(
    df_a,
    df_b,
    left_on="ID",
    right_on="Student_ID"
)

print(result)

# ======================================
# 11. MERGE INDICATOR
# ======================================

print("\n11. MERGE INDICATOR")

indicator_df = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="outer",
    indicator=True
)

print(indicator_df)

# ======================================
# 12. FIND UNMATCHED RECORDS
# ======================================

print("\n12. UNMATCHED RECORDS")

unmatched = indicator_df[
    indicator_df["_merge"]
    != "both"
]

print(unmatched)

# ======================================
# 13. USER INPUT EXAMPLE
# ======================================

print("\n13. USER INPUT EXAMPLE")

name = input(
    "Enter Student Name: "
)

marks_value = int(
    input(
        "Enter Marks: "
    )
)

user_df = pd.DataFrame(
    {
        "Name": [name],
        "Marks": [marks_value]
    }
)

print(user_df)

# ======================================
# 14. MINI PROJECT
# ======================================

print("\n14. MINI PROJECT")

students = pd.DataFrame(
    {
        "ID": [1, 2, 3],
        "Name": [
            "Saloni",
            "Riya",
            "Ankit"
        ]
    }
)

marks = pd.DataFrame(
    {
        "ID": [1, 2, 3],
        "Marks": [
            92,
            88,
            95
        ]
    }
)

departments = pd.DataFrame(
    {
        "ID": [1, 2, 3],
        "Department": [
            "Data Science",
            "Math",
            "Data Science"
        ]
    }
)

report = pd.merge(
    students,
    marks,
    on="ID"
)

report = pd.merge(
    report,
    departments,
    on="ID"
)

print("\nSTUDENT REPORT")
print(report)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create two DataFrames and
perform an Inner Join.

Exercise 2:
Perform:

- Left Join
- Right Join
- Outer Join

Exercise 3:
Use concat() for:

- Rows
- Columns

Exercise 4:
Use join() method.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a College Database.

DataFrames:

1. Students
2. Marks
3. Departments

Merge all DataFrames and display:

1. Student Name
2. Marks
3. Department

Generate a complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 057 Completed Successfully!")