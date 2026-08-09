# ==========================================================
# Day 38 : Multiple Linear Regression
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 38")
print("=" * 60)

print("\nMultiple Linear Regression")
print("-" * 30)

print("""
Multiple Linear Regression is an extension
of Simple Linear Regression.

Simple Linear Regression:
Uses one input feature.

Multiple Linear Regression:
Uses multiple input features.

Goal:

Predict a target variable using
two or more independent variables.
""")

# ----------------------------------------------------------
# Why Multiple Linear Regression?
# ----------------------------------------------------------

print("\nWhy Multiple Linear Regression?")
print("-" * 30)

print("""
Many real-world problems depend on
multiple factors.

Examples:

House Price depends on:
✓ Area
✓ Bedrooms
✓ Location

Student Marks depend on:
✓ Study Hours
✓ Attendance
✓ Assignment Scores

Salary depends on:
✓ Experience
✓ Education
✓ Skills
""")

# ----------------------------------------------------------
# Multiple Linear Regression Equation
# ----------------------------------------------------------

print("\nMultiple Linear Regression Equation")
print("-" * 30)

print("""
Equation:

Y = b0 + b1X1 + b2X2 + b3X3 + ...

Where:

Y  = Predicted Output
b0 = Intercept

X1 = Feature 1
X2 = Feature 2
X3 = Feature 3

b1, b2, b3 = Coefficients
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nStudent Dataset")
print("-" * 30)

study_hours = [4, 6, 8, 10]
attendance = [70, 80, 90, 95]
marks = [55, 70, 85, 95]

print("Study Hours =", study_hours)
print("Attendance  =", attendance)
print("Marks       =", marks)

print("""
Features:
1. Study Hours
2. Attendance

Target:
Marks
""")

# ----------------------------------------------------------
# Sample Coefficients
# ----------------------------------------------------------

print("\nSample Model Coefficients")
print("-" * 30)

b0 = 10
b1 = 5
b2 = 0.4

print("Intercept (b0) =", b0)
print("Study Hours Coefficient (b1) =", b1)
print("Attendance Coefficient (b2) =", b2)

# ----------------------------------------------------------
# Making Predictions
# ----------------------------------------------------------

print("\nPrediction Example")
print("-" * 30)

study_hour = 8
attendance_percentage = 90

predicted_marks = (
    b0 +
    b1 * study_hour +
    b2 * attendance_percentage
)

print("Study Hours =", study_hour)
print("Attendance  =", attendance_percentage)

print("Predicted Marks =",
      round(predicted_marks, 2))

# ----------------------------------------------------------
# Understanding Coefficients
# ----------------------------------------------------------

print("\nUnderstanding Coefficients")
print("-" * 30)

print("""
b1 = 5

If Study Hours increase by 1,
Marks increase by 5 units
(assuming attendance remains constant).

b2 = 0.4

If Attendance increases by 1%,
Marks increase by 0.4 units
(assuming study hours remain constant).
""")

# ----------------------------------------------------------
# Features Matrix
# ----------------------------------------------------------

print("\nFeature Matrix")
print("-" * 30)

X = [
    [4, 70],
    [6, 80],
    [8, 90],
    [10, 95]
]

print("Feature Matrix:")

for row in X:
    print(row)

print("""
Rows    → Observations
Columns → Features
""")

# ----------------------------------------------------------
# Target Vector
# ----------------------------------------------------------

print("\nTarget Vector")
print("-" * 30)

Y = [55, 70, 85, 95]

print("Target Values =", Y)

# ----------------------------------------------------------
# Real World Example
# ----------------------------------------------------------

print("\nHouse Price Prediction")
print("-" * 30)

house_data = [
    [1200, 2, 20],
    [1500, 3, 30],
    [1800, 3, 40],
    [2200, 4, 50]
]

print("""
Features:

Area (sq ft)
Bedrooms
Location Score

Target:

House Price
""")

for house in house_data:
    print(house)

# ----------------------------------------------------------
# Salary Prediction Example
# ----------------------------------------------------------

print("\nSalary Prediction")
print("-" * 30)

salary_data = [
    [1, 12, 25000],
    [3, 14, 40000],
    [5, 16, 60000]
]

print("""
Features:

Experience
Education Years

Target:

Salary
""")

for row in salary_data:
    print(row)

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Uses Multiple Features",
    "Improved Predictions",
    "Captures Complex Relationships",
    "Widely Used",
    "Easy to Interpret"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Sensitive to Outliers",
    "Requires Linear Relationship",
    "Can Suffer From Multicollinearity",
    "Needs Quality Data"
]

for item in limitations:
    print("✗", item)

# ----------------------------------------------------------
# Multicollinearity
# ----------------------------------------------------------

print("\nMulticollinearity")
print("-" * 30)

print("""
Multicollinearity occurs when
features are highly correlated.

Example:

Age and Years of Experience

Too much correlation between features
can reduce model quality.
""")

# ----------------------------------------------------------
# Machine Learning Workflow
# ----------------------------------------------------------

print("\nWorkflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Clean Data",
    "Select Features",
    "Train Model",
    "Evaluate Model",
    "Make Predictions"
]

for i, step in enumerate(steps, start=1):
    print(f"{i}. {step}")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

experience = 4
education_years = 15

salary_prediction = (
    5000 +
    (6000 * experience) +
    (1000 * education_years)
)

print("Experience =", experience)
print("Education Years =", education_years)

print("Predicted Salary =",
      salary_prediction)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

b0 = 5
b1 = 2
b2 = 3

x1 = 4
x2 = 6

y = (
    b0 +
    b1 * x1 +
    b2 * x2
)

print("Predicted Y =", y)

print("""
Question:

Y = 5 + 2(4) + 3(6)

Answer = 31
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Multiple Linear Regression?

2. How many features can it use?

3. What is a coefficient?

4. What is multicollinearity?

5. Give one real-world application.
""")

print("""
Answers:

1. Regression using multiple features
2. Two or more features
3. Value showing feature impact
4. High correlation among features
5. House Price Prediction
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 38 Summary")
print("-" * 30)

print("""
1. Multiple Linear Regression extends
   Simple Linear Regression.

2. It uses multiple input features.

3. General Equation:

   Y = b0 + b1X1 + b2X2 + ...

4. Coefficients measure feature impact.

5. It is widely used for prediction tasks.

6. Feature selection is important.

7. Multicollinearity should be avoided.
""")

print("\nDay 38 Completed Successfully!")
print("=" * 60)