# -------------------------------------------------
# Day 22 NumPy
# Create Your Own ufunc using frompyfunc()
# -------------------------------------------------

import numpy as np


print("----- Example 1: Custom Addition ufunc -----")

def myadd(x, y):
    return x + y

add_ufunc = np.frompyfunc(myadd, 2, 1)

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(add_ufunc(arr1, arr2))


print("\n----- Example 2: Square ufunc -----")

def square(x):
    return x * x

square_ufunc = np.frompyfunc(square, 1, 1)

arr = np.array([1,2,3,4,5])

print(square_ufunc(arr))


print("\n----- Example 3: Cube ufunc -----")

def cube(x):
    return x ** 3

cube_ufunc = np.frompyfunc(cube, 1, 1)

print(cube_ufunc(arr))


print("\n----- Example 4: Even number check -----")

def is_even(x):
    return x % 2 == 0

even_ufunc = np.frompyfunc(is_even, 1, 1)

print(even_ufunc(arr))


print("\n----- Example 5: Power function -----")

def power(x, y):
    return x ** y

power_ufunc = np.frompyfunc(power, 2, 1)

arr_power = np.array([2,3,4,5])

print(power_ufunc(arr_power, 2))


print("\n----- Check ufunc type -----")

print(type(np.add))