# ==========================================================
# Day 56 : Overfitting and Underfitting
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 56")
print("=" * 60)

print("\nOverfitting and Underfitting")
print("-" * 30)

print("""
Overfitting and Underfitting are two
common problems in Machine Learning.

They affect how well a model performs
on unseen data.

Goal:

Build a model that learns useful
patterns and generalizes well.
""")

# ----------------------------------------------------------
# What is Underfitting?
# ----------------------------------------------------------

print("\nWhat is Underfitting?")
print("-" * 30)

print("""
Underfitting occurs when a model is
too simple to learn patterns from data.

Characteristics:

✗ Poor Training Performance
✗ Poor Testing Performance
✗ High Bias

The model fails to capture
important relationships.
""")

# ----------------------------------------------------------
# Underfitting Example
# ----------------------------------------------------------

print("\nUnderfitting Example")
print("-" * 30)

print("""
Suppose actual relationship:

y = x²

Model tries:

y = x

The model is too simple and
cannot learn the true pattern.
""")

x = 5

actual_value = x ** 2
predicted_value = x

print("Actual Value    =", actual_value)
print("Predicted Value =", predicted_value)

# ----------------------------------------------------------
# What is Overfitting?
# ----------------------------------------------------------

print("\nWhat is Overfitting?")
print("-" * 30)

print("""
Overfitting occurs when a model
memorizes training data instead
of learning general patterns.

Characteristics:

✓ Excellent Training Performance
✗ Poor Testing Performance
✗ High Variance

The model performs poorly
on new unseen data.
""")

# ----------------------------------------------------------
# Overfitting Example
# ----------------------------------------------------------

print("\nOverfitting Example")
print("-" * 30)

print("""
The model learns:

✓ Useful Patterns
✓ Noise
✓ Random Fluctuations

As a result, it cannot
generalize effectively.
""")

training_accuracy = 99
testing_accuracy = 70

print("Training Accuracy =", training_accuracy, "%")
print("Testing Accuracy  =", testing_accuracy, "%")

# ----------------------------------------------------------
# Good Fit
# ----------------------------------------------------------

print("\nGood Fit")
print("-" * 30)

print("""
A good model achieves balance.

Characteristics:

✓ Good Training Performance
✓ Good Testing Performance
✓ Generalizes Well

This is the desired outcome.
""")

training_accuracy = 92
testing_accuracy = 90

print("Training Accuracy =", training_accuracy, "%")
print("Testing Accuracy  =", testing_accuracy, "%")

# ----------------------------------------------------------
# Visual Understanding
# ----------------------------------------------------------

print("\nVisual Understanding")
print("-" * 30)

print("""
Underfitting:

Data Pattern
     ~~~~~

Model:
---------

Too Simple

-------------------------

Good Fit:

Data Pattern
     ~~~~~

Model:
     ~~~~~

Matches Pattern

-------------------------

Overfitting:

Data Pattern
     ~~~~~

Model:
~~~~~^~~~^^~~~

Too Complex
""")

# ----------------------------------------------------------
# Bias and Variance
# ----------------------------------------------------------

print("\nBias and Variance")
print("-" * 30)

print("""
Underfitting:

✓ High Bias
✓ Low Variance

Overfitting:

✓ Low Bias
✓ High Variance

Good Fit:

✓ Balanced Bias
✓ Balanced Variance
""")

# ----------------------------------------------------------
# Causes of Underfitting
# ----------------------------------------------------------

print("\nCauses of Underfitting")
print("-" * 30)

causes_underfitting = [
    "Model Too Simple",
    "Insufficient Features",
    "Too Little Training",
    "Poor Feature Engineering"
]

for item in causes_underfitting:

    print("✓", item)

# ----------------------------------------------------------
# Causes of Overfitting
# ----------------------------------------------------------

print("\nCauses of Overfitting")
print("-" * 30)

causes_overfitting = [
    "Model Too Complex",
    "Small Dataset",
    "Too Many Features",
    "Excessive Training"
]

for item in causes_overfitting:

    print("✓", item)

# ----------------------------------------------------------
# Detecting Underfitting
# ----------------------------------------------------------

print("\nDetecting Underfitting")
print("-" * 30)

train_score = 60
test_score = 58

print("Training Score =", train_score)
print("Testing Score  =", test_score)

print("""
Both scores are low.

Possible Underfitting.
""")

# ----------------------------------------------------------
# Detecting Overfitting
# ----------------------------------------------------------

print("\nDetecting Overfitting")
print("-" * 30)

train_score = 98
test_score = 70

print("Training Score =", train_score)
print("Testing Score  =", test_score)

print("""
Large gap between scores.

Possible Overfitting.
""")

# ----------------------------------------------------------
# Reducing Underfitting
# ----------------------------------------------------------

print("\nReducing Underfitting")
print("-" * 30)

solutions_underfitting = [
    "Increase Model Complexity",
    "Add More Features",
    "Train Longer",
    "Improve Feature Engineering"
]

for item in solutions_underfitting:

    print("✓", item)

# ----------------------------------------------------------
# Reducing Overfitting
# ----------------------------------------------------------

print("\nReducing Overfitting")
print("-" * 30)

solutions_overfitting = [
    "Collect More Data",
    "Reduce Model Complexity",
    "Feature Selection",
    "Cross Validation",
    "Regularization"
]

for item in solutions_overfitting:

    print("✓", item)

# ----------------------------------------------------------
# Regularization
# ----------------------------------------------------------

print("\nRegularization")
print("-" * 30)

print("""
Regularization penalizes
overly complex models.

Popular Techniques:

✓ L1 Regularization
✓ L2 Regularization

Helps reduce overfitting.
""")

# ----------------------------------------------------------
# Cross Validation
# ----------------------------------------------------------

print("\nCross Validation")
print("-" * 30)

print("""
Cross Validation evaluates
model performance on multiple
data splits.

Benefits:

✓ Better Evaluation
✓ Detects Overfitting
✓ Improves Reliability
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

study_hours = [1, 2, 3, 4, 5]
marks = [35, 45, 55, 65, 75]

print("Study Hours =", study_hours)
print("Marks       =", marks)

# ----------------------------------------------------------
# Real-World Example
# ----------------------------------------------------------

print("\nHouse Price Prediction")
print("-" * 30)

print("""
Underfitting:

Using only house area.

Overfitting:

Using hundreds of unnecessary
features.

Good Fit:

Using relevant features such as:

✓ Area
✓ Bedrooms
✓ Location
""")

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Regression Models",
    "Classification Models",
    "Deep Learning",
    "Forecasting",
    "Recommendation Systems"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nModel Improvement Workflow")
print("-" * 30)

steps = [
    "Train Model",
    "Evaluate Training Score",
    "Evaluate Testing Score",
    "Detect Problem",
    "Apply Improvements",
    "Retrain Model"
]

for i, step in enumerate(
        steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

training_accuracy = 95
testing_accuracy = 94

difference = abs(
    training_accuracy -
    testing_accuracy
)

print("Difference =", difference)

if difference <= 5:

    print("Good Generalization")

else:

    print("Potential Overfitting")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

Training Accuracy = 99%
Testing Accuracy = 65%

What is the problem?

Answer:

Overfitting
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Underfitting?

2. What is Overfitting?

3. Which problem has High Bias?

4. Which problem has High Variance?

5. Name one method to reduce
   overfitting.
""")

print("""
Answers:

1. Model too simple
2. Model memorizes data
3. Underfitting
4. Overfitting
5. Regularization
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 56 Summary")
print("-" * 30)

print("""
1. Underfitting occurs when
   a model is too simple.

2. Overfitting occurs when
   a model is too complex.

3. Underfitting:

   ✓ High Bias
   ✓ Low Variance

4. Overfitting:

   ✓ Low Bias
   ✓ High Variance

5. Good models balance
   bias and variance.

6. Regularization and
   Cross Validation help
   reduce overfitting.

7. Understanding these concepts
   is essential for building
   reliable ML models.
""")

print("\nDay 56 Completed Successfully!")
print("=" * 60)