# ==========================================================
# Day 59 : Machine Learning Case Studies
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 59")
print("=" * 60)

print("\nMachine Learning Case Studies")
print("-" * 30)

print("""
Machine Learning is widely used
to solve real-world problems.

In this lesson, we will study
practical case studies from
different domains.

Goal:

✓ Understand Real Applications
✓ Connect Theory with Practice
✓ Learn Problem-Solving Approach
✓ Explore Industry Use Cases
""")

# ----------------------------------------------------------
# What is a Case Study?
# ----------------------------------------------------------

print("\nWhat is a Case Study?")
print("-" * 30)

print("""
A Case Study is a real-world
problem solved using Machine Learning.

It helps us understand:

✓ Problem Definition
✓ Data Collection
✓ Model Selection
✓ Evaluation
✓ Business Impact
""")

# ----------------------------------------------------------
# Case Study 1 : House Price Prediction
# ----------------------------------------------------------

print("\nCase Study 1 : House Price Prediction")
print("-" * 30)

print("""
Problem:

Predict house prices based on
property characteristics.

Features:

✓ Area
✓ Bedrooms
✓ Bathrooms
✓ Location
✓ Age of House

Target:

House Price

Type:

Regression Problem
""")

house_features = [
    ["Area", 1500],
    ["Bedrooms", 3],
    ["Bathrooms", 2]
]

for item in house_features:
    print(item)

print("""
Possible Models:

✓ Linear Regression
✓ Random Forest Regression
✓ Decision Tree Regression
""")

# ----------------------------------------------------------
# Case Study 2 : Email Spam Detection
# ----------------------------------------------------------

print("\nCase Study 2 : Email Spam Detection")
print("-" * 30)

print("""
Problem:

Classify emails as:

✓ Spam
✓ Not Spam

Features:

✓ Email Content
✓ Keywords
✓ Sender Information

Type:

Classification Problem
""")

emails = [
    "Win a Free Prize",
    "Meeting Schedule",
    "Claim Your Reward"
]

for email in emails:
    print("Email:", email)

print("""
Possible Models:

✓ Naive Bayes
✓ Logistic Regression
✓ SVM
""")

# ----------------------------------------------------------
# Case Study 3 : Student Performance Prediction
# ----------------------------------------------------------

print("\nCase Study 3 : Student Performance Prediction")
print("-" * 30)

print("""
Problem:

Predict student marks
before examinations.

Features:

✓ Study Hours
✓ Attendance
✓ Assignment Scores

Target:

Final Marks

Type:

Regression Problem
""")

students = [
    [5, 75, 70],
    [8, 85, 82],
    [10, 95, 92]
]

for student in students:
    print(student)

# ----------------------------------------------------------
# Case Study 4 : Customer Segmentation
# ----------------------------------------------------------

print("\nCase Study 4 : Customer Segmentation")
print("-" * 30)

print("""
Problem:

Group customers based on
similar behavior.

Features:

✓ Age
✓ Income
✓ Spending Score

Type:

Clustering Problem

Goal:

Create customer groups
for targeted marketing.
""")

customers = [
    [22, 20000, 30],
    [25, 25000, 40],
    [50, 90000, 90]
]

for customer in customers:
    print(customer)

print("""
Possible Models:

✓ K-Means
✓ Hierarchical Clustering
""")

# ----------------------------------------------------------
# Case Study 5 : Fraud Detection
# ----------------------------------------------------------

print("\nCase Study 5 : Fraud Detection")
print("-" * 30)

print("""
Problem:

Detect suspicious transactions.

Features:

✓ Transaction Amount
✓ Location
✓ Time
✓ Device Information

Type:

Classification / Anomaly Detection
""")

transactions = [
    500,
    700,
    900,
    100000
]

print("Transactions =", transactions)

print("""
Large unusual transactions
may indicate fraud.
""")

# ----------------------------------------------------------
# Case Study 6 : Medical Diagnosis
# ----------------------------------------------------------

print("\nCase Study 6 : Medical Diagnosis")
print("-" * 30)

print("""
Problem:

Predict disease risk.

Features:

✓ Age
✓ Blood Pressure
✓ Sugar Level
✓ Symptoms

Type:

Classification Problem

Goal:

Early Disease Detection
""")

patients = [
    [45, 120, 90],
    [60, 150, 180]
]

for patient in patients:
    print(patient)

# ----------------------------------------------------------
# Case Study 7 : Movie Recommendation
# ----------------------------------------------------------

print("\nCase Study 7 : Movie Recommendation")
print("-" * 30)

print("""
Problem:

Recommend movies users
are likely to enjoy.

Features:

✓ Watch History
✓ Ratings
✓ Preferences

Type:

Recommendation System
""")

movies = [
    "Interstellar",
    "Inception",
    "The Martian"
]

print("Recommended Movies =", movies)

# ----------------------------------------------------------
# Case Study 8 : Image Classification
# ----------------------------------------------------------

print("\nCase Study 8 : Image Classification")
print("-" * 30)

print("""
Problem:

Identify objects in images.

Examples:

✓ Cat vs Dog
✓ Fruit Recognition
✓ Medical Imaging

Type:

Classification Problem
""")

image_classes = [
    "Cat",
    "Dog",
    "Bird"
]

print("Classes =", image_classes)

# ----------------------------------------------------------
# Machine Learning Workflow
# ----------------------------------------------------------

print("\nCommon Workflow")
print("-" * 30)

steps = [
    "Define Problem",
    "Collect Data",
    "Clean Data",
    "Engineer Features",
    "Select Model",
    "Train Model",
    "Evaluate Model",
    "Deploy Solution"
]

for i, step in enumerate(
        steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Business Impact
# ----------------------------------------------------------

print("\nBusiness Impact")
print("-" * 30)

print("""
Machine Learning provides:

✓ Better Decisions
✓ Automation
✓ Cost Reduction
✓ Increased Revenue
✓ Better Customer Experience
""")

# ----------------------------------------------------------
# Industry Applications
# ----------------------------------------------------------

print("\nIndustry Applications")
print("-" * 30)

industries = [
    "Healthcare",
    "Finance",
    "Education",
    "Agriculture",
    "E-Commerce",
    "Manufacturing"
]

for industry in industries:
    print("✓", industry)

# ----------------------------------------------------------
# Advantages of Case Studies
# ----------------------------------------------------------

print("\nWhy Study Case Studies?")
print("-" * 30)

advantages = [
    "Understand Real Problems",
    "Learn Practical Thinking",
    "Connect Theory with Practice",
    "Improve Problem Solving",
    "Industry Awareness"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

problem = "Predict Student Marks"

model = "Linear Regression"

print("Problem =", problem)
print("Selected Model =", model)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

Which Machine Learning task is used
for Customer Segmentation?

Answer:

Clustering
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. Which ML task is used for
   House Price Prediction?

2. Which algorithm is commonly used
   for Spam Detection?

3. Which technique is used for
   Customer Segmentation?

4. What type of problem is
   Fraud Detection?

5. Give one application of
   Recommendation Systems.
""")

print("""
Answers:

1. Regression
2. Naive Bayes
3. Clustering
4. Classification
5. Movie Recommendation
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 59 Summary")
print("-" * 30)

print("""
1. Machine Learning solves
   real-world problems.

2. Common Applications:

   ✓ House Price Prediction
   ✓ Spam Detection
   ✓ Student Performance Prediction
   ✓ Customer Segmentation
   ✓ Fraud Detection
   ✓ Medical Diagnosis
   ✓ Recommendation Systems

3. Different problems require
   different ML techniques.

4. Case Studies help connect
   theory with practical use.

5. Understanding applications
   is essential for becoming
   a Data Scientist or
   Machine Learning Engineer.
""")

print("\nDay 59 Completed Successfully!")
print("=" * 60)