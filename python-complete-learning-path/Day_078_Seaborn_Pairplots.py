# ======================================
# Day 078: Seaborn Pairplots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Pairplots using
# Seaborn
# ======================================

print("=" * 50)
print("DAY 078 - SEABORN PAIRPLOTS")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Pairplot?

A Pairplot creates pairwise
relationships between all
numerical variables in a dataset.

Seaborn Function:

sns.pairplot()

Applications:

1. Exploratory Data Analysis
2. Machine Learning
3. Correlation Discovery
4. Feature Analysis
5. Research Projects

Advantages:

1. Multiple Visualizations
2. Relationship Analysis
3. Distribution Analysis
4. Easy EDA
"""

# ======================================
# SAMPLE DATASET
# ======================================

student_data = pd.DataFrame(
    {
        "Math": [
            92, 88, 95, 81, 90
        ],
        "Python": [
            95, 90, 89, 85, 93
        ],
        "DBMS": [
            88, 85, 91, 80, 87
        ],
        "Statistics": [
            90, 87, 92, 84, 89
        ]
    }
)

print("\nSTUDENT DATA")
print(student_data)

# ======================================
# 1. BASIC PAIRPLOT
# ======================================

print("\n1. BASIC PAIRPLOT")

sns.pairplot(
    student_data
)

plt.show()

# ======================================
# 2. PAIRPLOT WITH HISTOGRAM
# ======================================

print("\n2. HISTOGRAM DIAGONAL")

sns.pairplot(
    student_data,
    diag_kind="hist"
)

plt.show()

# ======================================
# 3. PAIRPLOT WITH KDE
# ======================================

print("\n3. KDE DIAGONAL")

sns.pairplot(
    student_data,
    diag_kind="kde"
)

plt.show()

# ======================================
# 4. EXAM PERFORMANCE DATA
# ======================================

print("\n4. EXAM PERFORMANCE")

exam_data = pd.DataFrame(
    {
        "Study_Hours": [
            2, 3, 4, 5, 6,
            7, 8, 9
        ],
        "Attendance": [
            70, 75, 80, 82,
            85, 90, 92, 95
        ],
        "Marks": [
            50, 58, 67, 75,
            82, 88, 93, 97
        ]
    }
)

print(exam_data)

sns.pairplot(
    exam_data
)

plt.show()

# ======================================
# 5. LOAD IRIS DATASET
# ======================================

print("\n5. IRIS DATASET")

iris = sns.load_dataset(
    "iris"
)

print(
    iris.head()
)

sns.pairplot(
    iris
)

plt.show()

# ======================================
# 6. PAIRPLOT WITH HUE
# ======================================

print("\n6. PAIRPLOT WITH HUE")

sns.pairplot(
    iris,
    hue="species"
)

plt.show()

# ======================================
# 7. CORRELATION ANALYSIS
# ======================================

print("\n7. CORRELATION ANALYSIS")

correlation = (
    student_data.corr()
)

print(correlation)

# ======================================
# 8. RANDOM DATASET
# ======================================

print("\n8. RANDOM DATASET")

random_data = pd.DataFrame(
    {
        "A":
        np.random.randint(
            1,
            100,
            50
        ),

        "B":
        np.random.randint(
            1,
            100,
            50
        ),

        "C":
        np.random.randint(
            1,
            100,
            50
        )
    }
)

sns.pairplot(
    random_data
)

plt.show()

# ======================================
# 9. SALES DATA ANALYSIS
# ======================================

print("\n9. SALES ANALYSIS")

sales_data = pd.DataFrame(
    {
        "Sales": [
            1000, 1200, 1500,
            1300, 1800
        ],

        "Profit": [
            200, 250, 350,
            300, 450
        ],

        "Customers": [
            50, 60, 75,
            70, 90
        ]
    }
)

sns.pairplot(
    sales_data
)

plt.show()

# ======================================
# 10. SAVE PAIRPLOT
# ======================================

print("\n10. SAVE PAIRPLOT")

pair_plot = sns.pairplot(
    student_data
)

pair_plot.savefig(
    "seaborn_pairplot.png"
)

plt.close()

print(
    "Pairplot Saved Successfully"
)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

value = int(
    input(
        "Enter Any Number: "
    )
)

print(
    f"You Entered: {value}"
)

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

project_data = pd.DataFrame(
    {
        "Math": [
            92, 88, 95, 81, 90
        ],

        "Python": [
            95, 90, 89, 85, 93
        ],

        "DBMS": [
            88, 85, 91, 80, 87
        ],

        "Statistics": [
            90, 87, 92, 84, 89
        ]
    }
)

print(project_data)

sns.pairplot(
    project_data,
    diag_kind="hist"
)

plt.show()

print(
    "\nAverage Marks"
)

print(
    project_data.mean()
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Pairplot
using student data.

Exercise 2:
Use:

- diag_kind="hist"
- diag_kind="kde"

Exercise 3:
Load Iris Dataset.

Exercise 4:
Use hue parameter.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is a Pairplot?

Q2. Why use Pairplots?

Q3. What is hue?

Q4. Difference between
Heatmap and Pairplot?

Q5. What is EDA?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Analytics System.

Columns:

1. Math
2. Python
3. DBMS
4. Statistics

Generate:

1. Pairplot
2. Correlation Analysis
3. Feature Relationships
4. Performance Insights

Perform complete EDA.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 078 Completed Successfully!"
)