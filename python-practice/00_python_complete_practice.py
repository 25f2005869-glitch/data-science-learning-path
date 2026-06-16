# ======================================
# Python Complete Practice
# Author: Saloni Tiwari
# Description: Python fundamentals practice
# ======================================

print("Python Complete Practice Started\n")

# --------------------------------------
# 1. Variables and Data Types
# --------------------------------------

print("Variables and Data Types")

name = "Saloni"
age = 21
height = 5.3
is_student = True

print(name, age, height, is_student)

# --------------------------------------
# 2. Arithmetic Operators
# --------------------------------------

print("\nArithmetic Operators")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)

# --------------------------------------
# 3. User Input
# --------------------------------------

print("\nUser Input")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)

# --------------------------------------
# 4. Conditional Statements
# --------------------------------------

print("\nConditional Statements")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number == 0:
    print("Zero")
else:
    print("Negative Number")

# --------------------------------------
# 5. Lists
# --------------------------------------

print("\nLists")

numbers = [1, 2, 3, 4, 5]

numbers.append(6)

print(numbers)

# --------------------------------------
# 6. Tuples
# --------------------------------------

print("\nTuples")

fruits = ("apple", "banana", "mango")

print(fruits)

# --------------------------------------
# 7. Sets
# --------------------------------------

print("\nSets")

unique_numbers = {1, 2, 3, 3, 4}

print(unique_numbers)

# --------------------------------------
# 8. Dictionaries
# --------------------------------------

print("\nDictionary")

student = {
    "name": "Saloni",
    "age": 21,
    "course": "Data Science"
}

print(student["name"])

# --------------------------------------
# 9. For Loop
# --------------------------------------

print("\nFor Loop")

for i in range(5):
    print(i)

# --------------------------------------
# 10. While Loop
# --------------------------------------

print("\nWhile Loop")

count = 0

while count < 5:
    print(count)
    count += 1

# --------------------------------------
# 11. Functions
# --------------------------------------

print("\nFunctions")

def add(x, y):
    return x + y

print(add(5, 7))

# --------------------------------------
# 12. Recursion
# --------------------------------------

print("\nRecursion")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# --------------------------------------
# 13. OOP
# --------------------------------------

print("\nObject Oriented Programming")

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)


s1 = Student("Saloni", 95)
s1.display()

# --------------------------------------
# 14. File Handling
# --------------------------------------

print("\nFile Handling")

file = open("sample.txt", "w")

file.write("Hello Python")

file.close()

# --------------------------------------
# 15. Exception Handling
# --------------------------------------

print("\nException Handling")

try:
    x = 10 / 0
except:
    print("Division by zero error")

# --------------------------------------

print("\nPython Practice Completed Successfully")