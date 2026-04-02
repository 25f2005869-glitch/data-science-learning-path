# ==========================================
# NumPy Complete Practice
# Author: Saloni Tiwari
# Description: NumPy practice from basics to distributions
# ==========================================

import numpy as np

print("NumPy Version:", np.__version__)

# ==========================================
# 1. Creating Arrays
# ==========================================

print("\n--- Creating Arrays ---")

arr1 = np.array([1,2,3,4,5])
print("1D Array:", arr1)

arr2 = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n", arr2)

# ==========================================
# 2. Array Attributes
# ==========================================

print("\n--- Array Attributes ---")

print("Shape:", arr2.shape)
print("Dimension:", arr2.ndim)
print("Size:", arr2.size)
print("Datatype:", arr2.dtype)

# ==========================================
# 3. Special Arrays
# ==========================================

print("\n--- Special Arrays ---")

zeros = np.zeros((3,3))
print("Zeros:\n", zeros)

ones = np.ones((2,2))
print("Ones:\n", ones)

full = np.full((2,2),7)
print("Full array:\n", full)

# ==========================================
# 4. Range Arrays
# ==========================================

print("\n--- Range Arrays ---")

a = np.arange(0,10)
print("Arange:", a)

b = np.arange(0,20,2)
print("Step array:", b)

c = np.linspace(0,10,5)
print("Linspace:", c)

# ==========================================
# 5. Reshape
# ==========================================

print("\n--- Reshape ---")

arr = np.arange(1,10)
reshaped = arr.reshape(3,3)

print("Original:", arr)
print("Reshaped:\n", reshaped)

# ==========================================
# 6. Flatten
# ==========================================

print("\n--- Flatten ---")

flat = reshaped.flatten()
print("Flatten:", flat)

# ==========================================
# 7. Indexing
# ==========================================

print("\n--- Indexing ---")

arr = np.array([10,20,30,40])

print("First element:", arr[0])
print("Last element:", arr[-1])

# ==========================================
# 8. Slicing
# ==========================================

print("\n--- Slicing ---")

print(arr[1:3])
print(arr[:2])
print(arr[2:])

# ==========================================
# 9. Copy vs View
# ==========================================

print("\n--- Copy vs View ---")

original = np.array([1,2,3])

copy_array = original.copy()
view_array = original.view()

original[0] = 100

print("Original:", original)
print("Copy:", copy_array)
print("View:", view_array)

# ==========================================
# 10. Iteration
# ==========================================

print("\n--- Iteration ---")

arr = np.array([[1,2],[3,4]])

for x in arr:
    for y in x:
        print(y)

# ==========================================
# 11. Joining Arrays
# ==========================================

print("\n--- Joining Arrays ---")

a = np.array([1,2,3])
b = np.array([4,5,6])

joined = np.concatenate((a,b))
print("Concatenated:", joined)

stack = np.stack((a,b))
print("Stack:\n", stack)

# ==========================================
# 12. Splitting Arrays
# ==========================================

print("\n--- Splitting Arrays ---")

arr = np.array([1,2,3,4,5,6])

split = np.array_split(arr,3)

print("Split:", split)

# ==========================================
# 13. Searching
# ==========================================

print("\n--- Searching ---")

arr = np.array([4,5,6,7,4,4])

index = np.where(arr == 4)

print("Index of 4:", index)

# ==========================================
# 14. Sorting
# ==========================================

print("\n--- Sorting ---")

arr = np.array([3,1,5,2])

sorted_arr = np.sort(arr)

print("Sorted:", sorted_arr)

# ==========================================
# 15. Filtering
# ==========================================

print("\n--- Filtering ---")

arr = np.array([10,20,30,40])

filtered = arr[arr > 20]

print("Filtered:", filtered)

# ==========================================
# 16. Random Numbers
# ==========================================

print("\n--- Random Numbers ---")

rand = np.random.rand(3,3)
print("Random matrix:\n", rand)

rand_int = np.random.randint(1,10,5)
print("Random integers:", rand_int)

# ==========================================
# 17. Random Choice
# ==========================================

print("\n--- Random Choice ---")

choice = np.random.choice([1,2,3,4], size=5)
print("Choice:", choice)

# ==========================================
# 18. Permutation and Shuffle
# ==========================================

print("\n--- Permutation ---")

arr = np.array([1,2,3,4])

print("Permutation:", np.random.permutation(arr))

np.random.shuffle(arr)
print("Shuffle:", arr)

# ==========================================
# 19. Normal Distribution
# ==========================================

print("\n--- Normal Distribution ---")

normal = np.random.normal(loc=0, scale=1, size=10)

print("Normal distribution:", normal)

# ==========================================
# 20. Binomial Distribution
# ==========================================

print("\n--- Binomial Distribution ---")

binomial = np.random.binomial(n=10, p=0.5, size=10)

print("Binomial:", binomial)

# ==========================================
# 21. Uniform Distribution
# ==========================================

print("\n--- Uniform Distribution ---")

uniform = np.random.uniform(size=10)

print("Uniform:", uniform)

# ==========================================
# 22. Logistic Distribution
# ==========================================

print("\n--- Logistic Distribution ---")

logistic = np.random.logistic(size=10)

print("Logistic:", logistic)

# ==========================================
# END
# ==========================================

print("\nNumPy Practice Completed Successfully")
