# ======================================
# Day 097: Correlation and Covariance
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Correlation and
# Covariance in Statistics
# ======================================

print("=" * 60)
print("DAY 097 - CORRELATION AND COVARIANCE")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Correlation and Covariance
measure relationships between
two variables.

Applications:

1. Data Science
2. Machine Learning
3. Business Analytics
4. Research
5. Finance

Examples:

Study Hours vs Marks

Advertising vs Sales

Experience vs Salary
"""

# ======================================
# SAMPLE DATASET
# ======================================

study_hours = [
    1,
    2,
    3,
    4,
    5
]

marks = [
    45,
    55,
    65,
    75,
    85
]

data = pd.DataFrame(
    {
        "Study_Hours":
        study_hours,

        "Marks":
        marks
    }
)

print("\nDATASET")
print(data)

# ======================================
# COVARIANCE
# ======================================

print("\nCOVARIANCE")

covariance = data[
    "Study_Hours"
].cov(
    data["Marks"]
)

print(
    "Covariance:",
    round(
        covariance,
        2
    )
)

# ======================================
# CORRELATION
# ======================================

print("\nCORRELATION")

correlation = data[
    "Study_Hours"
].corr(
    data["Marks"]
)

print(
    "Correlation:",
    round(
        correlation,
        2
    )
)

# ======================================
# POSITIVE CORRELATION
# ======================================

print("\nPOSITIVE CORRELATION")

positive_data = pd.DataFrame(
    {
        "Hours":
        [1, 2, 3, 4, 5],

        "Marks":
        [40, 50, 60, 70, 80]
    }
)

print(
    positive_data
)

print(
    "Correlation:",
    round(
        positive_data[
            "Hours"
        ].corr(
            positive_data[
                "Marks"
            ]
        ),
        2
    )
)

# ======================================
# NEGATIVE CORRELATION
# ======================================

print("\nNEGATIVE CORRELATION")

negative_data = pd.DataFrame(
    {
        "TV_Hours":
        [1, 2, 3, 4, 5],

        "Marks":
        [90, 80, 70, 60, 50]
    }
)

print(
    negative_data
)

print(
    "Correlation:",
    round(
        negative_data[
            "TV_Hours"
        ].corr(
            negative_data[
                "Marks"
            ]
        ),
        2
    )
)

# ======================================
# NO CORRELATION
# ======================================

print("\nNO CORRELATION")

random_data = pd.DataFrame(
    {
        "X":
        [1, 2, 3, 4, 5],

        "Y":
        [7, 2, 9, 1, 6]
    }
)

print(
    random_data
)

print(
    "Correlation:",
    round(
        random_data[
            "X"
        ].corr(
            random_data[
                "Y"
            ]
        ),
        2
    )
)

# ======================================
# SALES EXAMPLE
# ======================================

print("\nSALES EXAMPLE")

sales_data = pd.DataFrame(
    {
        "Advertising":
        [10, 20, 30, 40, 50],

        "Sales":
        [100, 150, 200, 250, 300]
    }
)

print(
    sales_data
)

print(
    "Correlation:",
    round(
        sales_data[
            "Advertising"
        ].corr(
            sales_data[
                "Sales"
            ]
        ),
        2
    )
)

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

x1 = int(
    input(
        "Enter Value 1: "
    )
)

x2 = int(
    input(
        "Enter Value 2: "
    )
)

x3 = int(
    input(
        "Enter Value 3: "
    )
)

user_x = [
    1,
    2,
    3
]

user_y = [
    x1,
    x2,
    x3
]

user_df = pd.DataFrame(
    {
        "X": user_x,
        "Y": user_y
    }
)

print(
    "Correlation:",
    round(
        user_df["X"].corr(
            user_df["Y"]
        ),
        2
    )
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

project_data = pd.DataFrame(
    {
        "Study_Hours":
        [2, 3, 4, 5, 6, 7],

        "Marks":
        [50, 60, 68, 75, 82, 90]
    }
)

print(
    project_data
)

print(
    "Covariance:",
    round(
        project_data[
            "Study_Hours"
        ].cov(
            project_data[
                "Marks"
            ]
        ),
        2
    )
)

print(
    "Correlation:",
    round(
        project_data[
            "Study_Hours"
        ].corr(
            project_data[
                "Marks"
            ]
        ),
        2
    )
)

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Covariance

Correlation

Positive Correlation

Negative Correlation

No Correlation
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Calculate Covariance.

Exercise 2:
Calculate Correlation.

Exercise 3:
Create Positive Correlation Data.

Exercise 4:
Create Negative Correlation Data.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Covariance?

Q2. What is Correlation?

Q3. Difference between
Covariance and Correlation?

Q4. What is Positive
Correlation?

Q5. What is Negative
Correlation?

Q6. What is No Correlation?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics System.

Input:

1. Study Hours
2. Marks

Generate:

1. Covariance
2. Correlation

Interpret Relationship.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 097 Completed Successfully!"
)