# ======================================
# Day 037: Property Decorators
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Property Decorators
# in Python
# ======================================

print("=" * 50)
print("DAY 037 - PROPERTY DECORATORS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Property Decorator?

Property decorators allow methods
to be accessed like attributes.

Decorators Used:

1. @property
2. @property_name.setter
3. @property_name.deleter

Benefits:

1. Data Encapsulation
2. Validation
3. Cleaner Syntax
4. Better Object Control

Without Property:

student.get_name()

With Property:

student.name
"""

# ======================================
# 1. BASIC PROPERTY
# ======================================

print("\n1. BASIC PROPERTY")

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

student = Student("Saloni")

print(student.name)

# ======================================
# 2. PROPERTY WITH SETTER
# ======================================

print("\n2. PROPERTY WITH SETTER")

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

student = Student("Saloni")

student.name = "Saloni Tiwari"

print(student.name)

# ======================================
# 3. PROPERTY WITH VALIDATION
# ======================================

print("\n3. PROPERTY WITH VALIDATION")

class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid Marks")

student = Student(95)

student.marks = 98

print(student.marks)

# ======================================
# 4. PROPERTY WITH DELETER
# ======================================

print("\n4. PROPERTY WITH DELETER")

class Employee:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):

        print("Name Deleted")

        del self._name

employee = Employee("Amit")

del employee.name

# ======================================
# 5. CALCULATED PROPERTY
# ======================================

print("\n5. CALCULATED PROPERTY")

class Rectangle:

    def __init__(
        self,
        length,
        width
    ):

        self.length = length
        self.width = width

    @property
    def area(self):

        return (
            self.length *
            self.width
        )

rectangle = Rectangle(10, 5)

print("Area:", rectangle.area)

# ======================================
# 6. TEMPERATURE CONVERTER
# ======================================

print("\n6. TEMPERATURE CONVERTER")

class Temperature:

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):

        return (
            self._celsius * 9 / 5
        ) + 32

temperature = Temperature(25)

print(
    "Fahrenheit:",
    temperature.fahrenheit
)

# ======================================
# 7. BANK ACCOUNT VALIDATION
# ======================================

print("\n7. BANK ACCOUNT VALIDATION")

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):

        if amount >= 0:
            self._balance = amount
        else:
            print(
                "Negative Balance Not Allowed"
            )

account = BankAccount(5000)

account.balance = 7000

print(account.balance)

# ======================================
# 8. USER INPUT EXAMPLE
# ======================================

print("\n8. USER INPUT EXAMPLE")

class User:

    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value >= 0:
            self._age = value
        else:
            print("Invalid Age")

user = User()

age = int(input("Enter Age: "))

user.age = age

print("Stored Age:", user.age)

# ======================================
# 9. PRODUCT PRICE VALIDATION
# ======================================

print("\n9. PRODUCT PRICE VALIDATION")

class Product:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):

        if value > 0:
            self._price = value
        else:
            print("Invalid Price")

product = Product(1000)

product.price = 1500

print(product.price)

# ======================================
# 10. STUDENT RESULT SYSTEM
# ======================================

print("\n10. STUDENT RESULT SYSTEM")

class Result:

    def __init__(
        self,
        math,
        python,
        dbms
    ):

        self.math = math
        self.python = python
        self.dbms = dbms

    @property
    def total(self):

        return (
            self.math +
            self.python +
            self.dbms
        )

    @property
    def average(self):

        return self.total / 3

result = Result(
    92,
    95,
    90
)

print("Total   :", result.total)
print("Average :", round(result.average, 2))

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - EMPLOYEE SYSTEM")

class Employee:

    def __init__(
        self,
        name,
        salary
    ):

        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value >= 0:
            self._salary = value
        else:
            print("Invalid Salary")

employee = Employee(
    "Saloni",
    50000
)

print("Salary:", employee.salary)

employee.salary = 60000

print(
    "Updated Salary:",
    employee.salary
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a Student class.

Use property decorators for:

- name
- marks

Exercise 2:
Create a Product class.

Validate price using setter.

Exercise 3:
Create a Rectangle class.

Create an area property.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Library Management System.

Class: Book

Attributes:
- title
- price

Requirements:

1. Use @property
2. Validate price
3. Create a discounted_price
   property

Display all information.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 037 Completed Successfully!")