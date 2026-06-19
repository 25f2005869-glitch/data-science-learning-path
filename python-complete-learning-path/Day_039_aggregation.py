# ======================================
# Day 039: Aggregation
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Aggregation in Python
# Object-Oriented Programming
# ======================================

print("=" * 50)
print("DAY 039 - AGGREGATION")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Aggregation?

Aggregation is a special form of
association where one object uses
another object, but both objects
can exist independently.

Aggregation represents:

"HAS-A Relationship"

Difference:

Composition:
If Parent is destroyed,
Child is also destroyed.

Aggregation:
Parent and Child can exist
independently.

Examples:

1. Student HAS-A Course
2. Employee HAS-A Department
3. Teacher HAS-A Subject

Aggregation is a weaker relationship
than Composition.
"""

# ======================================
# 1. SIMPLE AGGREGATION
# ======================================

print("\n1. SIMPLE AGGREGATION")

class Department:

    def __init__(self, name):
        self.name = name

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
print(employee.department.name)

# ======================================
# 2. STUDENT AND COURSE
# ======================================

print("\n2. STUDENT AND COURSE")

class Course:

    def __init__(self, course_name):
        self.course_name = course_name

class Student:

    def __init__(
        self,
        student_name,
        course
    ):

        self.student_name = student_name
        self.course = course

course = Course(
    "BS in Data Science"
)

student = Student(
    "Saloni",
    course
)

print(student.student_name)
print(student.course.course_name)

# ======================================
# 3. TEACHER AND SUBJECT
# ======================================

print("\n3. TEACHER AND SUBJECT")

class Subject:

    def __init__(self, name):
        self.name = name

class Teacher:

    def __init__(
        self,
        teacher_name,
        subject
    ):

        self.teacher_name = teacher_name
        self.subject = subject

subject = Subject("Mathematics")

teacher = Teacher(
    "Dr. Sharma",
    subject
)

print(teacher.teacher_name)
print(teacher.subject.name)

# ======================================
# 4. BANK CUSTOMER
# ======================================

print("\n4. BANK CUSTOMER")

class Account:

    def __init__(self, balance):
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
# 5. UNIVERSITY SYSTEM
# ======================================

print("\n5. UNIVERSITY SYSTEM")

class Professor:

    def __init__(self, name):
        self.name = name

class University:

    def __init__(
        self,
        university_name,
        professor
    ):

        self.university_name = university_name
        self.professor = professor

professor = Professor(
    "Dr. Kumar"
)

university = University(
    "IIT Madras",
    professor
)

print(university.university_name)
print(university.professor.name)

# ======================================
# 6. COMPANY SYSTEM
# ======================================

print("\n6. COMPANY SYSTEM")

class Department:

    def __init__(self, name):
        self.name = name

class Company:

    def __init__(
        self,
        company_name,
        department
    ):

        self.company_name = company_name
        self.department = department

department = Department("IT")

company = Company(
    "Tech Solutions",
    department
)

print(company.company_name)
print(company.department.name)

# ======================================
# 7. LIBRARY SYSTEM
# ======================================

print("\n7. LIBRARY SYSTEM")

class Book:

    def __init__(self, title):
        self.title = title

class Library:

    def __init__(
        self,
        library_name,
        book
    ):

        self.library_name = library_name
        self.book = book

book = Book(
    "Python Programming"
)

library = Library(
    "Central Library",
    book
)

print(library.library_name)
print(library.book.title)

# ======================================
# 8. USER INPUT EXAMPLE
# ======================================

print("\n8. USER INPUT EXAMPLE")

class Course:

    def __init__(self, name):
        self.name = name

class Student:

    def __init__(
        self,
        student_name,
        course
    ):

        self.student_name = student_name
        self.course = course

student_name = input(
    "Enter Student Name: "
)

course_name = input(
    "Enter Course Name: "
)

course = Course(course_name)

student = Student(
    student_name,
    course
)

print("\nStudent Details")
print("-" * 30)

print("Name   :", student.student_name)
print("Course :", student.course.name)

# ======================================
# 9. HOSPITAL SYSTEM
# ======================================

print("\n9. HOSPITAL SYSTEM")

class Doctor:

    def __init__(self, name):
        self.name = name

class Patient:

    def __init__(
        self,
        patient_name,
        doctor
    ):

        self.patient_name = patient_name
        self.doctor = doctor

doctor = Doctor(
    "Dr. Singh"
)

patient = Patient(
    "Rahul",
    doctor
)

print(patient.patient_name)
print(patient.doctor.name)

# ======================================
# 10. SCHOOL SYSTEM
# ======================================

print("\n10. SCHOOL SYSTEM")

class Principal:

    def __init__(self, name):
        self.name = name

class School:

    def __init__(
        self,
        school_name,
        principal
    ):

        self.school_name = school_name
        self.principal = principal

principal = Principal(
    "Mr. Verma"
)

school = School(
    "ABC School",
    principal
)

print(school.school_name)
print(school.principal.name)

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

class Student:

    def __init__(
        self,
        name,
        marks
    ):

        self.name = name
        self.marks = marks

    def total_marks(self):

        return (
            self.marks.math +
            self.marks.python +
            self.marks.dbms
        )

    def display_report(self):

        print("\nStudent Report")
        print("-" * 30)

        print("Name  :", self.name)
        print(
            "Total :",
            self.total_marks()
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

Course Class
Student Class

Student HAS-A Course.

Exercise 2:
Create:

Department Class
Employee Class

Employee HAS-A Department.

Exercise 3:
Create:

Book Class
Library Class

Library HAS-A Book.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a University Management System.

Classes:

1. Student
2. Course
3. Professor

Student HAS-A Course
Student HAS-A Professor

Display:

- Student Name
- Course Name
- Professor Name
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 039 Completed Successfully!")