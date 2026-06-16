# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Strings
# Day         : 08
# Description : Understanding string operations in Python.
# ==========================================================

# Creating a string
text = "Python"

print("Original String:", text)

# Accessing characters
print("First Character:", text[0])
print("Second Character:", text[1])

# Length
print("Length:", len(text))

# Concatenation
greeting = "Hello"
name = "Saloni"

print(greeting + " " + name)

# String methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Replace
print("Replace:", text.replace("Python", "PDSA"))

# Traversing a string
print("Characters:")

for ch in text:
    print(ch)