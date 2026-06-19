# ======================================
# Day 026: Custom Exceptions
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding User-Defined Exceptions
# in Python
# ======================================

print("=" * 50)
print("DAY 026 - CUSTOM EXCEPTIONS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Custom Exception?

Python provides many built-in exceptions,
but sometimes we need our own exceptions
for specific business rules.

A custom exception is created by
inheriting from the Exception class.

Syntax:

class MyException(Exception):
    pass

Raise Exception:

raise MyException("Error Message")

Benefits:

1. Better Error Handling
2. Business Rule Validation
3. More Readable Code
4. Professional Applications
"""

# ======================================
# 1. SIMPLE CUSTOM EXCEPTION
# ======================================

print("\n1. SIMPLE CUSTOM EXCEPTION")

class AgeError(Exception):
    pass

try:

    age = 15

    if age < 18:
        raise AgeError(
            "Age must be 18 or above."
        )

except AgeError as error:
    print(error)

# ======================================
# 2. MARKS VALIDATION
# ======================================

print("\n2. MARKS VALIDATION")

class MarksError(Exception):
    pass

try:

    marks = 120

    if marks > 100:
        raise MarksError(
            "Marks cannot exceed 100."
        )

except MarksError as error:
    print(error)

# ======================================
# 3. NEGATIVE NUMBER VALIDATION
# ======================================

print("\n3. NEGATIVE NUMBER VALIDATION")

class NegativeNumberError(Exception):
    pass

try:

    number = -10

    if number < 0:
        raise NegativeNumberError(
            "Negative numbers are not allowed."
        )

except NegativeNumberError as error:
    print(error)

# ======================================
# 4. USER INPUT VALIDATION
# ======================================

print("\n4. USER INPUT VALIDATION")

class InvalidAgeError(Exception):
    pass

try:

    age = int(input("Enter Age: "))

    if age < 0:
        raise InvalidAgeError(
            "Age cannot be negative."
        )

    print("Age:", age)

except InvalidAgeError as error:
    print(error)

except ValueError:
    print("Please enter a valid number.")

# ======================================
# 5. PASSWORD VALIDATION
# ======================================

print("\n5. PASSWORD VALIDATION")

class PasswordError(Exception):
    pass

try:

    password = "abc"

    if len(password) < 6:
        raise PasswordError(
            "Password must contain at least 6 characters."
        )

except PasswordError as error:
    print(error)

# ======================================
# 6. BANK WITHDRAWAL VALIDATION
# ======================================

print("\n6. BANK WITHDRAWAL VALIDATION")

class InsufficientBalanceError(Exception):
    pass

balance = 5000
withdraw_amount = 7000

try:

    if withdraw_amount > balance:
        raise InsufficientBalanceError(
            "Insufficient Balance."
        )

except InsufficientBalanceError as error:
    print(error)

# ======================================
# 7. FILE SIZE VALIDATION
# ======================================

print("\n7. FILE SIZE VALIDATION")

class FileSizeError(Exception):
    pass

file_size = 15

try:

    if file_size > 10:
        raise FileSizeError(
            "File size exceeds limit."
        )

except FileSizeError as error:
    print(error)

# ======================================
# 8. DIVISION VALIDATION
# ======================================

print("\n8. DIVISION VALIDATION")

class DivisionError(Exception):
    pass

try:

    divisor = 0

    if divisor == 0:
        raise DivisionError(
            "Division by zero is not allowed."
        )

except DivisionError as error:
    print(error)

# ======================================
# 9. MULTIPLE CUSTOM EXCEPTIONS
# ======================================

print("\n9. MULTIPLE CUSTOM EXCEPTIONS")

class AgeValidationError(Exception):
    pass

class MarksValidationError(Exception):
    pass

try:

    age = 16
    marks = 110

    if age < 18:
        raise AgeValidationError(
            "Age must be at least 18."
        )

    if marks > 100:
        raise MarksValidationError(
            "Marks cannot exceed 100."
        )

except AgeValidationError as error:
    print(error)

except MarksValidationError as error:
    print(error)

# ======================================
# 10. CUSTOM EXCEPTION WITH FUNCTION
# ======================================

print("\n10. FUNCTION VALIDATION")

class NumberRangeError(Exception):
    pass

def validate_number(number):

    if number < 1 or number > 100:
        raise NumberRangeError(
            "Number must be between 1 and 100."
        )

    return "Valid Number"

try:

    print(validate_number(150))

except NumberRangeError as error:
    print(error)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - ATM SYSTEM")

class InvalidPINError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

correct_pin = "1234"
balance = 10000

try:

    pin = input("Enter ATM PIN: ")

    if pin != correct_pin:
        raise InvalidPINError(
            "Invalid ATM PIN."
        )

    amount = float(
        input("Enter Withdrawal Amount: ")
    )

    if amount > balance:
        raise InsufficientFundsError(
            "Insufficient Funds."
        )

    balance -= amount

    print("Transaction Successful")
    print("Remaining Balance:", balance)

except InvalidPINError as error:
    print(error)

except InsufficientFundsError as error:
    print(error)

except ValueError:
    print("Please enter a valid amount.")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a custom exception
for invalid marks.

Exercise 2:
Create a custom exception
for negative age.

Exercise 3:
Validate password length
using a custom exception.

Exercise 4:
Create a custom exception
for insufficient balance.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Admission System.

Requirements:

1. Age must be >= 17
2. Marks must be between
   0 and 100

Create:

- AgeValidationError
- MarksValidationError

Use custom exceptions to
validate the input.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 026 Completed Successfully!")