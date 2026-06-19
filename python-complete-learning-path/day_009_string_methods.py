# ======================================
# Day 009: String Methods
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Common String Methods
# in Python
# ======================================

print("=" * 50)
print("DAY 009 - STRING METHODS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
String methods are built-in functions
used to perform operations on strings.

Important:
Strings are immutable.

This means string methods do not modify
the original string. Instead, they
return a new string.

Common String Methods:

1. upper()
2. lower()
3. title()
4. capitalize()
5. strip()
6. replace()
7. find()
8. count()
9. startswith()
10. endswith()
11. split()
"""

# ======================================
# 1. upper()
# ======================================

print("\n1. upper()")

text = "python programming"

print("Original :", text)
print("Upper    :", text.upper())

# ======================================
# 2. lower()
# ======================================

print("\n2. lower()")

text = "DATA SCIENCE"

print("Original :", text)
print("Lower    :", text.lower())

# ======================================
# 3. title()
# ======================================

print("\n3. title()")

name = "saloni tiwari"

print("Original :", name)
print("Title    :", name.title())

# ======================================
# 4. capitalize()
# ======================================

print("\n4. capitalize()")

course = "python complete learning path"

print("Original   :", course)
print("Capitalized:", course.capitalize())

# ======================================
# 5. strip()
# ======================================

print("\n5. strip()")

text = "     Python     "

print("Before:", repr(text))
print("After :", repr(text.strip()))

# ======================================
# 6. replace()
# ======================================

print("\n6. replace()")

sentence = "I love Java"

new_sentence = sentence.replace("Java", "Python")

print("Original:", sentence)
print("Updated :", new_sentence)

# ======================================
# 7. find()
# ======================================

print("\n7. find()")

text = "Data Science"

position = text.find("Science")

print("Position:", position)

# ======================================
# 8. count()
# ======================================

print("\n8. count()")

text = "programming"

print("Count of 'm':", text.count("m"))

# ======================================
# 9. startswith()
# ======================================

print("\n9. startswith()")

text = "Python Programming"

print(text.startswith("Python"))
print(text.startswith("Java"))

# ======================================
# 10. endswith()
# ======================================

print("\n10. endswith()")

filename = "report.pdf"

print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

# ======================================
# 11. split()
# ======================================

print("\n11. split()")

text = "Python,SQL,Statistics,ML"

subjects = text.split(",")

print(subjects)

# ======================================
# 12. COMBINING METHODS
# ======================================

print("\n12. COMBINING METHODS")

name = "    saloni tiwari    "

clean_name = name.strip().title()

print("Clean Name:", clean_name)

# ======================================
# 13. MINI PROJECT
# ======================================

print("\n13. MINI PROJECT - TEXT ANALYZER")

text = input("Enter a sentence: ")

print("\nAnalysis Report")
print("-" * 30)

print("Original Text     :", text)
print("Upper Case        :", text.upper())
print("Lower Case        :", text.lower())
print("Total Characters  :", len(text))
print("Word Count        :", len(text.split()))
print("Count of 'a'      :", text.lower().count("a"))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Take a sentence from the user.

Display:
- Upper Case
- Lower Case
- Title Case

Exercise 2:
Take a name from the user.

Remove extra spaces using strip()
and convert it to title case.

Exercise 3:
Count how many times the letter
'e' appears in a sentence.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Username Validator.

Rules:

1. Remove extra spaces.
2. Convert username to lowercase.
3. Check whether username starts
   with a letter.
4. Display the cleaned username.

Example:

Input:
   SALONI_123

Output:
saloni_123
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 009 Completed Successfully!")