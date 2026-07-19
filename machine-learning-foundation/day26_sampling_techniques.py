# ==========================================================
# Day 26 : Sampling Techniques
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 26")
print("=" * 60)

print("\nSampling Techniques")
print("-" * 30)

print("""
Sampling is the process of selecting
a subset of data from a larger population.

Instead of studying the entire population,
we study a representative sample.

Applications:

✓ Surveys
✓ Market Research
✓ Data Science
✓ Machine Learning
✓ Statistics
""")

# ----------------------------------------------------------
# Population and Sample
# ----------------------------------------------------------

print("\nPopulation vs Sample")
print("-" * 30)

population = list(range(1, 101))

sample = [5, 12, 25, 40, 55]

print("Population Size =", len(population))
print("Sample Size     =", len(sample))

print("""
Population:
Entire group of interest.

Sample:
Small subset selected from population.
""")

# ----------------------------------------------------------
# Why Sampling?
# ----------------------------------------------------------

print("\nWhy Sampling?")
print("-" * 30)

reasons = [
    "Saves Time",
    "Reduces Cost",
    "Faster Analysis",
    "Efficient Data Collection",
    "Useful for Large Datasets"
]

for reason in reasons:
    print("✓", reason)

# ----------------------------------------------------------
# Simple Random Sampling
# ----------------------------------------------------------

print("\n1. Simple Random Sampling")
print("-" * 30)

print("""
Every member has an equal chance
of being selected.
""")

simple_random_sample = [8, 21, 37, 49, 76]

print("Selected Sample:")
print(simple_random_sample)

# ----------------------------------------------------------
# Systematic Sampling
# ----------------------------------------------------------

print("\n2. Systematic Sampling")
print("-" * 30)

print("""
Select every kth element.

Example:
Every 10th student.
""")

systematic_sample = []

for i in range(10, 101, 10):
    systematic_sample.append(i)

print(systematic_sample)

# ----------------------------------------------------------
# Stratified Sampling
# ----------------------------------------------------------

print("\n3. Stratified Sampling")
print("-" * 30)

print("""
Population is divided into groups
(strata), then samples are taken
from each group.
""")

science_students = [1, 2, 3, 4, 5]
commerce_students = [6, 7, 8, 9, 10]

print("Science Group :", science_students)
print("Commerce Group:", commerce_students)

print("""
Sample selected from both groups.
""")

# ----------------------------------------------------------
# Cluster Sampling
# ----------------------------------------------------------

print("\n4. Cluster Sampling")
print("-" * 30)

print("""
Population is divided into clusters.

Entire clusters are selected randomly.
""")

cluster_A = [1, 2, 3, 4]
cluster_B = [5, 6, 7, 8]
cluster_C = [9, 10, 11, 12]

print("Cluster A =", cluster_A)
print("Cluster B =", cluster_B)
print("Cluster C =", cluster_C)

print("""
Suppose Cluster B is selected.
""")

# ----------------------------------------------------------
# Convenience Sampling
# ----------------------------------------------------------

print("\n5. Convenience Sampling")
print("-" * 30)

print("""
Data is collected from the easiest
available subjects.

Example:
Surveying nearby students.
""")

convenience_sample = [101, 102, 103]

print("Convenience Sample:")
print(convenience_sample)

# ----------------------------------------------------------
# Sampling Bias
# ----------------------------------------------------------

print("\nSampling Bias")
print("-" * 30)

print("""
Bias occurs when the sample
does not represent the population.

Example:

Surveying only one class
to represent an entire college.
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nSampling in Machine Learning")
print("-" * 30)

applications = [
    "Training Data Selection",
    "Model Validation",
    "Cross Validation",
    "Survey Analysis",
    "Big Data Processing",
    "Dataset Creation"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Student Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

students = [
    "Aman",
    "Riya",
    "Rahul",
    "Sneha",
    "Priya",
    "Vikas",
    "Anjali",
    "Karan"
]

sample_students = [
    "Rahul",
    "Priya",
    "Anjali"
]

print("Selected Sample:")
print(sample_students)

# ----------------------------------------------------------
# Business Example
# ----------------------------------------------------------

print("\nBusiness Example")
print("-" * 30)

customers = list(range(1, 1001))

print("Total Customers =", len(customers))

selected_customers = [15, 100, 250, 500, 800]

print("Survey Sample:")
print(selected_customers)

# ----------------------------------------------------------
# Sample Mean Example
# ----------------------------------------------------------

print("\nSample Mean")
print("-" * 30)

sample_marks = [60, 70, 80, 90, 100]

sample_mean = (
    sum(sample_marks) /
    len(sample_marks)
)

print("Sample Marks =", sample_marks)
print("Sample Mean  =", sample_mean)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

population_size = 500
sample_size = 50

print("Population Size =", population_size)
print("Sample Size     =", sample_size)

print("""
Question:
Why use a sample instead of
the entire population?

Answer:
Time and cost efficiency.
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Sampling?

2. What is a Population?

3. What is a Sample?

4. Name two sampling techniques.

5. Why is sampling useful?
""")

print("""
Answers:

1. Selecting a subset of data
2. Entire group of interest
3. Subset of population
4. Random and Stratified Sampling
5. Saves time and cost
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 26 Summary")
print("-" * 30)

print("""
1. Sampling selects a subset
   from a population.

2. Population is the complete group.

3. Sample is a smaller representative group.

4. Common techniques:

   ✓ Simple Random Sampling
   ✓ Systematic Sampling
   ✓ Stratified Sampling
   ✓ Cluster Sampling
   ✓ Convenience Sampling

5. Sampling is essential for
   Machine Learning and Statistics.
""")

print("\nDay 26 Completed Successfully!")
print("=" * 60)