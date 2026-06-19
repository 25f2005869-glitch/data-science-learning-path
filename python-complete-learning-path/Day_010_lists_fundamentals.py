# ======================================
# Day 010: Lists Fundamentals
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Lists and Basic
# List Operations in Python
# ======================================

print("=" * 50)
print("DAY 010 - LISTS FUNDAMENTALS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a List?

A list is an ordered collection of items.

Lists are:

1. Ordered
2. Mutable
3. Allow Duplicate Values
4. Can Store Multiple Data Types

Syntax:

list_name = [item1, item2, item3]

Examples:

numbers = [10, 20, 30]
names = ["Saloni", "Riya", "Ankit"]

Lists are one of the most important
data structures in Python.
"""

# ======================================
# 1. CREATING A LIST
# ======================================

print("\n1. CREATING A LIST")

subjects = [
    "Python",
    "Statistics",
    "DBMS",
    "Mathematics"
]

print(subjects)

# ======================================
# 2. LIST DATA TYPE
# ======================================

print("\n2. LIST DATA TYPE")

numbers = [10, 20, 30, 40]

print("List :", numbers)
print("Type :", type(numbers))

# ======================================
# 3. ACCESSING LIST ELEMENTS
# ======================================

print("\n3. ACCESSING LIST ELEMENTS")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("First Item :", fruits[0])
print("Second Item:", fruits[1])
print("Last Item  :", fruits[-1])

# ======================================
# 4. LIST LENGTH
# ======================================

print("\n4. LIST LENGTH")

students = ["Saloni", "Riya", "Ankit", "Priya"]

print("Total Students:", len(students))

# ======================================
# 5. LIST WITH DIFFERENT DATA TYPES
# ======================================

print("\n5. MIXED DATA TYPES")

student_profile = [
    "Saloni Tiwari",
    17,
    5.35,
    True
]

print(student_profile)

# ======================================
# 6. ITERATING THROUGH A LIST
# ======================================

print("\n6. ITERATING THROUGH A LIST")

subjects = [
    "Python",
    "DBMS",
    "Statistics",
    "Mathematics"
]

for subject in subjects:
    print(subject)

# ======================================
# 7. CHECKING MEMBERSHIP
# ======================================

print("\n7. MEMBERSHIP OPERATORS")

subjects = [
    "Python",
    "DBMS",
    "Statistics"
]

print("Python" in subjects)
print("Java" in subjects)

# ======================================
# 8. MODIFYING LIST ELEMENTS
# ======================================

print("\n8. MODIFYING LIST ELEMENTS")

subjects = [
    "Python",
    "DBMS",
    "Statistics"
]

print("Before:", subjects)

subjects[1] = "Machine Learning"

print("After :", subjects)

# ======================================
# 9. SIMPLE USER INPUT LIST
# ======================================

print("\n9. USER INPUT LIST")

subject1 = input("Enter Subject 1: ")
subject2 = input("Enter Subject 2: ")
subject3 = input("Enter Subject 3: ")

subject_list = [subject1, subject2, subject3]

print("Subjects:", subject_list)

# ======================================
# 10. MINI PROJECT
# ======================================

print("\n10. MINI PROJECT - MARKS ANALYZER")

marks = [85, 90, 78, 92, 88]

print("Marks:", marks)

total_marks = sum(marks)
average_marks = total_marks / len(marks)

print("Total Marks  :", total_marks)
print("Average Marks:", average_marks)
print("Highest Mark :", max(marks))
print("Lowest Mark  :", min(marks))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a list containing
your favourite subjects.

Print:
- Complete List
- First Subject
- Last Subject

Exercise 2:
Create a list of five numbers.

Find:
- Sum
- Maximum
- Minimum

Exercise 3:
Take three city names from
the user and store them in a list.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Marks System.

Store marks of 5 subjects in a list.

Calculate:

1. Total Marks
2. Average Marks
3. Highest Marks
4. Lowest Marks

Display all results neatly.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 010 Completed Successfully!")