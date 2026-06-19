# ======================================
# Day 025: Exception Handling Basics
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Exception Handling
# and Error Management in Python
# ======================================

print("=" * 50)
print("DAY 025 - EXCEPTION HANDLING BASICS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is an Exception?

An exception is an error that occurs
during program execution.

Without exception handling,
the program terminates immediately.

Common Exceptions:

1. ZeroDivisionError
2. ValueError
3. TypeError
4. IndexError
5. KeyError
6. FileNotFoundError

Exception Handling Keywords:

1. try
2. except
3. else
4. finally
"""

# ======================================
# 1. SIMPLE EXCEPTION HANDLING
# ======================================

print("\n1. SIMPLE EXCEPTION HANDLING")

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# ======================================
# 2. VALUE ERROR EXAMPLE
# ======================================

print("\n2. VALUE ERROR EXAMPLE")

try:
    number = int("Python")

except ValueError:
    print("Invalid conversion to integer.")

# ======================================
# 3. INDEX ERROR EXAMPLE
# ======================================

print("\n3. INDEX ERROR EXAMPLE")

try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Index out of range.")

# ======================================
# 4. MULTIPLE EXCEPT BLOCKS
# ======================================

print("\n4. MULTIPLE EXCEPT BLOCKS")

try:

    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

# ======================================
# 5. USING ELSE BLOCK
# ======================================

print("\n5. ELSE BLOCK")

try:

    number = int(input("Enter a number: "))
    result = 50 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division Successful")
    print("Result:", result)

# ======================================
# 6. USING FINALLY BLOCK
# ======================================

print("\n6. FINALLY BLOCK")

try:

    number = int(input("Enter a number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("This block always executes.")

# ======================================
# 7. GENERIC EXCEPTION
# ======================================

print("\n7. GENERIC EXCEPTION")

try:

    value = int(input("Enter a number: "))
    print(value)

except Exception as error:
    print("Error:", error)

# ======================================
# 8. SAFE LIST ACCESS
# ======================================

print("\n8. SAFE LIST ACCESS")

try:

    marks = [92, 85, 78]

    index = int(input("Enter index: "))

    print("Marks:", marks[index])

except IndexError:
    print("Invalid index entered.")

# ======================================
# 9. SAFE DICTIONARY ACCESS
# ======================================

print("\n9. SAFE DICTIONARY ACCESS")

student = {
    "name": "Saloni",
    "course": "Data Science"
}

try:

    key = input("Enter key: ")

    print(student[key])

except KeyError:
    print("Key not found.")

# ======================================
# 10. USER INPUT VALIDATION
# ======================================

print("\n10. USER INPUT VALIDATION")

try:

    age = int(input("Enter your age: "))

    print("Age:", age)

except ValueError:
    print("Age must be an integer.")

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - SAFE CALCULATOR")

try:

    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number: "))

    print("\nResults")
    print("-" * 20)

    print("Addition       :", num1 + num2)
    print("Subtraction    :", num1 - num2)
    print("Multiplication :", num1 * num2)
    print("Division       :", num1 / num2)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter valid numeric values.")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Handle ZeroDivisionError.

Exercise 2:
Handle ValueError while
taking integer input.

Exercise 3:
Handle IndexError while
accessing a list.

Exercise 4:
Use else and finally blocks
in a program.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Result System.

Requirements:

1. Take marks as input.
2. Handle invalid input.
3. Calculate average marks.
4. Display result safely.
5. Use:
   - try
   - except
   - else
   - finally
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 025 Completed Successfully!")