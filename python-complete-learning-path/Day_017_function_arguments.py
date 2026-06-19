# ======================================
# Day 017: Function Arguments
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Different Types of
# Function Arguments in Python
# ======================================

print("=" * 50)
print("DAY 017 - FUNCTION ARGUMENTS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Arguments are values passed to a function
when it is called.

Types of Arguments:

1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments (*args)
5. Keyword Variable-Length Arguments (**kwargs)

Understanding arguments is essential
for writing flexible and reusable
functions.
"""

# ======================================
# 1. POSITIONAL ARGUMENTS
# ======================================

print("\n1. POSITIONAL ARGUMENTS")

def student_info(name, age):
    print("Name:", name)
    print("Age :", age)

student_info("Saloni", 17)

# ======================================
# 2. KEYWORD ARGUMENTS
# ======================================

print("\n2. KEYWORD ARGUMENTS")

def course_details(course, semester):
    print("Course   :", course)
    print("Semester :", semester)

course_details(
    semester=3,
    course="BS in Data Science"
)

# ======================================
# 3. DEFAULT ARGUMENTS
# ======================================

print("\n3. DEFAULT ARGUMENTS")

def greet(name="Student"):
    print("Welcome,", name)

greet()
greet("Saloni")

# ======================================
# 4. MULTIPLE DEFAULT ARGUMENTS
# ======================================

print("\n4. MULTIPLE DEFAULT ARGUMENTS")

def profile(name, city="Aurangabad"):
    print("Name :", name)
    print("City :", city)

profile("Saloni")
profile("Riya", "Patna")

# ======================================
# 5. VARIABLE LENGTH ARGUMENTS (*args)
# ======================================

print("\n5. *args")

def find_sum(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total

print(find_sum(10, 20))
print(find_sum(10, 20, 30))
print(find_sum(10, 20, 30, 40))

# ======================================
# 6. DISPLAYING *args
# ======================================

print("\n6. DISPLAYING *args")

def subjects(*items):

    for item in items:
        print(item)

subjects(
    "Python",
    "DBMS",
    "Statistics",
    "Mathematics"
)

# ======================================
# 7. VARIABLE KEYWORD ARGUMENTS (**kwargs)
# ======================================

print("\n7. **kwargs")

def student_profile(**details):

    for key, value in details.items():
        print(f"{key} : {value}")

student_profile(
    name="Saloni",
    age=17,
    semester=3
)

# ======================================
# 8. COMBINING ARGUMENT TYPES
# ======================================

print("\n8. COMBINING ARGUMENT TYPES")

def employee(name, department="IT"):
    print("Name       :", name)
    print("Department :", department)

employee("Amit")
employee("Riya", "Data Science")

# ======================================
# 9. RETURNING VALUES
# ======================================

print("\n9. RETURNING VALUES")

def multiply(a, b):
    return a * b

result = multiply(10, 5)

print("Result:", result)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

def square(number):
    return number ** 2

num = int(input("Enter a number: "))

print("Square:", square(num))

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - MARKS REPORT")

def marks_report(name, *marks):

    total = sum(marks)
    average = total / len(marks)

    print("\nStudent Report")
    print("-" * 30)

    print("Name    :", name)
    print("Marks   :", marks)
    print("Total   :", total)
    print("Average :", round(average, 2))

marks_report(
    "Saloni Tiwari",
    92,
    95,
    90,
    88
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a function using
positional arguments.

Exercise 2:
Create a function using
keyword arguments.

Exercise 3:
Create a function using
default arguments.

Exercise 4:
Create a function that accepts
multiple numbers using *args
and returns their sum.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Profile Generator.

Requirements:

1. Use positional arguments
2. Use default arguments
3. Use **kwargs

Store:

- Name
- Age
- Course
- Semester
- City

Display the profile neatly.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 017 Completed Successfully!")