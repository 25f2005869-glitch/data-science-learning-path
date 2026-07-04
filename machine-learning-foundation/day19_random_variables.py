# ==========================================================
# Day 19 : Random Variables
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 19")
print("=" * 60)

print("\nRandom Variables")
print("-" * 30)

print("""
A Random Variable is a variable whose value
depends on the outcome of a random experiment.

Instead of storing outcomes directly,
we assign numerical values to outcomes.

Examples:

✓ Coin Toss
✓ Dice Roll
✓ Card Selection
✓ Customer Purchases
✓ Student Marks
""")

# ----------------------------------------------------------
# Coin Toss Example
# ----------------------------------------------------------

print("\nExample 1 : Coin Toss")
print("-" * 30)

print("""
Experiment:
Toss a coin

Random Variable X:

Head → 1
Tail → 0
""")

coin_results = {
    "Head": 1,
    "Tail": 0
}

for outcome, value in coin_results.items():
    print(outcome, "→", value)

# ----------------------------------------------------------
# Dice Example
# ----------------------------------------------------------

print("\nExample 2 : Dice Roll")
print("-" * 30)

dice = [1, 2, 3, 4, 5, 6]

print("Possible Values of X:")
print(dice)

print("""
Random Variable X:
Number appearing on the die.
""")

# ----------------------------------------------------------
# Types of Random Variables
# ----------------------------------------------------------

print("\nTypes of Random Variables")
print("-" * 30)

print("""
1. Discrete Random Variable
2. Continuous Random Variable
""")

# ----------------------------------------------------------
# Discrete Random Variable
# ----------------------------------------------------------

print("\nDiscrete Random Variable")
print("-" * 30)

print("""
A Discrete Random Variable takes
countable values.

Examples:

✓ Number of Students
✓ Number of Customers
✓ Number of Defective Products
✓ Dice Outcomes
""")

students_absent = [0, 1, 2, 3, 4]

print("Possible Values:")
print(students_absent)

# ----------------------------------------------------------
# Continuous Random Variable
# ----------------------------------------------------------

print("\nContinuous Random Variable")
print("-" * 30)

print("""
A Continuous Random Variable can take
any value within a range.

Examples:

✓ Height
✓ Weight
✓ Temperature
✓ Income
✓ Time
""")

heights = [165.5, 170.2, 172.8]

print("Sample Heights:")
print(heights)

# ----------------------------------------------------------
# Probability Distribution
# ----------------------------------------------------------

print("\nProbability Distribution")
print("-" * 30)

print("""
A Probability Distribution shows
the probability associated with
each value of a random variable.
""")

distribution = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

for value, probability in distribution.items():
    print(f"X = {value}, P(X) = {probability:.3f}")

# ----------------------------------------------------------
# Expected Value
# ----------------------------------------------------------

print("\nExpected Value")
print("-" * 30)

print("""
Expected Value represents the
long-run average outcome.

Formula:

E(X) = Σ [X × P(X)]
""")

expected_value = 0

for value, probability in distribution.items():
    expected_value += value * probability

print("Expected Value of Dice =", round(expected_value, 2))

# ----------------------------------------------------------
# Machine Learning Example
# ----------------------------------------------------------

print("\nMachine Learning Connection")
print("-" * 30)

print("""
In Machine Learning:

Random Variables represent:

✓ Features
✓ Labels
✓ Predictions
✓ Uncertain Outcomes

Many ML models are based on
probability distributions.
""")

# ----------------------------------------------------------
# Student Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

marks = [50, 60, 70, 80, 90]

print("Marks:", marks)

print("""
Random Variable X:

X = Student Marks
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

customers = [2, 4, 3, 5, 6]

average_customers = sum(customers) / len(customers)

print("Customers Per Hour:", customers)
print("Average Customers =", average_customers)

# ----------------------------------------------------------
# Discrete vs Continuous
# ----------------------------------------------------------

print("\nDiscrete vs Continuous")
print("-" * 30)

print("""
Discrete:
✓ Countable
✓ Finite values

Examples:
Students, Cars, Dice

Continuous:
✓ Measurable
✓ Infinite values

Examples:
Height, Weight, Time
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

coin_distribution = {
    0: 0.5,
    1: 0.5
}

expected_coin = 0

for value, probability in coin_distribution.items():
    expected_coin += value * probability

print("Expected Value =", expected_coin)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Random Variable?

2. What are the two types of
   Random Variables?

3. What is a Probability Distribution?

4. What is Expected Value?

5. Give one example of a
   Continuous Random Variable.
""")

print("""
Answers:

1. Variable whose value depends
   on a random experiment

2. Discrete and Continuous

3. Probability assigned to values

4. Long-run average outcome

5. Height, Weight, Time, etc.
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 19 Summary")
print("-" * 30)

print("""
1. Random Variables assign numerical
   values to outcomes.

2. Two types:
   ✓ Discrete
   ✓ Continuous

3. Probability Distributions describe
   probabilities of outcomes.

4. Expected Value measures average outcome.

5. Random Variables are fundamental
   to Machine Learning and Statistics.
""")

print("\nDay 19 Completed Successfully!")
print("=" * 60)