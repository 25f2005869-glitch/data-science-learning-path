# ======================================
# Day 036: Static and Class Methods
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Static Methods and
# Class Methods in Python
# ======================================

print("=" * 50)
print("DAY 036 - STATIC AND CLASS METHODS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Types of Methods in Python Classes:

1. Instance Methods
2. Class Methods
3. Static Methods

--------------------------------------

Instance Method

- Works with object data.
- Uses self parameter.

--------------------------------------

Class Method

- Works with class-level data.
- Uses cls parameter.
- Decorator: @classmethod

--------------------------------------

Static Method

- Does not use self or cls.
- Independent utility function.
- Decorator: @staticmethod
"""

# ======================================
# 1. INSTANCE METHOD
# ======================================

print("\n1. INSTANCE METHOD")

class Student:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Student Name:", self.name)

student = Student("Saloni")

student.display()

# ======================================
# 2. CLASS METHOD
# ======================================

print("\n2. CLASS METHOD")

class College:

    college_name = "IIT Madras"

    @classmethod
    def display_college(cls):

        print("College:", cls.college_name)

College.display_college()

# ======================================
# 3. MODIFY CLASS ATTRIBUTE
# ======================================

print("\n3. MODIFY CLASS ATTRIBUTE")

class College:

    college_name = "IIT Madras"

    @classmethod
    def change_college_name(
        cls,
        new_name
    ):

        cls.college_name = new_name

College.change_college_name(
    "Indian Institute of Technology Madras"
)

print(College.college_name)

# ======================================
# 4. STATIC METHOD
# ======================================

print("\n4. STATIC METHOD")

class Calculator:

    @staticmethod
    def add(a, b):

        return a + b

print(
    "Addition:",
    Calculator.add(10, 20)
)

# ======================================
# 5. STATIC METHOD EXAMPLE
# ======================================

print("\n5. STATIC METHOD EXAMPLE")

class Mathematics:

    @staticmethod
    def square(number):

        return number ** 2

print(
    "Square:",
    Mathematics.square(5)
)

# ======================================
# 6. CLASS METHOD AS ALTERNATIVE
# ======================================

print("\n6. ALTERNATIVE CONSTRUCTOR")

class Student:

    def __init__(
        self,
        name,
        age
    ):

        self.name = name
        self.age = age

    @classmethod
    def from_string(
        cls,
        student_data
    ):

        name, age = student_data.split(",")

        return cls(
            name,
            int(age)
        )

student = Student.from_string(
    "Saloni,17"
)

print(student.name)
print(student.age)

# ======================================
# 7. COMBINING ALL METHODS
# ======================================

print("\n7. COMBINING ALL METHODS")

class Employee:

    company = "Tech Company"

    def __init__(
        self,
        name
    ):

        self.name = name

    def display(self):

        print("Employee:", self.name)

    @classmethod
    def company_info(cls):

        print("Company:", cls.company)

    @staticmethod
    def working_hours():

        print(
            "Working Hours: 9 AM - 5 PM"
        )

employee = Employee("Saloni")

employee.display()

Employee.company_info()

Employee.working_hours()

# ======================================
# 8. USER INPUT EXAMPLE
# ======================================

print("\n8. USER INPUT EXAMPLE")

class Student:

    college = "IIT Madras"

    def __init__(
        self,
        name
    ):

        self.name = name

    @classmethod
    def show_college(cls):

        print(
            "College:",
            cls.college
        )

    @staticmethod
    def welcome():

        print(
            "Welcome Student"
        )

name = input(
    "Enter Student Name: "
)

student = Student(name)

Student.show_college()

Student.welcome()

print("Student:", student.name)

# ======================================
# 9. TEMPERATURE CONVERTER
# ======================================

print("\n9. TEMPERATURE CONVERTER")

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(
        celsius
    ):

        return (
            celsius * 9 / 5
        ) + 32

print(
    Temperature.celsius_to_fahrenheit(
        25
    )
)

# ======================================
# 10. BANK EXAMPLE
# ======================================

print("\n10. BANK EXAMPLE")

class Bank:

    bank_name = "State Bank"

    @classmethod
    def change_bank_name(
        cls,
        name
    ):

        cls.bank_name = name

Bank.change_bank_name(
    "National Bank"
)

print(Bank.bank_name)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT SYSTEM")

class Student:

    college_name = "IIT Madras"

    def __init__(
        self,
        name,
        marks
    ):

        self.name = name
        self.marks = marks

    def display(self):

        print(
            f"{self.name} : {self.marks}"
        )

    @classmethod
    def college_info(cls):

        print(
            "College:",
            cls.college_name
        )

    @staticmethod
    def grading_system():

        print(
            "Pass Marks: 40"
        )

student = Student(
    "Saloni",
    95
)

student.display()

Student.college_info()

Student.grading_system()

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Calculator class.

Create static methods:

- add()
- subtract()

Exercise 2:
Create a College class.

Create a class method to
display college information.

Exercise 3:
Create a Temperature class.

Create static methods for:

- Celsius to Fahrenheit
- Fahrenheit to Celsius
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Library Management System.

Class: Library

Class Attribute:
- library_name

Instance Attributes:
- book_title
- author

Methods:

1. Instance Method:
   display_book()

2. Class Method:
   display_library()

3. Static Method:
   calculate_late_fee(days)

Late Fee:
₹5 per day
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 036 Completed Successfully!")