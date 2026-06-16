# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Hash Tables
# Day         : 28
# Description : Basic hash table operations using Python
#               dictionaries.
# ==========================================================

# Creating a hash table
students = {}

# Insert Operations
students[101] = "Saloni"
students[102] = "Rahul"
students[103] = "Priya"

print("Hash Table:")

for key, value in students.items():

    print(key, "->", value)

# Search Operation
student_id = 102

if student_id in students:

    print("\nStudent Found:", students[student_id])

# Delete Operation
del students[101]

print("\nAfter Deletion:")

for key, value in students.items():

    print(key, "->", value)