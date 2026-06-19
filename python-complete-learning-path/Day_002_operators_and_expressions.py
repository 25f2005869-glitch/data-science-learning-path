# ======================================
# Day 002: Operators and Expressions
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Operators and Expressions
# in Python
# ======================================

print("=" * 50)
print("DAY 002 - OPERATORS AND EXPRESSIONS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is an Operator?

An operator is a symbol that performs
an operation on one or more operands.

Example:
10 + 5

'+' is the operator
10 and 5 are operands

Types of Operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators
"""

# ======================================
# 1. ARITHMETIC OPERATORS
# ======================================

print("\n1. ARITHMETIC OPERATORS")

a = 15
b = 4

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponentiation :", a ** b)

# ======================================
# 2. ASSIGNMENT OPERATORS
# ======================================

print("\n2. ASSIGNMENT OPERATORS")

x = 10
print("Initial Value:", x)

x += 5
print("After += 5 :", x)

x -= 2
print("After -= 2 :", x)

x *= 3
print("After *= 3 :", x)

# ======================================
# 3. COMPARISON OPERATORS
# ======================================

print("\n3. COMPARISON OPERATORS")

num1 = 20
num2 = 15

print("num1 == num2 :", num1 == num2)
print("num1 != num2 :", num1 != num2)
print("num1 > num2  :", num1 > num2)
print("num1 < num2  :", num1 < num2)
print("num1 >= num2 :", num1 >= num2)
print("num1 <= num2 :", num1 <= num2)

# ======================================
# 4. LOGICAL OPERATORS
# ======================================

print("\n4. LOGICAL OPERATORS")

age = 17
is_student = True

print("AND :", age >= 16 and is_student)
print("OR  :", age >= 18 or is_student)
print("NOT :", not is_student)

# ======================================
# 5. MEMBERSHIP OPERATORS
# ======================================

print("\n5. MEMBERSHIP OPERATORS")

course = "Data Science"

print("'Data' in course     :", "Data" in course)
print("'Python' in course   :", "Python" in course)
print("'AI' not in course   :", "AI" not in course)

# ======================================
# 6. IDENTITY OPERATORS
# ======================================

print("\n6. IDENTITY OPERATORS")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 == list3     :", list1 == list3)

# ======================================
# 7. EXPRESSIONS
# ======================================

print("\n7. EXPRESSIONS")

result = (10 + 5) * 2

print("Result:", result)

# ======================================
# 8. MINI PRACTICE
# ======================================

print("\n8. MINI PRACTICE")

math_marks = 92
python_marks = 95

average = (math_marks + python_marks) / 2

print("Math Marks   :", math_marks)
print("Python Marks :", python_marks)
print("Average      :", average)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Take two numbers from the user
and perform all arithmetic operations.

Exercise 2:
Check whether a student is eligible
for an exam.

Condition:
Attendance >= 75

Exercise 3:
Create two variables and compare them
using all comparison operators.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a simple percentage calculator.

Input:
Marks obtained
Total marks

Output:
Percentage

Formula:

Percentage = (Marks Obtained / Total Marks) * 100
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 002 Completed Successfully!")