# ======================================
# Day 015: Dictionary Methods
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Common Dictionary
# Methods in Python
# ======================================

print("=" * 50)
print("DAY 015 - DICTIONARY METHODS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Dictionary methods are built-in functions
used to perform operations on dictionaries.

Since dictionaries are mutable, methods
can modify the original dictionary.

Common Dictionary Methods:

1. keys()
2. values()
3. items()
4. get()
5. update()
6. pop()
7. popitem()
8. clear()
9. copy()
10. setdefault()
"""

# ======================================
# 1. keys()
# ======================================

print("\n1. keys()")

student = {
    "name": "Saloni",
    "age": 17,
    "course": "BS in Data Science"
}

print(student.keys())

# ======================================
# 2. values()
# ======================================

print("\n2. values()")

print(student.values())

# ======================================
# 3. items()
# ======================================

print("\n3. items()")

print(student.items())

# ======================================
# 4. get()
# ======================================

print("\n4. get()")

print(student.get("name"))
print(student.get("semester"))
print(student.get("semester", "Not Found"))

# ======================================
# 5. update()
# ======================================

print("\n5. update()")

student.update({
    "semester": 3,
    "cgpa": 8.75
})

print(student)

# ======================================
# 6. pop()
# ======================================

print("\n6. pop()")

removed_value = student.pop("age")

print("Removed Value:", removed_value)
print(student)

# ======================================
# 7. popitem()
# ======================================

print("\n7. popitem()")

last_item = student.popitem()

print("Removed Item:", last_item)
print(student)

# ======================================
# 8. setdefault()
# ======================================

print("\n8. setdefault()")

student.setdefault("city", "Aurangabad")

print(student)

student.setdefault("city", "Patna")

print(student)

# ======================================
# 9. copy()
# ======================================

print("\n9. copy()")

student_copy = student.copy()

print("Original:", student)
print("Copy    :", student_copy)

# ======================================
# 10. clear()
# ======================================

print("\n10. clear()")

temp_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

temp_dict.clear()

print(temp_dict)

# ======================================
# 11. ITERATING THROUGH DICTIONARY
# ======================================

print("\n11. ITERATING THROUGH DICTIONARY")

student = {
    "name": "Saloni",
    "semester": 3,
    "course": "BS in Data Science"
}

for key, value in student.items():
    print(f"{key} : {value}")

# ======================================
# 12. NESTED DICTIONARY PRACTICE
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

print("\n13. MINI PROJECT - STUDENT DATABASE")

student_database = {
    "name": "Saloni Tiwari",
    "age": 17,
    "semester": 3,
    "course": "BS in Data Science",
    "cgpa": 8.75
}

print("\nStudent Information")
print("-" * 30)

for key, value in student_database.items():
    print(f"{key.title()} : {value}")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a dictionary and print:

- keys()
- values()
- items()

Exercise 2:
Add a new key using update().

Exercise 3:
Remove a key using pop().

Exercise 4:
Create a copy of a dictionary
using copy().
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Marks Manager.

Store:

- Name
- Mathematics Marks
- Python Marks
- DBMS Marks

Using a dictionary:

1. Calculate Total Marks
2. Calculate Average Marks
3. Display all details
4. Display highest subject marks
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 015 Completed Successfully!")