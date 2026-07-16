# ==========================================================
# Day 25 : Covariance
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 25")
print("=" * 60)

print("\nCovariance")
print("-" * 30)

print("""
Covariance measures how two variables
change together.

It helps determine whether variables
move in the same direction or in
opposite directions.

Applications:

✓ Data Analysis
✓ Statistics
✓ Machine Learning
✓ Feature Engineering
✓ Financial Analysis
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]

print("Study Hours =", study_hours)
print("Marks       =", marks)

# ----------------------------------------------------------
# Calculate Means
# ----------------------------------------------------------

print("\nStep 1 : Calculate Means")
print("-" * 30)

mean_x = sum(study_hours) / len(study_hours)
mean_y = sum(marks) / len(marks)

print("Mean of Study Hours =", mean_x)
print("Mean of Marks       =", mean_y)

# ----------------------------------------------------------
# Covariance Calculation
# ----------------------------------------------------------

print("\nStep 2 : Covariance Calculation")
print("-" * 30)

covariance_sum = 0

for x, y in zip(study_hours, marks):

    covariance_sum += (
        (x - mean_x) *
        (y - mean_y)
    )

covariance = covariance_sum / len(study_hours)

print("Covariance =", round(covariance, 2))

# ----------------------------------------------------------
# Understanding Covariance
# ----------------------------------------------------------

print("\nInterpretation")
print("-" * 30)

print("""
Covariance > 0
→ Positive Relationship

Covariance < 0
→ Negative Relationship

Covariance = 0
→ No Linear Relationship
""")

if covariance > 0:
    print("Result : Positive Covariance")

elif covariance < 0:
    print("Result : Negative Covariance")

else:
    print("Result : No Covariance")

# ----------------------------------------------------------
# Positive Covariance Example
# ----------------------------------------------------------

print("\nPositive Covariance Example")
print("-" * 30)

temperature = [20, 22, 24, 26, 28]
ice_cream_sales = [100, 120, 140, 160, 180]

print("Temperature     =", temperature)
print("Ice Cream Sales =", ice_cream_sales)

print("""
As temperature increases,
ice cream sales also increase.

Positive Covariance
""")

# ----------------------------------------------------------
# Negative Covariance Example
# ----------------------------------------------------------

print("\nNegative Covariance Example")
print("-" * 30)

speed = [20, 30, 40, 50, 60]
travel_time = [60, 50, 40, 30, 20]

print("Speed       =", speed)
print("Travel Time =", travel_time)

print("""
As speed increases,
travel time decreases.

Negative Covariance
""")

# ----------------------------------------------------------
# Covariance Matrix
# ----------------------------------------------------------

print("\nCovariance Matrix")
print("-" * 30)

print("""
A Covariance Matrix stores covariance
between multiple variables.

Example:

           X      Y
X      Cov(X,X) Cov(X,Y)

Y      Cov(Y,X) Cov(Y,Y)
""")

covariance_matrix = [
    [1.00, 0.85],
    [0.85, 1.00]
]

print("Covariance Matrix:")

for row in covariance_matrix:
    print(row)

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nCovariance in Machine Learning")
print("-" * 30)

applications = [
    "Feature Selection",
    "Principal Component Analysis (PCA)",
    "Data Exploration",
    "Dimensionality Reduction",
    "Anomaly Detection",
    "Statistical Modeling"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# PCA Connection
# ----------------------------------------------------------

print("\nCovariance and PCA")
print("-" * 30)

print("""
Principal Component Analysis (PCA)
uses the covariance matrix to find
important directions in data.

Steps:

1. Create Covariance Matrix
2. Calculate Eigenvalues
3. Calculate Eigenvectors
4. Select Principal Components
""")

# ----------------------------------------------------------
# Student Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

attendance = [60, 70, 80, 90, 100]
grades = [55, 65, 75, 85, 95]

print("Attendance =", attendance)
print("Grades     =", grades)

print("""
Higher Attendance
→ Higher Grades

Positive Covariance
""")

# ----------------------------------------------------------
# Business Example
# ----------------------------------------------------------

print("\nBusiness Example")
print("-" * 30)

advertising = [10, 20, 30, 40, 50]
sales = [100, 150, 200, 250, 300]

print("Advertising Budget =", advertising)
print("Sales Revenue      =", sales)

print("""
More Advertising
→ More Sales

Positive Covariance
""")

# ----------------------------------------------------------
# Difference Between Covariance and Correlation
# ----------------------------------------------------------

print("\nCovariance vs Correlation")
print("-" * 30)

print("""
Covariance:

✓ Shows direction
✓ Depends on units
✓ Can be any value

Correlation:

✓ Shows direction
✓ Shows strength
✓ Always between -1 and +1
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

cov_sum = 0

for a, b in zip(x, y):
    cov_sum += (
        (a - mean_x) *
        (b - mean_y)
    )

practice_covariance = cov_sum / len(x)

print("Covariance =", practice_covariance)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Covariance?

2. What does positive covariance mean?

3. What does negative covariance mean?

4. What is a Covariance Matrix?

5. Which ML technique heavily uses
   Covariance Matrices?
""")

print("""
Answers:

1. Measure of joint variability
2. Variables move together
3. Variables move oppositely
4. Matrix of covariances
5. PCA
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 25 Summary")
print("-" * 30)

print("""
1. Covariance measures how variables
   change together.

2. Positive covariance indicates
   variables move in the same direction.

3. Negative covariance indicates
   variables move in opposite directions.

4. Covariance Matrix is important
   for multivariable analysis.

5. PCA relies heavily on covariance.

6. Covariance is the foundation of
   correlation analysis.
""")

print("\nStatistics Module Completed!")
print("Day 25 Completed Successfully!")
print("=" * 60)