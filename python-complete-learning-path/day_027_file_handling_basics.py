# ======================================
# Day 027: File Handling Basics
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding File Handling
# Operations in Python
# ======================================

print("=" * 50)
print("DAY 027 - FILE HANDLING BASICS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is File Handling?

File handling allows a program to:

1. Create files
2. Read files
3. Write files
4. Append data to files

Common File Modes:

'r'  -> Read
'w'  -> Write
'a'  -> Append
'x'  -> Create

Best Practice:

Always close files after use.

Preferred Method:

with open() as file

This automatically closes the file.
"""

# ======================================
# 1. WRITING TO A FILE
# ======================================

print("\n1. WRITING TO A FILE")

with open("sample.txt", "w") as file:

    file.write("Welcome to Python File Handling.\n")
    file.write("This is Day 027.\n")

print("Data written successfully.")

# ======================================
# 2. READING A FILE
# ======================================

print("\n2. READING A FILE")

with open("sample.txt", "r") as file:

    content = file.read()

print(content)

# ======================================
# 3. APPENDING DATA
# ======================================

print("\n3. APPENDING DATA")

with open("sample.txt", "a") as file:

    file.write("Learning Python is fun.\n")

print("New data appended.")

# ======================================
# 4. READING UPDATED FILE
# ======================================

print("\n4. UPDATED FILE CONTENT")

with open("sample.txt", "r") as file:

    content = file.read()

print(content)

# ======================================
# 5. READLINE()
# ======================================

print("\n5. readline()")

with open("sample.txt", "r") as file:

    first_line = file.readline()

print(first_line)

# ======================================
# 6. READLINES()
# ======================================

print("\n6. readlines()")

with open("sample.txt", "r") as file:

    lines = file.readlines()

print(lines)

# ======================================
# 7. ITERATING THROUGH FILE
# ======================================

print("\n7. ITERATING THROUGH FILE")

with open("sample.txt", "r") as file:

    for line in file:
        print(line.strip())

# ======================================
# 8. FILE EXISTS CHECK
# ======================================

print("\n8. FILE EXISTS CHECK")

import os

if os.path.exists("sample.txt"):
    print("File Found")
else:
    print("File Not Found")

# ======================================
# 9. FILE INFORMATION
# ======================================

print("\n9. FILE INFORMATION")

if os.path.exists("sample.txt"):

    file_size = os.path.getsize("sample.txt")

    print("File Size:", file_size, "bytes")

# ======================================
# 10. USER INPUT TO FILE
# ======================================

print("\n10. USER INPUT TO FILE")

name = input("Enter your name: ")

with open("students.txt", "w") as file:

    file.write(f"Student Name: {name}\n")

print("Student data saved.")

# ======================================
# 11. READING USER FILE
# ======================================

print("\n11. READING USER FILE")

with open("students.txt", "r") as file:

    print(file.read())

# ======================================
# 12. MINI PROJECT
# ======================================

print("\n12. MINI PROJECT - STUDENT RECORD")

student_name = input("Enter Student Name: ")
student_marks = input("Enter Student Marks: ")

with open("student_record.txt", "w") as file:

    file.write(f"Name : {student_name}\n")
    file.write(f"Marks: {student_marks}\n")

print("Student Record Saved Successfully")

print("\nStored Data")

with open("student_record.txt", "r") as file:

    print(file.read())

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a file called notes.txt

Write three lines into it.

Exercise 2:
Read and display all content
from notes.txt.

Exercise 3:
Append a new line to notes.txt.

Exercise 4:
Display file size using os module.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Database System.

Requirements:

1. Take student details:
   - Name
   - Age
   - Course

2. Store details in a file.

3. Read and display all data.

4. Check whether the file exists.

5. Display file size.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 027 Completed Successfully!")