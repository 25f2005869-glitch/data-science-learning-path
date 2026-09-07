# ==========================================================
# Day 55 : Machine Learning Pipeline
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 55")
print("=" * 60)

print("\nMachine Learning Pipeline")
print("-" * 30)

print("""
A Machine Learning Pipeline is a
structured sequence of steps used
to build a Machine Learning model.

It helps organize the complete
Machine Learning workflow from
raw data to final predictions.

Goal:

✓ Systematic Development
✓ Better Model Performance
✓ Reproducibility
✓ Automation
""")

# ----------------------------------------------------------
# What is a Machine Learning Pipeline?
# ----------------------------------------------------------

print("\nWhat is a Machine Learning Pipeline?")
print("-" * 30)

print("""
A Machine Learning Pipeline is a
series of connected stages.

Each stage performs a specific task.

Raw Data
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Prediction
""")

# ----------------------------------------------------------
# Why Use a Pipeline?
# ----------------------------------------------------------

print("\nWhy Use a Pipeline?")
print("-" * 30)

print("""
Benefits:

✓ Organized Workflow
✓ Easy Maintenance
✓ Reusable Process
✓ Reduced Human Error
✓ Better Productivity
""")

# ----------------------------------------------------------
# Complete Pipeline Stages
# ----------------------------------------------------------

print("\nMachine Learning Pipeline Stages")
print("-" * 30)

stages = [
    "Data Collection",
    "Data Preprocessing",
    "Feature Engineering",
    "Train-Test Split",
    "Model Training",
    "Model Evaluation",
    "Hyperparameter Tuning",
    "Deployment",
    "Monitoring"
]

for i, stage in enumerate(stages, start=1):

    print(f"{i}. {stage}")

# ----------------------------------------------------------
# Step 1 : Data Collection
# ----------------------------------------------------------

print("\nStep 1 : Data Collection")
print("-" * 30)

print("""
Data is collected from various sources.

Examples:

✓ Databases
✓ CSV Files
✓ APIs
✓ Sensors
✓ Websites
✓ Surveys

Good data is essential for
good model performance.
""")

# Example

student_data = [
    [5, 70, 60],
    [8, 85, 80],
    [10, 95, 92]
]

print("Sample Data =")

for row in student_data:

    print(row)

# ----------------------------------------------------------
# Step 2 : Data Preprocessing
# ----------------------------------------------------------

print("\nStep 2 : Data Preprocessing")
print("-" * 30)

print("""
Raw data often contains:

✗ Missing Values
✗ Duplicate Records
✗ Incorrect Values
✗ Noise

Preprocessing improves
data quality.
""")

# Example

data = [
    10,
    15,
    None,
    20,
    25
]

print("Original Data =", data)

cleaned_data = [
    value
    for value in data
    if value is not None
]

print("Cleaned Data =", cleaned_data)

# ----------------------------------------------------------
# Step 3 : Feature Engineering
# ----------------------------------------------------------

print("\nStep 3 : Feature Engineering")
print("-" * 30)

print("""
Feature Engineering creates
useful features from raw data.

Examples:

Age → Age Group

Date → Month, Year

Text → Word Counts

Good features improve
model performance.
""")

age = 21

if age < 18:

    age_group = "Teen"

elif age < 60:

    age_group = "Adult"

else:

    age_group = "Senior"

print("Age Group =", age_group)

# ----------------------------------------------------------
# Step 4 : Train-Test Split
# ----------------------------------------------------------

print("\nStep 4 : Train-Test Split")
print("-" * 30)

print("""
Data is divided into:

Training Data
Testing Data

Common Split:

80% Training
20% Testing

Purpose:

Evaluate model performance
on unseen data.
""")

total_samples = 100

train_samples = int(
    total_samples * 0.8
)

test_samples = total_samples - train_samples

print("Training Samples =", train_samples)
print("Testing Samples  =", test_samples)

# ----------------------------------------------------------
# Step 5 : Model Training
# ----------------------------------------------------------

print("\nStep 5 : Model Training")
print("-" * 30)

print("""
The Machine Learning algorithm
learns patterns from training data.

Examples:

✓ Linear Regression
✓ Logistic Regression
✓ Decision Tree
✓ Random Forest
✓ KNN
""")

algorithms = [
    "Linear Regression",
    "Decision Tree",
    "Random Forest"
]

for algorithm in algorithms:

    print("✓", algorithm)

# ----------------------------------------------------------
# Step 6 : Model Evaluation
# ----------------------------------------------------------

print("\nStep 6 : Model Evaluation")
print("-" * 30)

print("""
Evaluate model performance
using metrics.

Classification Metrics:

✓ Accuracy
✓ Precision
✓ Recall
✓ F1 Score

Regression Metrics:

✓ MAE
✓ MSE
✓ RMSE
✓ R² Score
""")

accuracy = 0.92

print("Example Accuracy =",
      accuracy)

# ----------------------------------------------------------
# Step 7 : Hyperparameter Tuning
# ----------------------------------------------------------

print("\nStep 7 : Hyperparameter Tuning")
print("-" * 30)

print("""
Hyperparameters control
model behavior.

Examples:

Decision Tree Depth

Number of Trees in
Random Forest

K Value in KNN

Tuning improves performance.
""")

k = 5

print("K Value =", k)

# ----------------------------------------------------------
# Step 8 : Deployment
# ----------------------------------------------------------

print("\nStep 8 : Deployment")
print("-" * 30)

print("""
After training, the model is
deployed into production.

Examples:

✓ Mobile Apps
✓ Websites
✓ Business Systems
✓ Cloud Platforms

Users can now interact
with the model.
""")

# ----------------------------------------------------------
# Step 9 : Monitoring
# ----------------------------------------------------------

print("\nStep 9 : Monitoring")
print("-" * 30)

print("""
After deployment:

Monitor performance.

Reasons:

✓ Data Changes
✓ User Behavior Changes
✓ Performance Degradation

Models may require retraining.
""")

# ----------------------------------------------------------
# End-to-End Example
# ----------------------------------------------------------

print("\nEnd-to-End Example")
print("-" * 30)

print("""
Student Marks Prediction

1. Collect Student Data
2. Clean Data
3. Create Features
4. Split Data
5. Train Regression Model
6. Evaluate Accuracy
7. Deploy Model
8. Monitor Results
""")

# ----------------------------------------------------------
# Pipeline Visualization
# ----------------------------------------------------------

print("\nPipeline Visualization")
print("-" * 30)

print("""
Data Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Deployment
        ↓
Monitoring
""")

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Organized Workflow",
    "Automation",
    "Reusability",
    "Scalability",
    "Better Productivity"
]

for item in advantages:

    print("✓", item)

# ----------------------------------------------------------
# Challenges
# ----------------------------------------------------------

print("\nChallenges")
print("-" * 30)

challenges = [
    "Poor Data Quality",
    "Overfitting",
    "Underfitting",
    "Feature Selection Issues",
    "Deployment Complexity"
]

for item in challenges:

    print("✗", item)

# ----------------------------------------------------------
# Real-World Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Healthcare",
    "Finance",
    "Education",
    "E-Commerce",
    "Manufacturing",
    "Marketing"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

steps_completed = 7
total_steps = 9

completion = (
    steps_completed /
    total_steps
) * 100

print("Pipeline Completion =",
      round(completion, 2),
      "%")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

Which step comes after
Feature Engineering?

Answer:

Train-Test Split
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Machine Learning Pipeline?

2. Why is Data Preprocessing important?

3. What is Feature Engineering?

4. Why do we split data?

5. What happens after deployment?
""")

print("""
Answers:

1. Structured ML workflow
2. Improves data quality
3. Creating useful features
4. Model evaluation
5. Monitoring
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 55 Summary")
print("-" * 30)

print("""
1. A Machine Learning Pipeline
   is a complete ML workflow.

2. Main Stages:

   ✓ Data Collection
   ✓ Data Preprocessing
   ✓ Feature Engineering
   ✓ Train-Test Split
   ✓ Model Training
   ✓ Model Evaluation
   ✓ Hyperparameter Tuning
   ✓ Deployment
   ✓ Monitoring

3. Pipelines improve organization,
   automation, and reliability.

4. They are widely used in
   real-world Machine Learning projects.

5. Understanding pipelines is
   essential for becoming a
   Machine Learning Engineer.
""")

print("\nDay 55 Completed Successfully!")
print("=" * 60)