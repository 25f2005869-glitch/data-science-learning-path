# ======================================
# Day 074: Seaborn Histograms
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Histograms using
# Seaborn
# ======================================

print("=" * 50)
print("DAY 074 - SEABORN HISTOGRAMS")
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
What is a Histogram?

A Histogram is used to show
the distribution of numerical data.

Unlike Bar Plots:

Bar Plot:
- Compares categories

Histogram:
- Shows frequency distribution

Seaborn Function:

sns.histplot()

Applications:

1. Student Marks Analysis
2. Salary Distribution
3. Sales Distribution
4. Data Science
5. Machine Learning

Advantages:

1. Understand Data Distribution
2. Detect Outliers
3. Identify Patterns
4. Useful for EDA
"""

# ======================================
# SAMPLE DATA
# ======================================

marks = [
    92, 88, 95, 81, 90,
    78, 84, 89, 91, 87,
    76, 85, 93, 80, 82
]

marks_df = pd.DataFrame(
    {
        "Marks": marks
    }
)

print("\nMARKS DATA")
print(marks_df.head())

# ======================================
# 1. BASIC HISTOGRAM
# ======================================

print("\n1. BASIC HISTOGRAM")

sns.histplot(
    data=marks_df,
    x="Marks"
)

plt.title(
    "Marks Distribution"
)

plt.show()

# ======================================
# 2. CUSTOM BINS
# ======================================

print("\n2. CUSTOM BINS")

sns.histplot(
    data=marks_df,
    x="Marks",
    bins=5
)

plt.title(
    "Histogram with 5 Bins"
)

plt.show()

# ======================================
# 3. KDE CURVE
# ======================================

print("\n3. KDE CURVE")

sns.histplot(
    data=marks_df,
    x="Marks",
    kde=True
)

plt.title(
    "Histogram with KDE"
)

plt.show()

# ======================================
# 4. SALES DATA ANALYSIS
# ======================================

print("\n4. SALES ANALYSIS")

sales_data = pd.DataFrame(
    {
        "Sales": [
            1000,
            1200,
            1500,
            1300,
            1800,
            2100,
            1700,
            1900
        ]
    }
)

sns.histplot(
    data=sales_data,
    x="Sales",
    kde=True
)

plt.title(
    "Sales Distribution"
)

plt.show()

# ======================================
# 5. STUDENT PERFORMANCE
# ======================================

print("\n5. STUDENT PERFORMANCE")

student_marks = pd.DataFrame(
    {
        "Marks": [
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100
        ]
    }
)

sns.histplot(
    data=student_marks,
    x="Marks",
    bins=8
)

plt.title(
    "Student Performance Distribution"
)

plt.show()

# ======================================
# 6. RANDOM DATASET
# ======================================

print("\n6. RANDOM DATASET")

random_data = pd.DataFrame(
    {
        "Values":
        np.random.randint(
            1,
            100,
            100
        )
    }
)

sns.histplot(
    data=random_data,
    x="Values",
    kde=True
)

plt.title(
    "Random Data Distribution"
)

plt.show()

# ======================================
# 7. STYLE SETTINGS
# ======================================

print("\n7. DARKGRID STYLE")

sns.set_style(
    "darkgrid"
)

sns.histplot(
    data=marks_df,
    x="Marks"
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# 8. WHITEGRID STYLE
# ======================================

print("\n8. WHITEGRID STYLE")

sns.set_style(
    "whitegrid"
)

sns.histplot(
    data=marks_df,
    x="Marks"
)

plt.title(
    "White Grid Style"
)

plt.show()

# ======================================
# 9. EXAM ANALYSIS
# ======================================

print("\n9. EXAM ANALYSIS")

exam_data = pd.DataFrame(
    {
        "Scores": [
            55, 60, 62, 65, 67,
            70, 72, 75, 78, 80,
            82, 85, 88, 90, 92
        ]
    }
)

sns.histplot(
    data=exam_data,
    x="Scores",
    bins=6,
    kde=True
)

plt.title(
    "Exam Score Distribution"
)

plt.show()

# ======================================
# 10. SAVE HISTOGRAM
# ======================================

print("\n10. SAVE HISTOGRAM")

sns.histplot(
    data=marks_df,
    x="Marks",
    kde=True
)

plt.title(
    "Saved Histogram"
)

plt.savefig(
    "seaborn_histogram.png"
)

plt.close()

print(
    "Histogram Saved Successfully"
)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

value = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"Marks Entered: {value}"
)

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT")

performance_data = pd.DataFrame(
    {
        "Marks": [
            92, 88, 95, 81, 90,
            78, 84, 89, 91, 87,
            76, 85, 93, 80, 82
        ]
    }
)

sns.histplot(
    data=performance_data,
    x="Marks",
    bins=5,
    kde=True
)

plt.title(
    "Student Marks Dashboard"
)

plt.xlabel(
    "Marks"
)

plt.ylabel(
    "Frequency"
)

plt.show()

print(
    "Highest Marks:",
    performance_data["Marks"].max()
)

print(
    "Lowest Marks:",
    performance_data["Marks"].min()
)

print(
    "Average Marks:",
    round(
        performance_data["Marks"].mean(),
        2
    )
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Histogram
using marks data.

Exercise 2:
Use:

- bins=5
- bins=10

Exercise 3:
Add KDE Curve.

Exercise 4:
Save Histogram as PNG.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is sns.histplot()?

Q2. Difference between
Histogram and Bar Plot?

Q3. What is KDE?

Q4. Why use Histograms?

Q5. What is a distribution?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create an Exam Analysis System.

Columns:

1. Student Marks

Generate:

1. Histogram
2. KDE Curve
3. Highest Marks
4. Lowest Marks
5. Average Marks

Analyze distribution.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 074 Completed Successfully!"
)