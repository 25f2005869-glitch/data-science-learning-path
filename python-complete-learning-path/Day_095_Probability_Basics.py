# ======================================
# Day 095: Probability Basics
# Author: Saloni Tiwari
# Repository: python-complete-learning-path
# Description:
# Introduction to Probability
# for Statistics and Data Science
# ======================================

print("=" * 60)
print("DAY 095 - PROBABILITY BASICS")
print("=" * 60)

# ======================================
# IMPORT LIBRARY
# ======================================

import random

# ======================================
# PROFESSIONAL NOTES
# ======================================

"""
What is Probability?

Probability measures the
chance of an event occurring.

Range:

0 ≤ Probability ≤ 1

0 = Impossible Event
1 = Certain Event

Applications:

1. Data Science
2. Machine Learning
3. Risk Analysis
4. Business Forecasting
5. Artificial Intelligence
"""

# ======================================
# SAMPLE SPACE
# ======================================

print("\nSAMPLE SPACE")

dice = [
    1,
    2,
    3,
    4,
    5,
    6
]

print(
    "Possible Outcomes:",
    dice
)

# ======================================
# PROBABILITY FORMULA
# ======================================

print("\nPROBABILITY FORMULA")

"""
Probability =
Favorable Outcomes
------------------
Total Outcomes
"""

favorable = 1
total = 6

probability = (
    favorable /
    total
)

print(
    "Probability of getting 1:",
    round(
        probability,
        2
    )
)

# ======================================
# COIN TOSS
# ======================================

print("\nCOIN TOSS")

coin = [
    "Head",
    "Tail"
]

print(
    "Sample Space:",
    coin
)

print(
    "Probability of Head:",
    1 / 2
)

# ======================================
# DICE ROLL
# ======================================

print("\nDICE ROLL")

result = random.randint(
    1,
    6
)

print(
    "Dice Result:",
    result
)

# ======================================
# EVEN NUMBER PROBABILITY
# ======================================

print("\nEVEN NUMBER PROBABILITY")

even_numbers = [
    2,
    4,
    6
]

prob_even = (
    len(even_numbers) /
    len(dice)
)

print(
    "Probability:",
    prob_even
)

# ======================================
# CARD EXAMPLE
# ======================================

print("\nCARD EXAMPLE")

total_cards = 52
aces = 4

prob_ace = (
    aces /
    total_cards
)

print(
    "Probability of Ace:",
    round(
        prob_ace,
        4
    )
)

# ======================================
# RANDOM CHOICE
# ======================================

print("\nRANDOM CHOICE")

colors = [
    "Red",
    "Blue",
    "Green"
]

selected = random.choice(
    colors
)

print(
    "Selected Color:",
    selected
)

# ======================================
# USER INPUT EXAMPLE
# ======================================

print("\nUSER INPUT EXAMPLE")

favorable = int(
    input(
        "Enter Favorable Outcomes: "
    )
)

total = int(
    input(
        "Enter Total Outcomes: "
    )
)

prob = (
    favorable /
    total
)

print(
    "Probability:",
    round(
        prob,
        4
    )
)

# ======================================
# MINI PROJECT
# ======================================

print("\nMINI PROJECT")

students = [
    "Saloni",
    "Riya",
    "Ankit",
    "Rahul",
    "Priya"
]

winner = random.choice(
    students
)

print(
    "Lucky Winner:",
    winner
)

# ======================================
# IMPORTANT TERMS
# ======================================

"""
Experiment

Outcome

Sample Space

Event

Probability
"""

# ======================================
# EXERCISES
# ======================================

"""
Exercise 1:
Find probability of
getting Tail.

Exercise 2:
Find probability of
getting an even number.

Exercise 3:
Find probability of
drawing a King.

Exercise 4:
Create a dice simulator.
"""

# ======================================
# INTERVIEW QUESTIONS
# ======================================

"""
Q1. What is Probability?

Q2. What is Sample Space?

Q3. What is an Event?

Q4. Range of Probability?

Q5. What is a Random Experiment?

Q6. Why is Probability
important in ML?
"""

# ======================================
# CHALLENGE PROJECT
# ======================================

"""
Create a Lottery Simulator.

Input:

1. Total Tickets
2. Winning Tickets

Generate:

Probability of Winning
"""

# ======================================
# END OF FILE
# ======================================

print(
    "\nDay 095 Completed Successfully!"
)