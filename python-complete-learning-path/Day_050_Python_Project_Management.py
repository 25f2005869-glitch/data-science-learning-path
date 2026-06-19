# ======================================
# Day 050: Python Project Management
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Professional Python
# Project Structure and Management
# ======================================

print("=" * 60)
print("DAY 050 - PYTHON PROJECT MANAGEMENT")
print("=" * 60)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Project Management?

Project Management in Python means
organizing files, folders, code,
documentation, and dependencies
professionally.

Benefits:

1. Clean Code Organization
2. Easy Maintenance
3. Better Collaboration
4. Professional Development
5. Industry Standards

Typical Python Project Structure:

project_name/
│
├── README.md
├── requirements.txt
├── main.py
├── config.py
│
├── data/
├── notebooks/
├── src/
├── tests/
└── docs/

This structure is widely used in:

- Data Science
- Machine Learning
- Software Development
"""

# ======================================
# 1. PROJECT INFORMATION
# ======================================

print("\n1. PROJECT INFORMATION")

project_name = "Student Management System"

version = "1.0.0"

author = "Saloni Tiwari"

print("Project :", project_name)
print("Version :", version)
print("Author  :", author)

# ======================================
# 2. PROJECT CONFIGURATION
# ======================================

print("\n2. PROJECT CONFIGURATION")

config = {
    "database": "student.db",
    "max_students": 1000,
    "debug_mode": True
}

print(config)

# ======================================
# 3. USING FUNCTIONS
# ======================================

print("\n3. USING FUNCTIONS")

def display_project_info():

    print("Project Management Demo")

display_project_info()

# ======================================
# 4. LOGGING EXAMPLE
# ======================================

print("\n4. LOGGING EXAMPLE")

import logging

logging.basicConfig(
    level=logging.INFO
)

logging.info(
    "Project Started Successfully"
)

# ======================================
# 5. DATE AND TIME
# ======================================

print("\n5. DATE AND TIME")

from datetime import datetime

current_time = datetime.now()

print(current_time)

# ======================================
# 6. FILE PATH MANAGEMENT
# ======================================

print("\n6. FILE PATH MANAGEMENT")

from pathlib import Path

project_folder = Path.cwd()

print("Current Folder:")
print(project_folder)

# ======================================
# 7. CREATE DIRECTORY
# ======================================

print("\n7. CREATE DIRECTORY")

data_folder = Path("data")

data_folder.mkdir(
    exist_ok=True
)

print("Data Folder Created")

# ======================================
# 8. CREATE FILE
# ======================================

print("\n8. CREATE FILE")

file_path = Path(
    "data/sample.txt"
)

file_path.write_text(
    "Python Project Management"
)

print("File Created")

# ======================================
# 9. READ FILE
# ======================================

print("\n9. READ FILE")

content = file_path.read_text()

print(content)

# ======================================
# 10. REQUIREMENTS LIST
# ======================================

print("\n10. REQUIREMENTS")

requirements = [
    "numpy",
    "pandas",
    "matplotlib"
]

for package in requirements:

    print(package)

# ======================================
# 11. ENVIRONMENT INFO
# ======================================

print("\n11. ENVIRONMENT INFO")

import sys

print("Python Version:")
print(sys.version)

# ======================================
# 12. PROJECT TASK LIST
# ======================================

print("\n12. PROJECT TASK LIST")

tasks = [
    "Create Project",
    "Write Code",
    "Test Code",
    "Document Project",
    "Deploy Project"
]

for task in tasks:

    print("-", task)

# ======================================
# 13. SIMPLE TEST FUNCTION
# ======================================

print("\n13. TEST FUNCTION")

def add(a, b):

    return a + b

assert add(10, 20) == 30

print("Test Passed")

# ======================================
# 14. USER INPUT PROJECT
# ======================================

print("\n14. USER INPUT PROJECT")

project = input(
    "Enter Project Name: "
)

print(
    f"Project '{project}' Created"
)

# ======================================
# 15. PROJECT REPORT
# ======================================

print("\n15. PROJECT REPORT")

print("-" * 40)

print("Project Name :", project)
print("Status       : Active")
print("Version      : 1.0.0")

print("-" * 40)

# ======================================
# 16. MINI PROJECT
# ======================================

print("\n16. MINI PROJECT")

class Project:

    def __init__(
        self,
        name,
        status
    ):

        self.name = name
        self.status = status

    def display(self):

        print("\nProject Details")
        print("-" * 30)

        print("Name   :", self.name)
        print("Status :", self.status)

project1 = Project(
    "Student Dashboard",
    "Completed"
)

project1.display()

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a project folder
using pathlib.

Exercise 2:
Create and read a file.

Exercise 3:
Create a project class.

Exercise 4:
Display Python version.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Project Tracker.

Features:

1. Project Name
2. Version
3. Author
4. Status

Display a professional
project report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 050 Completed Successfully!")