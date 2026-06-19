# ======================================
# Day 029: JSON File Handling
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding JSON (JavaScript Object
# Notation) File Handling in Python
# ======================================

print("=" * 50)
print("DAY 029 - JSON FILE HANDLING")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is JSON?

JSON stands for:

JavaScript Object Notation

JSON is a lightweight format used
for storing and exchanging data.

JSON is widely used in:

1. APIs
2. Web Applications
3. Databases
4. Data Science Projects

Example:

{
    "name": "Saloni",
    "age": 17,
    "course": "Data Science"
}

Python provides the json module
for working with JSON data.
"""

# ======================================
# IMPORT JSON MODULE
# ======================================

import json

# ======================================
# 1. PYTHON DICTIONARY
# ======================================

print("\n1. PYTHON DICTIONARY")

student = {
    "name": "Saloni Tiwari",
    "age": 17,
    "course": "BS in Data Science"
}

print(student)

# ======================================
# 2. WRITING JSON FILE
# ======================================

print("\n2. WRITING JSON FILE")

with open(
    "student.json",
    "w"
) as file:

    json.dump(
        student,
        file,
        indent=4
    )

print("JSON File Created Successfully")

# ======================================
# 3. READING JSON FILE
# ======================================

print("\n3. READING JSON FILE")

with open(
    "student.json",
    "r"
) as file:

    data = json.load(file)

print(data)

# ======================================
# 4. ACCESSING JSON DATA
# ======================================

print("\n4. ACCESSING JSON DATA")

print("Name   :", data["name"])
print("Age    :", data["age"])
print("Course :", data["course"])

# ======================================
# 5. JSON STRING
# ======================================

print("\n5. JSON STRING")

json_string = json.dumps(
    student,
    indent=4
)

print(json_string)

# ======================================
# 6. CONVERT JSON STRING TO DICTIONARY
# ======================================

print("\n6. JSON STRING TO DICTIONARY")

text = '''
{
    "city": "Aurangabad",
    "state": "Bihar"
}
'''

location = json.loads(text)

print(location)

# ======================================
# 7. LIST OF STUDENTS
# ======================================

print("\n7. LIST OF STUDENTS")

students = [
    {
        "name": "Saloni",
        "marks": 95
    },
    {
        "name": "Riya",
        "marks": 88
    },
    {
        "name": "Ankit",
        "marks": 91
    }
]

with open(
    "students.json",
    "w"
) as file:

    json.dump(
        students,
        file,
        indent=4
    )

print("Students JSON Created")

# ======================================
# 8. READING STUDENT LIST
# ======================================

print("\n8. READING STUDENT LIST")

with open(
    "students.json",
    "r"
) as file:

    student_data = json.load(file)

for student in student_data:
    print(student)

# ======================================
# 9. USER INPUT TO JSON
# ======================================

print("\n9. USER INPUT TO JSON")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")

user_data = {
    "name": name,
    "age": age,
    "course": course
}

with open(
    "user_profile.json",
    "w"
) as file:

    json.dump(
        user_data,
        file,
        indent=4
    )

print("User Profile Saved")

# ======================================
# 10. DISPLAY USER PROFILE
# ======================================

print("\n10. DISPLAY USER PROFILE")

with open(
    "user_profile.json",
    "r"
) as file:

    profile = json.load(file)

print(profile)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT DATABASE")

student_database = {
    "students": [
        {
            "name": "Saloni",
            "math": 92,
            "python": 95,
            "dbms": 90
        },
        {
            "name": "Riya",
            "math": 88,
            "python": 91,
            "dbms": 87
        }
    ]
}

with open(
    "student_database.json",
    "w"
) as file:

    json.dump(
        student_database,
        file,
        indent=4
    )

print("Database Created Successfully")

print("\nDatabase Content")

with open(
    "student_database.json",
    "r"
) as file:

    database = json.load(file)

print(json.dumps(database, indent=4))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a dictionary containing:

- Name
- Age
- City

Save it to a JSON file.

Exercise 2:
Read data from a JSON file.

Exercise 3:
Convert a Python dictionary
to a JSON string.

Exercise 4:
Convert a JSON string into
a Python dictionary.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Management System.

Requirements:

1. Add Student Information
2. Save Data to JSON File
3. Read Data from JSON File
4. Display Student Details

Fields:

- Name
- Age
- Course
- Marks

Store all records in a JSON file.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 029 Completed Successfully!")