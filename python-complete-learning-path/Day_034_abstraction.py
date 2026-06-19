# ======================================
# Day 034: Abstraction
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Abstraction and
# Abstract Classes in Python
# ======================================

print("=" * 50)
print("DAY 034 - ABSTRACTION")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Abstraction?

Abstraction means hiding internal
implementation details and showing
only the essential features to users.

Real-Life Examples:

1. ATM Machine
2. Car Driving
3. Mobile Phone
4. Television Remote

Users interact with features without
knowing the internal implementation.

Benefits:

1. Security
2. Simplicity
3. Better Design
4. Reduced Complexity

Python provides abstraction using:

ABC (Abstract Base Class)

Module:

from abc import ABC, abstractmethod
"""

# ======================================
# IMPORTS
# ======================================

from abc import ABC, abstractmethod

# ======================================
# 1. ABSTRACT CLASS
# ======================================

print("\n1. ABSTRACT CLASS")

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

print("Abstract Class Created")

# ======================================
# 2. IMPLEMENTING ABSTRACT METHOD
# ======================================

print("\n2. IMPLEMENTING ABSTRACT METHOD")

class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width

rectangle = Rectangle(10, 5)

print("Area:", rectangle.area())

# ======================================
# 3. MULTIPLE SHAPES
# ======================================

print("\n3. MULTIPLE SHAPES")

class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return 3.14159 * self.radius ** 2

circle = Circle(7)

print("Area:", round(circle.area(), 2))

# ======================================
# 4. VEHICLE EXAMPLE
# ======================================

print("\n4. VEHICLE EXAMPLE")

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

class Bike(Vehicle):

    def start(self):
        print("Bike Started")

car = Car()
bike = Bike()

car.start()
bike.start()

# ======================================
# 5. PAYMENT SYSTEM
# ======================================

print("\n5. PAYMENT SYSTEM")

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print(f"UPI Payment: ₹{amount}")

class CreditCard(Payment):

    def pay(self, amount):
        print(f"Credit Card Payment: ₹{amount}")

upi = UPI()
card = CreditCard()

upi.pay(500)
card.pay(1000)

# ======================================
# 6. EMPLOYEE EXAMPLE
# ======================================

print("\n6. EMPLOYEE EXAMPLE")

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Developing Software")

class Teacher(Employee):

    def work(self):
        print("Teaching Students")

developer = Developer()
teacher = Teacher()

developer.work()
teacher.work()

# ======================================
# 7. POLYMORPHISM + ABSTRACTION
# ======================================

print("\n7. POLYMORPHISM + ABSTRACTION")

employees = [
    Developer(),
    Teacher()
]

for employee in employees:
    employee.work()

# ======================================
# 8. USER INPUT EXAMPLE
# ======================================

print("\n8. USER INPUT EXAMPLE")

class Person(ABC):

    @abstractmethod
    def role(self):
        pass

class Student(Person):

    def role(self):
        print("I am a Student")

class Professor(Person):

    def role(self):
        print("I am a Professor")

choice = input(
    "Enter student/professor: "
).lower()

if choice == "student":
    person = Student()
else:
    person = Professor()

person.role()

# ======================================
# 9. BANKING SYSTEM
# ======================================

print("\n9. BANKING SYSTEM")

class Account(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):

    def calculate_interest(self):
        print("Savings Interest: 4%")

class FixedDeposit(Account):

    def calculate_interest(self):
        print("FD Interest: 7%")

savings = SavingsAccount()
fd = FixedDeposit()

savings.calculate_interest()
fd.calculate_interest()

# ======================================
# 10. ONLINE COURSE PLATFORM
# ======================================

print("\n10. ONLINE COURSE PLATFORM")

class Course(ABC):

    @abstractmethod
    def course_type(self):
        pass

class ProgrammingCourse(Course):

    def course_type(self):
        print("Programming Course")

class MathematicsCourse(Course):

    def course_type(self):
        print("Mathematics Course")

programming = ProgrammingCourse()
mathematics = MathematicsCourse()

programming.course_type()
mathematics.course_type()

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - RESULT SYSTEM")

class Result(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass

class Undergraduate(Result):

    def calculate_grade(self):
        print("Grade Calculated for UG")

class Postgraduate(Result):

    def calculate_grade(self):
        print("Grade Calculated for PG")

students = [
    Undergraduate(),
    Postgraduate()
]

for student in students:
    student.calculate_grade()

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create an abstract class Animal.

Create child classes:

- Dog
- Cat

Implement sound() method.

Exercise 2:
Create an abstract class Vehicle.

Create child classes:

- Car
- Bike

Implement start() method.

Exercise 3:
Create an abstract class Employee.

Create:

- Teacher
- Developer

Implement work() method.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Library Management System.

Abstract Class:
Book

Abstract Method:
display_details()

Child Classes:

1. PrintedBook
2. EBook

Implement display_details()
for both classes.

Display details using
polymorphism.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 034 Completed Successfully!")