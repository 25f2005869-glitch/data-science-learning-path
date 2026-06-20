# ==========================================================
# Day 03 : Types of Machine Learning
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 03")
print("=" * 60)

print("\nTypes of Machine Learning")
print("-" * 30)

print("""
Machine Learning is generally divided into
three major categories:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
""")

# ----------------------------------------------------------
# Supervised Learning
# ----------------------------------------------------------

print("\n1. Supervised Learning")
print("-" * 30)

print("""
In Supervised Learning, the model learns from
labeled data.

Input  ---> Output

The correct answers are already available during training.
""")

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]

print("Example Dataset:")
for h, m in zip(study_hours, marks):
    print(f"Study Hours = {h} --> Marks = {m}")

print("""
Goal:
Predict marks for a new student based on study hours.
""")

# ----------------------------------------------------------
# Unsupervised Learning
# ----------------------------------------------------------

print("\n2. Unsupervised Learning")
print("-" * 30)

print("""
In Unsupervised Learning, the model learns from
unlabeled data.

Input ---> No predefined output

The algorithm discovers hidden patterns automatically.
""")

customers = [1200, 1300, 1400, 5000, 5200, 5400]

print("Customer Spending Data:")
print(customers)

print("""
Possible Result:

Group 1 -> Low Spending Customers
Group 2 -> High Spending Customers

This process is called Clustering.
""")

# ----------------------------------------------------------
# Reinforcement Learning
# ----------------------------------------------------------

print("\n3. Reinforcement Learning")
print("-" * 30)

print("""
In Reinforcement Learning, an agent learns by
interacting with an environment.

Action ---> Reward/Penalty

The goal is to maximize rewards over time.
""")

print("""
Examples:
• Self-Driving Cars
• Robotics
• Game Playing AI
• Recommendation Systems
""")

# ----------------------------------------------------------
# Comparison Table
# ----------------------------------------------------------

print("\nComparison of ML Types")
print("-" * 30)

print(f"{'Type':<20} {'Data':<15} {'Goal'}")
print("-" * 60)

print(f"{'Supervised':<20} {'Labeled':<15} Predict Output")
print(f"{'Unsupervised':<20} {'Unlabeled':<15} Find Patterns")
print(f"{'Reinforcement':<20} {'Rewards':<15} Learn Actions")

# ----------------------------------------------------------
# Real-World Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = {
    "Supervised Learning": [
        "Spam Detection",
        "House Price Prediction",
        "Medical Diagnosis"
    ],
    "Unsupervised Learning": [
        "Customer Segmentation",
        "Market Basket Analysis",
        "Data Clustering"
    ],
    "Reinforcement Learning": [
        "Robotics",
        "Self-Driving Cars",
        "Game AI"
    ]
}

for ml_type, apps in applications.items():
    print(f"\n{ml_type}:")
    for app in apps:
        print(f"  ✓ {app}")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

questions = [
    "Predicting exam marks from study hours",
    "Grouping customers by spending behavior",
    "Training a robot using rewards"
]

for i, q in enumerate(questions, start=1):
    print(f"{i}. {q}")

print("""
Answers:
1 -> Supervised Learning
2 -> Unsupervised Learning
3 -> Reinforcement Learning
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 03 Summary")
print("-" * 30)

print("""
1. Supervised Learning uses labeled data.
2. Unsupervised Learning finds hidden patterns.
3. Reinforcement Learning learns using rewards.
4. Different ML problems require different approaches.
5. Understanding ML types is the foundation of
   advanced Machine Learning algorithms.
""")

print("\nDay 03 Completed Successfully!")
print("=" * 60)