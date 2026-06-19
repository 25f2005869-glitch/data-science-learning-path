# ======================================
# Day 055: Data Cleaning
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Data Cleaning using Pandas for
# Data Analysis and Machine Learning
# ======================================

print("=" * 50)
print("DAY 055 - DATA CLEANING")
print("=" * 50)

# ======================================
# IMPORT PANDAS & NUMPY
# ======================================

import pandas as pd
import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Data Cleaning?

Data Cleaning is the process of
detecting and correcting inaccurate,
incomplete, duplicate, or missing data.

Why Data Cleaning?

1. Improves Data Quality
2. Better Analysis
3. Better ML Models
4. Removes Errors

Common Problems:

1. Missing Values
2. Null Values
3. Duplicate Records
4. Incorrect Data Types
5. Outliers

Important Functions:

1. isnull()
2. notnull()
3. dropna()
4. fillna()
5. duplicated()
6. drop_duplicates()
"""

# ======================================
# SAMPLE DATAFRAME
# ======================================

data = {
    "Name": [
        "Saloni",
        "Riya",
        np.nan,
        "Rahul",
        "Saloni"
    ],
    "Marks": [
        92,
        np.nan,
        88,
        95,
        92
    ],
    "City": [
        "Patna",
        "Delhi",
        "Patna",
        np.nan,
        "Patna"
    ]
}

df = pd.DataFrame(data)

print("\nORIGINAL DATAFRAME")
print(df)

# ======================================
# 1. CHECK NULL VALUES
# ======================================

print("\n1. CHECK NULL VALUES")

print(df.isnull())

# ======================================
# 2. COUNT NULL VALUES
# ======================================

print("\n2. COUNT NULL VALUES")

print(df.isnull().sum())

# ======================================
# 3. CHECK NOT NULL VALUES
# ======================================

print("\n3. NOT NULL VALUES")

print(df.notnull())

# ======================================
# 4. DROP ROWS WITH NULL VALUES
# ======================================

print("\n4. DROP NULL ROWS")

print(df.dropna())

# ======================================
# 5. FILL NULL VALUES
# ======================================

print("\n5. FILL NULL VALUES")

filled_df = df.fillna(
    "Unknown"
)

print(filled_df)

# ======================================
# 6. FILL NUMERIC NULL VALUES
# ======================================

print("\n6. FILL NUMERIC NULL VALUES")

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print(df)

# ======================================
# 7. FORWARD FILL
# ======================================

print("\n7. FORWARD FILL")

forward_df = df.ffill()

print(forward_df)

# ======================================
# 8. BACKWARD FILL
# ======================================

print("\n8. BACKWARD FILL")

backward_df = df.bfill()

print(backward_df)

# ======================================
# 9. CHECK DUPLICATES
# ======================================

print("\n9. CHECK DUPLICATES")

print(df.duplicated())

# ======================================
# 10. COUNT DUPLICATES
# ======================================

print("\n10. COUNT DUPLICATES")

print(df.duplicated().sum())

# ======================================
# 11. REMOVE DUPLICATES
# ======================================

print("\n11. REMOVE DUPLICATES")

print(df.drop_duplicates())

# ======================================
# 12. REPLACE VALUES
# ======================================

print("\n12. REPLACE VALUES")

cities_df = pd.DataFrame(
    {
        "City": [
            "Patna",
            "Delhi",
            "Mumbai"
        ]
    }
)

cities_df["City"] = (
    cities_df["City"]
    .replace(
        "Patna",
        "Patna, Bihar"
    )
)

print(cities_df)

# ======================================
# 13. CHANGE DATA TYPE
# ======================================

print("\n13. CHANGE DATA TYPE")

numbers = pd.DataFrame(
    {
        "Marks": [
            "90",
            "85",
            "95"
        ]
    }
)

numbers["Marks"] = (
    numbers["Marks"]
    .astype(int)
)

print(numbers.dtypes)

# ======================================
# 14. REMOVE WHITESPACES
# ======================================

print("\n14. REMOVE WHITESPACES")

names = pd.DataFrame(
    {
        "Name": [
            " Saloni ",
            " Riya ",
            " Rahul "
        ]
    }
)

names["Name"] = (
    names["Name"]
    .str.strip()
)

print(names)

# ======================================
# 15. CONVERT TO UPPERCASE
# ======================================

print("\n15. UPPERCASE")

names["Name"] = (
    names["Name"]
    .str.upper()
)

print(names)

# ======================================
# 16. USER INPUT EXAMPLE
# ======================================

print("\n16. USER INPUT EXAMPLE")

name = input(
    "Enter Student Name: "
)

marks = input(
    "Enter Marks: "
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
        None,
        "Ankit",
        "Saloni"
    ],
    "Marks": [
        92,
        None,
        95,
        92
    ]
}

students_df = pd.DataFrame(
    student_data
)

print("\nORIGINAL DATA")

print(students_df)

students_df["Name"] = (
    students_df["Name"]
    .fillna("Unknown")
)

students_df["Marks"] = (
    students_df["Marks"]
    .fillna(
        students_df["Marks"].mean()
    )
)

students_df = (
    students_df
    .drop_duplicates()
)

print("\nCLEANED DATA")

print(students_df)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a DataFrame with
missing values.

Use:

- isnull()
- dropna()

Exercise 2:
Fill missing values
using fillna().

Exercise 3:
Create duplicate records
and remove them.

Exercise 4:
Convert string numbers
to integers.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Dataset.

Include:

- Missing Values
- Duplicate Records
- Extra Spaces

Perform:

1. Remove Duplicates
2. Fill Missing Values
3. Remove Spaces
4. Convert Data Types

Display cleaned dataset.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 055 Completed Successfully!")