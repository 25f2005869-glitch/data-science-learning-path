# ==========================================================
# Day 06 : Sets and Functions
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 06")
print("=" * 60)

print("\nMathematical Foundations for Machine Learning")
print("-" * 30)

print("""
Sets and Functions are fundamental concepts in
Mathematics and Machine Learning.

They help us represent data, relationships,
and mappings between inputs and outputs.
""")

# ----------------------------------------------------------
# Sets
# ----------------------------------------------------------

print("\nWhat is a Set?")
print("-" * 30)

print("""
A Set is a collection of distinct objects.

Properties:
✓ Unordered
✓ Unique Elements
✓ No Duplicate Values
""")

students = {"Aman", "Rahul", "Priya", "Sneha"}

print("Student Set:")
print(students)

# ----------------------------------------------------------
# Duplicate Removal
# ----------------------------------------------------------

print("\nDuplicate Removal Using Sets")
print("-" * 30)

marks = [85, 90, 85, 95, 90, 80]

print("Original List:")
print(marks)

unique_marks = set(marks)

print("Unique Values:")
print(unique_marks)

# ----------------------------------------------------------
# Set Operations
# ----------------------------------------------------------

print("\nSet Operations")
print("-" * 30)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A =", A)
print("Set B =", B)

print("\nUnion (A ∪ B):")
print(A.union(B))

print("\nIntersection (A ∩ B):")
print(A.intersection(B))

print("\nDifference (A - B):")
print(A.difference(B))

# ----------------------------------------------------------
# ML Example Using Sets
# ----------------------------------------------------------

print("\nMachine Learning Example")
print("-" * 30)

feature_set = {
    "Age",
    "Income",
    "Education",
    "Experience"
}

print("Features Used in ML Model:")
print(feature_set)

# ----------------------------------------------------------
# Functions
# ----------------------------------------------------------

print("\nWhat is a Function?")
print("-" * 30)

print("""
A Function maps every input
to exactly one output.

f(x) = y

Input  → Process → Output
""")

# Example Function

def square(x):
    return x * x

number = 5

print("Input:", number)
print("Output:", square(number))

# ----------------------------------------------------------
# Multiple Inputs Example
# ----------------------------------------------------------

print("\nFunction with Multiple Inputs")
print("-" * 30)

def add(a, b):
    return a + b

result = add(10, 20)

print("10 + 20 =", result)

# ----------------------------------------------------------
# ML Perspective
# ----------------------------------------------------------

print("\nFunctions in Machine Learning")
print("-" * 30)

print("""
Machine Learning models can be viewed
as mathematical functions.

Example:

Study Hours → Predicted Marks

f(5) = 60
f(8) = 80
f(10) = 95

The model learns the function from data.
""")

# ----------------------------------------------------------
# Input-Output Mapping
# ----------------------------------------------------------

print("\nInput-Output Mapping Example")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]

for x, y in zip(study_hours, marks):
    print(f"f({x}) = {y}")

# ----------------------------------------------------------
# Domain and Range
# ----------------------------------------------------------

print("\nDomain and Range")
print("-" * 30)

print("""
Domain:
Set of all possible inputs.

Range:
Set of all possible outputs.
""")

domain = {2, 4, 6, 8, 10}
range_values = {40, 50, 65, 80, 95}

print("Domain:", domain)
print("Range :", range_values)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. Can a set contain duplicate values?
2. What does Union do?
3. What is a Function?
4. What is the Domain of a Function?
""")

print("""
Answers:
1. No
2. Combines all unique elements
3. Maps input to output
4. Set of possible inputs
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 06 Summary")
print("-" * 30)

print("""
1. Sets contain unique elements.
2. Sets are useful for removing duplicates.
3. Union, Intersection, and Difference are
   common set operations.
4. Functions map inputs to outputs.
5. Machine Learning models can be viewed
   as mathematical functions.
6. Sets and Functions form the foundation
   of mathematical thinking in ML.
""")

print("\nDay 06 Completed Successfully!")
print("=" * 60)