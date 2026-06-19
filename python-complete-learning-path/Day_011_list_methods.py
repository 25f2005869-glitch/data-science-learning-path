# ======================================
# Day 011: List Methods
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Common List Methods
# in Python
# ======================================

print("=" * 50)
print("DAY 011 - LIST METHODS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
List methods are built-in functions
used to perform operations on lists.

Since lists are mutable, methods can
modify the original list directly.

Common List Methods:

1. append()
2. insert()
3. extend()
4. remove()
5. pop()
6. clear()
7. index()
8. count()
9. sort()
10. reverse()
11. copy()
"""

# ======================================
# 1. append()
# ======================================

print("\n1. append()")

subjects = ["Python", "DBMS"]

subjects.append("Statistics")

print(subjects)

# ======================================
# 2. insert()
# ======================================

print("\n2. insert()")

subjects = ["Python", "Statistics"]

subjects.insert(1, "DBMS")

print(subjects)

# ======================================
# 3. extend()
# ======================================

print("\n3. extend()")

list1 = ["Python", "DBMS"]
list2 = ["Statistics", "Mathematics"]

list1.extend(list2)

print(list1)

# ======================================
# 4. remove()
# ======================================

print("\n4. remove()")

subjects = ["Python", "DBMS", "Statistics"]

subjects.remove("DBMS")

print(subjects)

# ======================================
# 5. pop()
# ======================================

print("\n5. pop()")

subjects = ["Python", "DBMS", "Statistics"]

removed_item = subjects.pop()

print("Removed:", removed_item)
print("Updated:", subjects)

# ======================================
# 6. clear()
# ======================================

print("\n6. clear()")

temp_list = [10, 20, 30]

temp_list.clear()

print(temp_list)

# ======================================
# 7. index()
# ======================================

print("\n7. index()")

subjects = ["Python", "DBMS", "Statistics"]

position = subjects.index("DBMS")

print("Index:", position)

# ======================================
# 8. count()
# ======================================

print("\n8. count()")

numbers = [10, 20, 10, 30, 10, 40]

print("Count of 10:", numbers.count(10))

# ======================================
# 9. sort()
# ======================================

print("\n9. sort()")

numbers = [45, 12, 89, 23, 5]

numbers.sort()

print(numbers)

# ======================================
# 10. reverse()
# ======================================

print("\n10. reverse()")

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)

# ======================================
# 11. copy()
# ======================================

print("\n11. copy()")

original = [10, 20, 30]

duplicate = original.copy()

print("Original :", original)
print("Copy     :", duplicate)

# ======================================
# 12. COMBINING METHODS
# ======================================

print("\n12. COMBINING METHODS")

subjects = ["Python"]

subjects.append("DBMS")
subjects.append("Statistics")
subjects.sort()

print(subjects)

# ======================================
# 13. MINI PROJECT
# ======================================

print("\n13. MINI PROJECT - STUDENT LIST MANAGER")

students = ["Saloni", "Riya", "Ankit"]

print("Initial List:", students)

students.append("Priya")

print("After Adding Student:")
print(students)

students.remove("Riya")

print("After Removing Student:")
print(students)

students.sort()

print("Sorted List:")
print(students)

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Create a list of your favourite books.

Add one more book using append().

Exercise 2:
Create a list of numbers.

Sort the list in ascending order.

Exercise 3:
Remove an element from a list
using remove() and pop().

Exercise 4:
Create a copy of a list using copy().
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Marks Manager.

Store marks in a list.

Perform:

1. Add a new mark
2. Remove a mark
3. Sort marks
4. Find highest mark
5. Find lowest mark

Display the updated list.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 011 Completed Successfully!")