# ==========================================================
# Day 32 : Bias-Variance Tradeoff
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 32")
print("=" * 60)

print("\nBias-Variance Tradeoff")
print("-" * 30)

print("""
Bias and Variance are two major sources
of prediction error in Machine Learning.

A good model must balance both.

High Bias:
✓ Oversimplified Model
✗ Underfitting

High Variance:
✓ Very Complex Model
✗ Overfitting

Goal:
Find the right balance.
""")

# ----------------------------------------------------------
# Understanding Bias
# ----------------------------------------------------------

print("\nWhat is Bias?")
print("-" * 30)

print("""
Bias measures how far model predictions
are from the true values on average.

High Bias means:

✓ Model is too simple
✓ Important patterns ignored
✓ Underfitting occurs
""")

# Example
actual_marks = [60, 70, 80, 90]
simple_model_predictions = [70, 70, 70, 70]

print("Actual Marks        =", actual_marks)
print("Simple Predictions  =", simple_model_predictions)

print("""
Model predicts nearly the same value
for every input.

This indicates High Bias.
""")

# ----------------------------------------------------------
# Understanding Variance
# ----------------------------------------------------------

print("\nWhat is Variance?")
print("-" * 30)

print("""
Variance measures how much model
predictions change with different datasets.

High Variance means:

✓ Model memorizes training data
✓ Sensitive to small changes
✓ Overfitting occurs
""")

complex_model_predictions = [60, 69, 81, 91]

print("Actual Marks        =", actual_marks)
print("Complex Predictions =", complex_model_predictions)

print("""
Predictions closely match training data.

May perform poorly on new data.
""")

# ----------------------------------------------------------
# Underfitting
# ----------------------------------------------------------

print("\nUnderfitting")
print("-" * 30)

print("""
Underfitting occurs when the model
cannot learn important patterns.

Characteristics:

✗ High Training Error
✗ High Testing Error
✓ High Bias
✓ Low Variance
""")

# Example
training_accuracy = 55
testing_accuracy = 52

print("Training Accuracy =", training_accuracy, "%")
print("Testing Accuracy  =", testing_accuracy, "%")

# ----------------------------------------------------------
# Overfitting
# ----------------------------------------------------------

print("\nOverfitting")
print("-" * 30)

print("""
Overfitting occurs when the model
memorizes training data.

Characteristics:

✓ Very Low Training Error
✗ High Testing Error
✓ Low Bias
✓ High Variance
""")

training_accuracy = 99
testing_accuracy = 72

print("Training Accuracy =", training_accuracy, "%")
print("Testing Accuracy  =", testing_accuracy, "%")

# ----------------------------------------------------------
# Ideal Model
# ----------------------------------------------------------

print("\nIdeal Model")
print("-" * 30)

print("""
A good model should:

✓ Learn patterns
✓ Generalize well
✓ Have Low Bias
✓ Have Low Variance
""")

good_training_accuracy = 92
good_testing_accuracy = 90

print("Training Accuracy =", good_training_accuracy, "%")
print("Testing Accuracy  =", good_testing_accuracy, "%")

# ----------------------------------------------------------
# Bias vs Variance Comparison
# ----------------------------------------------------------

print("\nBias vs Variance")
print("-" * 30)

print("""
High Bias:

✓ Simple Model
✓ Underfitting
✓ Misses Patterns

High Variance:

✓ Complex Model
✓ Overfitting
✓ Learns Noise
""")

# ----------------------------------------------------------
# Real Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
marks = [40, 55, 70, 85, 95]

print("Study Hours =", study_hours)
print("Marks       =", marks)

print("""
A straight line may underfit.

A very complex curve may overfit.

A moderate model often works best.
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nBias-Variance in ML")
print("-" * 30)

applications = [
    "Linear Regression",
    "Decision Trees",
    "Random Forest",
    "Neural Networks",
    "Deep Learning",
    "Model Selection"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Model Complexity Example
# ----------------------------------------------------------

print("\nModel Complexity")
print("-" * 30)

complexity_levels = [
    "Very Simple Model",
    "Simple Model",
    "Balanced Model",
    "Complex Model",
    "Very Complex Model"
]

for level in complexity_levels:
    print("✓", level)

print("""
Increasing complexity:

Bias ↓
Variance ↑
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

models = {
    "Model A": 65,
    "Model B": 85,
    "Model C": 98
}

for model, accuracy in models.items():
    print(model, "Training Accuracy =", accuracy, "%")

print("""
Higher training accuracy alone
does not guarantee a better model.

Testing performance is also important.
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

train_accuracy = 97
test_accuracy = 60

print("Training Accuracy =", train_accuracy)
print("Testing Accuracy  =", test_accuracy)

print("""
Question:
Overfitting or Underfitting?

Answer:
Overfitting
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Bias?

2. What is Variance?

3. What causes Underfitting?

4. What causes Overfitting?

5. What is the goal of the
   Bias-Variance Tradeoff?
""")

print("""
Answers:

1. Error from overly simple assumptions
2. Sensitivity to data changes
3. High Bias
4. High Variance
5. Balance Bias and Variance
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 32 Summary")
print("-" * 30)

print("""
1. Bias and Variance are major
   sources of prediction error.

2. High Bias leads to Underfitting.

3. High Variance leads to Overfitting.

4. Good models balance Bias
   and Variance.

5. The Bias-Variance Tradeoff is
   fundamental in Machine Learning.

6. Model evaluation helps identify
   whether a model is underfitting
   or overfitting.
""")

print("\nDay 32 Completed Successfully!")
print("=" * 60)