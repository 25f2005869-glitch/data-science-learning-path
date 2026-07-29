# ==========================================================
# Day 29 : Feature Engineering
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 29")
print("=" * 60)

print("\nFeature Engineering")
print("-" * 30)

print("""
Feature Engineering is the process of
creating, transforming, and selecting
useful features from raw data.

A feature is an input variable used
by a Machine Learning model.

Feature Engineering often improves
model performance more than changing
the algorithm itself.

Applications:

✓ Data Science
✓ Machine Learning
✓ Predictive Analytics
✓ Recommendation Systems
✓ Deep Learning
""")

# ----------------------------------------------------------
# What is a Feature?
# ----------------------------------------------------------

print("\nWhat is a Feature?")
print("-" * 30)

print("""
Example:

House Price Prediction

Features:

✓ Area
✓ Bedrooms
✓ Bathrooms
✓ Location

Target:

✓ House Price
""")

house = {
    "Area": 1200,
    "Bedrooms": 3,
    "Bathrooms": 2
}

print("House Features:")
print(house)

# ----------------------------------------------------------
# Raw Data Example
# ----------------------------------------------------------

print("\nRaw Data Example")
print("-" * 30)

students = [
    {"Name": "Rahul", "Math": 80, "Science": 90},
    {"Name": "Priya", "Math": 70, "Science": 85},
    {"Name": "Aman", "Math": 60, "Science": 75}
]

for student in students:
    print(student)

# ----------------------------------------------------------
# Creating New Features
# ----------------------------------------------------------

print("\n1. Creating New Features")
print("-" * 30)

print("""
New features can be created
from existing features.
""")

for student in students:

    total_marks = (
        student["Math"] +
        student["Science"]
    )

    student["Total"] = total_marks

print("Dataset with New Feature:")

for student in students:
    print(student)

# ----------------------------------------------------------
# Feature Transformation
# ----------------------------------------------------------

print("\n2. Feature Transformation")
print("-" * 30)

print("""
Sometimes data needs transformation
before model training.
""")

salary = [25000, 30000, 35000, 40000]

print("Original Salary =", salary)

salary_in_lakhs = []

for value in salary:
    salary_in_lakhs.append(value / 100000)

print("Salary in Lakhs =", salary_in_lakhs)

# ----------------------------------------------------------
# Date Feature Extraction
# ----------------------------------------------------------

print("\n3. Date Feature Extraction")
print("-" * 30)

dates = [
    "2026-01-15",
    "2026-04-20",
    "2026-07-10"
]

print("Dates =", dates)

months = []

for date in dates:

    month = date.split("-")[1]

    months.append(month)

print("Extracted Months =", months)

# ----------------------------------------------------------
# Encoding Categorical Features
# ----------------------------------------------------------

print("\n4. Encoding Categorical Features")
print("-" * 30)

cities = [
    "Delhi",
    "Mumbai",
    "Delhi",
    "Kolkata"
]

encoding = {
    "Delhi": 1,
    "Mumbai": 2,
    "Kolkata": 3
}

encoded_cities = []

for city in cities:
    encoded_cities.append(encoding[city])

print("Original Cities =", cities)
print("Encoded Cities  =", encoded_cities)

# ----------------------------------------------------------
# Feature Scaling
# ----------------------------------------------------------

print("\n5. Feature Scaling")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]

minimum = min(study_hours)
maximum = max(study_hours)

scaled_hours = []

for value in study_hours:

    scaled = (
        (value - minimum) /
        (maximum - minimum)
    )

    scaled_hours.append(round(scaled, 2))

print("Original Hours =", study_hours)
print("Scaled Hours   =", scaled_hours)

# ----------------------------------------------------------
# Feature Selection
# ----------------------------------------------------------

print("\n6. Feature Selection")
print("-" * 30)

print("""
Not every feature is useful.

Useful Features:
✓ Study Hours
✓ Attendance

Less Useful:
✓ Student ID
✓ Roll Number

Feature Selection improves
model efficiency.
""")

features = [
    "Study Hours",
    "Attendance",
    "Student ID",
    "Marks"
]

selected_features = [
    "Study Hours",
    "Attendance",
    "Marks"
]

print("All Features      =", features)
print("Selected Features =", selected_features)

# ----------------------------------------------------------
# Machine Learning Example
# ----------------------------------------------------------

print("\nMachine Learning Example")
print("-" * 30)

student_data = [
    [18, 6, 90],
    [19, 8, 95],
    [17, 5, 85]
]

print("""
Features:

Age
Study Hours
Attendance
""")

for row in student_data:
    print(row)

# ----------------------------------------------------------
# Feature Importance Concept
# ----------------------------------------------------------

print("\nFeature Importance")
print("-" * 30)

importance = {
    "Study Hours": 0.60,
    "Attendance": 0.30,
    "Age": 0.10
}

for feature, score in importance.items():
    print(feature, "=", score)

print("""
Higher score means
greater influence on predictions.
""")

# ----------------------------------------------------------
# Business Example
# ----------------------------------------------------------

print("\nBusiness Example")
print("-" * 30)

sales_data = [
    {"Advertising": 1000, "Sales": 5000},
    {"Advertising": 2000, "Sales": 8000},
    {"Advertising": 3000, "Sales": 12000}
]

for row in sales_data:
    print(row)

print("""
Advertising can be an important
feature for predicting sales.
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

weights = [50, 60, 70, 80]

weight_category = []

for weight in weights:

    if weight < 60:
        weight_category.append("Low")

    elif weight < 75:
        weight_category.append("Medium")

    else:
        weight_category.append("High")

print("Weights          =", weights)
print("Weight Categories =", weight_category)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

ages = [18, 19, 20, 21]

age_squared = []

for age in ages:
    age_squared.append(age ** 2)

print("Ages        =", ages)
print("Age Squared =", age_squared)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Feature?

2. What is Feature Engineering?

3. Why is Feature Selection important?

4. Give one example of
   Feature Transformation.

5. Why is Feature Engineering useful?
""")

print("""
Answers:

1. Input variable used by ML model
2. Creating and improving features
3. Removes unnecessary information
4. Scaling salary values
5. Improves model performance
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 29 Summary")
print("-" * 30)

print("""
1. Features are inputs used by ML models.

2. Feature Engineering creates better
   representations of data.

3. New features can be derived from
   existing features.

4. Feature Transformation improves
   data quality.

5. Feature Selection removes
   unnecessary features.

6. Good Feature Engineering often leads
   to better Machine Learning models.
""")

print("\nDay 29 Completed Successfully!")
print("=" * 60)