# ======================================
# Day 032: Inheritance
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Inheritance and Code
# Reusability in Python
# ======================================

print("=" * 50)
print("DAY 032 - INHERITANCE")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Inheritance?

Inheritance allows one class to
acquire the properties and methods
of another class.

Benefits:

1. Code Reusability
2. Reduced Redundancy
3. Better Organization
4. Easy Maintenance

Terminology:

Parent Class (Base Class)
        ↓
Child Class (Derived Class)

Syntax:

class Parent:
    pass

class Child(Parent):
    pass
"""

# ======================================
# 1. SIMPLE INHERITANCE
# ======================================

print("\n1. SIMPLE INHERITANCE")

class Person:

    def display(self):
        print("I am a Person")

class Student(Person):
    pass

student = Student()

student.display()

# ======================================
# 2. ACCESSING PARENT METHODS
# ======================================

print("\n2. ACCESSING PARENT METHODS")

class Animal:

    def speak(self):
        print("Animal can make sounds")

class Dog(Animal):
    pass

dog = Dog()

dog.speak()

# ======================================
# 3. PARENT CONSTRUCTOR
# ======================================

print("\n3. PARENT CONSTRUCTOR")

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

student = Student("Saloni")

print(student.name)

# ======================================
# 4. USING super()
# ======================================

print("\n4. USING super()")

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course

student = Student(
    "Saloni",
    "Data Science"
)

print(student.name)
print(student.course)

# ======================================
# 5. ADDING NEW METHODS
# ======================================

print("\n5. ADDING NEW METHODS")

class Person:

    def greet(self):
        print("Welcome")

class Student(Person):

    def study(self):
        print("Student is studying")

student = Student()

student.greet()
student.study()

# ======================================
# 6. METHOD OVERRIDING
# ======================================

print("\n6. METHOD OVERRIDING")

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()

# ======================================
# 7. MULTILEVEL INHERITANCE
# ======================================

print("\n7. MULTILEVEL INHERITANCE")

class Person:

    def introduce(self):
        print("I am a Person")

class Student(Person):

    def study(self):
        print("Studying")

class GraduateStudent(Student):

    def research(self):
        print("Doing Research")

student = GraduateStudent()

student.introduce()
student.study()
student.research()

# ======================================
# 8. HIERARCHICAL INHERITANCE
# ======================================

print("\n8. HIERARCHICAL INHERITANCE")

class Person:

    def display(self):
        print("Person Class")

class Student(Person):
    pass

class Teacher(Person):
    pass

student = Student()
teacher = Teacher()

student.display()
teacher.display()

# ======================================
# 9. USER INPUT EXAMPLE
# ======================================

print("\n9. USER INPUT EXAMPLE")

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def show(self):
        print("Student Name:", self.name)

name = input("Enter Name: ")

student = Student(name)

student.show()

# ======================================
# 10. EMPLOYEE MANAGEMENT SYSTEM
# ======================================

print("\n10. EMPLOYEE MANAGEMENT SYSTEM")

class Employee:

    def __init__(self, name):
        self.name = name

class Manager(Employee):

    def manage(self):
        print(self.name, "manages the team")

manager = Manager("Amit")

manager.manage()

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT RESULT")

class Student:

    def __init__(self, name):
        self.name = name

class Result(Student):

    def __init__(
        self,
        name,
        math,
        python,
        dbms
    ):

        super().__init__(name)

        self.math = math
        self.python = python
        self.dbms = dbms

    def total(self):

        return (
            self.math +
            self.python +
            self.dbms
        )

    def average(self):

        return self.total() / 3

    def display_report(self):

        print("\nStudent Report")
        print("-" * 30)

        print("Name    :", self.name)
        print("Total   :", self.total())
        print(
            "Average :",
            round(
                self.average(),
                2
            )
        )

student = Result(
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
Create a class Vehicle.

Create a child class Car.

Display vehicle information.

Exercise 2:
Create a class Person.

Create a child class Teacher.

Add a new method in Teacher.

Exercise 3:
Create multilevel inheritance:

Animal
  ↓
Dog
  ↓
Puppy

Display methods from all classes.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a College Management System.

Parent Class:
Person

Child Classes:
Student
Teacher

Attributes:
- Name
- Age

Methods:
- Display Information

Add specific methods for
Student and Teacher.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 032 Completed Successfully!")