# ======================================
# Day 045: NumPy Statistical Functions
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Statistical Functions
# in NumPy for Data Analysis
# ======================================

print("=" * 50)
print("DAY 045 - NUMPY STATISTICAL FUNCTIONS")
print("=" * 50)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Statistical Functions are used to
analyze numerical data efficiently.

Common Statistical Functions:

1. np.sum()
2. np.mean()
3. np.median()
4. np.min()
5. np.max()
6. np.std()
7. np.var()
8. np.percentile()
9. np.argmin()
10. np.argmax()

Applications:

1. Data Analysis
2. Machine Learning
3. Business Analytics
4. Scientific Research
"""

# ======================================
# 1. SAMPLE DATA
# ======================================

print("\n1. SAMPLE DATA")

marks = np.array(
    [92, 85, 78, 95, 88]
)

print("Marks:", marks)

# ======================================
# 2. SUM
# ======================================

print("\n2. SUM")

print("Total Marks:",
      np.sum(marks))

# ======================================
# 3. MEAN
# ======================================

print("\n3. MEAN")

print("Average Marks:",
      np.mean(marks))

# ======================================
# 4. MEDIAN
# ======================================

print("\n4. MEDIAN")

print("Median:",
      np.median(marks))

# ======================================
# 5. MAXIMUM VALUE
# ======================================

print("\n5. MAXIMUM")

print("Highest Marks:",
      np.max(marks))

# ======================================
# 6. MINIMUM VALUE
# ======================================

print("\n6. MINIMUM")

print("Lowest Marks:",
      np.min(marks))

# ======================================
# 7. STANDARD DEVIATION
# ======================================

print("\n7. STANDARD DEVIATION")

print("Standard Deviation:",
      np.std(marks))

# ======================================
# 8. VARIANCE
# ======================================

print("\n8. VARIANCE")

print("Variance:",
      np.var(marks))

# ======================================
# 9. PERCENTILE
# ======================================

print("\n9. PERCENTILE")

print("25th Percentile:",
      np.percentile(marks, 25))

print("50th Percentile:",
      np.percentile(marks, 50))

print("75th Percentile:",
      np.percentile(marks, 75))

# ======================================
# 10. INDEX OF MAXIMUM
# ======================================

print("\n10. ARGMAX")

print("Highest Marks Index:",
      np.argmax(marks))

# ======================================
# 11. INDEX OF MINIMUM
# ======================================

print("\n11. ARGMIN")

print("Lowest Marks Index:",
      np.argmin(marks))

# ======================================
# 12. RANGE
# ======================================

print("\n12. RANGE")

data_range = (
    np.max(marks) -
    np.min(marks)
)

print("Range:", data_range)

# ======================================
# 13. SORTED DATA
# ======================================

print("\n13. SORTED DATA")

print(np.sort(marks))

# ======================================
# 14. 2D ARRAY STATISTICS
# ======================================

print("\n14. 2D ARRAY STATISTICS")

student_marks = np.array(
    [
        [92, 85, 78],
        [95, 88, 90]
    ]
)

print(student_marks)

print("Total:",
      np.sum(student_marks))

print("Average:",
      np.mean(student_marks))

# ======================================
# 15. ROW-WISE SUM
# ======================================

print("\n15. ROW-WISE SUM")

print(
    np.sum(
        student_marks,
        axis=1
    )
)

# ======================================
# 16. COLUMN-WISE SUM
# ======================================

print("\n16. COLUMN-WISE SUM")

print(
    np.sum(
        student_marks,
        axis=0
    )
)

# ======================================
# 17. USER INPUT EXAMPLE
# ======================================

print("\n17. USER INPUT EXAMPLE")

numbers = input(
    "Enter numbers separated by spaces: "
).split()

numbers = np.array(
    numbers,
    dtype=float
)

print("Numbers:", numbers)

print("Mean:",
      np.mean(numbers))

print("Median:",
      np.median(numbers))

# ======================================
# 18. MINI PROJECT
# ======================================

print("\n18. MINI PROJECT - STUDENT ANALYZER")

marks = np.array(
    [92, 85, 78, 95, 88]
)

print("Marks:", marks)

print("Total      :",
      np.sum(marks))

print("Average    :",
      round(np.mean(marks), 2))

print("Median     :",
      np.median(marks))

print("Highest    :",
      np.max(marks))

print("Lowest     :",
      np.min(marks))

print("Std Dev    :",
      round(np.std(marks), 2))

print("Variance   :",
      round(np.var(marks), 2))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create an array and find:

- Sum
- Mean
- Median

Exercise 2:
Find:

- Maximum
- Minimum
- Range

Exercise 3:
Calculate:

- Variance
- Standard Deviation

Exercise 4:
Find 25th, 50th,
and 75th percentiles.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Performance Analyzer.

Store marks of 10 students.

Calculate:

1. Total Marks
2. Average Marks
3. Median
4. Highest Marks
5. Lowest Marks
6. Variance
7. Standard Deviation
8. Range

Display a complete statistical report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 045 Completed Successfully!")