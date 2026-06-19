# ======================================
# Day 012: Tuples
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Tuples and Tuple
# Operations in Python
# ======================================

print("=" * 50)
print("DAY 012 - TUPLES")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Tuple?

A tuple is an ordered collection of items.

Tuples are:

1. Ordered
2. Immutable
3. Allow Duplicate Values
4. Faster than Lists

Syntax:

tuple_name = (item1, item2, item3)

Example:

subjects = ("Python", "DBMS", "Statistics")

Important:

Unlike lists, tuples cannot be modified
after creation.
"""

# ======================================
# 1. CREATING A TUPLE
# ======================================

print("\n1. CREATING A TUPLE")

subjects = (
    "Python",
    "DBMS",
    "Statistics",
    "Mathematics"
)

print(subjects)

# ======================================
# 2. TUPLE DATA TYPE
# ======================================

print("\n2. TUPLE DATA TYPE")

numbers = (10, 20, 30)

print("Tuple:", numbers)
print("Type :", type(numbers))

# ======================================
# 3. ACCESSING ELEMENTS
# ======================================

print("\n3. ACCESSING ELEMENTS")

fruits = (
    "Apple",
    "Banana",
    "Mango",
    "Orange"
)

print("First Fruit :", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit  :", fruits[-1])

# ======================================
# 4. TUPLE LENGTH
# ======================================

print("\n4. TUPLE LENGTH")

students = (
    "Saloni",
    "Riya",
    "Ankit",
    "Priya"
)

print("Total Students:", len(students))

# ======================================
# 5. ITERATING THROUGH A TUPLE
# ======================================

print("\n5. ITERATING THROUGH A TUPLE")

subjects = (
    "Python",
    "DBMS",
    "Statistics"
)

for subject in subjects:
    print(subject)

# ======================================
# 6. MEMBERSHIP OPERATORS
# ======================================

print("\n6. MEMBERSHIP OPERATORS")

subjects = (
    "Python",
    "DBMS",
    "Statistics"
)

print("Python" in subjects)
print("Java" in subjects)

# ======================================
# 7. COUNT METHOD
# ======================================

print("\n7. count() METHOD")

numbers = (
    10,
    20,
    10,
    30,
    10,
    40
)

print("Count of 10:", numbers.count(10))

# ======================================
# 8. INDEX METHOD
# ======================================

print("\n8. index() METHOD")

subjects = (
    "Python",
    "DBMS",
    "Statistics"
)

print("Index of DBMS:", subjects.index("DBMS"))

# ======================================
# 9. TUPLE PACKING
# ======================================

print("\n9. TUPLE PACKING")

student = (
    "Saloni Tiwari",
    17,
    "Data Science"
)

print(student)

# ======================================
# 10. TUPLE UNPACKING
# ======================================

print("\n10. TUPLE UNPACKING")

name, age, course = student

print("Name  :", name)
print("Age   :", age)
print("Course:", course)

# ======================================
# 11. SINGLE ELEMENT TUPLE
# ======================================

print("\n11. SINGLE ELEMENT TUPLE")

single_value = (100,)

print(single_value)
print(type(single_value))

# ======================================
# 12. NESTED TUPLE
# ======================================

print("\n12. NESTED TUPLE")

student_record = (
    ("Saloni", 95),
    ("Riya", 88),
    ("Ankit", 91)
)

print(student_record)

# ======================================
# 13. MINI PROJECT
# ======================================

print("\n13. MINI PROJECT - STUDENT RECORD")

student = (
    "Saloni Tiwari",
    17,
    "BS in Data Science",
    3,
    8.75
)

print("\nStudent Information")
print("-" * 30)

print("Name     :", student[0])
print("Age      :", student[1])
print("Course   :", student[2])
print("Semester :", student[3])
print("CGPA     :", student[4])

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a tuple containing
your favourite subjects.

Print:
- Complete Tuple
- First Subject
- Last Subject

Exercise 2:
Create a tuple of numbers.

Find:
- Length
- Count of a number
- Index of a number

Exercise 3:
Create a student tuple and
perform tuple unpacking.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Result System.

Store the following in a tuple:

- Name
- Roll Number
- Mathematics Marks
- Python Marks
- DBMS Marks

Calculate:

1. Total Marks
2. Average Marks

Display all details neatly.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 012 Completed Successfully!")