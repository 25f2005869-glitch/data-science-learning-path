# ==========================================================
# Day 16 : Probability Basics
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 16")
print("=" * 60)

print("\nProbability Basics")
print("-" * 30)

print("""
Probability measures the likelihood of an event.

Probability is one of the most important
foundations of Machine Learning because
many ML algorithms are based on uncertainty.

Examples:

✓ Weather Prediction
✓ Spam Detection
✓ Risk Analysis
✓ Medical Diagnosis
✓ Recommendation Systems
""")

# ----------------------------------------------------------
# Basic Probability Formula
# ----------------------------------------------------------

print("\nProbability Formula")
print("-" * 30)

print("""
Probability(Event) =

Favorable Outcomes
-------------------
Total Outcomes
""")

# ----------------------------------------------------------
# Coin Toss Example
# ----------------------------------------------------------

print("\nExample 1 : Coin Toss")
print("-" * 30)

sample_space = ["Head", "Tail"]

print("Sample Space =", sample_space)

favorable_outcomes = 1
total_outcomes = 2

probability_head = favorable_outcomes / total_outcomes

print("P(Head) =", probability_head)

# ----------------------------------------------------------
# Dice Example
# ----------------------------------------------------------

print("\nExample 2 : Dice Roll")
print("-" * 30)

dice = [1, 2, 3, 4, 5, 6]

print("Sample Space =", dice)

favorable_outcomes = 1
total_outcomes = 6

probability_six = favorable_outcomes / total_outcomes

print("P(6) =", probability_six)

# ----------------------------------------------------------
# Even Number Probability
# ----------------------------------------------------------

print("\nExample 3 : Even Number")
print("-" * 30)

even_numbers = [2, 4, 6]

probability_even = len(even_numbers) / len(dice)

print("Even Numbers =", even_numbers)
print("P(Even Number) =", probability_even)

# ----------------------------------------------------------
# Card Example
# ----------------------------------------------------------

print("\nExample 4 : Playing Cards")
print("-" * 30)

total_cards = 52
hearts = 13

probability_heart = hearts / total_cards

print("Total Cards =", total_cards)
print("Hearts =", hearts)

print("P(Heart) =", probability_heart)

# ----------------------------------------------------------
# Probability Range
# ----------------------------------------------------------

print("\nProbability Range")
print("-" * 30)

print("""
0  → Impossible Event

0.5 → Equal Chance

1  → Certain Event
""")

print("Example:")
print("P(Sun rises tomorrow) = 1")
print("P(Rolling 7 on a standard die) = 0")

# ----------------------------------------------------------
# Sample Space
# ----------------------------------------------------------

print("\nSample Space")
print("-" * 30)

print("""
Sample Space:
Set of all possible outcomes.
""")

coin_space = {"Head", "Tail"}

print("Coin Toss Sample Space =", coin_space)

# ----------------------------------------------------------
# Event
# ----------------------------------------------------------

print("\nEvent")
print("-" * 30)

print("""
An Event is a subset of
the Sample Space.
""")

event = {"Head"}

print("Event =", event)

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nProbability in Machine Learning")
print("-" * 30)

applications = [
    "Naive Bayes",
    "Bayesian Learning",
    "Spam Detection",
    "Medical Diagnosis",
    "Recommendation Systems",
    "Risk Prediction"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Practical Dataset Example
# ----------------------------------------------------------

print("\nDataset Example")
print("-" * 30)

student_results = [
    "Pass",
    "Pass",
    "Pass",
    "Fail",
    "Pass"
]

print("Results =", student_results)

passes = student_results.count("Pass")

probability_pass = passes / len(student_results)

print("P(Pass) =", probability_pass)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

balls = ["Red", "Red", "Blue", "Green"]

print("Balls =", balls)

probability_red = balls.count("Red") / len(balls)

print("P(Red Ball) =", probability_red)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Probability?

2. What is a Sample Space?

3. What is an Event?

4. What is P(Head) in a fair coin toss?

5. What is P(6) in a fair die?
""")

print("""
Answers:

1. Likelihood of an event
2. Set of all possible outcomes
3. Subset of sample space
4. 1/2 = 0.5
5. 1/6 ≈ 0.167
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 16 Summary")
print("-" * 30)

print("""
1. Probability measures uncertainty.
2. Probability ranges from 0 to 1.
3. Sample Space contains all outcomes.
4. Events are subsets of sample space.
5. Probability is widely used in ML.
6. Bayesian methods are based on probability.
""")

print("\nDay 16 Completed Successfully!")
print("=" * 60)