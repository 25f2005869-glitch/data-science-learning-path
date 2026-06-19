# ======================================
# Day 008: Strings Fundamentals
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Strings and Basic
# String Operations in Python
# ======================================

print("=" * 50)
print("DAY 008 - STRINGS FUNDAMENTALS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a String?

A string is a sequence of characters
enclosed within single quotes (' ')
or double quotes (" ").

Examples:
"Python"
'Data Science'
"Saloni Tiwari"

Strings are:
1. Ordered
2. Immutable
3. Iterable

Common Operations:
- Accessing Characters
- String Length
- Concatenation
- Repetition
- Membership Testing
"""

# ======================================
# 1. CREATING STRINGS
# ======================================

print("\n1. CREATING STRINGS")

name = "Saloni Tiwari"
course = 'BS in Data Science'

print(name)
print(course)

# ======================================
# 2. STRING DATA TYPE
# ======================================

print("\n2. STRING DATA TYPE")

text = "Python"

print("Value:", text)
print("Type :", type(text))

# ======================================
# 3. ACCESSING CHARACTERS
# ======================================

print("\n3. ACCESSING CHARACTERS")

language = "Python"

print("First Character :", language[0])
print("Second Character:", language[1])
print("Last Character  :", language[-1])

# ======================================
# 4. STRING LENGTH
# ======================================

print("\n4. STRING LENGTH")

student_name = "Saloni Tiwari"

print("Length:", len(student_name))

# ======================================
# 5. STRING CONCATENATION
# ======================================

print("\n5. STRING CONCATENATION")

first_name = "Saloni"
last_name = "Tiwari"

full_name = first_name + " " + last_name

print("Full Name:", full_name)

# ======================================
# 6. STRING REPETITION
# ======================================

print("\n6. STRING REPETITION")

word = "Python "

print(word * 3)

# ======================================
# 7. MEMBERSHIP OPERATORS
# ======================================

print("\n7. MEMBERSHIP OPERATORS")

text = "Data Science"

print("'Data' in text     :", "Data" in text)
print("'Python' in text   :", "Python" in text)
print("'AI' not in text   :", "AI" not in text)

# ======================================
# 8. ITERATING THROUGH A STRING
# ======================================

print("\n8. ITERATING THROUGH A STRING")

name = "SALONI"

for character in name:
    print(character)

# ======================================
# 9. USER INPUT STRING
# ======================================

print("\n9. USER INPUT STRING")

user_name = input("Enter your name: ")

print("Welcome,", user_name)

# ======================================
# 10. MINI PROJECT
# ======================================

print("\n10. MINI PROJECT - NAME ANALYZER")

name = input("Enter your full name: ")

print("\nAnalysis Report")
print("-" * 30)

print("Name            :", name)
print("Total Characters:", len(name))
print("First Character :", name[0])
print("Last Character  :", name[-1])

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a string containing
your favourite subject.

Print:
- Value
- Length
- First Character

Exercise 2:
Take a string from the user
and print each character
using a for loop.

Exercise 3:
Create two strings and
concatenate them.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a String Analyzer.

Input:
A user's name

Output:
1. Name
2. Length of Name
3. First Character
4. Last Character
5. Check whether the name
   contains the letter 'a'
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 008 Completed Successfully!")