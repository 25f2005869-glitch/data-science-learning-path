# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Recursion
# Day         : 06
# Description : Understanding recursive functions using
#               factorial calculation.
# ==========================================================

def factorial(n):

    # Base Case
    if n == 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)


number = int(input("Enter a number: "))

result = factorial(number)

print("Factorial =", result)