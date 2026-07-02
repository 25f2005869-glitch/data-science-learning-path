# ==========================================================
# Day 18 : Bayes Theorem
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 18")
print("=" * 60)

print("\nBayes Theorem")
print("-" * 30)

print("""
Bayes Theorem helps us update probabilities
when new information becomes available.

It is one of the most important concepts in:

✓ Machine Learning
✓ Statistics
✓ Medical Diagnosis
✓ Spam Detection
✓ Risk Analysis
✓ Artificial Intelligence
""")

# ----------------------------------------------------------
# Bayes Theorem Formula
# ----------------------------------------------------------

print("\nBayes Theorem Formula")
print("-" * 30)

print("""
P(A|B) = [P(B|A) × P(A)] / P(B)

where:

P(A|B) = Posterior Probability
P(B|A) = Likelihood
P(A)   = Prior Probability
P(B)   = Evidence
""")

# ----------------------------------------------------------
# Medical Diagnosis Example
# ----------------------------------------------------------

print("\nExample 1 : Medical Diagnosis")
print("-" * 30)

print("""
Suppose:

P(Disease) = 0.01

P(Positive | Disease) = 0.95

P(Positive) = 0.05

Find:

P(Disease | Positive)
""")

P_Disease = 0.01
P_Positive_given_Disease = 0.95
P_Positive = 0.05

posterior = (
    P_Positive_given_Disease *
    P_Disease
) / P_Positive

print("P(Disease | Positive) =",
      round(posterior, 4))

# ----------------------------------------------------------
# Spam Detection Example
# ----------------------------------------------------------

print("\nExample 2 : Spam Detection")
print("-" * 30)

print("""
Suppose:

P(Spam) = 0.30

P(Win | Spam) = 0.80

P(Win) = 0.40

Find:

P(Spam | Win)
""")

P_Spam = 0.30
P_Win_given_Spam = 0.80
P_Win = 0.40

spam_probability = (
    P_Win_given_Spam *
    P_Spam
) / P_Win

print("P(Spam | Win) =",
      round(spam_probability, 4))

# ----------------------------------------------------------
# Student Example
# ----------------------------------------------------------

print("\nExample 3 : Student Performance")
print("-" * 30)

print("""
Suppose:

P(Pass) = 0.70

P(Study | Pass) = 0.90

P(Study) = 0.75

Find:

P(Pass | Study)
""")

P_Pass = 0.70
P_Study_given_Pass = 0.90
P_Study = 0.75

result = (
    P_Study_given_Pass *
    P_Pass
) / P_Study

print("P(Pass | Study) =",
      round(result, 4))

# ----------------------------------------------------------
# Prior and Posterior
# ----------------------------------------------------------

print("\nPrior vs Posterior")
print("-" * 30)

print("""
Prior Probability:
Initial belief before observing evidence.

Posterior Probability:
Updated belief after observing evidence.

Bayes Theorem converts:

Prior → Posterior
""")

# ----------------------------------------------------------
# Why Bayes Theorem Matters
# ----------------------------------------------------------

print("\nImportance in Machine Learning")
print("-" * 30)

applications = [
    "Naive Bayes Classifier",
    "Spam Filtering",
    "Medical Diagnosis",
    "Recommendation Systems",
    "Fraud Detection",
    "Risk Prediction"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Naive Bayes Connection
# ----------------------------------------------------------

print("\nNaive Bayes Classifier")
print("-" * 30)

print("""
Naive Bayes is a Machine Learning algorithm
based directly on Bayes Theorem.

It assumes:

Features are conditionally independent.

Applications:

✓ Email Classification
✓ Sentiment Analysis
✓ Text Classification
✓ Document Categorization
""")

# ----------------------------------------------------------
# Practical Dataset Example
# ----------------------------------------------------------

print("\nPractical Dataset")
print("-" * 30)

emails = [
    {"Win": True, "Spam": True},
    {"Win": True, "Spam": True},
    {"Win": False, "Spam": False},
    {"Win": True, "Spam": False},
    {"Win": True, "Spam": True}
]

spam_count = 0
win_count = 0
win_and_spam = 0

for email in emails:

    if email["Spam"]:
        spam_count += 1

    if email["Win"]:
        win_count += 1

    if email["Win"] and email["Spam"]:
        win_and_spam += 1

P_Spam = spam_count / len(emails)
P_Win_given_Spam = win_and_spam / spam_count
P_Win = win_count / len(emails)

bayes_result = (
    P_Win_given_Spam *
    P_Spam
) / P_Win

print("Calculated P(Spam | Win) =",
      round(bayes_result, 4))

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

P_A = 0.40
P_B_given_A = 0.50
P_B = 0.25

P_A_given_B = (
    P_B_given_A *
    P_A
) / P_B

print("P(A | B) =",
      round(P_A_given_B, 4))

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Bayes Theorem?

2. What is Prior Probability?

3. What is Posterior Probability?

4. Which ML algorithm is based on
   Bayes Theorem?

5. Why is Bayes Theorem useful?
""")

print("""
Answers:

1. Method to update probabilities
2. Initial belief
3. Updated belief after evidence
4. Naive Bayes
5. Helps make better predictions
   using available evidence
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 18 Summary")
print("-" * 30)

print("""
1. Bayes Theorem updates probabilities
   using new evidence.

2. Formula:

   P(A|B) =
   [P(B|A) × P(A)] / P(B)

3. Prior probability becomes
   posterior probability.

4. Bayes Theorem is the foundation
   of Naive Bayes.

5. Widely used in Machine Learning,
   AI, and Statistics.
""")

print("\nDay 18 Completed Successfully!")
print("=" * 60)