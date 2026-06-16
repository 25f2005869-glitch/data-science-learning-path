"""
========================================
NumPy Arithmetic ufunc Demo

Author: Saloni Tiwari
Topic: NumPy ufunc (Arithmetic + Custom)
Description:
Demonstrates arithmetic ufuncs like add, subtract,
multiply, divide and creation of custom ufunc using frompyfunc.
========================================
"""

# ========================================
# Import NumPy
# ========================================
import numpy as np


# ========================================
# Arithmetic ufunc Examples
# ========================================
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])

print("Array a:", a)
print("Array b:", b)

print("\n--- Arithmetic Operations ---")
print("Addition:", np.add(a, b))
print("Subtraction:", np.subtract(a, b))
print("Multiplication:", np.multiply(a, b))
print("Division:", np.divide(a, b))


# ========================================
# Custom ufunc using frompyfunc
# ========================================
def myadd(x, y):
    return x + y

myadd_ufunc = np.frompyfunc(myadd, 2, 1)

print("\n--- Custom ufunc ---")
print("Custom Add:", myadd_ufunc(a, b))


# ========================================
# Check ufunc type
# ========================================
print("\n--- Type Check ---")
print("Type of np.add:", type(np.add))
print("Type of custom ufunc:", type(myadd_ufunc))
