# ======================================
# Day 028: CSV File Handling
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding CSV (Comma Separated
# Values) File Handling in Python
# ======================================

print("=" * 50)
print("DAY 028 - CSV FILE HANDLING")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a CSV File?

CSV stands for:

Comma Separated Values

CSV files are widely used for:

1. Data Storage
2. Data Analysis
3. Database Export
4. Machine Learning Datasets

Example:

Name,Age,Marks
Saloni,17,95
Riya,18,88

Python provides the csv module
to work with CSV files.
"""

# ======================================
# IMPORT CSV MODULE
# ======================================

import csv

# ======================================
# 1. WRITING TO A CSV FILE
# ======================================

print("\n1. WRITING TO A CSV FILE")

with open(
    "students.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Name", "Age", "Marks"]
    )

    writer.writerow(
        ["Saloni", 17, 95]
    )

    writer.writerow(
        ["Riya", 18, 88]
    )

print("CSV File Created Successfully")

# ======================================
# 2. READING A CSV FILE
# ======================================

print("\n2. READING A CSV FILE")

with open(
    "students.csv",
    "r"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ======================================
# 3. APPENDING DATA TO CSV
# ======================================

print("\n3. APPENDING DATA")

with open(
    "students.csv",
    "a",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Ankit", 19, 91]
    )

print("New Record Added")

# ======================================
# 4. READING UPDATED FILE
# ======================================

print("\n4. UPDATED CSV CONTENT")

with open(
    "students.csv",
    "r"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ======================================
# 5. USING DICTIONARY WRITER
# ======================================

print("\n5. DICTIONARY WRITER")

with open(
    "employees.csv",
    "w",
    newline=""
) as file:

    fieldnames = [
        "Name",
        "Department",
        "Salary"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow({
        "Name": "Saloni",
        "Department": "Data Science",
        "Salary": 50000
    })

print("Employee CSV Created")

# ======================================
# 6. USING DICTIONARY READER
# ======================================

print("\n6. DICTIONARY READER")

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)

# ======================================
# 7. COUNT RECORDS
# ======================================

print("\n7. COUNT RECORDS")

record_count = 0

with open(
    "students.csv",
    "r"
) as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        record_count += 1

print("Total Records:", record_count)

# ======================================
# 8. SEARCH STUDENT
# ======================================

print("\n8. SEARCH STUDENT")

search_name = "Saloni"

with open(
    "students.csv",
    "r"
) as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        if row[0] == search_name:
            print("Student Found:", row)

# ======================================
# 9. USER INPUT TO CSV
# ======================================

print("\n9. USER INPUT TO CSV")

name = input("Enter Name: ")
age = input("Enter Age: ")
marks = input("Enter Marks: ")

with open(
    "students.csv",
    "a",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        [name, age, marks]
    )

print("Record Saved Successfully")

# ======================================
# 10. DISPLAY ALL RECORDS
# ======================================

print("\n10. DISPLAY ALL RECORDS")

with open(
    "students.csv",
    "r"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT DATABASE")

students = [
    ["Name", "Math", "Python", "DBMS"],
    ["Saloni", 92, 95, 90],
    ["Riya", 88, 91, 87],
    ["Ankit", 85, 89, 93]
]

with open(
    "student_database.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerows(students)

print("Database Created Successfully")

print("\nDatabase Content")

with open(
    "student_database.csv",
    "r"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a CSV file containing:

Name
Age
City

Add at least 3 records.

Exercise 2:
Read all records from the CSV file.

Exercise 3:
Count total records in the CSV file.

Exercise 4:
Search for a specific student
using their name.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Management System.

Requirements:

1. Add Student
2. View Students
3. Search Student
4. Count Students

Store all data in a CSV file.

Fields:

- Name
- Age
- Course
- Marks
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 028 Completed Successfully!")