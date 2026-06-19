# ======================================
# Day 035: Special Methods
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Special (Magic/Dunder)
# Methods in Python
# ======================================

print("=" * 50)
print("DAY 035 - SPECIAL METHODS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What are Special Methods?

Special methods are predefined methods
that begin and end with double underscores.

Example:

__init__()
__str__()
__len__()
__add__()

They are also called:

1. Magic Methods
2. Dunder Methods

(Dunder = Double Underscore)

Benefits:

1. Customize Object Behavior
2. Operator Overloading
3. Better Object Representation
4. Professional Class Design
"""

# ======================================
# 1. __init__()
# ======================================

print("\n1. __init__()")

class Student:

    def __init__(self, name):

        self.name = name

student = Student("Saloni")

print(student.name)

# ======================================
# 2. __str__()
# ======================================

print("\n2. __str__()")

class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return f"Student Name: {self.name}"

student = Student("Saloni")

print(student)

# ======================================
# 3. WITHOUT __str__()
# ======================================

print("\n3. WITHOUT __str__()")

class Demo:
    pass

demo = Demo()

print(demo)

# ======================================
# 4. __len__()
# ======================================

print("\n4. __len__()")

class SubjectList:

    def __init__(self, subjects):

        self.subjects = subjects

    def __len__(self):

        return len(self.subjects)

subjects = SubjectList(
    ["Python", "DBMS", "Statistics"]
)

print(len(subjects))

# ======================================
# 5. __add__()
# ======================================

print("\n5. __add__()")

class Marks:

    def __init__(self, marks):

        self.marks = marks

    def __add__(self, other):

        return self.marks + other.marks

student1 = Marks(90)
student2 = Marks(95)

print(student1 + student2)

# ======================================
# 6. __eq__()
# ======================================

print("\n6. __eq__()")

class Student:

    def __init__(self, roll):

        self.roll = roll

    def __eq__(self, other):

        return self.roll == other.roll

student1 = Student(101)
student2 = Student(101)

print(student1 == student2)

# ======================================
# 7. __lt__()
# ======================================

print("\n7. __lt__()")

class Product:

    def __init__(self, price):

        self.price = price

    def __lt__(self, other):

        return self.price < other.price

product1 = Product(500)
product2 = Product(1000)

print(product1 < product2)

# ======================================
# 8. __repr__()
# ======================================

print("\n8. __repr__()")

class Book:

    def __init__(self, title):

        self.title = title

    def __repr__(self):

        return f"Book('{self.title}')"

book = Book("Python Programming")

print(book)

# ======================================
# 9. __contains__()
# ======================================

print("\n9. __contains__()")

class SubjectCollection:

    def __init__(self, subjects):

        self.subjects = subjects

    def __contains__(self, item):

        return item in self.subjects

collection = SubjectCollection(
    ["Python", "DBMS", "Statistics"]
)

print("Python" in collection)
print("Java" in collection)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return f"Student: {self.name}"

name = input("Enter Student Name: ")

student = Student(name)

print(student)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - BANK ACCOUNT")

class BankAccount:

    def __init__(
        self,
        account_holder,
        balance
    ):

        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):

        return (
            f"Account Holder: "
            f"{self.account_holder}, "
            f"Balance: ₹{self.balance}"
        )

    def __add__(self, other):

        return self.balance + other.balance

account1 = BankAccount(
    "Saloni",
    10000
)

account2 = BankAccount(
    "Riya",
    15000
)

print(account1)
print(account2)

print(
    "Combined Balance:",
    account1 + account2
)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a class Student.

Implement __str__().

Exercise 2:
Create a class Book.

Implement __repr__().

Exercise 3:
Create a class Product.

Implement __lt__().

Exercise 4:
Create a class Marks.

Implement __add__().
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Library System.

Class:
Book

Attributes:
- Title
- Price

Implement:

1. __str__()
2. __repr__()
3. __eq__()
4. __lt__()

Compare multiple books and
display results.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 035 Completed Successfully!")