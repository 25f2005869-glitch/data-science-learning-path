# ======================================
# Day 031: Encapsulation
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Encapsulation and
# Data Hiding in Python
# ======================================

print("=" * 50)
print("DAY 031 - ENCAPSULATION")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Encapsulation?

Encapsulation is the process of
binding data (attributes) and methods
(functions) together inside a class.

It also helps in restricting direct
access to sensitive data.

Benefits:

1. Data Security
2. Better Control
3. Code Maintainability
4. Data Hiding

Access Modifiers in Python:

1. Public
2. Protected (_variable)
3. Private (__variable)

Note:

Python does not enforce strict access
control, but naming conventions are
used to indicate access levels.
"""

# ======================================
# 1. PUBLIC ATTRIBUTE
# ======================================

print("\n1. PUBLIC ATTRIBUTE")

class Student:

    def __init__(self):
        self.name = "Saloni"

student = Student()

print(student.name)

# ======================================
# 2. PROTECTED ATTRIBUTE
# ======================================

print("\n2. PROTECTED ATTRIBUTE")

class Student:

    def __init__(self):
        self._course = "BS in Data Science"

student = Student()

print(student._course)

# ======================================
# 3. PRIVATE ATTRIBUTE
# ======================================

print("\n3. PRIVATE ATTRIBUTE")

class Student:

    def __init__(self):
        self.__age = 17

student = Student()

# print(student.__age)  # Error

print("Private Attribute Created")

# ======================================
# 4. ACCESS PRIVATE ATTRIBUTE
# ======================================

print("\n4. ACCESS PRIVATE ATTRIBUTE")

class Student:

    def __init__(self):
        self.__age = 17

    def display_age(self):
        print("Age:", self.__age)

student = Student()

student.display_age()

# ======================================
# 5. GETTER METHOD
# ======================================

print("\n5. GETTER METHOD")

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

print("Balance:", account.get_balance())

# ======================================
# 6. SETTER METHOD
# ======================================

print("\n6. SETTER METHOD")

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def set_balance(self, amount):

        if amount >= 0:
            self.__balance = amount

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

account.set_balance(8000)

print("Updated Balance:", account.get_balance())

# ======================================
# 7. DATA VALIDATION
# ======================================

print("\n7. DATA VALIDATION")

class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks

student = Student()

student.set_marks(95)

print("Marks:", student.get_marks())

# ======================================
# 8. NAME MANGLING
# ======================================

print("\n8. NAME MANGLING")

class Demo:

    def __init__(self):
        self.__value = 100

demo = Demo()

print(demo._Demo__value)

# ======================================
# 9. USER INPUT EXAMPLE
# ======================================

print("\n9. USER INPUT EXAMPLE")

class User:

    def __init__(self):
        self.__age = 0

    def set_age(self, age):

        if age >= 0:
            self.__age = age
        else:
            print("Invalid Age")

    def get_age(self):
        return self.__age

user = User()

age = int(input("Enter Age: "))

user.set_age(age)

print("Stored Age:", user.get_age())

# ======================================
# 10. BANK ACCOUNT SYSTEM
# ======================================

print("\n10. BANK ACCOUNT SYSTEM")

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)

account.deposit(2000)
account.withdraw(3000)

print("Current Balance:",
      account.get_balance())

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

        self.__math = math
        self.__python = python
        self.__dbms = dbms

    def total_marks(self):

        return (
            self.__math +
            self.__python +
            self.__dbms
        )

    def average_marks(self):

        return self.total_marks() / 3

    def display_report(self):

        print("\nStudent Report")
        print("-" * 30)

        print("Name    :", self.name)
        print("Total   :", self.total_marks())
        print(
            "Average :",
            round(
                self.average_marks(),
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
Create a class Employee.

Private Attribute:
__salary

Create getter and setter methods.

Exercise 2:
Create a class Product.

Private Attribute:
__price

Validate that price is positive.

Exercise 3:
Create a class Student.

Private Attribute:
__marks

Display marks using getter.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Library System.

Class: Book

Private Attributes:
- __title
- __author
- __price

Methods:
- set_price()
- get_price()
- display_details()

Validate that price
cannot be negative.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 031 Completed Successfully!")