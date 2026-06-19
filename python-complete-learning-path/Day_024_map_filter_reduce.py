# ======================================
# Day 024: map(), filter() and reduce()
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Functional Programming
# Tools in Python
# ======================================

print("=" * 50)
print("DAY 024 - MAP, FILTER AND REDUCE")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
map()

Applies a function to every element
of an iterable.

Syntax:

map(function, iterable)

--------------------------------------

filter()

Filters elements based on a condition.

Syntax:

filter(function, iterable)

--------------------------------------

reduce()

Reduces an iterable to a single value.

Syntax:

reduce(function, iterable)

Note:
reduce() must be imported from
the functools module.
"""

# ======================================
# IMPORTS
# ======================================

from functools import reduce

# ======================================
# 1. MAP FUNCTION
# ======================================

print("\n1. MAP FUNCTION")

numbers = [1, 2, 3, 4, 5]

squares = list(
    map(
        lambda x: x ** 2,
        numbers
    )
)

print("Original:", numbers)
print("Squares :", squares)

# ======================================
# 2. MAP WITH STRINGS
# ======================================

print("\n2. MAP WITH STRINGS")

subjects = [
    "python",
    "dbms",
    "statistics"
]

uppercase_subjects = list(
    map(
        lambda subject: subject.upper(),
        subjects
    )
)

print(uppercase_subjects)

# ======================================
# 3. FILTER FUNCTION
# ======================================

print("\n3. FILTER FUNCTION")

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print("Even Numbers:", even_numbers)

# ======================================
# 4. FILTER PASSED STUDENTS
# ======================================

print("\n4. FILTER PASSED STUDENTS")

marks = [92, 35, 78, 28, 85, 45]

passed_marks = list(
    filter(
        lambda mark: mark >= 40,
        marks
    )
)

print("Passed Marks:", passed_marks)

# ======================================
# 5. REDUCE FUNCTION
# ======================================

print("\n5. REDUCE FUNCTION")

numbers = [10, 20, 30, 40]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print("Total:", total)

# ======================================
# 6. REDUCE FOR PRODUCT
# ======================================

print("\n6. REDUCE FOR PRODUCT")

numbers = [1, 2, 3, 4, 5]

product = reduce(
    lambda a, b: a * b,
    numbers
)

print("Product:", product)

# ======================================
# 7. MAP + FILTER
# ======================================

print("\n7. MAP + FILTER")

numbers = [1, 2, 3, 4, 5, 6]

even_squares = list(
    map(
        lambda x: x ** 2,
        filter(
            lambda x: x % 2 == 0,
            numbers
        )
    )
)

print(even_squares)

# ======================================
# 8. USER INPUT EXAMPLE
# ======================================

print("\n8. USER INPUT EXAMPLE")

numbers = input(
    "Enter numbers separated by spaces: "
).split()

numbers = list(
    map(
        int,
        numbers
    )
)

print("Numbers:", numbers)

# ======================================
# 9. FIND MAXIMUM USING REDUCE
# ======================================

print("\n9. FIND MAXIMUM USING REDUCE")

numbers = [12, 45, 78, 23, 99, 34]

maximum = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print("Maximum:", maximum)

# ======================================
# 10. BONUS MARKS SYSTEM
# ======================================

print("\n10. BONUS MARKS SYSTEM")

marks = [85, 90, 78, 92, 88]

bonus_marks = list(
    map(
        lambda mark: mark + 5,
        marks
    )
)

print("Original Marks:", marks)
print("Bonus Marks   :", bonus_marks)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT ANALYZER")

marks = [92, 35, 78, 88, 25, 95]

passed_marks = list(
    filter(
        lambda mark: mark >= 40,
        marks
    )
)

bonus_marks = list(
    map(
        lambda mark: mark + 5,
        passed_marks
    )
)

total_marks = reduce(
    lambda a, b: a + b,
    bonus_marks
)

print("Original Marks:", marks)
print("Passed Marks  :", passed_marks)
print("Bonus Marks   :", bonus_marks)
print("Total         :", total_marks)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Use map() to create a list
of squares from 1 to 10.

Exercise 2:
Use filter() to find all
odd numbers from a list.

Exercise 3:
Use reduce() to calculate
the sum of a list.

Exercise 4:
Use map() to convert all
names to uppercase.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Marks Processing System.

Store marks in a list.

Using:

1. filter()
   - Extract passed students

2. map()
   - Add 5 bonus marks

3. reduce()
   - Calculate total marks

Display:

- Original Marks
- Passed Marks
- Bonus Marks
- Total Marks
- Average Marks
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 024 Completed Successfully!")