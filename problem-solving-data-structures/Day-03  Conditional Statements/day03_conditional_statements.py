# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Conditional Statements
# Day         : 03
# Description : Understanding if, elif and else statements.
# ==========================================================

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")