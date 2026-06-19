# ======================================
# Day 071: Seaborn Introduction
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Seaborn for
# Statistical Data Visualization
# ======================================

print("=" * 50)
print("DAY 071 - SEABORN INTRODUCTION")
print("=" * 50)

# ======================================
# IMPORT LIBRARIES
# ======================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Seaborn?

Seaborn is a Python data
visualization library built on
top of Matplotlib.

Developed By:
Michael Waskom

Official Purpose:

Statistical Data Visualization

Why Seaborn?

1. Beautiful Visualizations
2. Less Code
3. Statistical Analysis
4. Data Science Friendly
5. Works with Pandas

Applications:

1. Data Analysis
2. Machine Learning
3. Business Analytics
4. Research Projects
5. Exploratory Data Analysis (EDA)

Import Statement:

import seaborn as sns
"""

# ======================================
# CHECK SEABORN VERSION
# ======================================

print("\n1. SEABORN VERSION")

print(
    "Version:",
    sns.__version__
)

# ======================================
# LOAD SAMPLE DATASET
# ======================================

print("\n2. LOAD DATASET")

tips = sns.load_dataset(
    "tips"
)

print(
    tips.head()
)

# ======================================
# DATASET INFORMATION
# ======================================

print("\n3. DATASET INFO")

print(
    tips.info()
)

# ======================================
# DESCRIPTIVE STATISTICS
# ======================================

print("\n4. DESCRIPTIVE STATISTICS")

print(
    tips.describe()
)

# ======================================
# SIMPLE SCATTER PLOT
# ======================================

print("\n5. SIMPLE SCATTER PLOT")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title(
    "Total Bill vs Tip"
)

plt.show()

# ======================================
# SIMPLE LINE PLOT
# ======================================

print("\n6. SIMPLE LINE PLOT")

sns.lineplot(
    data=tips,
    x="size",
    y="tip"
)

plt.title(
    "Group Size vs Tip"
)

plt.show()

# ======================================
# SIMPLE HISTOGRAM
# ======================================

print("\n7. HISTOGRAM")

sns.histplot(
    data=tips,
    x="total_bill"
)

plt.title(
    "Total Bill Distribution"
)

plt.show()

# ======================================
# SIMPLE BAR PLOT
# ======================================

print("\n8. BAR PLOT")

sns.barplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title(
    "Average Bill by Day"
)

plt.show()

# ======================================
# SIMPLE BOX PLOT
# ======================================

print("\n9. BOX PLOT")

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title(
    "Bill Distribution by Day"
)

plt.show()

# ======================================
# COUNT PLOT
# ======================================

print("\n10. COUNT PLOT")

sns.countplot(
    data=tips,
    x="day"
)

plt.title(
    "Customer Count by Day"
)

plt.show()

# ======================================
# STYLE SETTINGS
# ======================================

print("\n11. STYLE SETTINGS")

sns.set_style(
    "darkgrid"
)

sns.lineplot(
    data=tips,
    x="size",
    y="total_bill"
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# COLOR PALETTES
# ======================================

print("\n12. COLOR PALETTES")

sns.set_palette(
    "deep"
)

sns.barplot(
    data=tips,
    x="day",
    y="tip"
)

plt.title(
    "Color Palette Example"
)

plt.show()

# ======================================
# USER DATA EXAMPLE
# ======================================

print("\n13. USER DATA")

student_data = pd.DataFrame(
    {
        "Student": [
            "A",
            "B",
            "C",
            "D",
            "E"
        ],
        "Marks": [
            85,
            92,
            78,
            95,
            88
        ]
    }
)

print(student_data)

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Student Marks"
)

plt.show()

# ======================================
# MINI PROJECT
# ======================================

print("\n14. MINI PROJECT")

students = pd.DataFrame(
    {
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
        ]
    }
)

print(students)

print(
    "\nAverage Marks:",
    students["Math"].mean()
)

sns.barplot(
    data=students,
    x="Name",
    y="Math"
)

plt.title(
    "Student Performance"
)

plt.show()

# ======================================
# IMPORTANT SEABORN FUNCTIONS
# ======================================

"""
sns.lineplot()
sns.barplot()
sns.scatterplot()
sns.histplot()
sns.boxplot()
sns.countplot()
sns.heatmap()
sns.pairplot()
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Install Seaborn and
check its version.

Exercise 2:
Load tips dataset and
display first 5 rows.

Exercise 3:
Create:

- Scatter Plot
- Bar Plot

Exercise 4:
Change chart style.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Seaborn?

Q2. Why is Seaborn used?

Q3. Difference between
Matplotlib and Seaborn?

Q4. What is a statistical
visualization library?

Q5. What is sns.load_dataset()?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Dataset.

Columns:

1. Name
2. Marks
3. Attendance

Create:

- Bar Plot
- Scatter Plot
- Histogram

Analyze performance.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 071 Completed Successfully!"
)