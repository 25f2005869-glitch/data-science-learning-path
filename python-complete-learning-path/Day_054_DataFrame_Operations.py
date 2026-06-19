# ======================================
# Day 054: DataFrame Operations
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Performing Operations on Pandas
# DataFrames for Data Analysis
# ======================================

print("=" * 50)
print("DAY 054 - DATAFRAME OPERATIONS")
print("=" * 50)

# ======================================
# IMPORT PANDAS
# ======================================

import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
DataFrame Operations are used for:

1. Selecting Data
2. Filtering Data
3. Updating Data
4. Adding Columns
5. Deleting Columns
6. Renaming Columns
7. Sorting Data

These operations are essential for:

- Data Cleaning
- Data Analysis
- Machine Learning
- Business Analytics
"""

# ======================================
# SAMPLE DATAFRAME
# ======================================

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

df = pd.DataFrame(student_data)

print("\nORIGINAL DATAFRAME")
print(df)

# ======================================
# 1. SELECT SINGLE COLUMN
# ======================================

print("\n1. SINGLE COLUMN")

print(df["Name"])

# ======================================
# 2. SELECT MULTIPLE COLUMNS
# ======================================

print("\n2. MULTIPLE COLUMNS")

print(
    df[
        ["Name", "Math"]
    ]
)

# ======================================
# 3. SELECT ROW USING loc
# ======================================

print("\n3. ROW USING loc")

print(df.loc[0])

# ======================================
# 4. SELECT ROW USING iloc
# ======================================

print("\n4. ROW USING iloc")

print(df.iloc[1])

# ======================================
# 5. FILTER DATA
# ======================================

print("\n5. FILTER DATA")

print(
    df[
        df["Math"] > 90
    ]
)

# ======================================
# 6. MULTIPLE CONDITIONS
# ======================================

print("\n6. MULTIPLE CONDITIONS")

print(
    df[
        (df["Math"] > 85)
        &
        (df["Python"] > 90)
    ]
)

# ======================================
# 7. ADD NEW COLUMN
# ======================================

print("\n7. ADD NEW COLUMN")

df["Total"] = (
    df["Math"] +
    df["Python"]
)

print(df)

# ======================================
# 8. ADD AVERAGE COLUMN
# ======================================

print("\n8. ADD AVERAGE COLUMN")

df["Average"] = (
    df["Total"] / 2
)

print(df)

# ======================================
# 9. UPDATE VALUES
# ======================================

print("\n9. UPDATE VALUES")

df.loc[0, "Math"] = 100

print(df)

# ======================================
# 10. RENAME COLUMN
# ======================================

print("\n10. RENAME COLUMN")

df.rename(
    columns={
        "Math": "Mathematics"
    },
    inplace=True
)

print(df)

# ======================================
# 11. DELETE COLUMN
# ======================================

print("\n11. DELETE COLUMN")

df.drop(
    "Average",
    axis=1,
    inplace=True
)

print(df)

# ======================================
# 12. SORT DATA
# ======================================

print("\n12. SORT DATA")

print(
    df.sort_values(
        by="Total",
        ascending=False
    )
)

# ======================================
# 13. RESET INDEX
# ======================================

print("\n13. RESET INDEX")

sorted_df = df.sort_values(
    by="Total",
    ascending=False
)

print(
    sorted_df.reset_index(
        drop=True
    )
)

# ======================================
# 14. UNIQUE VALUES
# ======================================

print("\n14. UNIQUE VALUES")

cities = pd.DataFrame(
    {
        "City": [
            "Patna",
            "Delhi",
            "Patna",
            "Mumbai"
        ]
    }
)

print(
    cities["City"].unique()
)

# ======================================
# 15. VALUE COUNTS
# ======================================

print("\n15. VALUE COUNTS")

print(
    cities["City"].value_counts()
)

# ======================================
# 16. APPLY FUNCTION
# ======================================

print("\n16. APPLY FUNCTION")

df["Grade"] = df["Total"].apply(
    lambda x:
    "A" if x >= 180
    else "B"
)

print(df)

# ======================================
# 17. USER INPUT EXAMPLE
# ======================================

print("\n17. USER INPUT EXAMPLE")

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
# 18. MINI PROJECT
# ======================================

print("\n18. MINI PROJECT")

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

students_df["Total"] = (
    students_df["Math"] +
    students_df["Python"]
)

students_df["Average"] = (
    students_df["Total"] / 2
)

print("\nSTUDENT REPORT")
print(students_df)

print("\nTOP STUDENT")

top_student = students_df.loc[
    students_df["Total"].idxmax()
]

print(top_student)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a DataFrame and:

- Add a new column
- Delete a column

Exercise 2:
Rename a column.

Exercise 3:
Filter records where
marks > 80.

Exercise 4:
Sort students by marks.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Result System.

Store:

- Name
- Mathematics
- Python
- DBMS

Calculate:

1. Total
2. Average
3. Grade

Display:

- Top Student
- Lowest Student
- Complete Report
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 054 Completed Successfully!")