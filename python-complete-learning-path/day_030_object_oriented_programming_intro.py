# ======================================
# Day 030: Object-Oriented Programming
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Object-Oriented
# Programming (OOP) in Python
# ======================================

print("=" * 50)
print("DAY 030 - OBJECT ORIENTED PROGRAMMING")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a
programming paradigm based on objects
and classes.

OOP helps us organize code in a more
structured and reusable way.

Main OOP Concepts:

1. Class
2. Object
3. Attributes
4. Methods
5. Encapsulation
6. Inheritance
7. Polymorphism
8. Abstraction

Real-Life Example:

Class  -> Student

Objects ->
    Saloni
    Riya
    Ankit

Each student has:
- Name
- Age
- Course

These are called attributes.
"""

# ======================================
# 1. CREATING A CLASS
# ======================================

print("\n1. CREATING A CLASS")

class Student:
    pass

print("Class Created Successfully")

# ======================================
# 2. CREATING AN OBJECT
# ======================================

print("\n2. CREATING AN OBJECT")

class Student:
    pass

student1 = Student()

print(student1)

# ======================================
# 3. CLASS WITH ATTRIBUTES
# ======================================

print("\n3. CLASS WITH ATTRIBUTES")

class Student:

    def __init__(self):

        self.name = "Saloni"
        self.age = 17
        self.course = "BS in Data Science"

student = Student()

print(student.name)
print(student.age)
print(student.course)

# ======================================
# 4. CONSTRUCTOR (__init__)
# ======================================

print("\n4. CONSTRUCTOR")

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student1 = Student("Saloni", 17)

print(student1.name)
print(student1.age)

# ======================================
# 5. INSTANCE METHODS
# ======================================

print("\n5. INSTANCE METHODS")

class Student:

    def __init__(self, name):

        self.name = name

    def greet(self):

        print("Hello,", self.name)

student1 = Student("Saloni")

student1.greet()

# ======================================
# 6. MULTIPLE OBJECTS
# ======================================

print("\n6. MULTIPLE OBJECTS")

class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def display(self):

        print(
            f"{self.name} : {self.marks}"
        )

student1 = Student("Saloni", 95)
student2 = Student("Riya", 88)

student1.display()
student2.display()

# ======================================
# 7. CLASS ATTRIBUTES
# ======================================

print("\n7. CLASS ATTRIBUTES")

class College:

    college_name = "IIT Madras"

print(College.college_name)

# ======================================
# 8. MODIFYING ATTRIBUTES
# ======================================

print("\n8. MODIFYING ATTRIBUTES")

class Student:

    def __init__(self, name):

        self.name = name

student = Student("Saloni")

print("Before:", student.name)

student.name = "Saloni Tiwari"

print("After :", student.name)

# ======================================
# 9. USER INPUT EXAMPLE
# ======================================

print("\n9. USER INPUT EXAMPLE")

class Student:

    def __init__(
        self,
        name,
        age
    ):

        self.name = name
        self.age = age

    def display(self):

        print("\nStudent Information")
        print("-" * 30)

        print("Name :", self.name)
        print("Age  :", self.age)

name = input("Enter Name: ")
age = int(input("Enter Age: "))

student = Student(name, age)

student.display()

# ======================================
# 10. SIMPLE BANK ACCOUNT
# ======================================

print("\n10. SIMPLE BANK ACCOUNT")

class BankAccount:

    def __init__(self, balance):

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def display_balance(self):

        print(
            "Current Balance:",
            self.balance
        )

account = BankAccount(5000)

account.deposit(2000)

account.display_balance()

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT RESULT")

class Student:

    def __init__(
        self,
        name,
        math,
        python,
        dbms
    ):

        self.name = name
        self.math = math
        self.python = python
        self.dbms = dbms

    def calculate_total(self):

        return (
            self.math +
            self.python +
            self.dbms
        )

    def calculate_average(self):

        return (
            self.calculate_total() / 3
        )

    def display_report(self):

        print("\nStudent Report")
        print("-" * 30)

        print("Name    :", self.name)
        print(
            "Total   :",
            self.calculate_total()
        )
        print(
            "Average :",
            round(
                self.calculate_average(),
                2
            )
        )

student = Student(
    "Saloni Tiwari",
    92,
    95,
    90
)

student.display_report()

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a class called Car.

Attributes:
- Brand
- Model

Create an object and display data.

Exercise 2:
Create a class called Book.

Attributes:
- Title
- Author

Display the details.

Exercise 3:
Create a Student class with:

- Name
- Marks

Create multiple objects.

Exercise 4:
Create a Rectangle class.

Methods:
- Area
- Perimeter
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Library Management System.

Class: Book

Attributes:
- Title
- Author
- Price

Methods:
- Display Details
- Apply Discount

Create multiple book objects and
display updated prices.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 030 Completed Successfully!")