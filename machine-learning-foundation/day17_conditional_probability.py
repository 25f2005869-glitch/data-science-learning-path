# ==========================================================
# Day 17 : Conditional Probability
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 17")
print("=" * 60)

print("\nConditional Probability")
print("-" * 30)

print("""
Conditional Probability measures the probability
of an event occurring given that another event
has already occurred.

Notation:

P(A|B)

Read as:
Probability of A given B
""")

# ----------------------------------------------------------
# Formula
# ----------------------------------------------------------

print("\nConditional Probability Formula")
print("-" * 30)

print("""
P(A|B) = P(A ∩ B) / P(B)

where:

P(A|B) = Probability of A given B
P(A ∩ B) = Probability of A and B
P(B) = Probability of B
""")

# ----------------------------------------------------------
# Example 1 : Students Dataset
# ----------------------------------------------------------

print("\nExample 1 : Students Dataset")
print("-" * 30)

students = [
    {"Gender": "Male", "Passed": True},
    {"Gender": "Female", "Passed": True},
    {"Gender": "Male", "Passed": False},
    {"Gender": "Female", "Passed": True},
    {"Gender": "Male", "Passed": True}
]

total_students = len(students)

passed_students = 0
male_and_passed = 0

for student in students:

    if student["Passed"]:
        passed_students += 1

    if student["Gender"] == "Male" and student["Passed"]:
        male_and_passed += 1

conditional_probability = male_and_passed / passed_students

print("Total Students =", total_students)
print("Passed Students =", passed_students)
print("Male and Passed =", male_and_passed)

print("P(Male | Passed) =",
      round(conditional_probability, 2))

# ----------------------------------------------------------
# Example 2 : Card Example
# ----------------------------------------------------------

print("\nExample 2 : Playing Cards")
print("-" * 30)

print("""
A standard deck contains:

52 Cards
26 Red Cards
13 Hearts

Find:

P(Heart | Red)
""")

hearts = 13
red_cards = 26

probability = hearts / red_cards

print("P(Heart | Red) =", probability)

# ----------------------------------------------------------
# Example 3 : Machine Learning Dataset
# ----------------------------------------------------------

print("\nExample 3 : ML Dataset")
print("-" * 30)

results = [
    {"Study": "Yes", "Pass": "Yes"},
    {"Study": "Yes", "Pass": "Yes"},
    {"Study": "Yes", "Pass": "No"},
    {"Study": "No", "Pass": "No"},
    {"Study": "No", "Pass": "Yes"}
]

study_yes = 0
study_yes_and_pass = 0

for record in results:

    if record["Study"] == "Yes":
        study_yes += 1

    if record["Study"] == "Yes" and record["Pass"] == "Yes":
        study_yes_and_pass += 1

probability_pass_given_study = (
    study_yes_and_pass / study_yes
)

print("Students Who Studied =", study_yes)
print("Studied and Passed =", study_yes_and_pass)

print("P(Pass | Study) =",
      round(probability_pass_given_study, 2))

# ----------------------------------------------------------
# Independent Events
# ----------------------------------------------------------

print("\nIndependent Events")
print("-" * 30)

print("""
Two events are independent if the occurrence
of one event does not affect the other.

Example:

✓ Tossing a coin
✓ Rolling a die

These events do not influence each other.
""")

# ----------------------------------------------------------
# Dependent Events
# ----------------------------------------------------------

print("\nDependent Events")
print("-" * 30)

print("""
Two events are dependent if one event
affects the probability of another.

Example:

Drawing cards without replacement.
""")

# ----------------------------------------------------------
# Why Conditional Probability Matters
# ----------------------------------------------------------

print("\nImportance in Machine Learning")
print("-" * 30)

applications = [
    "Naive Bayes Classifier",
    "Spam Detection",
    "Medical Diagnosis",
    "Fraud Detection",
    "Risk Analysis",
    "Recommendation Systems"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

emails = [
    {"Contains_Link": True, "Spam": True},
    {"Contains_Link": True, "Spam": True},
    {"Contains_Link": False, "Spam": False},
    {"Contains_Link": True, "Spam": False},
    {"Contains_Link": True, "Spam": True}
]

link_count = 0
link_and_spam = 0

for email in emails:

    if email["Contains_Link"]:
        link_count += 1

    if email["Contains_Link"] and email["Spam"]:
        link_and_spam += 1

spam_given_link = link_and_spam / link_count

print("Emails with Links =", link_count)
print("Spam and Link =", link_and_spam)

print("P(Spam | Link) =",
      round(spam_given_link, 2))

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

boys = 12
boys_play_cricket = 8

probability = boys_play_cricket / boys

print("P(Cricket | Boy) =", probability)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Conditional Probability?

2. What does P(A|B) mean?

3. What is the formula for
   Conditional Probability?

4. Which ML algorithm heavily uses
   Conditional Probability?
""")

print("""
Answers:

1. Probability given another event
2. Probability of A given B
3. P(A ∩ B) / P(B)
4. Naive Bayes
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 17 Summary")
print("-" * 30)

print("""
1. Conditional Probability measures
   probability under a condition.

2. Formula:

   P(A|B) = P(A ∩ B) / P(B)

3. Conditional Probability is a key
   concept in Machine Learning.

4. It is widely used in Naive Bayes,
   spam detection, and medical diagnosis.

5. Understanding conditional probability
   is essential before learning Bayes Theorem.
""")

print("\nDay 17 Completed Successfully!")
print("=" * 60)