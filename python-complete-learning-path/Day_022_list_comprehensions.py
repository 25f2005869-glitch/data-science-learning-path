# ======================================
# Day 022: List Comprehensions
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding List Comprehensions
# for Efficient List Creation
# ======================================

print("=" * 50)
print("DAY 022 - LIST COMPREHENSIONS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a List Comprehension?

A list comprehension provides a concise
way to create lists in Python.

Traditional Approach:

numbers = []

for i in range(5):
    numbers.append(i)

List Comprehension:

numbers = [i for i in range(5)]

Benefits:

1. Cleaner Code
2. Better Readability
3. Faster Execution
4. Less Code
"""

# ======================================
# 1. BASIC LIST COMPREHENSION
# ======================================

print("\n1. BASIC LIST COMPREHENSION")

numbers = [x for x in range(1, 11)]

print(numbers)

# ======================================
# 2. SQUARES OF NUMBERS
# ======================================

print("\n2. SQUARES OF NUMBERS")

squares = [x ** 2 for x in range(1, 11)]

print(squares)

# ======================================
# 3. CUBES OF NUMBERS
# ======================================

print("\n3. CUBES OF NUMBERS")

cubes = [x ** 3 for x in range(1, 11)]

print(cubes)

# ======================================
# 4. EVEN NUMBERS
# ======================================

print("\n4. EVEN NUMBERS")

even_numbers = [
    x
    for x in range(1, 21)
    if x % 2 == 0
]

print(even_numbers)

# ======================================
# 5. ODD NUMBERS
# ======================================

print("\n5. ODD NUMBERS")

odd_numbers = [
    x
    for x in range(1, 21)
    if x % 2 != 0
]

print(odd_numbers)

# ======================================
# 6. STRING UPPERCASE
# ======================================

print("\n6. STRING UPPERCASE")

subjects = [
    "python",
    "dbms",
    "statistics",
    "mathematics"
]

uppercase_subjects = [
    subject.upper()
    for subject in subjects
]

print(uppercase_subjects)

# ======================================
# 7. STRING LENGTHS
# ======================================

print("\n7. STRING LENGTHS")

subjects = [
    "Python",
    "DBMS",
    "Statistics"
]

lengths = [
    len(subject)
    for subject in subjects
]

print(lengths)

# ======================================
# 8. CONDITIONAL LIST COMPREHENSION
# ======================================

print("\n8. CONDITIONAL LIST COMPREHENSION")

numbers = [1, 2, 3, 4, 5]

result = [
    "Even"
    if number % 2 == 0
    else "Odd"
    for number in numbers
]

print(result)

# ======================================
# 9. NESTED LIST COMPREHENSION
# ======================================

print("\n9. NESTED LIST COMPREHENSION")

matrix = [
    [row * column for column in range(1, 4)]
    for row in range(1, 4)
]

print(matrix)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

numbers = input(
    "Enter numbers separated by spaces: "
).split()

numbers = [int(num) for num in numbers]

print(numbers)

# ======================================
# 11. FILTERING MARKS
# ======================================

print("\n11. FILTERING MARKS")

marks = [92, 45, 78, 35, 88, 95, 50]

passed_students = [
    mark
    for mark in marks
    if mark >= 40
]

print("Passed Marks:", passed_students)

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT - STUDENT ANALYZER")

marks = [92, 85, 78, 95, 88]

grades = [
    "Pass"
    if mark >= 40
    else "Fail"
    for mark in marks
]

print("Marks :", marks)
print("Grades:", grades)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a list of numbers
from 1 to 20 using list
comprehension.

Exercise 2:
Create a list containing
squares of numbers from
1 to 10.

Exercise 3:
Create a list of all
even numbers from 1 to 50.

Exercise 4:
Convert a list of names
to uppercase using list
comprehension.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Marks Processing System.

Store marks in a list.

Using List Comprehension:

1. Create a list of passed marks
2. Create a list of failed marks
3. Create a grade list:
   Pass if marks >= 40
   Fail otherwise
4. Create a list of bonus marks
   (marks + 5)

Display all results neatly.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 022 Completed Successfully!")