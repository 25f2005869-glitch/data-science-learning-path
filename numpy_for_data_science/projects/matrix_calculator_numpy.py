"""
NumPy Matrix Calculator

Operations:
1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication

Author: Saloni Tiwari
"""
import numpy as np

print("=== NumPy Matrix Calculator ===")

# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter values for Matrix A")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("\nEnter values for Matrix B")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

# Convert to NumPy arrays
A = np.array(A)
B = np.array(B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nChoose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    result = A + B
    print("\nResult (Addition):")
    print(result)

elif choice == "2":
    result = A - B
    print("\nResult (Subtraction):")
    print(result)

elif choice == "3":
    result = np.dot(A, B)
    print("\nResult (Multiplication):")
    print(result)

else:
    print("Invalid choice")