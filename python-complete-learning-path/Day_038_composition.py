# ======================================
# Day 038: Composition
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Composition in Python
# Object-Oriented Programming
# ======================================

print("=" * 50)
print("DAY 038 - COMPOSITION")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Composition?

Composition is a relationship where
one class contains an object of
another class.

Composition represents:

"HAS-A Relationship"

Examples:

Car HAS-A Engine
Library HAS-A Books
Student HAS-A Address

Benefits:

1. Code Reusability
2. Better Modularity
3. Flexible Design
4. Real-World Modeling

Composition is generally preferred
over deep inheritance structures.
"""

# ======================================
# 1. SIMPLE COMPOSITION
# ======================================

print("\n1. SIMPLE COMPOSITION")

class Engine:

    def start(self):
        print("Engine Started")

class Car:

    def __init__(self):
        self.engine = Engine()

car = Car()

car.engine.start()

# ======================================
# 2. STUDENT AND ADDRESS
# ======================================

print("\n2. STUDENT AND ADDRESS")

class Address:

    def __init__(
        self,
        city,
        state
    ):

        self.city = city
        self.state = state

class Student:

    def __init__(
        self,
        name,
        address
    ):

        self.name = name
        self.address = address

address = Address(
    "Aurangabad",
    "Bihar"
)

student = Student(
    "Saloni",
    address
)

print(student.name)
print(student.address.city)
print(student.address.state)

# ======================================
# 3. LIBRARY AND BOOK
# ======================================

print("\n3. LIBRARY AND BOOK")

class Book:

    def __init__(self, title):

        self.title = title

class Library:

    def __init__(self):

        self.book = Book(
            "Python Programming"
        )

library = Library()

print(library.book.title)

# ======================================
# 4. CAR AND ENGINE
# ======================================

print("\n4. CAR AND ENGINE")

class Engine:

    def start(self):
        print("Engine Running")

class Car:

    def __init__(self):

        self.engine = Engine()

    def drive(self):

        self.engine.start()

        print("Car is Moving")

car = Car()

car.drive()

# ======================================
# 5. COMPUTER AND CPU
# ======================================

print("\n5. COMPUTER AND CPU")

class CPU:

    def process(self):

        print("Processing Data")

class Computer:

    def __init__(self):

        self.cpu = CPU()

computer = Computer()

computer.cpu.process()

# ======================================
# 6. UNIVERSITY SYSTEM
# ======================================

print("\n6. UNIVERSITY SYSTEM")

class Course:

    def __init__(self, name):

        self.name = name

class Student:

    def __init__(
        self,
        name,
        course
    ):

        self.name = name
        self.course = course

course = Course(
    "BS in Data Science"
)

student = Student(
    "Saloni",
    course
)

print(student.name)
print(student.course.name)

# ======================================
# 7. BANK ACCOUNT SYSTEM
# ======================================

print("\n7. BANK ACCOUNT SYSTEM")

class Account:

    def __init__(
        self,
        balance
    ):

        self.balance = balance

class Customer:

    def __init__(
        self,
        name,
        account
    ):

        self.name = name
        self.account = account

account = Account(10000)

customer = Customer(
    "Saloni",
    account
)

print(customer.name)
print(customer.account.balance)

# ======================================
# 8. USER INPUT EXAMPLE
# ======================================

print("\n8. USER INPUT EXAMPLE")

class Address:

    def __init__(
        self,
        city
    ):

        self.city = city

class Student:

    def __init__(
        self,
        name,
        address
    ):

        self.name = name
        self.address = address

name = input("Enter Name: ")
city = input("Enter City: ")

address = Address(city)

student = Student(
    name,
    address
)

print("\nStudent Details")
print("-" * 30)

print("Name :", student.name)
print("City :", student.address.city)

# ======================================
# 9. COMPANY SYSTEM
# ======================================

print("\n9. COMPANY SYSTEM")

class Department:

    def __init__(
        self,
        department_name
    ):

        self.department_name = department_name

class Employee:

    def __init__(
        self,
        employee_name,
        department
    ):

        self.employee_name = employee_name
        self.department = department

department = Department(
    "Data Science"
)

employee = Employee(
    "Saloni",
    department
)

print(employee.employee_name)
print(employee.department.department_name)

# ======================================
# 10. ONLINE SHOPPING SYSTEM
# ======================================

print("\n10. ONLINE SHOPPING SYSTEM")

class Product:

    def __init__(
        self,
        name,
        price
    ):

        self.name = name
        self.price = price

class Order:

    def __init__(
        self,
        product
    ):

        self.product = product

product = Product(
    "Laptop",
    50000
)

order = Order(product)

print(order.product.name)
print(order.product.price)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT RESULT")

class Marks:

    def __init__(
        self,
        math,
        python,
        dbms
    ):

        self.math = math
        self.python = python
        self.dbms = dbms

    def total(self):

        return (
            self.math +
            self.python +
            self.dbms
        )

class Student:

    def __init__(
        self,
        name,
        marks
    ):

        self.name = name
        self.marks = marks

    def display_report(self):

        print("\nStudent Report")
        print("-" * 30)

        print("Name  :", self.name)
        print(
            "Total :",
            self.marks.total()
        )

marks = Marks(
    92,
    95,
    90
)

student = Student(
    "Saloni Tiwari",
    marks
)

student.display_report()

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create:

Engine Class
Car Class

Car should contain Engine.

Exercise 2:
Create:

Book Class
Library Class

Library should contain Book.

Exercise 3:
Create:

Department Class
Employee Class

Employee should contain Department.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a College Management System.

Classes:

1. Address
2. Course
3. Student

Student HAS-A:
- Address
- Course

Display:

- Student Name
- City
- State
- Course Name
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 038 Completed Successfully!")