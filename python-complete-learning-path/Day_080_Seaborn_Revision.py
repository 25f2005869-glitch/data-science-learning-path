# ======================================
# Day 080: Seaborn Revision
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Complete Revision of Seaborn
# for Data Visualization
# ======================================

print("=" * 60)
print("DAY 080 - SEABORN REVISION")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ======================================
# REVISION NOTES
# ======================================

"""
SEABORN REVISION CHEAT SHEET

Seaborn is a statistical
data visualization library
built on top of Matplotlib.

Topics Covered:

Day 071 : Introduction
Day 072 : Line Plots
Day 073 : Bar Plots
Day 074 : Histograms
Day 075 : Box Plots
Day 076 : Scatter Plots
Day 077 : Heatmaps
Day 078 : Pairplots
Day 079 : Visualization Project

Main Library:

import seaborn as sns
"""

# ======================================
# SAMPLE DATASET
# ======================================

student_data = pd.DataFrame(
    {
        "Student": [
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
        ],

        "Attendance": [
            95,
            88,
            97,
            82,
            91
        ],

        "Study_Hours": [
            8,
            6,
            9,
            5,
            7
        ]
    }
)

print("\nDATASET")
print(student_data)

# ======================================
# 1. LINE PLOT REVISION
# ======================================

print("\n1. LINE PLOT")

sns.lineplot(
    data=student_data,
    x="Student",
    y="Marks",
    marker="o"
)

plt.title(
    "Line Plot"
)

plt.show()

# ======================================
# 2. BAR PLOT REVISION
# ======================================

print("\n2. BAR PLOT")

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Bar Plot"
)

plt.show()

# ======================================
# 3. HISTOGRAM REVISION
# ======================================

print("\n3. HISTOGRAM")

sns.histplot(
    data=student_data,
    x="Marks",
    kde=True
)

plt.title(
    "Histogram"
)

plt.show()

# ======================================
# 4. BOX PLOT REVISION
# ======================================

print("\n4. BOX PLOT")

sns.boxplot(
    data=student_data,
    y="Marks"
)

plt.title(
    "Box Plot"
)

plt.show()

# ======================================
# 5. SCATTER PLOT REVISION
# ======================================

print("\n5. SCATTER PLOT")

sns.scatterplot(
    data=student_data,
    x="Study_Hours",
    y="Marks"
)

plt.title(
    "Scatter Plot"
)

plt.show()

# ======================================
# 6. HEATMAP REVISION
# ======================================

print("\n6. HEATMAP")

correlation = student_data[
    [
        "Marks",
        "Attendance",
        "Study_Hours"
    ]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Heatmap"
)

plt.show()

# ======================================
# 7. PAIRPLOT REVISION
# ======================================

print("\n7. PAIRPLOT")

sns.pairplot(
    student_data[
        [
            "Marks",
            "Attendance",
            "Study_Hours"
        ]
    ]
)

plt.show()

# ======================================
# 8. STYLE SETTINGS
# ======================================

print("\n8. STYLE SETTINGS")

sns.set_style(
    "darkgrid"
)

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Dark Grid Style"
)

plt.show()

# ======================================
# 9. COLOR PALETTES
# ======================================

print("\n9. COLOR PALETTES")

sns.set_palette(
    "deep"
)

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Color Palette"
)

plt.show()

# ======================================
# 10. SAVE CHART
# ======================================

print("\n10. SAVE CHART")

sns.barplot(
    data=student_data,
    x="Student",
    y="Marks"
)

plt.title(
    "Saved Chart"
)

plt.savefig(
    "seaborn_revision_chart.png"
)

plt.close()

print(
    "Chart Saved Successfully"
)

# ======================================
# IMPORTANT FUNCTIONS
# ======================================

"""
sns.lineplot()
sns.barplot()
sns.histplot()
sns.boxplot()
sns.scatterplot()
sns.heatmap()
sns.pairplot()

sns.set_style()
sns.set_palette()
sns.load_dataset()
"""

# ======================================
# STUDENT ANALYSIS
# ======================================

print("\nSTUDENT ANALYSIS")

print(
    "Highest Marks:",
    student_data["Marks"].max()
)

print(
    "Lowest Marks:",
    student_data["Marks"].min()
)

print(
    "Average Marks:",
    round(
        student_data["Marks"].mean(),
        2
    )
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

correlation = student_data[
    [
        "Marks",
        "Attendance",
        "Study_Hours"
    ]
].corr()

sns.heatmap(
    correlation,
    annot=True
)

plt.title(
    "Student Dashboard"
)

plt.show()

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Seaborn?

Q2. Difference between
Matplotlib and Seaborn?

Q3. What is Pairplot?

Q4. What is Heatmap?

Q5. What is Correlation?

Q6. What is KDE?

Q7. What is a Box Plot?

Q8. What is EDA?

Q9. Why use Histograms?

Q10. What is sns.load_dataset()?
"""

# ======================================
# PRACTICE QUESTIONS
# ======================================

"""
Practice 1:
Create a Line Plot.

Practice 2:
Create a Bar Plot.

Practice 3:
Create a Histogram.

Practice 4:
Create a Box Plot.

Practice 5:
Create a Scatter Plot.

Practice 6:
Create a Heatmap.

Practice 7:
Create a Pairplot.
"""

# ======================================
# FINAL CHEAT SHEET
# ======================================

"""
Line Plot     -> Trends

Bar Plot      -> Comparison

Histogram     -> Distribution

Box Plot      -> Outliers

Scatter Plot  -> Relationships

Heatmap       -> Correlation

Pairplot      -> Multi-variable EDA

Seaborn       -> Statistical
                 Visualization
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a College Analytics Dashboard.

Dataset:

1. Marks
2. Attendance
3. Study Hours

Generate:

1. Line Plot
2. Bar Plot
3. Histogram
4. Box Plot
5. Scatter Plot
6. Heatmap
7. Pairplot

Perform complete EDA.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 080 Completed Successfully!"
)