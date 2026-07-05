# ==========================================================
# Day 20 : Probability Distributions
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 20")
print("=" * 60)

print("\nProbability Distributions")
print("-" * 30)

print("""
A Probability Distribution describes how
probabilities are assigned to the values of
a Random Variable.

It helps us understand:

✓ Likely Outcomes
✓ Uncertain Events
✓ Data Behavior
✓ Machine Learning Models
""")

# ----------------------------------------------------------
# Discrete Probability Distribution
# ----------------------------------------------------------

print("\nDiscrete Probability Distribution")
print("-" * 30)

print("""
A Discrete Distribution assigns probabilities
to countable values.

Example:
Rolling a Fair Die
""")

dice_distribution = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

for value, probability in dice_distribution.items():
    print(f"X = {value}  P(X) = {probability:.3f}")

# ----------------------------------------------------------
# Verify Probability Sum
# ----------------------------------------------------------

print("\nChecking Total Probability")
print("-" * 30)

total_probability = sum(dice_distribution.values())

print("Total Probability =", total_probability)

print("""
For every valid probability distribution:

Σ P(X) = 1
""")

# ----------------------------------------------------------
# Expected Value
# ----------------------------------------------------------

print("\nExpected Value")
print("-" * 30)

expected_value = 0

for value, probability in dice_distribution.items():
    expected_value += value * probability

print("Expected Value =", round(expected_value, 2))

print("""
Formula:

E(X) = Σ [X × P(X)]
""")

# ----------------------------------------------------------
# Continuous Probability Distribution
# ----------------------------------------------------------

print("\nContinuous Probability Distribution")
print("-" * 30)

print("""
Continuous variables can take
infinitely many values.

Examples:

✓ Height
✓ Weight
✓ Temperature
✓ Income
✓ Time
""")

heights = [160.5, 165.8, 170.2, 172.4]

print("Sample Heights:")
print(heights)

# ----------------------------------------------------------
# Uniform Distribution
# ----------------------------------------------------------

print("\nUniform Distribution")
print("-" * 30)

print("""
All outcomes have equal probability.

Example:
Fair Coin
Fair Die
""")

coin_distribution = {
    "Head": 0.5,
    "Tail": 0.5
}

for outcome, probability in coin_distribution.items():
    print(f"{outcome} → {probability}")

# ----------------------------------------------------------
# Biased Distribution
# ----------------------------------------------------------

print("\nBiased Distribution")
print("-" * 30)

biased_coin = {
    "Head": 0.8,
    "Tail": 0.2
}

for outcome, probability in biased_coin.items():
    print(f"{outcome} → {probability}")

# ----------------------------------------------------------
# Mean of Distribution
# ----------------------------------------------------------

print("\nMean of Distribution")
print("-" * 30)

marks = [60, 70, 80, 90, 100]

mean_marks = sum(marks) / len(marks)

print("Marks =", marks)
print("Mean =", mean_marks)

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nProbability Distributions in ML")
print("-" * 30)

applications = [
    "Naive Bayes",
    "Anomaly Detection",
    "Recommendation Systems",
    "Prediction Models",
    "Generative Models",
    "Risk Analysis"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Student Marks Distribution
# ----------------------------------------------------------

print("\nStudent Marks Distribution")
print("-" * 30)

student_marks = {
    50: 0.10,
    60: 0.20,
    70: 0.30,
    80: 0.25,
    90: 0.15
}

for mark, probability in student_marks.items():
    print(f"Marks = {mark}, P(X) = {probability}")

# ----------------------------------------------------------
# Expected Marks
# ----------------------------------------------------------

print("\nExpected Marks")
print("-" * 30)

expected_marks = 0

for mark, probability in student_marks.items():
    expected_marks += mark * probability

print("Expected Marks =", round(expected_marks, 2))

# ----------------------------------------------------------
# Real-World Example
# ----------------------------------------------------------

print("\nReal-World Example")
print("-" * 30)

sales = {
    100: 0.20,
    200: 0.30,
    300: 0.25,
    400: 0.15,
    500: 0.10
}

expected_sales = 0

for value, probability in sales.items():
    expected_sales += value * probability

print("Expected Sales =", expected_sales)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

distribution = {
    1: 0.25,
    2: 0.25,
    3: 0.25,
    4: 0.25
}

expected = 0

for value, probability in distribution.items():
    expected += value * probability

print("Expected Value =", expected)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Probability Distribution?

2. What condition must all valid
   distributions satisfy?

3. What is Expected Value?

4. Give one example of a Continuous
   Random Variable.

5. Why are distributions important in ML?
""")

print("""
Answers:

1. Assignment of probabilities to values
2. Total probability must equal 1
3. Long-run average outcome
4. Height, Weight, Time, etc.
5. They model uncertainty and data behavior
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 20 Summary")
print("-" * 30)

print("""
1. Probability Distributions describe
   the behavior of Random Variables.

2. Distributions may be:
   ✓ Discrete
   ✓ Continuous

3. Total probability must always be 1.

4. Expected Value represents
   the average outcome.

5. Probability Distributions are widely
   used throughout Machine Learning.
""")

print("\nProbability Module Completed!")
print("Day 20 Completed Successfully!")
print("=" * 60)