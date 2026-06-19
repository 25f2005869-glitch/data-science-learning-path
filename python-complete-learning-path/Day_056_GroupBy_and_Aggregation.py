# ======================================
# Day 056: GroupBy and Aggregation
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding GroupBy and
# Aggregation in Pandas
# ======================================

print("=" * 50)
print("DAY 056 - GROUPBY AND AGGREGATION")
print("=" * 50)

# ======================================
# IMPORT PANDAS
# ======================================

import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is GroupBy?

GroupBy is used to split data
into groups and perform
calculations on each group.

Process:

1. Split
2. Apply
3. Combine

Syntax:

df.groupby("Column")

Aggregation Functions:

1. sum()
2. mean()
3. max()
4. min()
5. count()
6. std()
7. var()

Applications:

- Business Analytics
- Sales Analysis
- Student Analysis
- Data Science
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
        "Priya",
        "Aman"
    ],
    "Department": [
        "Data Science",
        "Data Science",
        "Mathematics",
        "Mathematics",
        "Data Science",
        "Mathematics"
    ],
    "Marks": [
        92,
        88,
        95,
        81,
        90,
        85
    ]
}

df = pd.DataFrame(student_data)

print("\nORIGINAL DATAFRAME")
print(df)

# ======================================
# 1. GROUPBY DEPARTMENT
# ======================================

print("\n1. GROUPBY DEPARTMENT")

grouped = df.groupby(
    "Department"
)

print(grouped)

# ======================================
# 2. SUM
# ======================================

print("\n2. SUM")

print(
    grouped["Marks"].sum()
)

# ======================================
# 3. MEAN
# ======================================

print("\n3. MEAN")

print(
    grouped["Marks"].mean()
)

# ======================================
# 4. MAXIMUM
# ======================================

print("\n4. MAXIMUM")

print(
    grouped["Marks"].max()
)

# ======================================
# 5. MINIMUM
# ======================================

print("\n5. MINIMUM")

print(
    grouped["Marks"].min()
)

# ======================================
# 6. COUNT
# ======================================

print("\n6. COUNT")

print(
    grouped["Marks"].count()
)

# ======================================
# 7. STANDARD DEVIATION
# ======================================

print("\n7. STANDARD DEVIATION")

print(
    grouped["Marks"].std()
)

# ======================================
# 8. MULTIPLE AGGREGATIONS
# ======================================

print("\n8. MULTIPLE AGGREGATIONS")

print(
    grouped["Marks"].agg(
        [
            "sum",
            "mean",
            "max",
            "min",
            "count"
        ]
    )
)

# ======================================
# 9. GROUPBY MULTIPLE COLUMNS
# ======================================

print("\n9. MULTIPLE COLUMNS")

sales_data = {
    "City": [
        "Patna",
        "Patna",
        "Delhi",
        "Delhi"
    ],
    "Product": [
        "Laptop",
        "Mobile",
        "Laptop",
        "Mobile"
    ],
    "Sales": [
        50000,
        30000,
        60000,
        35000
    ]
}

sales_df = pd.DataFrame(
    sales_data
)

print(
    sales_df.groupby(
        ["City", "Product"]
    )["Sales"].sum()
)

# ======================================
# 10. SIZE
# ======================================

print("\n10. SIZE")

print(
    df.groupby(
        "Department"
    ).size()
)

# ======================================
# 11. FIRST RECORD
# ======================================

print("\n11. FIRST RECORD")

print(
    grouped.first()
)

# ======================================
# 12. LAST RECORD
# ======================================

print("\n12. LAST RECORD")

print(
    grouped.last()
)

# ======================================
# 13. DESCRIBE GROUPS
# ======================================

print("\n13. DESCRIBE")

print(
    grouped["Marks"]
    .describe()
)

# ======================================
# 14. ITERATING GROUPS
# ======================================

print("\n14. ITERATING GROUPS")

for department, data in grouped:

    print("\nDepartment:")
    print(department)

    print(data)

# ======================================
# 15. CUSTOM AGGREGATION
# ======================================

print("\n15. CUSTOM AGGREGATION")

print(
    grouped["Marks"]
    .agg(
        lambda x:
        x.max() - x.min()
    )
)

# ======================================
# 16. USER INPUT EXAMPLE
# ======================================

print("\n16. USER INPUT EXAMPLE")

department = input(
    "Enter Department: "
)

marks = int(
    input(
        "Enter Marks: "
    )
)

user_df = pd.DataFrame(
    {
        "Department": [department],
        "Marks": [marks]
    }
)

print(user_df)

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT")

student_data = {
    "Student": [
        "A",
        "B",
        "C",
        "D",
        "E"
    ],
    "Department": [
        "Data Science",
        "Data Science",
        "Math",
        "Math",
        "Data Science"
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

report = (
    students_df
    .groupby("Department")
    ["Marks"]
    .agg(
        [
            "count",
            "mean",
            "max",
            "min"
        ]
    )
)

print("\nDEPARTMENT REPORT")

print(report)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a DataFrame and
group by Department.

Exercise 2:
Calculate:

- Sum
- Mean
- Max
- Min

Exercise 3:
Perform multiple
aggregations.

Exercise 4:
Group by two columns.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a College Analysis System.

Columns:

- Student Name
- Department
- Marks

Generate Department-wise:

1. Student Count
2. Total Marks
3. Average Marks
4. Highest Marks
5. Lowest Marks

Display a complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 056 Completed Successfully!")