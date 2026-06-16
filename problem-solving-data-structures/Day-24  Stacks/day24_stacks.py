# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Stacks
# Day         : 24
# Description : Basic stack operations using Python list.
# ==========================================================

stack = []

# Push Operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack After Push:", stack)

# Peek Operation
print("Top Element:", stack[-1])

# Pop Operation
removed = stack.pop()

print("Removed Element:", removed)

print("Stack After Pop:", stack)

# Is Empty Check
if len(stack) == 0:

    print("Stack is Empty")

else:

    print("Stack is Not Empty")