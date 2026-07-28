# ==========================================================
# Day 27 : Hypothesis Testing
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 27")
print("=" * 60)

print("\nHypothesis Testing")
print("-" * 30)

print("""
Hypothesis Testing is a statistical method
used to make decisions based on sample data.

It helps answer questions like:

✓ Is a new teaching method effective?
✓ Has sales increased significantly?
✓ Does a new medicine work better?
✓ Is a machine learning improvement real?

Applications:

✓ Statistics
✓ Data Science
✓ Machine Learning
✓ Scientific Research
✓ Business Analytics
""")

# ----------------------------------------------------------
# What is a Hypothesis?
# ----------------------------------------------------------

print("\nWhat is a Hypothesis?")
print("-" * 30)

print("""
A Hypothesis is a statement or claim
about a population parameter that can
be tested using data.

Example:

'Average student marks are 70.'
""")

# ----------------------------------------------------------
# Null and Alternative Hypothesis
# ----------------------------------------------------------

print("\nNull and Alternative Hypothesis")
print("-" * 30)

print("""
Null Hypothesis (H₀):
No significant difference exists.

Alternative Hypothesis (H₁):
A significant difference exists.
""")

print("Example:")
print("H₀ : Average Marks = 70")
print("H₁ : Average Marks ≠ 70")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

marks = [72, 75, 68, 70, 74]

print("Sample Marks =", marks)

sample_mean = sum(marks) / len(marks)

print("Sample Mean =", round(sample_mean, 2))

# ----------------------------------------------------------
# Significance Level
# ----------------------------------------------------------

print("\nSignificance Level (α)")
print("-" * 30)

alpha = 0.05

print("Alpha =", alpha)

print("""
Common Values:

0.05 (5%)
0.01 (1%)

Alpha represents the acceptable
probability of making an incorrect decision.
""")

# ----------------------------------------------------------
# Test Statistic Concept
# ----------------------------------------------------------

print("\nTest Statistic")
print("-" * 30)

print("""
A Test Statistic measures how far
sample results differ from the null hypothesis.

Common Test Statistics:

✓ Z-Test
✓ T-Test
✓ Chi-Square Test
✓ ANOVA
""")

# ----------------------------------------------------------
# Simple Z-Score Example
# ----------------------------------------------------------

print("\nSimple Z-Score Example")
print("-" * 30)

population_mean = 70
sample_mean = 74
standard_deviation = 8
sample_size = 25

z_score = (
    sample_mean - population_mean
) / (standard_deviation / (sample_size ** 0.5))

print("Population Mean =", population_mean)
print("Sample Mean     =", sample_mean)
print("Z-Score         =", round(z_score, 2))

# ----------------------------------------------------------
# Decision Making
# ----------------------------------------------------------

print("\nDecision Making")
print("-" * 30)

critical_value = 1.96

print("Critical Value =", critical_value)

if abs(z_score) > critical_value:
    print("Reject Null Hypothesis (H₀)")
else:
    print("Fail to Reject Null Hypothesis (H₀)")

# ----------------------------------------------------------
# Type I Error
# ----------------------------------------------------------

print("\nType I Error")
print("-" * 30)

print("""
Type I Error:

Rejecting H₀ when H₀ is actually true.

Also called:

False Positive
""")

# ----------------------------------------------------------
# Type II Error
# ----------------------------------------------------------

print("\nType II Error")
print("-" * 30)

print("""
Type II Error:

Failing to reject H₀ when H₀ is false.

Also called:

False Negative
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nHypothesis Testing in ML")
print("-" * 30)

applications = [
    "A/B Testing",
    "Feature Selection",
    "Model Comparison",
    "Experiment Analysis",
    "Business Analytics",
    "Scientific Research"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Student Performance Example
# ----------------------------------------------------------

print("\nStudent Performance Example")
print("-" * 30)

old_method = [60, 65, 70, 68, 72]
new_method = [70, 75, 78, 80, 82]

old_avg = sum(old_method) / len(old_method)
new_avg = sum(new_method) / len(new_method)

print("Old Method Average =", old_avg)
print("New Method Average =", new_avg)

if new_avg > old_avg:
    print("New Method Appears Better")

# ----------------------------------------------------------
# Business Example
# ----------------------------------------------------------

print("\nBusiness Example")
print("-" * 30)

before_sales = [100, 110, 120, 115, 105]
after_sales = [130, 140, 150, 145, 135]

avg_before = sum(before_sales) / len(before_sales)
avg_after = sum(after_sales) / len(after_sales)

print("Average Before =", avg_before)
print("Average After  =", avg_after)

if avg_after > avg_before:
    print("Sales Improved After Campaign")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

sample_mean = 55
population_mean = 50

if sample_mean > population_mean:
    print("Evidence Against H₀")
else:
    print("Support for H₀")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Hypothesis?

2. What is H₀?

3. What is H₁?

4. What is a Type I Error?

5. Why is Hypothesis Testing useful?
""")

print("""
Answers:

1. A testable claim
2. Null Hypothesis
3. Alternative Hypothesis
4. False Positive
5. Helps make decisions using data
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 27 Summary")
print("-" * 30)

print("""
1. Hypothesis Testing helps evaluate claims.
2. H₀ represents no significant effect.
3. H₁ represents a significant effect.
4. Z-Test and T-Test are common methods.
5. Type I Error = False Positive.
6. Type II Error = False Negative.
7. Widely used in ML, research,
   business analytics, and experiments.
""")

print("\nDay 27 Completed Successfully!")
print("=" * 60)