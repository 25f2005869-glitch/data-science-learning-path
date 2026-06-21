# ==========================================================
# Day 05 : ML Case Studies
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 05")
print("=" * 60)

print("\nWhat is a Case Study?")
print("-" * 30)

print("""
A Machine Learning Case Study is a real-world problem
that can be solved using data and machine learning.

Case studies help us understand how ML is applied
in practical situations.
""")

# ----------------------------------------------------------
# Case Study 1 : Student Performance Prediction
# ----------------------------------------------------------

print("\nCase Study 1 : Student Performance Prediction")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]

print("Study Hours :", study_hours)
print("Marks       :", marks)

print("""
Problem:
Predict student marks based on study hours.

Input Feature:
✓ Study Hours

Target:
✓ Marks

Possible Algorithm:
✓ Linear Regression
""")

# ----------------------------------------------------------
# Case Study 2 : House Price Prediction
# ----------------------------------------------------------

print("\nCase Study 2 : House Price Prediction")
print("-" * 30)

house_sizes = [800, 1000, 1200, 1500, 1800]
house_prices = [20, 25, 30, 38, 45]

print("House Sizes (sq ft):", house_sizes)
print("House Prices (Lakhs):", house_prices)

print("""
Problem:
Predict the price of a house.

Input Features:
✓ Area
✓ Number of Rooms
✓ Location

Target:
✓ House Price

Possible Algorithm:
✓ Linear Regression
✓ Random Forest
""")

# ----------------------------------------------------------
# Case Study 3 : Email Spam Detection
# ----------------------------------------------------------

print("\nCase Study 3 : Email Spam Detection")
print("-" * 30)

emails = [
    "Win a free iPhone now!",
    "Meeting scheduled for tomorrow",
    "Claim your reward today"
]

for email in emails:
    print("Email:", email)

print("""
Problem:
Classify emails as Spam or Not Spam.

Output Classes:
✓ Spam
✓ Not Spam

Possible Algorithm:
✓ Naive Bayes
✓ Logistic Regression
""")

# ----------------------------------------------------------
# Case Study 4 : Customer Segmentation
# ----------------------------------------------------------

print("\nCase Study 4 : Customer Segmentation")
print("-" * 30)

customer_spending = [1200, 1500, 1700, 6000, 6500, 7000]

print("Customer Spending Data:")
print(customer_spending)

print("""
Problem:
Group customers based on spending behavior.

Output:
✓ Low Spending Customers
✓ Medium Spending Customers
✓ High Spending Customers

Possible Algorithm:
✓ K-Means Clustering
""")

# ----------------------------------------------------------
# Case Study 5 : Medical Diagnosis
# ----------------------------------------------------------

print("\nCase Study 5 : Medical Diagnosis")
print("-" * 30)

print("""
Problem:
Predict whether a patient has a disease.

Input Features:
✓ Age
✓ Blood Pressure
✓ Sugar Level
✓ Medical History

Output:
✓ Disease Present
✓ Disease Not Present

Possible Algorithms:
✓ Decision Tree
✓ Random Forest
✓ Logistic Regression
""")

# ----------------------------------------------------------
# Case Study 6 : Recommendation System
# ----------------------------------------------------------

print("\nCase Study 6 : Recommendation System")
print("-" * 30)

movies = [
    "Inception",
    "Interstellar",
    "The Dark Knight"
]

print("Movies Watched:")
for movie in movies:
    print("✓", movie)

print("""
Problem:
Recommend movies similar to user interests.

Applications:
✓ Netflix
✓ YouTube
✓ Amazon

Possible Algorithms:
✓ Collaborative Filtering
✓ Content-Based Filtering
""")

# ----------------------------------------------------------
# Case Study 7 : Fraud Detection
# ----------------------------------------------------------

print("\nCase Study 7 : Fraud Detection")
print("-" * 30)

transactions = [500, 700, 1000, 25000, 40000]

print("Transaction Amounts:")
print(transactions)

print("""
Problem:
Identify suspicious transactions.

Output:
✓ Fraud
✓ Genuine

Applications:
✓ Banking
✓ Online Payments
✓ Credit Cards

Possible Algorithms:
✓ Decision Tree
✓ Random Forest
✓ Isolation Forest
""")

# ----------------------------------------------------------
# Benefits of ML Case Studies
# ----------------------------------------------------------

print("\nBenefits of ML Case Studies")
print("-" * 30)

benefits = [
    "Understand real-world problems",
    "Learn data-driven decision making",
    "Connect theory with practice",
    "Build project experience",
    "Improve problem-solving skills"
]

for benefit in benefits:
    print("✓", benefit)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

questions = [
    "Predicting house prices",
    "Grouping customers",
    "Detecting spam emails",
    "Predicting student marks"
]

for i, question in enumerate(questions, start=1):
    print(f"{i}. {question}")

print("""
Suggested Answers:
1 -> Regression
2 -> Clustering
3 -> Classification
4 -> Regression
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 05 Summary")
print("-" * 30)

print("""
1. Machine Learning solves real-world problems.
2. Regression predicts continuous values.
3. Classification predicts categories.
4. Clustering groups similar data.
5. ML is widely used in healthcare,
   finance, education, and e-commerce.
6. Case studies help bridge theory
   and practical implementation.
""")

print("\nDay 05 Completed Successfully!")
print("=" * 60)