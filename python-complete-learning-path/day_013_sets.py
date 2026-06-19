# ======================================
# Day 013: Sets
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Sets and Set Operations
# in Python
# ======================================

print("=" * 50)
print("DAY 013 - SETS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is a Set?

A set is an unordered collection
of unique elements.

Sets are:

1. Unordered
2. Mutable
3. Do Not Allow Duplicates
4. Fast for Membership Testing

Syntax:

set_name = {item1, item2, item3}

Example:

subjects = {"Python", "DBMS", "Statistics"}

Important:

Sets automatically remove
duplicate values.
"""

# ======================================
# 1. CREATING A SET
# ======================================

print("\n1. CREATING A SET")

subjects = {
    "Python",
    "DBMS",
    "Statistics",
    "Mathematics"
}

print(subjects)

# ======================================
# 2. SET DATA TYPE
# ======================================

print("\n2. SET DATA TYPE")

numbers = {10, 20, 30}

print("Set :", numbers)
print("Type:", type(numbers))

# ======================================
# 3. DUPLICATE VALUES
# ======================================

print("\n3. DUPLICATE VALUES")

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

# ======================================
# 4. ADDING ELEMENTS
# ======================================

print("\n4. add() METHOD")

subjects = {"Python", "DBMS"}

subjects.add("Statistics")

print(subjects)

# ======================================
# 5. UPDATING A SET
# ======================================

print("\n5. update() METHOD")

subjects = {"Python", "DBMS"}

subjects.update(["Statistics", "Mathematics"])

print(subjects)

# ======================================
# 6. REMOVING ELEMENTS
# ======================================

print("\n6. remove() METHOD")

subjects = {
    "Python",
    "DBMS",
    "Statistics"
}

subjects.remove("DBMS")

print(subjects)

# ======================================
# 7. discard() METHOD
# ======================================

print("\n7. discard() METHOD")

subjects = {
    "Python",
    "DBMS",
    "Statistics"
}

subjects.discard("Java")

print(subjects)

# ======================================
# 8. MEMBERSHIP OPERATORS
# ======================================

print("\n8. MEMBERSHIP OPERATORS")

subjects = {
    "Python",
    "DBMS",
    "Statistics"
}

print("Python" in subjects)
print("Java" in subjects)

# ======================================
# 9. UNION OPERATION
# ======================================

print("\n9. UNION OPERATION")

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.union(set_b))

# ======================================
# 10. INTERSECTION OPERATION
# ======================================

print("\n10. INTERSECTION OPERATION")

set_a = {1, 2, 3}
set_b = {2, 3, 4}

print(set_a.intersection(set_b))

# ======================================
# 11. DIFFERENCE OPERATION
# ======================================

print("\n11. DIFFERENCE OPERATION")

set_a = {1, 2, 3}
set_b = {2, 3, 4}

print(set_a.difference(set_b))

# ======================================
# 12. ITERATING THROUGH A SET
# ======================================

print("\n12. ITERATING THROUGH A SET")

subjects = {
    "Python",
    "DBMS",
    "Statistics"
}

for subject in subjects:
    print(subject)

# ======================================
# 13. MINI PROJECT
# ======================================

print("\n13. MINI PROJECT - UNIQUE SUBJECTS")

subjects = [
    "Python",
    "DBMS",
    "Python",
    "Statistics",
    "DBMS",
    "Mathematics"
]

unique_subjects = set(subjects)

print("Original List:")
print(subjects)

print("\nUnique Subjects:")
print(unique_subjects)

print("\nTotal Unique Subjects:")
print(len(unique_subjects))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a set of your
favourite subjects.

Print all elements.

Exercise 2:
Create a set with duplicate values.

Observe the output.

Exercise 3:
Perform:

- Union
- Intersection
- Difference

on two sets.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Club System.

Club A Members:
{"Saloni", "Riya", "Ankit"}

Club B Members:
{"Saloni", "Priya", "Rohit"}

Find:

1. All Members
2. Common Members
3. Members Only in Club A
4. Members Only in Club B
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 013 Completed Successfully!")