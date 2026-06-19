# ======================================
# Day 003: Input and Output
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Input and Output
# Operations in Python
# ======================================

print("=" * 50)
print("DAY 003 - INPUT AND OUTPUT")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Input:
Input allows a user to provide data
to a program during execution.

Python uses the input() function
to accept user input.

Output:
Output is the information displayed
to the user.

Python uses the print() function
to display output.

Important:
The input() function always returns
data as a string.

Type conversion is required when
working with numbers.
"""

# ======================================
# 1. BASIC OUTPUT
# ======================================

print("\n1. BASIC OUTPUT")

print("Hello, World!")
print("Welcome to Python Programming")

# ======================================
# 2. BASIC INPUT
# ======================================

print("\n2. BASIC INPUT")

name = input("Enter your name: ")

print("Hello,", name)

# ======================================
# 3. MULTIPLE INPUTS
# ======================================

print("\n3. MULTIPLE INPUTS")

city = input("Enter your city: ")
course = input("Enter your course: ")

print("\nStudent Information")
print("-------------------")
print("City   :", city)
print("Course :", course)

# ======================================
# 4. NUMERIC INPUT
# ======================================

print("\n4. NUMERIC INPUT")

age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))

print("Age    :", age)
print("Height :", height)

# ======================================
# 5. ADDITION USING INPUT
# ======================================

print("\n5. ADDITION USING INPUT")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("Sum =", sum_result)

# ======================================
# 6. FORMATTED OUTPUT
# ======================================

print("\n6. FORMATTED OUTPUT")

student_name = "Saloni Tiwari"
semester = 3
cgpa = 8.75

print(f"Name     : {student_name}")
print(f"Semester : {semester}")
print(f"CGPA     : {cgpa}")

# ======================================
# 7. MULTI-LINE OUTPUT
# ======================================

print("\n7. MULTI-LINE OUTPUT")

print("""
IIT Madras BS Degree
Diploma Level
Python Complete Learning Path
""")

# ======================================
# 8. MINI PRACTICE
# ======================================

print("\n8. MINI PRACTICE")

student_name = input("Enter Student Name: ")
student_age = int(input("Enter Student Age: "))
student_course = input("Enter Course Name: ")

print("\nStudent Profile")
print("-------------------------")
print(f"Name   : {student_name}")
print(f"Age    : {student_age}")
print(f"Course : {student_course}")

# ======================================
# 9. SIMPLE MARKSHEET
# ======================================

print("\n9. SIMPLE MARKSHEET")

math_marks = float(input("Enter Mathematics Marks: "))
python_marks = float(input("Enter Python Marks: "))

total = math_marks + python_marks
average = total / 2

print("\nResult Summary")
print("-------------------------")
print(f"Total Marks : {total}")
print(f"Average     : {average}")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Take user input for:

- Name
- Age
- City

Display the information neatly.

Exercise 2:
Take two numbers from the user
and calculate:

- Sum
- Difference
- Product
- Quotient

Exercise 3:
Create a simple profile generator
using user input.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Percentage Calculator.

Input:
- Student Name
- Total Marks Obtained
- Maximum Marks

Output:
- Student Name
- Percentage

Formula:

Percentage = (Obtained Marks / Maximum Marks) * 100
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 003 Completed Successfully!")