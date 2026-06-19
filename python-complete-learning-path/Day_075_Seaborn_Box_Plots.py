# ======================================
# Day 075: Seaborn Box Plots
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Box Plots using
# Seaborn
# ======================================

print("=" * 50)
print("DAY 075 - SEABORN BOX PLOTS")
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
What is a Box Plot?

A Box Plot is used to visualize
the distribution of data and
identify outliers.

Seaborn Function:

sns.boxplot()

Components:

1. Minimum Value
2. First Quartile (Q1)
3. Median (Q2)
4. Third Quartile (Q3)
5. Maximum Value
6. Outliers

Applications:

1. Data Analysis
2. Statistics
3. Machine Learning
4. Research
5. EDA (Exploratory Data Analysis)

Advantages:

1. Detect Outliers
2. Compare Distributions
3. Understand Spread
4. Summarize Data Quickly
"""

# ======================================
# SAMPLE DATA
# ======================================

marks_data = pd.DataFrame(
    {
        "Marks": [
            92, 88, 95, 81, 90,
            78, 84, 89, 91, 87,
            76, 85, 93, 80, 82
        ]
    }
)

print("\nMARKS DATA")
print(marks_data.head())

# ======================================
# 1. BASIC BOX PLOT
# ======================================

print("\n1. BASIC BOX PLOT")

sns.boxplot(
    data=marks_data,
    y="Marks"
)

plt.title(
    "Student Marks Distribution"
)

plt.show()

# ======================================
# 2. HORIZONTAL BOX PLOT
# ======================================

print("\n2. HORIZONTAL BOX PLOT")

sns.boxplot(
    data=marks_data,
    x="Marks"
)

plt.title(
    "Horizontal Box Plot"
)

plt.show()

# ======================================
# 3. SUBJECT-WISE ANALYSIS
# ======================================

print("\n3. SUBJECT ANALYSIS")

subject_data = pd.DataFrame(
    {
        "Subject": [
            "Math", "Math", "Math",
            "Python", "Python", "Python",
            "DBMS", "DBMS", "DBMS"
        ],
        "Marks": [
            92, 88, 95,
            85, 90, 93,
            78, 82, 80
        ]
    }
)

print(subject_data)

sns.boxplot(
    data=subject_data,
    x="Subject",
    y="Marks"
)

plt.title(
    "Subject-wise Marks Distribution"
)

plt.show()

# ======================================
# 4. OUTLIER DETECTION
# ======================================

print("\n4. OUTLIER DETECTION")

outlier_data = pd.DataFrame(
    {
        "Marks": [
            70, 72, 75, 78,
            80, 82, 85, 88,
            90, 95, 150
        ]
    }
)

sns.boxplot(
    data=outlier_data,
    y="Marks"
)

plt.title(
    "Outlier Detection"
)

plt.show()

# ======================================
# 5. SALES ANALYSIS
# ======================================

print("\n5. SALES ANALYSIS")

sales_data = pd.DataFrame(
    {
        "Sales": [
            1000, 1200, 1500,
            1300, 1800, 2100,
            1700, 1900
        ]
    }
)

sns.boxplot(
    data=sales_data,
    y="Sales"
)

plt.title(
    "Sales Distribution"
)

plt.show()

# ======================================
# 6. DARKGRID STYLE
# ======================================

print("\n6. DARKGRID STYLE")

sns.set_style(
    "darkgrid"
)

sns.boxplot(
    data=marks_data,
    y="Marks"
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# 7. WHITEGRID STYLE
# ======================================

print("\n7. WHITEGRID STYLE")

sns.set_style(
    "whitegrid"
)

sns.boxplot(
    data=marks_data,
    y="Marks"
)

plt.title(
    "White Grid Style"
)

plt.show()

# ======================================
# 8. ATTENDANCE ANALYSIS
# ======================================

print("\n8. ATTENDANCE ANALYSIS")

attendance_data = pd.DataFrame(
    {
        "Attendance": [
            95, 88, 97, 82,
            91, 85, 93, 89
        ]
    }
)

sns.boxplot(
    data=attendance_data,
    y="Attendance"
)

plt.title(
    "Attendance Distribution"
)

plt.show()

# ======================================
# 9. RANDOM DATASET
# ======================================

print("\n9. RANDOM DATASET")

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

sns.boxplot(
    data=random_data,
    y="Values"
)

plt.title(
    "Random Data Distribution"
)

plt.show()

# ======================================
# 10. SAVE BOX PLOT
# ======================================

print("\n10. SAVE BOX PLOT")

sns.boxplot(
    data=marks_data,
    y="Marks"
)

plt.title(
    "Saved Box Plot"
)

plt.savefig(
    "seaborn_boxplot.png"
)

plt.close()

print(
    "Box Plot Saved Successfully"
)

# ======================================
# 11. DESCRIPTIVE STATISTICS
# ======================================

print("\n11. STATISTICAL SUMMARY")

print(
    marks_data.describe()
)

# ======================================
# 12. USER INPUT EXAMPLE
# ======================================

print("\n12. USER INPUT EXAMPLE")

value = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"Marks Entered: {value}"
)

# ======================================
# 13. MINI PROJECT
# ======================================

print("\n13. MINI PROJECT")

student_performance = pd.DataFrame(
    {
        "Department": [
            "DS", "DS", "DS",
            "Math", "Math", "Math",
            "Physics", "Physics", "Physics"
        ],
        "Marks": [
            92, 88, 95,
            85, 90, 87,
            78, 82, 80
        ]
    }
)

print(student_performance)

sns.boxplot(
    data=student_performance,
    x="Department",
    y="Marks"
)

plt.title(
    "Department Performance Analysis"
)

plt.show()

print(
    "Average Marks:",
    round(
        student_performance["Marks"].mean(),
        2
    )
)

print(
    "Highest Marks:",
    student_performance["Marks"].max()
)

print(
    "Lowest Marks:",
    student_performance["Marks"].min()
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a basic box plot.

Exercise 2:
Create a horizontal box plot.

Exercise 3:
Detect outliers.

Exercise 4:
Compare subject-wise marks.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is a Box Plot?

Q2. What is an Outlier?

Q3. What is the Median?

Q4. What are Quartiles?

Q5. Why use Box Plots?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a College Performance System.

Columns:

1. Department
2. Student Marks

Generate:

1. Box Plot
2. Outlier Detection
3. Department Comparison
4. Statistical Summary

Analyze performance.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 075 Completed Successfully!"
)