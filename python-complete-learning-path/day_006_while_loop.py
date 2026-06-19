# ======================================
# Day 006: While Loop
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding While Loops and Repetition
# in Python
# ======================================

print("=" * 50)
print("DAY 006 - WHILE LOOP")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
A while loop executes a block of code
as long as a condition remains True.

Syntax:

while condition:
    statement

The loop stops when the condition
becomes False.

Important:
Always update the loop variable,
otherwise an infinite loop may occur.
"""

# ======================================
# 1. BASIC WHILE LOOP
# ======================================

print("\n1. BASIC WHILE LOOP")

count = 1

while count <= 5:
    print(count)
    count += 1

# ======================================
# 2. PRINT NUMBERS 1 TO 10
# ======================================

print("\n2. PRINT NUMBERS 1 TO 10")

number = 1

while number <= 10:
    print(number)
    number += 1

# ======================================
# 3. PRINT EVEN NUMBERS
# ======================================

print("\n3. PRINT EVEN NUMBERS")

even = 2

while even <= 20:
    print(even)
    even += 2

# ======================================
# 4. SUM OF FIRST 10 NUMBERS
# ======================================

print("\n4. SUM OF FIRST 10 NUMBERS")

count = 1
total = 0

while count <= 10:
    total += count
    count += 1

print("Sum =", total)

# ======================================
# 5. MULTIPLICATION TABLE
# ======================================

print("\n5. MULTIPLICATION TABLE")

number = 5
counter = 1

while counter <= 10:
    print(f"{number} x {counter} = {number * counter}")
    counter += 1

# ======================================
# 6. FACTORIAL USING WHILE LOOP
# ======================================

print("\n6. FACTORIAL USING WHILE LOOP")

number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial =", factorial)

# ======================================
# 7. USER INPUT EXAMPLE
# ======================================

print("\n7. USER INPUT EXAMPLE")

limit = int(input("Enter a positive number: "))

counter = 1

while counter <= limit:
    print(counter)
    counter += 1

# ======================================
# 8. PASSWORD CHECKER
# ======================================

print("\n8. PASSWORD CHECKER")

correct_password = "python123"

password = input("Enter password: ")

while password != correct_password:
    print("Incorrect Password!")
    password = input("Try Again: ")

print("Access Granted!")

# ======================================
# 9. COUNTDOWN TIMER
# ======================================

print("\n9. COUNTDOWN TIMER")

countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Time's Up!")

# ======================================
# 10. MINI PROJECT
# ======================================

print("\n10. MINI PROJECT - SIMPLE ATM")

balance = 5000

while True:

    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Updated Balance:", balance)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Updated Balance:", balance)
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank You for Using ATM")
        break

    else:
        print("Invalid Choice!")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Print numbers from 1 to 50
using a while loop.

Exercise 2:
Print odd numbers from
1 to 25.

Exercise 3:
Calculate the sum of
first 100 natural numbers.

Exercise 4:
Create a multiplication table
using a while loop.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Number Guessing Game.

Rules:

1. Store a secret number.
2. Ask the user to guess.
3. Continue until the correct
   number is entered.
4. Display the number of attempts.

Example:

Secret Number = 7

Input:
5
3
7

Output:
Correct Guess!
Attempts: 3
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 006 Completed Successfully!")