# ======================================
# Day 047: NumPy Random Module
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Understanding Random Number
# Generation using NumPy
# ======================================

print("=" * 50)
print("DAY 047 - NUMPY RANDOM MODULE")
print("=" * 50)

# ======================================
# IMPORT NUMPY
# ======================================

import numpy as np

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
NumPy Random Module

The random module is used to:

1. Generate Random Numbers
2. Create Random Arrays
3. Simulate Experiments
4. Generate Sample Datasets
5. Machine Learning Testing

Common Functions:

1. np.random.randint()
2. np.random.rand()
3. np.random.randn()
4. np.random.choice()
5. np.random.seed()

Applications:

- Data Science
- Machine Learning
- Statistics
- Simulations
"""

# ======================================
# 1. RANDOM INTEGER
# ======================================

print("\n1. RANDOM INTEGER")

random_number = np.random.randint(
    1,
    101
)

print(random_number)

# ======================================
# 2. RANDOM FLOAT
# ======================================

print("\n2. RANDOM FLOAT")

random_float = np.random.rand()

print(random_float)

# ======================================
# 3. RANDOM FLOAT ARRAY
# ======================================

print("\n3. RANDOM FLOAT ARRAY")

array = np.random.rand(5)

print(array)

# ======================================
# 4. RANDOM INTEGER ARRAY
# ======================================

print("\n4. RANDOM INTEGER ARRAY")

array = np.random.randint(
    1,
    100,
    size=10
)

print(array)

# ======================================
# 5. 2D RANDOM ARRAY
# ======================================

print("\n5. 2D RANDOM ARRAY")

matrix = np.random.randint(
    1,
    10,
    size=(3, 3)
)

print(matrix)

# ======================================
# 6. RANDOM NORMAL VALUES
# ======================================

print("\n6. RANDOM NORMAL VALUES")

values = np.random.randn(5)

print(values)

# ======================================
# 7. RANDOM CHOICE
# ======================================

print("\n7. RANDOM CHOICE")

subjects = [
    "Python",
    "DBMS",
    "Statistics",
    "MLF"
]

selected = np.random.choice(
    subjects
)

print(selected)

# ======================================
# 8. MULTIPLE RANDOM CHOICES
# ======================================

print("\n8. MULTIPLE RANDOM CHOICES")

choices = np.random.choice(
    subjects,
    size=3
)

print(choices)

# ======================================
# 9. RANDOM SEED
# ======================================

print("\n9. RANDOM SEED")

np.random.seed(42)

print(
    np.random.randint(
        1,
        100,
        size=5
    )
)

# ======================================
# 10. RANDOM SHUFFLE
# ======================================

print("\n10. RANDOM SHUFFLE")

numbers = np.array(
    [1, 2, 3, 4, 5]
)

np.random.shuffle(numbers)

print(numbers)

# ======================================
# 11. RANDOM PERMUTATION
# ======================================

print("\n11. RANDOM PERMUTATION")

numbers = np.array(
    [10, 20, 30, 40, 50]
)

permutation = np.random.permutation(
    numbers
)

print(permutation)

# ======================================
# 12. RANDOM SAMPLE
# ======================================

print("\n12. RANDOM SAMPLE")

sample = np.random.random(
    size=5
)

print(sample)

# ======================================
# 13. GENERATE MARKS DATA
# ======================================

print("\n13. GENERATED MARKS DATA")

marks = np.random.randint(
    40,
    101,
    size=10
)

print(marks)

# ======================================
# 14. RANDOM MATRIX
# ======================================

print("\n14. RANDOM MATRIX")

matrix = np.random.randint(
    1,
    100,
    size=(4, 4)
)

print(matrix)

# ======================================
# 15. USER INPUT SIZE
# ======================================

print("\n15. USER INPUT SIZE")

size = int(
    input(
        "Enter Array Size: "
    )
)

random_array = np.random.randint(
    1,
    100,
    size=size
)

print(random_array)

# ======================================
# 16. RANDOM STATISTICS
# ======================================

print("\n16. RANDOM STATISTICS")

data = np.random.randint(
    1,
    100,
    size=20
)

print("Data:")
print(data)

print("Mean:",
      np.mean(data))

print("Maximum:",
      np.max(data))

print("Minimum:",
      np.min(data))

# ======================================
# 17. MINI PROJECT
# ======================================

print("\n17. MINI PROJECT - STUDENT MARKS GENERATOR")

marks = np.random.randint(
    40,
    101,
    size=20
)

print("Generated Marks:")
print(marks)

print("\nStatistics")
print("-" * 25)

print("Total   :",
      np.sum(marks))

print("Average :",
      round(
          np.mean(marks),
          2
      ))

print("Highest :",
      np.max(marks))

print("Lowest  :",
      np.min(marks))

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Generate:

- Random Integer
- Random Float

Exercise 2:
Generate:

- Random 1D Array
- Random 2D Array

Exercise 3:
Use:

- shuffle()
- permutation()

Exercise 4:
Generate marks of
30 students and find:

- Mean
- Maximum
- Minimum
"""

# ======================================
# CHALLENGE QUESTION
# ======================================

"""
Create a Student Performance Simulator.

Generate marks of 50 students.

Calculate:

1. Total Marks
2. Average Marks
3. Highest Marks
4. Lowest Marks
5. Standard Deviation

Display a complete report.
"""

# ======================================
# END OF PROGRAM
# ======================================

print("\nDay 047 Completed Successfully!")