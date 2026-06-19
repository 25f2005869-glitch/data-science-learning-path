# ======================================
# Day 007: break, continue and pass
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Loop Control Statements
# in Python
# ======================================

print("=" * 50)
print("DAY 007 - BREAK, CONTINUE AND PASS")
print("=" * 50)

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
Loop Control Statements are used to
change the normal execution of loops.

1. break
   - Terminates the loop immediately.

2. continue
   - Skips the current iteration and
     moves to the next iteration.

3. pass
   - Does nothing.
   - Used as a placeholder for future code.
"""

# ======================================
# 1. BREAK STATEMENT
# ======================================

print("\n1. BREAK STATEMENT")

for number in range(1, 11):

    if number == 6:
        break

    print(number)

# ======================================
# 2. CONTINUE STATEMENT
# ======================================

print("\n2. CONTINUE STATEMENT")

for number in range(1, 11):

    if number == 6:
        continue

    print(number)

# ======================================
# 3. PASS STATEMENT
# ======================================

print("\n3. PASS STATEMENT")

for number in range(1, 6):

    if number == 3:
        pass

    print(number)

# ======================================
# 4. BREAK WITH WHILE LOOP
# ======================================

print("\n4. BREAK WITH WHILE LOOP")

count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1

# ======================================
# 5. CONTINUE WITH WHILE LOOP
# ======================================

print("\n5. CONTINUE WITH WHILE LOOP")

count = 0

while count < 10:

    count += 1

    if count % 2 == 0:
        continue

    print(count)

# ======================================
# 6. SEARCHING A NUMBER
# ======================================

print("\n6. SEARCHING A NUMBER")

numbers = [10, 25, 40, 55, 70]

target = 40

for number in numbers:

    if number == target:
        print("Number Found!")
        break

# ======================================
# 7. SKIPPING VOWELS
# ======================================

print("\n7. SKIPPING VOWELS")

text = "SALONI TIWARI"

for character in text:

    if character in "AEIOU":
        continue

    print(character)

# ======================================
# 8. SIMPLE MENU SYSTEM
# ======================================

print("\n8. SIMPLE MENU SYSTEM")

while True:

    print("\n1. Start")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Program Started")

    elif choice == "2":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")

# ======================================
# 9. PASS IN FUNCTION
# ======================================

print("\n9. PASS IN FUNCTION")

def future_feature():
    pass

print("Function Created Successfully")

# ======================================
# 10. MINI PROJECT
# ======================================

print("\n10. MINI PROJECT - LOGIN SYSTEM")

correct_username = "saloni"
correct_password = "python123"

attempts = 0

while attempts < 3:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break

    else:
        print("Invalid Credentials")
        attempts += 1

if attempts == 3:
    print("Account Temporarily Locked")

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Print numbers from 1 to 20.

Stop the loop when the number
reaches 15 using break.

Exercise 2:
Print numbers from 1 to 20.

Skip all multiples of 3 using
continue.

Exercise 3:
Create a program that searches
for a specific number in a list.

Use break when the number is found.

Exercise 4:
Create an empty function using pass.
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a PIN Verification System.

Rules:

1. Correct PIN = 1234
2. User gets 3 attempts.
3. If PIN is correct:
   Display "Access Granted"
4. If all attempts fail:
   Display "Account Locked"

Use:
- while loop
- break statement
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 007 Completed Successfully!")