# ======================================
# Day 021: List Slicing and Indexing
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding List Indexing and
# Slicing Techniques in Python
# ======================================

print("=" * 50)
print("DAY 021 - LIST SLICING AND INDEXING")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Indexing:

Indexing is used to access individual
elements of a list.

Positive Indexing:

0, 1, 2, 3, ...

Negative Indexing:

-1, -2, -3, ...

--------------------------------------

Slicing:

Slicing is used to extract a portion
of a list.

Syntax:

list[start : stop : step]

Important:

start -> inclusive
stop  -> exclusive
step  -> optional
"""

# ======================================
# 1. LIST INDEXING
# ======================================

print("\n1. LIST INDEXING")

subjects = [
    "Python",
    "DBMS",
    "Statistics",
    "Mathematics",
    "Machine Learning"
]

print("First Subject :", subjects[0])
print("Second Subject:", subjects[1])
print("Last Subject  :", subjects[-1])

# ======================================
# 2. POSITIVE INDEXING
# ======================================

print("\n2. POSITIVE INDEXING")

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[4])

# ======================================
# 3. NEGATIVE INDEXING
# ======================================

print("\n3. NEGATIVE INDEXING")

numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])

# ======================================
# 4. BASIC SLICING
# ======================================

print("\n4. BASIC SLICING")

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[0:3])

# ======================================
# 5. SLICING FROM BEGINNING
# ======================================

print("\n5. SLICING FROM BEGINNING")

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

# ======================================
# 6. SLICING TO THE END
# ======================================

print("\n6. SLICING TO THE END")

numbers = [10, 20, 30, 40, 50]

print(numbers[2:])

# ======================================
# 7. COMPLETE LIST COPY
# ======================================

print("\n7. COMPLETE LIST COPY")

numbers = [10, 20, 30, 40, 50]

copied_list = numbers[:]

print("Original:", numbers)
print("Copied  :", copied_list)

# ======================================
# 8. STEP SLICING
# ======================================

print("\n8. STEP SLICING")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(numbers[::2])
print(numbers[::3])

# ======================================
# 9. REVERSE A LIST
# ======================================

print("\n9. REVERSE A LIST")

numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])

# ======================================
# 10. MODIFYING VALUES USING INDEX
# ======================================

print("\n10. MODIFYING VALUES")

subjects = [
    "Python",
    "DBMS",
    "Statistics"
]

print("Before:", subjects)

subjects[1] = "Machine Learning"

print("After :", subjects)

# ======================================
# 11. USER INPUT EXAMPLE
# ======================================

print("\n11. USER INPUT EXAMPLE")

cities = []

for i in range(3):

    city = input(f"Enter City {i + 1}: ")
    cities.append(city)

print("\nCities:", cities)

print("First Two Cities:", cities[:2])

# ======================================
# 12. NESTED LIST INDEXING
# ======================================

print("\n12. NESTED LIST INDEXING")

students = [
    ["Saloni", 95],
    ["Riya", 88],
    ["Ankit", 91]
]

print("Name :", students[0][0])
print("Marks:", students[0][1])

# ======================================
# 13. MINI PROJECT
# ======================================

print("\n13. MINI PROJECT - MARKS ANALYZER")

marks = [92, 85, 90, 88, 95, 78]

print("Marks List:", marks)

print("First 3 Marks :", marks[:3])
print("Last 3 Marks  :", marks[-3:])
print("Even Positions:", marks[::2])
print("Reversed List :", marks[::-1])

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a list of five numbers.

Print:
- First Element
- Last Element

Exercise 2:
Print:

- First Three Elements
- Last Two Elements

using slicing.

Exercise 3:
Reverse a list using slicing.

Exercise 4:
Create a nested list and
access its elements.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Performance Analyzer.

Store marks of 8 subjects.

Display:

1. First Four Marks
2. Last Four Marks
3. Alternate Marks
4. Highest Mark
5. Lowest Mark
6. Reversed Marks List

Use:
- Indexing
- Slicing
- max()
- min()
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 021 Completed Successfully!")