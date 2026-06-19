# ======================================
# Day 005: For Loop
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding For Loops and Iteration
# in Python
# ======================================

print("=" * 50)
print("DAY 005 - FOR LOOP")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
A for loop is used to iterate over a
sequence such as:

1. String
2. List
3. Tuple
4. Dictionary
5. Range of numbers

Syntax:

for variable in sequence:
    statement

The loop runs once for each item
present in the sequence.
"""

# ======================================
# 1. BASIC FOR LOOP
# ======================================

print("\n1. BASIC FOR LOOP")

for number in range(1, 6):
    print(number)

# ======================================
# 2. FOR LOOP WITH STRING
# ======================================

print("\n2. FOR LOOP WITH STRING")

name = "SALONI"

for character in name:
    print(character)

# ======================================
# 3. FOR LOOP WITH LIST
# ======================================

print("\n3. FOR LOOP WITH LIST")

subjects = [
    "Mathematics",
    "Python",
    "Statistics",
    "DBMS"
]

for subject in subjects:
    print(subject)

# ======================================
# 4. RANGE FUNCTION
# ======================================

print("\n4. RANGE FUNCTION")

for value in range(5):
    print(value)

# ======================================
# 5. RANGE WITH START AND STOP
# ======================================

print("\n5. RANGE WITH START AND STOP")

for value in range(10, 16):
    print(value)

# ======================================
# 6. RANGE WITH STEP
# ======================================

print("\n6. RANGE WITH STEP")

for value in range(0, 21, 2):
    print(value)

# ======================================
# 7. SUM OF FIRST 10 NUMBERS
# ======================================

print("\n7. SUM OF FIRST 10 NUMBERS")

total = 0

for number in range(1, 11):
    total += number

print("Sum =", total)

# ======================================
# 8. MULTIPLICATION TABLE
# ======================================

print("\n8. MULTIPLICATION TABLE")

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# ======================================
# 9. FACTORIAL USING FOR LOOP
# ======================================

print("\n9. FACTORIAL USING FOR LOOP")

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)

# ======================================
# 10. USER INPUT EXAMPLE
# ======================================

print("\n10. USER INPUT EXAMPLE")

n = int(input("Enter a positive number: "))

for i in range(1, n + 1):
    print(i)

# ======================================
# 11. MINI PROJECT
# ======================================

print("\n11. MINI PROJECT - STUDENT MARKS")

marks = [85, 90, 78, 92, 88]

total_marks = 0

for mark in marks:
    total_marks += mark

average = total_marks / len(marks)

print("Marks   :", marks)
print("Total   :", total_marks)
print("Average :", average)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Print numbers from 1 to 20
using a for loop.

Exercise 2:
Print all even numbers from
1 to 50.

Exercise 3:
Take a number from the user
and print its multiplication table.

Exercise 4:
Find the sum of numbers from
1 to 100 using a for loop.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a program to count:

1. Total vowels
2. Total consonants

in a given string.

Example:

Input:
Saloni Tiwari

Output:
Vowels     : ?
Consonants : ?
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 005 Completed Successfully!")