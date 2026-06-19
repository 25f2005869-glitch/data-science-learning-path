# ======================================
# Day 019: Modules and Imports
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Modules and Import
# Statements in Python
# ======================================

print("=" * 50)
print("DAY 019 - MODULES AND IMPORTS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Module?

A module is a Python file containing
functions, variables, and classes that
can be reused in other programs.

Benefits of Modules:

1. Code Reusability
2. Better Organization
3. Easy Maintenance
4. Modular Programming

Common Built-in Modules:

1. math
2. random
3. datetime
4. os
5. statistics

Import Syntax:

import module_name

from module_name import function_name
"""

# ======================================
# 1. IMPORTING A MODULE
# ======================================

print("\n1. IMPORTING A MODULE")

import math

print("Square Root of 25:", math.sqrt(25))
print("Value of Pi      :", math.pi)

# ======================================
# 2. USING math MODULE
# ======================================

print("\n2. USING math MODULE")

number = 16

print("Square Root:", math.sqrt(number))
print("Power      :", math.pow(2, 5))
print("Factorial  :", math.factorial(5))

# ======================================
# 3. IMPORTING SPECIFIC FUNCTIONS
# ======================================

print("\n3. IMPORTING SPECIFIC FUNCTIONS")

from math import sqrt, factorial

print("Square Root:", sqrt(49))
print("Factorial  :", factorial(6))

# ======================================
# 4. USING ALIAS
# ======================================

print("\n4. USING ALIAS")

import math as m

print("Pi Value:", m.pi)

# ======================================
# 5. RANDOM MODULE
# ======================================

print("\n5. RANDOM MODULE")

import random

print("Random Number:", random.randint(1, 10))

# ======================================
# 6. RANDOM CHOICE
# ======================================

print("\n6. RANDOM CHOICE")

subjects = [
    "Python",
    "DBMS",
    "Statistics",
    "Mathematics"
]

print("Selected Subject:")
print(random.choice(subjects))

# ======================================
# 7. DATETIME MODULE
# ======================================

print("\n7. DATETIME MODULE")

import datetime

today = datetime.datetime.now()

print("Current Date and Time:")
print(today)

# ======================================
# 8. STATISTICS MODULE
# ======================================

print("\n8. STATISTICS MODULE")

import statistics

marks = [85, 90, 78, 92, 88]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))

# ======================================
# 9. CREATING YOUR OWN MODULE
# ======================================

print("\n9. CUSTOM MODULE (EXAMPLE)")

"""
File: my_module.py

def greet():
    print("Welcome to Python")

---------------------------------

Main File:

import my_module

my_module.greet()
"""

print("Custom Module Example Shown")

# ======================================
# 10. dir() FUNCTION
# ======================================

print("\n10. dir() FUNCTION")

print(dir(math)[:10])

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

number = int(input("Enter a number: "))

print("Square Root:", math.sqrt(number))

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT - STUDENT ANALYZER")

student_marks = [92, 95, 90, 88, 94]

print("Marks :", student_marks)

print("Average :", statistics.mean(student_marks))
print("Highest :", max(student_marks))
print("Lowest  :", min(student_marks))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Import the math module and find:

- Square Root of 64
- Factorial of 7

Exercise 2:
Generate a random number
between 1 and 100.

Exercise 3:
Display the current date
using datetime module.

Exercise 4:
Find the mean of a list
using statistics module.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Result Analyzer.

Requirements:

1. Store marks in a list.
2. Use statistics module to find:
   - Mean
   - Median
3. Find:
   - Highest Marks
   - Lowest Marks
4. Display a complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 019 Completed Successfully!")