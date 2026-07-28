# ==========================================================
# Day 28 : Data Preprocessing
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 28")
print("=" * 60)

print("\nData Preprocessing")
print("-" * 30)

print("""
Data Preprocessing is the process of
cleaning and transforming raw data before
using it in a Machine Learning model.

Real-world data is often:

✓ Incomplete
✓ Noisy
✓ Inconsistent
✓ Missing Values
✓ Duplicate Records

Therefore, preprocessing is a critical
step in the ML workflow.
""")

# ----------------------------------------------------------
# Sample Raw Dataset
# ----------------------------------------------------------

print("\nRaw Dataset")
print("-" * 30)

student_data = [
    ["Rahul", 18, 85],
    ["Priya", None, 90],
    ["Aman", 19, None],
    ["Sneha", 18, 85],
    ["Rahul", 18, 85]
]

for row in student_data:
    print(row)

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\n1. Handling Missing Values")
print("-" * 30)

print("""
Missing values can affect
model performance.

Common Solutions:

✓ Remove Records
✓ Replace with Mean
✓ Replace with Median
✓ Replace with Mode
""")

ages = [18, 19, 18]

mean_age = sum(ages) / len(ages)

print("Mean Age =", mean_age)

filled_age = mean_age

print("Missing Age Replaced With =", filled_age)

# ----------------------------------------------------------
# Duplicate Records
# ----------------------------------------------------------

print("\n2. Removing Duplicate Records")
print("-" * 30)

unique_records = []

for record in student_data:

    if record not in unique_records:
        unique_records.append(record)

print("Dataset After Removing Duplicates:")

for row in unique_records:
    print(row)

# ----------------------------------------------------------
# Data Cleaning
# ----------------------------------------------------------

print("\n3. Data Cleaning")
print("-" * 30)

names = [
    " Rahul ",
    " PRIYA ",
    " aman "
]

print("Original Names:")
print(names)

cleaned_names = []

for name in names:

    cleaned_name = name.strip().title()

    cleaned_names.append(cleaned_name)

print("Cleaned Names:")
print(cleaned_names)

# ----------------------------------------------------------
# Feature Scaling
# ----------------------------------------------------------

print("\n4. Feature Scaling")
print("-" * 30)

print("""
Feature Scaling brings features
to a similar range.

Benefits:

✓ Faster Training
✓ Better Accuracy
✓ Stable Optimization
""")

study_hours = [2, 4, 6, 8, 10]

minimum = min(study_hours)
maximum = max(study_hours)

scaled_values = []

for value in study_hours:

    scaled = (
        (value - minimum) /
        (maximum - minimum)
    )

    scaled_values.append(round(scaled, 2))

print("Original Values =", study_hours)
print("Scaled Values   =", scaled_values)

# ----------------------------------------------------------
# Normalization
# ----------------------------------------------------------

print("\n5. Normalization")
print("-" * 30)

print("""
Min-Max Normalization:

(X - Min) / (Max - Min)

Result:
Values between 0 and 1
""")

# ----------------------------------------------------------
# Standardization
# ----------------------------------------------------------

print("\n6. Standardization")
print("-" * 30)

print("""
Formula:

Z = (X - Mean) / SD

Result:
Mean = 0
Standard Deviation = 1
""")

data = [10, 20, 30, 40, 50]

mean = sum(data) / len(data)

variance = sum(
    (x - mean) ** 2
    for x in data
) / len(data)

sd = variance ** 0.5

standardized = []

for x in data:

    z = round((x - mean) / sd, 2)

    standardized.append(z)

print("Original Data     =", data)
print("Standardized Data =", standardized)

# ----------------------------------------------------------
# Encoding Categorical Data
# ----------------------------------------------------------

print("\n7. Encoding Categorical Data")
print("-" * 30)

print("""
Machine Learning models work
with numbers.

Categorical values must be encoded.
""")

gender = [
    "Male",
    "Female",
    "Male",
    "Female"
]

encoded_gender = []

for value in gender:

    if value == "Male":
        encoded_gender.append(1)
    else:
        encoded_gender.append(0)

print("Original =", gender)
print("Encoded  =", encoded_gender)

# ----------------------------------------------------------
# Train-Test Split Concept
# ----------------------------------------------------------

print("\n8. Train-Test Split")
print("-" * 30)

print("""
Training Data:
Used to train model.

Testing Data:
Used to evaluate model.

Common Split:

80% Training
20% Testing
""")

dataset = list(range(1, 11))

train_data = dataset[:8]
test_data = dataset[8:]

print("Training Data =", train_data)
print("Testing Data  =", test_data)

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nData Preprocessing in ML")
print("-" * 30)

applications = [
    "Data Cleaning",
    "Feature Engineering",
    "Feature Scaling",
    "Model Training",
    "Data Transformation",
    "Machine Learning Pipelines"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Student Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

marks = [50, 60, 70, 80, 90]

mean_marks = sum(marks) / len(marks)

print("Marks =", marks)
print("Average Marks =", mean_marks)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

salary = [25000, 30000, 35000, 40000, 45000]

min_salary = min(salary)
max_salary = max(salary)

normalized_salary = []

for value in salary:

    normalized = (
        (value - min_salary) /
        (max_salary - min_salary)
    )

    normalized_salary.append(round(normalized, 2))

print("Original Salary =", salary)
print("Normalized Salary =", normalized_salary)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

cities = [
    " Delhi ",
    " mumbai ",
    " KOLKATA "
]

cleaned_cities = []

for city in cities:
    cleaned_cities.append(city.strip().title())

print("Cleaned Cities =", cleaned_cities)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Data Preprocessing?

2. Why are missing values a problem?

3. What is Feature Scaling?

4. Why do we encode categorical data?

5. What is Train-Test Split?
""")

print("""
Answers:

1. Cleaning and transforming data
2. They can affect model performance
3. Bringing features to similar scale
4. ML models require numerical values
5. Dividing data for training and testing
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 28 Summary")
print("-" * 30)

print("""
1. Data Preprocessing prepares raw data
   for Machine Learning.

2. Missing values should be handled carefully.

3. Duplicate records should be removed.

4. Feature Scaling improves model performance.

5. Normalization scales data between 0 and 1.

6. Standardization uses mean and standard deviation.

7. Categorical data must be encoded.

8. Train-Test Split is essential for evaluation.
""")

print("\nDay 28 Completed Successfully!")
print("=" * 60)