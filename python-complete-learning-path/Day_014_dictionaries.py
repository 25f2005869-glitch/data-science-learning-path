# ======================================
# Day 014: Dictionaries
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Dictionaries and
# Key-Value Pair Data Storage in Python
# ======================================

print("=" * 50)
print("DAY 014 - DICTIONARIES")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Dictionary?

A dictionary is a collection of
key-value pairs.

Dictionaries are:

1. Ordered (Python 3.7+)
2. Mutable
3. Do Not Allow Duplicate Keys
4. Fast Data Retrieval

Syntax:

dictionary_name = {
    key1: value1,
    key2: value2
}

Example:

student = {
    "name": "Saloni",
    "age": 17
}
"""

# ======================================
# 1. CREATING A DICTIONARY
# ======================================

print("\n1. CREATING A DICTIONARY")

student = {
    "name": "Saloni Tiwari",
    "age": 17,
    "course": "BS in Data Science"
}

print(student)

# ======================================
# 2. DICTIONARY DATA TYPE
# ======================================

print("\n2. DICTIONARY DATA TYPE")

print(type(student))

# ======================================
# 3. ACCESSING VALUES
# ======================================

print("\n3. ACCESSING VALUES")

print("Name   :", student["name"])
print("Age    :", student["age"])
print("Course :", student["course"])

# ======================================
# 4. USING get()
# ======================================

print("\n4. get() METHOD")

print(student.get("name"))
print(student.get("semester"))
print(student.get("semester", "Not Available"))

# ======================================
# 5. ADDING NEW KEY-VALUE PAIRS
# ======================================

print("\n5. ADDING NEW DATA")

student["semester"] = 3
student["cgpa"] = 8.75

print(student)

# ======================================
# 6. MODIFYING VALUES
# ======================================

print("\n6. MODIFYING VALUES")

student["cgpa"] = 9.00

print(student)

# ======================================
# 7. REMOVING DATA
# ======================================

print("\n7. REMOVING DATA")

student.pop("age")

print(student)

# ======================================
# 8. CHECKING KEYS
# ======================================

print("\n8. MEMBERSHIP TEST")

print("name" in student)
print("roll_number" in student)

# ======================================
# 9. ITERATING THROUGH KEYS
# ======================================

print("\n9. ITERATING THROUGH KEYS")

for key in student:
    print(key)

# ======================================
# 10. ITERATING THROUGH VALUES
# ======================================

print("\n10. ITERATING THROUGH VALUES")

for value in student.values():
    print(value)

# ======================================
# 11. ITERATING THROUGH KEY-VALUE PAIRS
# ======================================

print("\n11. ITERATING THROUGH ITEMS")

for key, value in student.items():
    print(f"{key} : {value}")

# ======================================
# 12. NESTED DICTIONARY
# ======================================

print("\n12. NESTED DICTIONARY")

students = {
    "student1": {
        "name": "Saloni",
        "marks": 95
    },
    "student2": {
        "name": "Riya",
        "marks": 88
    }
}

print(students)

# ======================================
# 13. MINI PROJECT
# ======================================

print("\n13. MINI PROJECT - STUDENT PROFILE")

student_profile = {
    "name": "Saloni Tiwari",
    "age": 17,
    "semester": 3,
    "course": "BS in Data Science",
    "cgpa": 8.75
}

print("\nStudent Information")
print("-" * 30)

for key, value in student_profile.items():
    print(f"{key.title()} : {value}")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a dictionary containing:

- Name
- Age
- City

Print all values.

Exercise 2:
Add a new key called 'course'
to the dictionary.

Exercise 3:
Modify an existing value.

Exercise 4:
Iterate through the dictionary
and print all key-value pairs.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Result System.

Store:

- Name
- Mathematics Marks
- Python Marks
- DBMS Marks

Calculate:

1. Total Marks
2. Average Marks

Display all information neatly.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 014 Completed Successfully!")