# ==========================================================
# Day 02 : History and Applications of Machine Learning
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("     MACHINE LEARNING FOUNDATIONS - DAY 02")
print("=" * 60)

print("\nHistory of Machine Learning")
print("-" * 30)

history = [
    ("1950", "Alan Turing proposed the Turing Test"),
    ("1957", "Frank Rosenblatt developed the Perceptron"),
    ("1980s", "Neural Networks gained popularity"),
    ("1997", "IBM Deep Blue defeated Garry Kasparov"),
    ("2006", "Deep Learning revival began"),
    ("2012", "AlexNet revolutionized Computer Vision"),
    ("2022+", "Generative AI and Large Language Models")
]

for year, event in history:
    print(f"{year} --> {event}")

print("\nWhat is the Goal of Machine Learning?")
print("-" * 30)

print("""
The main goal of Machine Learning is to build systems
that can learn patterns from data and make intelligent
predictions or decisions without explicit programming.
""")

print("\nMajor Applications of Machine Learning")
print("-" * 30)

applications = [
    "Email Spam Detection",
    "Recommendation Systems",
    "Medical Diagnosis",
    "Fraud Detection",
    "Speech Recognition",
    "Face Recognition",
    "Weather Forecasting",
    "Stock Market Analysis",
    "Autonomous Vehicles",
    "Language Translation"
]

for i, app in enumerate(applications, start=1):
    print(f"{i}. {app}")

print("\nReal-Life Examples")
print("-" * 30)

print("""
YouTube  -> Video Recommendations
Netflix  -> Movie Recommendations
Google   -> Search Ranking
Amazon   -> Product Suggestions
Uber     -> Demand Prediction
Banks    -> Fraud Detection
Hospitals-> Disease Prediction
""")

print("\nIndustries Using Machine Learning")
print("-" * 30)

industries = [
    "Healthcare",
    "Finance",
    "Education",
    "Agriculture",
    "Transportation",
    "Cybersecurity",
    "Manufacturing",
    "E-Commerce"
]

for industry in industries:
    print(f"• {industry}")

print("\nMini Example")
print("-" * 30)

student_marks = [45, 52, 67, 78, 89]

average = sum(student_marks) / len(student_marks)

print("Student Marks:", student_marks)
print("Average Marks:", average)

print("""
A Machine Learning model can use similar data
to predict future student performance.
""")

print("\nAdvantages of Machine Learning")
print("-" * 30)

advantages = [
    "Automates repetitive tasks",
    "Improves decision making",
    "Handles large datasets",
    "Discovers hidden patterns",
    "Provides accurate predictions"
]

for item in advantages:
    print(f"✓ {item}")

print("\nChallenges of Machine Learning")
print("-" * 30)

challenges = [
    "Requires quality data",
    "Can be computationally expensive",
    "Risk of overfitting",
    "Model interpretability issues",
    "Data privacy concerns"
]

for item in challenges:
    print(f"• {item}")

print("\nDay 02 Summary")
print("-" * 30)

print("""
1. Machine Learning evolved over several decades.
2. It is used in almost every industry today.
3. ML helps computers learn from data.
4. Applications include healthcare, finance,
   recommendation systems, and AI assistants.
5. Quality data is essential for successful ML models.
""")

print("\nDay 02 Completed Successfully!")
print("=" * 60)