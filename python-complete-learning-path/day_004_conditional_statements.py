# ======================================
# Day 004: Conditional Statements
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Decision Making
# using Conditional Statements in Python
# ======================================

print("=" * 50)
print("DAY 004 - CONDITIONAL STATEMENTS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Conditional statements allow a program
to make decisions based on conditions.

Python provides:

1. if
2. if-else
3. if-elif-else
4. Nested if

Comparison operators are commonly used
with conditional statements.

Examples:
==
!=
>
<
>=
<=

The condition must evaluate to either
True or False.
"""

# ======================================
# 1. SIMPLE IF STATEMENT
# ======================================

print("\n1. SIMPLE IF STATEMENT")

age = 17

if age >= 18:
    print("You are eligible to vote.")

# ======================================
# 2. IF-ELSE STATEMENT
# ======================================

print("\n2. IF-ELSE STATEMENT")

marks = 75

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# ======================================
# 3. IF-ELIF-ELSE STATEMENT
# ======================================

print("\n3. IF-ELIF-ELSE STATEMENT")

score = 88

if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# ======================================
# 4. NESTED IF
# ======================================

print("\n4. NESTED IF")

age = 19
has_id_card = True

if age >= 18:
    if has_id_card:
        print("Entry Allowed")
    else:
        print("ID Card Required")
else:
    print("Entry Not Allowed")

# ======================================
# 5. CHECK EVEN OR ODD
# ======================================

print("\n5. EVEN OR ODD")

number = 12

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

# ======================================
# 6. POSITIVE, NEGATIVE OR ZERO
# ======================================

print("\n6. NUMBER CHECKER")

number = -5

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# ======================================
# 7. USER INPUT EXAMPLE
# ======================================

print("\n7. USER INPUT EXAMPLE")

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ======================================
# 8. STUDENT RESULT SYSTEM
# ======================================

print("\n8. STUDENT RESULT SYSTEM")

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# ======================================
# 9. MINI PROJECT
# ======================================

print("\n9. MINI PROJECT - ELIGIBILITY CHECKER")

student_age = int(input("Enter your age: "))
attendance = float(input("Enter attendance percentage: "))

if student_age >= 17 and attendance >= 75:
    print("Eligible for Examination")
else:
    print("Not Eligible for Examination")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Take a number from the user and
check whether it is even or odd.

Exercise 2:
Take marks as input and display:

A+ : 90 and above
A  : 80-89
B  : 70-79
C  : 60-69
D  : 40-59
F  : Below 40

Exercise 3:
Take age as input and check whether
the user is eligible to vote.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a BMI Category Checker.

Input:
- Weight (kg)
- Height (m)

Formula:

BMI = Weight / (Height ** 2)

Output:

BMI < 18.5      -> Underweight
18.5 - 24.9     -> Normal Weight
25 - 29.9       -> Overweight
30 and above    -> Obese
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 004 Completed Successfully!")