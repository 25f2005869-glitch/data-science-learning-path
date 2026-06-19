# ======================================
# Day 033: Polymorphism
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Polymorphism and
# Method Overriding in Python
# ======================================

print("=" * 50)
print("DAY 033 - POLYMORPHISM")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Polymorphism?

Polymorphism means:

"One Interface, Multiple Forms"

It allows the same method name
to behave differently depending
on the object.

Benefits:

1. Flexibility
2. Reusability
3. Cleaner Code
4. Extensibility

Types of Polymorphism:

1. Method Overriding
2. Duck Typing
3. Operator Overloading
"""

# ======================================
# 1. SIMPLE POLYMORPHISM
# ======================================

print("\n1. SIMPLE POLYMORPHISM")

class Dog:

    def sound(self):
        print("Dog Barks")

class Cat:

    def sound(self):
        print("Cat Meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# ======================================
# 2. POLYMORPHISM USING LOOP
# ======================================

print("\n2. POLYMORPHISM USING LOOP")

class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

class Cow:

    def sound(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

# ======================================
# 3. METHOD OVERRIDING
# ======================================

print("\n3. METHOD OVERRIDING")

class Person:

    def role(self):
        print("I am a Person")

class Student(Person):

    def role(self):
        print("I am a Student")

student = Student()

student.role()

# ======================================
# 4. DUCK TYPING
# ======================================

print("\n4. DUCK TYPING")

class Student:

    def introduce(self):
        print("I am a Student")

class Teacher:

    def introduce(self):
        print("I am a Teacher")

def introduction(person):
    person.introduce()

student = Student()
teacher = Teacher()

introduction(student)
introduction(teacher)

# ======================================
# 5. BUILT-IN POLYMORPHISM
# ======================================

print("\n5. BUILT-IN POLYMORPHISM")

print(len("Python"))
print(len([10, 20, 30]))
print(len((1, 2, 3, 4)))

# ======================================
# 6. OPERATOR OVERLOADING
# ======================================

print("\n6. OPERATOR OVERLOADING")

print(10 + 20)

print("Data" + "Science")

print([1, 2] + [3, 4])

# ======================================
# 7. POLYMORPHIC FUNCTION
# ======================================

print("\n7. POLYMORPHIC FUNCTION")

def addition(a, b):
    return a + b

print(addition(10, 20))
print(addition("Python ", "Programming"))

# ======================================
# 8. VEHICLE EXAMPLE
# ======================================

print("\n8. VEHICLE EXAMPLE")

class Car:

    def move(self):
        print("Car is Moving")

class Bicycle:

    def move(self):
        print("Bicycle is Moving")

class Airplane:

    def move(self):
        print("Airplane is Flying")

vehicles = [
    Car(),
    Bicycle(),
    Airplane()
]

for vehicle in vehicles:
    vehicle.move()

# ======================================
# 9. USER INPUT EXAMPLE
# ======================================

print("\n9. USER INPUT EXAMPLE")

class Student:

    def details(self):
        print("Student Details")

class Teacher:

    def details(self):
        print("Teacher Details")

choice = input(
    "Enter Student or Teacher: "
).lower()

if choice == "student":

    obj = Student()

else:

    obj = Teacher()

obj.details()

# ======================================
# 10. PAYMENT SYSTEM
# ======================================

print("\n10. PAYMENT SYSTEM")

class CreditCard:

    def pay(self):
        print("Payment by Credit Card")

class UPI:

    def pay(self):
        print("Payment by UPI")

class NetBanking:

    def pay(self):
        print("Payment by Net Banking")

payments = [
    CreditCard(),
    UPI(),
    NetBanking()
]

for payment in payments:
    payment.pay()

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - RESULT SYSTEM")

class Undergraduate:

    def calculate_grade(self):
        print("Undergraduate Grading System")

class Postgraduate:

    def calculate_grade(self):
        print("Postgraduate Grading System")

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
Create classes:

Dog
Cat

Both should have a sound() method.

Exercise 2:
Create classes:

Car
Bike

Both should have a move() method.

Exercise 3:
Create a function that accepts
different objects and calls
their display() method.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a College Management System.

Classes:

Student
Teacher
Administrator

Each class should have:

show_role()

Use polymorphism to display
different roles using a loop.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 033 Completed Successfully!")