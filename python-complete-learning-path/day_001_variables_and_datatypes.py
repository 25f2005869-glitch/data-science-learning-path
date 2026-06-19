# ======================================
# Day 001: Variables and Data Types
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Variables and Data Types
# ======================================

print("=" * 50)
print("DAY 001 - VARIABLES AND DATA TYPES")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Variable?

A variable is a named memory location used
to store data in a program.

Python is a dynamically typed language,
which means the data type is assigned
automatically at runtime.

Common Data Types:
1. str   -> Text/String
2. int   -> Integer Numbers
3. float -> Decimal Numbers
4. bool  -> True or False
"""

# ======================================
# 1. STRING DATA TYPE
# ======================================

print("\n1. STRING DATA TYPE")

name = "Saloni Tiwari"

print("Name:", name)
print("Type:", type(name))

# ======================================
# 2. INTEGER DATA TYPE
# ======================================

print("\n2. INTEGER DATA TYPE")

age = 17

print("Age:", age)
print("Type:", type(age))

# ======================================
# 3. FLOAT DATA TYPE
# ======================================

print("\n3. FLOAT DATA TYPE")

height = 5.35

print("Height:", height)
print("Type:", type(height))

# ======================================
# 4. BOOLEAN DATA TYPE
# ======================================

print("\n4. BOOLEAN DATA TYPE")

is_student = True

print("Student:", is_student)
print("Type:", type(is_student))

# ======================================
# 5. MULTIPLE VARIABLES
# ======================================

print("\n5. MULTIPLE VARIABLES")

course = "BS in Data Science"
semester = 3

print("Course:", course)
print("Semester:", semester)

# ======================================
# 6. VARIABLE NAMING RULES
# ======================================

print("\n6. VARIABLE NAMING RULES")

student_name = "Saloni"
student_age = 17

print(student_name)
print(student_age)

# ======================================
# 7. DYNAMIC TYPING
# ======================================

print("\n7. DYNAMIC TYPING")

value = 100
print(value, type(value))

value = "Python"
print(value, type(value))

# ======================================
# 8. TYPE CONVERSION
# ======================================

print("\n8. TYPE CONVERSION")

num1 = "10"
num2 = "20"

total = int(num1) + int(num2)

print("Sum:", total)

# ======================================
# 9. USER INPUT
# ======================================

print("\n9. USER INPUT")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("\nStudent Information")
print("-------------------")
print("Name :", user_name)
print("Age  :", user_age)

# ======================================
# 10. MINI PRACTICE
# ======================================

print("\n10. MINI PRACTICE")

city = input("Enter your city: ")
college = input("Enter your college: ")

print("\nProfile Summary")
print("-------------------")
print("Name    :", user_name)
print("Age     :", user_age)
print("City    :", city)
print("College :", college)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create variables for:
- favourite_subject
- marks
- percentage

Print their values and types.

Exercise 2:
Take user input for:
- Name
- Course
- Semester

Display the information neatly.

Exercise 3:
Convert the string "100"
into an integer and add 50.
Print the result.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a student profile containing:

Name
Age
Height
Course
Semester

Print all details in a formatted way.
"""

print("\nDay 001 Completed Successfully!")