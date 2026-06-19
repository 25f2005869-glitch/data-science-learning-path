# ======================================
# Day 020: Packages and Project Structure
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Python Packages and
# Professional Project Structure
# ======================================

print("=" * 50)
print("DAY 020 - PACKAGES AND PROJECT STRUCTURE")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Package?

A package is a collection of related
Python modules organized in a directory.

Benefits of Packages:

1. Better Code Organization
2. Reusability
3. Scalability
4. Professional Project Structure

Package Structure:

my_package/
│
├── __init__.py
├── math_utils.py
└── string_utils.py

Important:

The __init__.py file tells Python
that the folder should be treated
as a package.
"""

# ======================================
# 1. MODULE VS PACKAGE
# ======================================

print("\n1. MODULE VS PACKAGE")

print("Module  = Single Python File")
print("Package = Collection of Modules")

# ======================================
# 2. EXAMPLE PACKAGE STRUCTURE
# ======================================

print("\n2. PACKAGE STRUCTURE")

package_structure = """
calculator_package/
│
├── __init__.py
├── arithmetic.py
├── scientific.py
└── utility.py
"""

print(package_structure)

# ======================================
# 3. IMPORTING FROM A PACKAGE
# ======================================

print("\n3. IMPORTING FROM A PACKAGE")

"""
Example:

from calculator_package.arithmetic import add

result = add(10, 20)
"""

print("Package Import Example Shown")

# ======================================
# 4. USING CUSTOM FUNCTIONS
# ======================================

print("\n4. CUSTOM FUNCTION EXAMPLE")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Addition    :", add(10, 5))
print("Subtraction :", subtract(10, 5))

# ======================================
# 5. PROJECT FOLDER STRUCTURE
# ======================================

print("\n5. PROFESSIONAL PROJECT STRUCTURE")

project_structure = """
student_management_system/
│
├── main.py
├── database.py
├── utilities.py
├── requirements.txt
│
├── data/
│   └── students.csv
│
├── reports/
│
└── README.md
"""

print(project_structure)

# ======================================
# 6. WHY PROJECT STRUCTURE MATTERS
# ======================================

print("\n6. WHY PROJECT STRUCTURE MATTERS")

advantages = [
    "Easy Maintenance",
    "Scalability",
    "Professional Development",
    "Team Collaboration",
    "Better Code Organization"
]

for item in advantages:
    print("-", item)

# ======================================
# 7. __name__ == '__main__'
# ======================================

print("\n7. __name__ == '__main__'")

def greet():
    print("Welcome to Python")

if __name__ == "__main__":
    greet()

# ======================================
# 8. REQUIREMENTS FILE
# ======================================

print("\n8. REQUIREMENTS.TXT")

requirements_example = """
numpy
pandas
matplotlib
"""

print(requirements_example)

# ======================================
# 9. README FILE PURPOSE
# ======================================

print("\n9. README FILE")

print("""
README.md should contain:

1. Project Title
2. Description
3. Features
4. Installation Steps
5. Usage Instructions
6. Author Information
""")

# ======================================
# 10. PYTHON COMPLETE LEARNING PATH
# ======================================

print("\n10. REPOSITORY STRUCTURE")

repository_structure = """
python-complete-learning-path/
│
├── README.md
│
├── day_001_variables_and_datatypes.py
├── day_002_operators_and_expressions.py
├── day_003_input_and_output.py
├── day_004_conditional_statements.py
├── day_005_for_loop.py
│
├── ...
│
├── day_020_packages_and_project_structure.py
"""

print(repository_structure)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - PROJECT PLANNER")

project = {
    "Project Name": "Student Management System",
    "Language": "Python",
    "Database": "SQLite",
    "Version": "1.0"
}

print("\nProject Details")
print("-" * 30)

for key, value in project.items():
    print(f"{key} : {value}")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a folder structure for:

Library Management System

Exercise 2:
Write a sample requirements.txt file.

Exercise 3:
Create a sample README structure.

Exercise 4:
Design a package containing:

- math_utils.py
- string_utils.py
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Design a Professional Python Project.

Requirements:

1. Project Name
2. Folder Structure
3. Modules Required
4. README Contents
5. requirements.txt Contents

Present everything in a structured way.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 020 Completed Successfully!")