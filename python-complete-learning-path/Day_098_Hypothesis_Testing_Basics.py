# ======================================
# Day 098: Hypothesis Testing Basics
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Hypothesis Testing
# in Statistics
# ======================================

print("=" * 60)
print("DAY 098 - HYPOTHESIS TESTING BASICS")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

from statistics import mean

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Hypothesis Testing?

Hypothesis Testing is a statistical
method used to make decisions
about a population using sample data.

Applications:

1. Data Science
2. Machine Learning
3. Medical Research
4. Business Analytics
5. Scientific Research

Key Concepts:

1. Null Hypothesis (H0)
2. Alternative Hypothesis (H1)
3. Significance Level
4. Decision Making
"""

# ======================================
# NULL HYPOTHESIS
# ======================================

print("\nNULL HYPOTHESIS (H0)")

"""
H0:

No Effect
No Difference
No Change

Example:

Average Marks = 80
"""

print(
    "H0: Average Marks = 80"
)

# ======================================
# ALTERNATIVE HYPOTHESIS
# ======================================

print("\nALTERNATIVE HYPOTHESIS (H1)")

"""
H1:

Effect Exists
Difference Exists
Change Exists

Example:

Average Marks ≠ 80
"""

print(
    "H1: Average Marks != 80"
)

# ======================================
# SAMPLE DATASET
# ======================================

marks = [
    82,
    85,
    88,
    90,
    84
]

print("\nSAMPLE DATA")
print(marks)

# ======================================
# SAMPLE MEAN
# ======================================

sample_mean = mean(
    marks
)

print(
    "Sample Mean:",
    round(
        sample_mean,
        2
    )
)

# ======================================
# HYPOTHESIS COMPARISON
# ======================================

print("\nHYPOTHESIS COMPARISON")

hypothesized_mean = 80

print(
    "Hypothesized Mean:",
    hypothesized_mean
)

print(
    "Sample Mean:",
    round(
        sample_mean,
        2
    )
)

# ======================================
# SIMPLE DECISION
# ======================================

print("\nDECISION")

if sample_mean > hypothesized_mean:

    print(
        "Evidence suggests "
        "sample mean is higher."
    )

else:

    print(
        "No evidence found."
    )

# ======================================
# SIGNIFICANCE LEVEL
# ======================================

print("\nSIGNIFICANCE LEVEL")

alpha = 0.05

print(
    "Alpha:",
    alpha
)

"""
Common Values:

0.05
0.01
"""

# ======================================
# BUSINESS EXAMPLE
# ======================================

print("\nBUSINESS EXAMPLE")

sales = [
    100,
    120,
    130,
    140,
    150
]

sales_mean = mean(
    sales
)

print(
    "Average Sales:",
    round(
        sales_mean,
        2
    )
)

# ======================================
# EDUCATION EXAMPLE
# ======================================

print("\nEDUCATION EXAMPLE")

attendance = [
    85,
    88,
    90,
    92,
    95
]

attendance_mean = mean(
    attendance
)

print(
    "Average Attendance:",
    round(
        attendance_mean,
        2
    )
)

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

num1 = int(
    input(
        "Enter Marks 1: "
    )
)

num2 = int(
    input(
        "Enter Marks 2: "
    )
)

num3 = int(
    input(
        "Enter Marks 3: "
    )
)

user_marks = [
    num1,
    num2,
    num3
]

user_mean = mean(
    user_marks
)

print(
    "Mean:",
    round(
        user_mean,
        2
    )
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

student_scores = [
    75,
    80,
    85,
    90,
    95
]

project_mean = mean(
    student_scores
)

print(
    "Scores:",
    student_scores
)

print(
    "Mean:",
    round(
        project_mean,
        2
    )
)

if project_mean >= 80:

    print(
        "Performance Above Benchmark"
    )

else:

    print(
        "Performance Below Benchmark"
    )

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Null Hypothesis (H0)

Alternative Hypothesis (H1)

Sample

Population

Significance Level

Decision Rule
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Define H0.

Exercise 2:
Define H1.

Exercise 3:
Calculate Sample Mean.

Exercise 4:
Compare with Benchmark.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Hypothesis Testing?

Q2. What is Null Hypothesis?

Q3. What is Alternative Hypothesis?

Q4. What is Alpha?

Q5. Why is Hypothesis Testing
important?

Q6. Difference between
Population and Sample?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Evaluation System.

Input:

1. Student Marks

Generate:

1. Sample Mean
2. Compare with Benchmark

Decision:

Above or Below Benchmark
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 098 Completed Successfully!"
)