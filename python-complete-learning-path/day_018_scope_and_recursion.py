# ======================================
# Day 018: Scope and Recursion
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Variable Scope and
# Recursive Functions in Python
# ======================================

print("=" * 50)
print("DAY 018 - SCOPE AND RECURSION")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Scope:

Scope defines where a variable can
be accessed in a program.

Types of Scope:

1. Local Scope
2. Global Scope

Local Variable:
A variable declared inside a function.

Global Variable:
A variable declared outside a function.

--------------------------------------

Recursion:

Recursion is a technique where a
function calls itself.

Important Components:

1. Base Case
2. Recursive Case

Without a base case, recursion
can lead to infinite calls.
"""

# ======================================
# 1. LOCAL SCOPE
# ======================================

print("\n1. LOCAL SCOPE")

def display_name():

    student_name = "Saloni Tiwari"

    print("Inside Function:", student_name)

display_name()

# ======================================
# 2. GLOBAL SCOPE
# ======================================

print("\n2. GLOBAL SCOPE")

course = "BS in Data Science"

def show_course():
    print("Inside Function:", course)

show_course()

print("Outside Function:", course)

# ======================================
# 3. LOCAL VS GLOBAL VARIABLE
# ======================================

print("\n3. LOCAL VS GLOBAL VARIABLE")

value = 100

def example():

    value = 50

    print("Local Value :", value)

example()

print("Global Value:", value)

# ======================================
# 4. GLOBAL KEYWORD
# ======================================

print("\n4. GLOBAL KEYWORD")

counter = 0

def increase_counter():

    global counter

    counter += 1

increase_counter()

print("Counter:", counter)

# ======================================
# 5. SIMPLE RECURSION
# ======================================

print("\n5. SIMPLE RECURSION")

def countdown(number):

    if number == 0:
        print("Completed")
        return

    print(number)

    countdown(number - 1)

countdown(5)

# ======================================
# 6. FACTORIAL USING RECURSION
# ======================================

print("\n6. FACTORIAL USING RECURSION")

def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)

print("Factorial:", factorial(5))

# ======================================
# 7. SUM OF NATURAL NUMBERS
# ======================================

print("\n7. SUM OF NATURAL NUMBERS")

def natural_sum(number):

    if number == 1:
        return 1

    return number + natural_sum(number - 1)

print("Sum:", natural_sum(10))

# ======================================
# 8. POWER CALCULATION
# ======================================

print("\n8. POWER CALCULATION")

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print("Result:", power(2, 5))

# ======================================
# 9. USER INPUT EXAMPLE
# ======================================

print("\n9. USER INPUT EXAMPLE")

def recursive_count(number):

    if number == 0:
        return

    print(number)

    recursive_count(number - 1)

user_number = int(input("Enter a number: "))

recursive_count(user_number)

# ======================================
# 10. FIBONACCI USING RECURSION
# ======================================

print("\n10. FIBONACCI USING RECURSION")

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(8):
    print(fibonacci(i), end=" ")

print()

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - RECURSIVE RESULT")

def calculate_total(*marks):

    if len(marks) == 0:
        return 0

    return sum(marks)

student_marks = (92, 95, 90, 88)

total_marks = calculate_total(*student_marks)

average_marks = total_marks / len(student_marks)

print("Marks   :", student_marks)
print("Total   :", total_marks)
print("Average :", round(average_marks, 2))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a global variable and
access it inside a function.

Exercise 2:
Create a local variable and
observe its scope.

Exercise 3:
Find factorial of a number
using recursion.

Exercise 4:
Find the sum of first n
natural numbers using recursion.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Recursive Calculator.

Functions:

1. Factorial
2. Power
3. Sum of Natural Numbers

Take input from the user and
display the result using recursion.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 018 Completed Successfully!")