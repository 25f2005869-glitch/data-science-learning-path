# ==========================================================
# Day 33 : Cross Validation
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 33")
print("=" * 60)

print("\nCross Validation")
print("-" * 30)

print("""
Cross Validation is a technique used to
evaluate Machine Learning models more reliably.

Instead of using only one train-test split,
the dataset is divided into multiple parts.

Benefits:

✓ Better Model Evaluation
✓ More Reliable Results
✓ Reduced Overfitting Risk
✓ Efficient Use of Data
✓ Better Generalization
""")

# ----------------------------------------------------------
# Why Cross Validation?
# ----------------------------------------------------------

print("\nWhy Cross Validation?")
print("-" * 30)

print("""
A single train-test split may produce
biased results.

Different splits can produce
different accuracies.

Cross Validation helps obtain
a more stable estimate of performance.
""")

# ----------------------------------------------------------
# Traditional Train-Test Split
# ----------------------------------------------------------

print("\nTraditional Train-Test Split")
print("-" * 30)

dataset = list(range(1, 11))

train_data = dataset[:8]
test_data = dataset[8:]

print("Training Data =", train_data)
print("Testing Data  =", test_data)

print("""
Only one evaluation is performed.
""")

# ----------------------------------------------------------
# K-Fold Cross Validation
# ----------------------------------------------------------

print("\nK-Fold Cross Validation")
print("-" * 30)

print("""
In K-Fold Cross Validation:

1. Divide data into K folds.
2. Use one fold for testing.
3. Use remaining folds for training.
4. Repeat K times.
5. Compute average performance.

Most common:

✓ 5-Fold
✓ 10-Fold
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample : 5-Fold Cross Validation")
print("-" * 30)

data = [1, 2, 3, 4, 5,
        6, 7, 8, 9, 10]

fold_size = len(data) // 5

print("Dataset =", data)
print("Fold Size =", fold_size)

# ----------------------------------------------------------
# Creating Folds
# ----------------------------------------------------------

print("\nCreating Folds")
print("-" * 30)

folds = []

for i in range(0, len(data), fold_size):
    folds.append(data[i:i + fold_size])

for index, fold in enumerate(folds, start=1):
    print(f"Fold {index} =", fold)

# ----------------------------------------------------------
# Simulating Cross Validation
# ----------------------------------------------------------

print("\nCross Validation Process")
print("-" * 30)

for i in range(len(folds)):

    test_fold = folds[i]

    train_folds = []

    for j in range(len(folds)):

        if i != j:
            train_folds.extend(folds[j])

    print(f"\nIteration {i + 1}")
    print("Training =", train_folds)
    print("Testing  =", test_fold)

# ----------------------------------------------------------
# Example Accuracy Scores
# ----------------------------------------------------------

print("\nFold Accuracy Scores")
print("-" * 30)

accuracy_scores = [
    88,
    90,
    92,
    89,
    91
]

for i, score in enumerate(accuracy_scores, start=1):
    print(f"Fold {i} Accuracy = {score}%")

# ----------------------------------------------------------
# Average Accuracy
# ----------------------------------------------------------

print("\nAverage Accuracy")
print("-" * 30)

average_accuracy = (
    sum(accuracy_scores) /
    len(accuracy_scores)
)

print("Average Accuracy =",
      round(average_accuracy, 2), "%")

# ----------------------------------------------------------
# Leave-One-Out Cross Validation
# ----------------------------------------------------------

print("\nLeave-One-Out Cross Validation")
print("-" * 30)

print("""
LOOCV:

Each observation becomes
a test sample once.

Advantages:

✓ Uses Maximum Data

Disadvantages:

✗ Computationally Expensive
""")

# ----------------------------------------------------------
# Stratified Cross Validation
# ----------------------------------------------------------

print("\nStratified Cross Validation")
print("-" * 30)

print("""
Maintains class distribution
across all folds.

Useful for:

✓ Classification Problems
✓ Imbalanced Datasets
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nCross Validation in ML")
print("-" * 30)

applications = [
    "Model Selection",
    "Hyperparameter Tuning",
    "Performance Evaluation",
    "Classification Models",
    "Regression Models",
    "Deep Learning Experiments"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Student Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

student_marks = [
    55, 60, 65, 70, 75,
    80, 85, 90, 95, 100
]

print("Student Marks =", student_marks)

print("""
Cross Validation can evaluate
how well a prediction model
generalizes to unseen students.
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

model_scores = [
    82,
    84,
    83,
    85,
    86
]

average_score = (
    sum(model_scores) /
    len(model_scores)
)

print("Fold Scores =", model_scores)
print("Average Score =", average_score)

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages of Cross Validation")
print("-" * 30)

advantages = [
    "Better Evaluation",
    "Efficient Data Usage",
    "More Reliable Accuracy",
    "Less Bias",
    "Better Model Selection"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

scores = [80, 82, 84, 86, 88]

mean_score = (
    sum(scores) /
    len(scores)
)

print("Fold Scores =", scores)
print("Average Accuracy =", mean_score)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Cross Validation?

2. Why is it better than a single
   train-test split?

3. What is K-Fold Cross Validation?

4. What does LOOCV stand for?

5. Why is Cross Validation useful?
""")

print("""
Answers:

1. Model evaluation technique
2. Produces more reliable results
3. Dataset divided into K folds
4. Leave-One-Out Cross Validation
5. Helps estimate model performance
   more accurately
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 33 Summary")
print("-" * 30)

print("""
1. Cross Validation evaluates models
   using multiple train-test splits.

2. K-Fold Cross Validation is the
   most commonly used method.

3. Average performance across folds
   provides a reliable estimate.

4. LOOCV uses one observation
   as test data at a time.

5. Cross Validation helps improve
   model selection and evaluation.

6. It is a standard practice in
   Machine Learning projects.
""")

print("\nDay 33 Completed Successfully!")
print("=" * 60)