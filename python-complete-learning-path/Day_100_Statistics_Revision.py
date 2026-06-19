# ======================================
# Day 100: Statistics Revision
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Complete Revision of Statistics
# for Data Science and Machine Learning
# ======================================

print("=" * 60)
print("DAY 100 - STATISTICS REVISION")
print("=" * 60)

# ======================================
# IMPORT LIBRARIES
# ======================================

from statistics import (
    mean,
    median,
    mode,
    variance,
    stdev
)

# ======================================
# REVISION NOTES
# ======================================

"""
STATISTICS REVISION

Topics Covered:

Day 091:
Statistics Introduction

Day 092:
Descriptive Statistics

Day 093:
Mean, Median, Mode

Day 094:
Variance and
Standard Deviation

Day 095:
Probability Basics

Day 096:
Data Distributions

Day 097:
Correlation and
Covariance

Day 098:
Hypothesis Testing

Day 099:
Statistics Mini Project
"""

# ======================================
# SAMPLE DATASET
# ======================================

marks = [
    92,
    88,
    95,
    81,
    90,
    85,
    87,
    91,
    89,
    93
]

print("\nDATASET")
print(marks)

# ======================================
# DESCRIPTIVE STATISTICS
# ======================================

print("\nDESCRIPTIVE STATISTICS")

print(
    "Count:",
    len(marks)
)

print(
    "Sum:",
    sum(marks)
)

print(
    "Minimum:",
    min(marks)
)

print(
    "Maximum:",
    max(marks)
)

print(
    "Range:",
    max(marks)
    -
    min(marks)
)

# ======================================
# MEAN
# ======================================

print("\nMEAN")

mean_value = mean(
    marks
)

print(
    "Mean:",
    round(
        mean_value,
        2
    )
)

# ======================================
# MEDIAN
# ======================================

print("\nMEDIAN")

median_value = median(
    marks
)

print(
    "Median:",
    median_value
)

# ======================================
# MODE
# ======================================

print("\nMODE")

mode_data = [
    90,
    90,
    88,
    92,
    90,
    85
]

print(
    "Mode:",
    mode(
        mode_data
    )
)

# ======================================
# VARIANCE
# ======================================

print("\nVARIANCE")

variance_value = variance(
    marks
)

print(
    "Variance:",
    round(
        variance_value,
        2
    )
)

# ======================================
# STANDARD DEVIATION
# ======================================

print("\nSTANDARD DEVIATION")

std_value = stdev(
    marks
)

print(
    "Standard Deviation:",
    round(
        std_value,
        2
    )
)

# ======================================
# PROBABILITY
# ======================================

print("\nPROBABILITY")

favorable = 1
total = 6

probability = (
    favorable /
    total
)

print(
    "Probability of Dice 1:",
    round(
        probability,
        4
    )
)

# ======================================
# DISTRIBUTION EXAMPLE
# ======================================

print("\nDATA DISTRIBUTION")

distribution = [
    70,
    75,
    80,
    85,
    90,
    95
]

print(
    distribution
)

print(
    "Mean:",
    round(
        mean(distribution),
        2
    )
)

# ======================================
# CORRELATION EXAMPLE
# ======================================

print("\nCORRELATION EXAMPLE")

study_hours = [
    1,
    2,
    3,
    4,
    5
]

student_marks = [
    50,
    60,
    70,
    80,
    90
]

print(
    "Study Hours:",
    study_hours
)

print(
    "Marks:",
    student_marks
)

print(
    "Positive Correlation"
)

# ======================================
# HYPOTHESIS TESTING
# ======================================

print("\nHYPOTHESIS TESTING")

print(
    "H0: Average Marks = 80"
)

print(
    "H1: Average Marks != 80"
)

# ======================================
# PERFORMANCE REPORT
# ======================================

print("\nPERFORMANCE REPORT")

if mean_value >= 90:

    print(
        "Excellent Performance"
    )

elif mean_value >= 80:

    print(
        "Good Performance"
    )

else:

    print(
        "Needs Improvement"
    )

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

name = input(
    "Enter Student Name: "
)

score = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"{name} scored {score}"
)

# ======================================
# FINAL MINI PROJECT
# ======================================

print("\nFINAL MINI PROJECT")

scores = [
    75,
    80,
    85,
    90,
    95
]

print(
    "Scores:",
    scores
)

print(
    "Mean:",
    round(
        mean(scores),
        2
    )
)

print(
    "Median:",
    median(scores)
)

print(
    "Variance:",
    round(
        variance(scores),
        2
    )
)

print(
    "Standard Deviation:",
    round(
        stdev(scores),
        2
    )
)

# ======================================
# CHEAT SHEET
# ======================================

"""
Mean:
Average

Median:
Middle Value

Mode:
Most Frequent Value

Range:
Max - Min

Variance:
Spread of Data

Standard Deviation:
Square Root of Variance

Probability:
Chance of Event

Correlation:
Relationship Between Variables

Hypothesis Testing:
Decision Making
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Statistics?

Q2. What is Mean?

Q3. What is Median?

Q4. What is Mode?

Q5. What is Variance?

Q6. What is Standard Deviation?

Q7. What is Probability?

Q8. What is Correlation?

Q9. What is Covariance?

Q10. What is Hypothesis Testing?
"""

# ======================================
# NEXT PHASE
# ======================================

"""
Day 101:
Machine Learning Introduction

Day 102:
Types of Machine Learning

Day 103:
Supervised Learning

Day 104:
Linear Regression

Day 105:
Classification Basics
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 100 Completed Successfully!"
)

print(
    "\nCongratulations!"
)

print(
    "Statistics Module Completed."
)