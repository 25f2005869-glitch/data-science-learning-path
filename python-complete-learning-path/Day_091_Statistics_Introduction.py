# ======================================
# Day 091: Statistics Introduction
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Statistics for
# Data Science and Machine Learning
# ======================================

print("=" * 60)
print("DAY 091 - STATISTICS INTRODUCTION")
print("=" * 60)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Statistics?

Statistics is the science of
collecting, organizing,
analyzing, interpreting,
and presenting data.

Why Statistics?

Statistics helps us:

1. Understand Data
2. Make Decisions
3. Identify Patterns
4. Predict Outcomes
5. Build ML Models

Applications:

1. Data Science
2. Machine Learning
3. Business Analytics
4. Economics
5. Research
6. Artificial Intelligence

Examples:

- Average student marks
- Election predictions
- Weather forecasting
- Sales analysis
- Medical research
"""

# ======================================
# TYPES OF STATISTICS
# ======================================

print("\nTYPES OF STATISTICS")

print(
    """
1. Descriptive Statistics
   - Summarizes data

2. Inferential Statistics
   - Makes predictions
     about a population
   """
)

# ======================================
# DESCRIPTIVE STATISTICS
# ======================================

print("\nDESCRIPTIVE STATISTICS")

"""
Examples:

1. Mean
2. Median
3. Mode
4. Variance
5. Standard Deviation
"""

marks = [
    85,
    90,
    78,
    92,
    88
]

print(
    "Sample Marks:",
    marks
)

# ======================================
# POPULATION VS SAMPLE
# ======================================

print("\nPOPULATION VS SAMPLE")

"""
Population:
Entire Group

Sample:
Subset of Population

Example:

Population:
All IITM Students

Sample:
100 IITM Students
"""

population = 10000
sample = 100

print(
    "Population Size:",
    population
)

print(
    "Sample Size:",
    sample
)

# ======================================
# DATA TYPES
# ======================================

print("\nDATA TYPES")

print(
    """
1. Qualitative Data
   Example:
   Gender, City, Color

2. Quantitative Data
   Example:
   Marks, Salary, Age
   """
)

# ======================================
# QUALITATIVE DATA
# ======================================

print("\nQUALITATIVE DATA")

cities = [
    "Delhi",
    "Patna",
    "Mumbai",
    "Kolkata"
]

print(cities)

# ======================================
# QUANTITATIVE DATA
# ======================================

print("\nQUANTITATIVE DATA")

ages = [
    18,
    20,
    22,
    24,
    26
]

print(ages)

# ======================================
# DATA COLLECTION METHODS
# ======================================

print("\nDATA COLLECTION METHODS")

methods = [
    "Survey",
    "Interview",
    "Observation",
    "Experiment"
]

for method in methods:
    print(method)

# ======================================
# REAL-WORLD DATASET
# ======================================

print("\nREAL-WORLD EXAMPLE")

student_marks = [
    92,
    88,
    95,
    81,
    90
]

print(
    "Student Marks:",
    student_marks
)

print(
    "Total Students:",
    len(student_marks)
)

# ======================================
# BASIC ANALYSIS
# ======================================

total_marks = sum(
    student_marks
)

print(
    "Total Marks:",
    total_marks
)

average_marks = (
    total_marks /
    len(student_marks)
)

print(
    "Average Marks:",
    round(
        average_marks,
        2
    )
)

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

student_name = input(
    "Enter Student Name: "
)

student_score = int(
    input(
        "Enter Marks: "
    )
)

print(
    f"{student_name} scored "
    f"{student_score}"
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

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
    "Highest Score:",
    max(scores)
)

print(
    "Lowest Score:",
    min(scores)
)

print(
    "Average Score:",
    round(
        sum(scores) /
        len(scores),
        2
    )
)

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Population

Sample

Variable

Observation

Mean

Median

Mode

Variance

Standard Deviation
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Define Statistics.

Exercise 2:
Explain Population
and Sample.

Exercise 3:
Give examples of:

1. Qualitative Data
2. Quantitative Data

Exercise 4:
Find average marks
for 5 students.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Statistics?

Q2. Why is Statistics
important in Data Science?

Q3. What is Population?

Q4. What is Sample?

Q5. Difference between
Qualitative and
Quantitative Data?

Q6. What is Descriptive
Statistics?

Q7. What is Inferential
Statistics?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Student Statistics System.

Input:

1. Student Name
2. Marks

Generate:

1. Total Marks
2. Average Marks
3. Highest Marks
4. Lowest Marks

Display Summary Report.
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 091 Completed Successfully!"
)