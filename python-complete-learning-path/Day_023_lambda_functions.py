# ======================================
# Day 023: Lambda Functions
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Anonymous Functions
# (Lambda Functions) in Python
# ======================================

print("=" * 50)
print("DAY 023 - LAMBDA FUNCTIONS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Lambda Function?

A lambda function is a small anonymous
function that can have any number of
arguments but only one expression.

Syntax:

lambda arguments: expression

Example:

square = lambda x: x ** 2

Benefits:

1. Short and Concise
2. Useful for Small Tasks
3. Commonly Used with:
   - map()
   - filter()
   - sorted()
"""

# ======================================
# 1. SIMPLE LAMBDA FUNCTION
# ======================================

print("\n1. SIMPLE LAMBDA FUNCTION")

square = lambda x: x ** 2

print("Square of 5:", square(5))

# ======================================
# 2. ADDITION USING LAMBDA
# ======================================

print("\n2. ADDITION USING LAMBDA")

add = lambda a, b: a + b

print("Sum:", add(10, 20))

# ======================================
# 3. MULTIPLICATION USING LAMBDA
# ======================================

print("\n3. MULTIPLICATION USING LAMBDA")

multiply = lambda a, b: a * b

print("Product:", multiply(6, 7))

# ======================================
# 4. CHECK EVEN OR ODD
# ======================================

print("\n4. EVEN OR ODD")

check_even = lambda number: number % 2 == 0

print(check_even(10))
print(check_even(7))

# ======================================
# 5. FIND MAXIMUM OF TWO NUMBERS
# ======================================

print("\n5. MAXIMUM OF TWO NUMBERS")

maximum = lambda a, b: a if a > b else b

print("Maximum:", maximum(25, 40))

# ======================================
# 6. STRING TO UPPERCASE
# ======================================

print("\n6. STRING TO UPPERCASE")

convert_upper = lambda text: text.upper()

print(convert_upper("python"))

# ======================================
# 7. LAMBDA WITH LIST
# ======================================

print("\n7. LAMBDA WITH LIST")

numbers = [10, 20, 30, 40, 50]

squares = list(
    map(
        lambda x: x ** 2,
        numbers
    )
)

print(squares)

# ======================================
# 8. SORTING USING LAMBDA
# ======================================

print("\n8. SORTING USING LAMBDA")

students = [
    ("Saloni", 92),
    ("Riya", 85),
    ("Ankit", 95)
]

students.sort(
    key=lambda student: student[1]
)

print(students)

# ======================================
# 9. USER INPUT EXAMPLE
# ======================================

print("\n9. USER INPUT EXAMPLE")

number = int(input("Enter a number: "))

cube = lambda x: x ** 3

print("Cube:", cube(number))

# ======================================
# 10. MULTIPLE OPERATIONS
# ======================================

print("\n10. MULTIPLE OPERATIONS")

addition = lambda a, b: a + b
subtraction = lambda a, b: a - b
division = lambda a, b: a / b

print("Addition    :", addition(20, 10))
print("Subtraction :", subtraction(20, 10))
print("Division    :", division(20, 10))

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - MARKS ANALYZER")

marks = [92, 85, 78, 95, 88]

bonus_marks = list(
    map(
        lambda mark: mark + 5,
        marks
    )
)

print("Original Marks:", marks)
print("Bonus Marks   :", bonus_marks)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a lambda function to find
the square of a number.

Exercise 2:
Create a lambda function to find
the product of two numbers.

Exercise 3:
Create a lambda function that
returns the larger of two numbers.

Exercise 4:
Convert a string to uppercase
using lambda.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Performance System.

Store marks in a list.

Using lambda functions:

1. Add 5 bonus marks
2. Create squared marks
3. Find pass/fail status
   (Pass if marks >= 40)

Display all results neatly.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 023 Completed Successfully!")