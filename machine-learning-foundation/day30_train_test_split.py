# ==========================================================
# Day 30 : Train-Test Split
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 30")
print("=" * 60)

print("\nTrain-Test Split")
print("-" * 30)

print("""
Train-Test Split is the process of dividing
a dataset into two parts:

1. Training Set
2. Testing Set

Training Set:
Used to train the Machine Learning model.

Testing Set:
Used to evaluate model performance.

This helps determine how well a model
works on unseen data.
""")

# ----------------------------------------------------------
# Why Train-Test Split?
# ----------------------------------------------------------

print("\nWhy Train-Test Split?")
print("-" * 30)

reasons = [
    "Evaluate Model Performance",
    "Detect Overfitting",
    "Measure Generalization",
    "Test on Unseen Data",
    "Build Reliable Models"
]

for reason in reasons:
    print("✓", reason)

# ----------------------------------------------------------
# Sample Dataset
# ----------------------------------------------------------

print("\nSample Dataset")
print("-" * 30)

dataset = [10, 20, 30, 40, 50,
           60, 70, 80, 90, 100]

print("Dataset =", dataset)

print("Total Records =", len(dataset))

# ----------------------------------------------------------
# 80-20 Split
# ----------------------------------------------------------

print("\n80-20 Train-Test Split")
print("-" * 30)

split_index = int(len(dataset) * 0.8)

train_data = dataset[:split_index]
test_data = dataset[split_index:]

print("Training Data =", train_data)
print("Testing Data  =", test_data)

print("Training Size =", len(train_data))
print("Testing Size  =", len(test_data))

# ----------------------------------------------------------
# Understanding the Split
# ----------------------------------------------------------

print("\nUnderstanding the Split")
print("-" * 30)

print("""
80% Data → Training

20% Data → Testing

Example:

10 Records

8 Records → Training
2 Records → Testing
""")

# ----------------------------------------------------------
# Student Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

students = [
    [18, 6, 90],
    [19, 8, 95],
    [17, 5, 85],
    [20, 7, 88],
    [21, 9, 96],
    [18, 4, 75],
    [19, 6, 82],
    [20, 8, 91],
    [17, 5, 78],
    [21, 10, 98]
]

split_index = int(len(students) * 0.8)

train_students = students[:split_index]
test_students = students[split_index:]

print("Training Records =", len(train_students))
print("Testing Records  =", len(test_students))

# ----------------------------------------------------------
# Features and Labels
# ----------------------------------------------------------

print("\nFeatures and Labels")
print("-" * 30)

print("""
Features:
Input variables

Labels:
Target values

Example:

Features:
[Study Hours, Attendance]

Label:
Marks
""")

features = [
    [2, 80],
    [4, 85],
    [6, 90],
    [8, 95]
]

labels = [50, 60, 75, 90]

print("Features =", features)
print("Labels   =", labels)

# ----------------------------------------------------------
# Splitting Features and Labels
# ----------------------------------------------------------

print("\nSplitting Features and Labels")
print("-" * 30)

split_index = int(len(features) * 0.75)

X_train = features[:split_index]
X_test = features[split_index:]

y_train = labels[:split_index]
y_test = labels[split_index:]

print("X_train =", X_train)
print("X_test  =", X_test)

print("y_train =", y_train)
print("y_test  =", y_test)

# ----------------------------------------------------------
# Common Split Ratios
# ----------------------------------------------------------

print("\nCommon Split Ratios")
print("-" * 30)

ratios = [
    "70% Train / 30% Test",
    "80% Train / 20% Test",
    "90% Train / 10% Test"
]

for ratio in ratios:
    print("✓", ratio)

# ----------------------------------------------------------
# Overfitting Concept
# ----------------------------------------------------------

print("\nOverfitting")
print("-" * 30)

print("""
Overfitting occurs when a model
memorizes training data instead
of learning patterns.

Result:

✓ High Training Accuracy
✗ Poor Test Accuracy

Train-Test Split helps detect this.
""")

# ----------------------------------------------------------
# Underfitting Concept
# ----------------------------------------------------------

print("\nUnderfitting")
print("-" * 30)

print("""
Underfitting occurs when a model
fails to learn important patterns.

Result:

✗ Poor Training Accuracy
✗ Poor Test Accuracy
""")

# ----------------------------------------------------------
# Machine Learning Workflow
# ----------------------------------------------------------

print("\nML Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Preprocess Data",
    "Feature Engineering",
    "Train-Test Split",
    "Train Model",
    "Evaluate Model",
    "Deploy Model"
]

for i, step in enumerate(steps, start=1):
    print(f"{i}. {step}")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

marks = [55, 60, 65, 70, 75,
         80, 85, 90, 95, 100]

split_index = int(len(marks) * 0.8)

train_marks = marks[:split_index]
test_marks = marks[split_index:]

print("Train Marks =", train_marks)
print("Test Marks  =", test_marks)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

data = [1, 2, 3, 4, 5,
        6, 7, 8, 9, 10]

split_index = int(len(data) * 0.7)

train = data[:split_index]
test = data[split_index:]

print("70% Training =", train)
print("30% Testing  =", test)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Train-Test Split?

2. Why do we split data?

3. What is the purpose of
   the Training Set?

4. What is the purpose of
   the Testing Set?

5. What problem can Train-Test Split
   help detect?
""")

print("""
Answers:

1. Dividing data into train and test sets
2. To evaluate model performance
3. To train the model
4. To evaluate the model
5. Overfitting
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 30 Summary")
print("-" * 30)

print("""
1. Train-Test Split divides data
   into training and testing sets.

2. Training data is used to
   build the model.

3. Testing data evaluates
   model performance.

4. Common ratios include:
   70:30, 80:20, and 90:10.

5. Train-Test Split helps detect
   overfitting and measure
   generalization ability.

6. It is a fundamental step in
   every Machine Learning project.
""")

print("\nDay 30 Completed Successfully!")
print("=" * 60)