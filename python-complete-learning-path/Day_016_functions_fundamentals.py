# ======================================
# Day 016: Functions Fundamentals
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Functions and Code
# Reusability in Python
# ======================================

print("=" * 50)
print("DAY 016 - FUNCTIONS FUNDAMENTALS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Function?

A function is a reusable block of code
designed to perform a specific task.

Benefits of Functions:

1. Code Reusability
2. Better Organization
3. Easy Maintenance
4. Reduced Code Duplication

Syntax:

def function_name():
    statements

function_name()
"""

# ======================================
# 1. SIMPLE FUNCTION
# ======================================

print("\n1. SIMPLE FUNCTION")

def greet():
    print("Welcome to Python Programming")

greet()

# ======================================
# 2. FUNCTION CALLED MULTIPLE TIMES
# ======================================

print("\n2. FUNCTION CALLED MULTIPLE TIMES")

def welcome():
    print("Hello, Saloni!")

welcome()
welcome()
welcome()

# ======================================
# 3. FUNCTION WITH PARAMETERS
# ======================================

print("\n3. FUNCTION WITH PARAMETERS")

def display_name(name):
    print("Student Name:", name)

display_name("Saloni Tiwari")
display_name("Riya Sharma")

# ======================================
# 4. FUNCTION WITH MULTIPLE PARAMETERS
# ======================================

print("\n4. FUNCTION WITH MULTIPLE PARAMETERS")

def student_info(name, semester):
    print("Name     :", name)
    print("Semester :", semester)

student_info("Saloni Tiwari", 3)

# ======================================
# 5. FUNCTION WITH RETURN VALUE
# ======================================

print("\n5. FUNCTION WITH RETURN VALUE")

def add(a, b):
    return a + b

result = add(10, 20)

print("Sum:", result)

# ======================================
# 6. AREA OF RECTANGLE
# ======================================

print("\n6. AREA OF RECTANGLE")

def rectangle_area(length, width):
    return length * width

area = rectangle_area(10, 5)

print("Area:", area)

# ======================================
# 7. EVEN OR ODD FUNCTION
# ======================================

print("\n7. EVEN OR ODD FUNCTION")

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))

# ======================================
# 8. USER INPUT FUNCTION
# ======================================

print("\n8. USER INPUT FUNCTION")

def square(number):
    return number ** 2

num = int(input("Enter a number: "))

print("Square:", square(num))

# ======================================
# 9. FUNCTION TO CALCULATE AVERAGE
# ======================================

print("\n9. FUNCTION TO CALCULATE AVERAGE")

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

average = calculate_average(85, 90, 95)

print("Average:", average)

# ======================================
# 10. FUNCTION RETURNING MULTIPLE VALUES
# ======================================

print("\n10. MULTIPLE RETURN VALUES")

def calculate_result(m1, m2, m3):

    total = m1 + m2 + m3
    average = total / 3

    return total, average

total_marks, average_marks = calculate_result(
    85,
    90,
    95
)

print("Total   :", total_marks)
print("Average :", average_marks)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT RESULT")

def student_result(name, math, python, dbms):

    total = math + python + dbms
    average = total / 3

    print("\nStudent Report")
    print("-" * 30)

    print("Name    :", name)
    print("Total   :", total)
    print("Average :", round(average, 2))

student_result(
    "Saloni Tiwari",
    92,
    95,
    90
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a function that prints
your name.

Exercise 2:
Create a function that accepts
two numbers and returns their product.

Exercise 3:
Create a function that checks
whether a number is positive,
negative, or zero.

Exercise 4:
Create a function that calculates
the area of a circle.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Grade Calculator Function.

Input:
- Student Name
- Marks

Output:

90+      -> A+
80-89    -> A
70-79    -> B
60-69    -> C
40-59    -> D
Below 40 -> F

Use:
- Function
- Parameters
- Return Statement
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 016 Completed Successfully!")