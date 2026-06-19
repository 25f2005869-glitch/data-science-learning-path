# ======================================
# Day 040: OOP Mini Project
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Student Management System using
# Object-Oriented Programming
# ======================================

print("=" * 60)
print("DAY 040 - OOP MINI PROJECT")
print("STUDENT MANAGEMENT SYSTEM")
print("=" * 60)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Project Objectives:

1. Use Classes and Objects
2. Use Encapsulation
3. Use Inheritance
4. Use Methods
5. Use Lists
6. Use User Input
7. Generate Student Reports

This project combines the major
OOP concepts learned from
Day 030 to Day 039.
"""

# ======================================
# PARENT CLASS
# ======================================

class Person:

    def __init__(
        self,
        name,
        age
    ):

        self.name = name
        self.age = age

# ======================================
# CHILD CLASS
# ======================================

class Student(Person):

    college_name = "IIT Madras"

    def __init__(
        self,
        name,
        age,
        roll_number,
        math,
        python,
        dbms
    ):

        super().__init__(
            name,
            age
        )

        self.roll_number = roll_number

        self.__math = math
        self.__python = python
        self.__dbms = dbms

    # ==================================
    # ENCAPSULATION
    # ==================================

    @property
    def math(self):
        return self.__math

    @property
    def python(self):
        return self.__python

    @property
    def dbms(self):
        return self.__dbms

    # ==================================
    # CALCULATIONS
    # ==================================

    def total_marks(self):

        return (
            self.__math +
            self.__python +
            self.__dbms
        )

    def average_marks(self):

        return (
            self.total_marks() / 3
        )

    def grade(self):

        average = self.average_marks()

        if average >= 90:
            return "A+"

        elif average >= 80:
            return "A"

        elif average >= 70:
            return "B"

        elif average >= 60:
            return "C"

        elif average >= 40:
            return "D"

        else:
            return "F"

    # ==================================
    # DISPLAY REPORT
    # ==================================

    def display_report(self):

        print("\n" + "=" * 40)
        print("STUDENT REPORT")
        print("=" * 40)

        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Roll Number :", self.roll_number)

        print("-" * 40)

        print("Mathematics :", self.__math)
        print("Python      :", self.__python)
        print("DBMS        :", self.__dbms)

        print("-" * 40)

        print(
            "Total Marks :",
            self.total_marks()
        )

        print(
            "Average     :",
            round(
                self.average_marks(),
                2
            )
        )

        print(
            "Grade       :",
            self.grade()
        )

        print(
            "College     :",
            Student.college_name
        )

        print("=" * 40)

# ======================================
# STUDENT DATABASE
# ======================================

students = []

# ======================================
# MAIN MENU
# ======================================

while True:

    print("\n")
    print("=" * 50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input(
        "\nEnter Choice: "
    )

    # ==================================
    # ADD STUDENT
    # ==================================

    if choice == "1":

        name = input(
            "Enter Name: "
        )

        age = int(
            input(
                "Enter Age: "
            )
        )

        roll_number = input(
            "Enter Roll Number: "
        )

        math = int(
            input(
                "Enter Mathematics Marks: "
            )
        )

        python_marks = int(
            input(
                "Enter Python Marks: "
            )
        )

        dbms = int(
            input(
                "Enter DBMS Marks: "
            )
        )

        student = Student(
            name,
            age,
            roll_number,
            math,
            python_marks,
            dbms
        )

        students.append(student)

        print(
            "\nStudent Added Successfully!"
        )

    # ==================================
    # VIEW STUDENTS
    # ==================================

    elif choice == "2":

        if len(students) == 0:

            print(
                "\nNo Student Records Found."
            )

        else:

            for student in students:

                student.display_report()

    # ==================================
    # EXIT
    # ==================================

    elif choice == "3":

        print(
            "\nThank You for Using "
            "Student Management System"
        )

        break

    # ==================================
    # INVALID CHOICE
    # ==================================

    else:

        print(
            "\nInvalid Choice."
        )

# ======================================
# END OF PROJECT
# ======================================

print("\nDay 040 Completed Successfully!")