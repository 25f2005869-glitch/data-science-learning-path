# ==========================================================
# Day 58 : End-to-End Machine Learning Workflow
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 58")
print("=" * 60)

print("\nEnd-to-End Machine Learning Workflow")
print("-" * 30)

print("""
An End-to-End Machine Learning Workflow
covers the complete journey of a Machine
Learning project.

From raw data collection to deployment,
every stage is important.

Goal:

✓ Build Reliable Models
✓ Solve Real Problems
✓ Generate Predictions
✓ Deploy Solutions
""")

# ----------------------------------------------------------
# What is an End-to-End Workflow?
# ----------------------------------------------------------

print("\nWhat is an End-to-End Workflow?")
print("-" * 30)

print("""
A Machine Learning project follows
a sequence of connected steps.

Problem Definition
        ↓
Data Collection
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Model Building
        ↓
Model Evaluation
        ↓
Deployment
        ↓
Monitoring
""")

# ----------------------------------------------------------
# Step 1 : Problem Definition
# ----------------------------------------------------------

print("\nStep 1 : Problem Definition")
print("-" * 30)

print("""
Before building a model,
the problem must be clearly defined.

Examples:

✓ Predict House Prices
✓ Detect Fraud
✓ Predict Student Performance
✓ Recommend Products

A clear objective guides
the entire project.
""")

problem_statement = (
    "Predict Student Marks"
)

print("Problem =", problem_statement)

# ----------------------------------------------------------
# Step 2 : Data Collection
# ----------------------------------------------------------

print("\nStep 2 : Data Collection")
print("-" * 30)

print("""
Data can come from:

✓ CSV Files
✓ Databases
✓ APIs
✓ Sensors
✓ Surveys
✓ Websites
""")

student_data = [
    [5, 70],
    [7, 80],
    [9, 90]
]

print("Sample Data =")

for row in student_data:
    print(row)

# ----------------------------------------------------------
# Step 3 : Data Exploration
# ----------------------------------------------------------

print("\nStep 3 : Data Exploration")
print("-" * 30)

print("""
Understand the dataset.

Questions:

✓ How many rows?
✓ How many columns?
✓ Missing values?
✓ Outliers?
✓ Data Types?

EDA = Exploratory Data Analysis
""")

rows = len(student_data)
columns = len(student_data[0])

print("Rows =", rows)
print("Columns =", columns)

# ----------------------------------------------------------
# Step 4 : Data Preprocessing
# ----------------------------------------------------------

print("\nStep 4 : Data Preprocessing")
print("-" * 30)

print("""
Raw data often contains:

✗ Missing Values
✗ Duplicates
✗ Noise

Cleaning improves quality.
""")

data = [10, 15, None, 20, 25]

clean_data = [
    value
    for value in data
    if value is not None
]

print("Clean Data =", clean_data)

# ----------------------------------------------------------
# Step 5 : Feature Engineering
# ----------------------------------------------------------

print("\nStep 5 : Feature Engineering")
print("-" * 30)

print("""
Feature Engineering creates
useful features from raw data.

Examples:

Age → Age Group

Date → Month

Income → Income Category

Better Features
→ Better Models
""")

age = 22

if age < 18:
    age_group = "Teen"

elif age < 60:
    age_group = "Adult"

else:
    age_group = "Senior"

print("Age Group =", age_group)

# ----------------------------------------------------------
# Step 6 : Train-Test Split
# ----------------------------------------------------------

print("\nStep 6 : Train-Test Split")
print("-" * 30)

print("""
Split data into:

Training Data
Testing Data

Common Split:

80% Training
20% Testing
""")

total_samples = 100

train_samples = int(
    total_samples * 0.8
)

test_samples = (
    total_samples -
    train_samples
)

print("Training Samples =", train_samples)
print("Testing Samples  =", test_samples)

# ----------------------------------------------------------
# Step 7 : Model Selection
# ----------------------------------------------------------

print("\nStep 7 : Model Selection")
print("-" * 30)

print("""
Choose a suitable algorithm.

Examples:

Regression:

✓ Linear Regression

Classification:

✓ Logistic Regression
✓ Decision Tree
✓ Random Forest

Clustering:

✓ K-Means
""")

models = [
    "Linear Regression",
    "Decision Tree",
    "Random Forest"
]

for model in models:
    print("✓", model)

# ----------------------------------------------------------
# Step 8 : Model Training
# ----------------------------------------------------------

print("\nStep 8 : Model Training")
print("-" * 30)

print("""
The model learns patterns
from training data.

Training transforms the model
from an empty state into
a predictive system.
""")

training_accuracy = 91

print("Training Accuracy =",
      training_accuracy,
      "%")

# ----------------------------------------------------------
# Step 9 : Model Evaluation
# ----------------------------------------------------------

print("\nStep 9 : Model Evaluation")
print("-" * 30)

print("""
Evaluate performance using metrics.

Classification:

✓ Accuracy
✓ Precision
✓ Recall
✓ F1 Score

Regression:

✓ MAE
✓ MSE
✓ RMSE
✓ R² Score
""")

testing_accuracy = 89

print("Testing Accuracy =",
      testing_accuracy,
      "%")

# ----------------------------------------------------------
# Step 10 : Cross Validation
# ----------------------------------------------------------

print("\nStep 10 : Cross Validation")
print("-" * 30)

print("""
Cross Validation provides
more reliable evaluation.

Benefits:

✓ Detect Overfitting
✓ Better Generalization
✓ Reliable Scores
""")

cv_scores = [
    0.89,
    0.91,
    0.90,
    0.88,
    0.92
]

average_cv = (
    sum(cv_scores) /
    len(cv_scores)
)

print("Average CV Score =",
      round(average_cv, 4))

# ----------------------------------------------------------
# Step 11 : Hyperparameter Tuning
# ----------------------------------------------------------

print("\nStep 11 : Hyperparameter Tuning")
print("-" * 30)

print("""
Hyperparameters control
model behavior.

Examples:

✓ K in KNN
✓ Tree Depth
✓ Learning Rate

Tuning improves performance.
""")

k = 5

print("K Value =", k)

# ----------------------------------------------------------
# Step 12 : Deployment
# ----------------------------------------------------------

print("\nStep 12 : Deployment")
print("-" * 30)

print("""
Deploy the model into production.

Examples:

✓ Website
✓ Mobile App
✓ Business Software
✓ Cloud Service

Users can now use the model.
""")

deployment_status = "Successful"

print("Deployment Status =",
      deployment_status)

# ----------------------------------------------------------
# Step 13 : Monitoring
# ----------------------------------------------------------

print("\nStep 13 : Monitoring")
print("-" * 30)

print("""
Monitor model performance
after deployment.

Reasons:

✓ Data Drift
✓ Performance Changes
✓ New User Behavior

Models may require retraining.
""")

# ----------------------------------------------------------
# End-to-End Example
# ----------------------------------------------------------

print("\nStudent Performance Prediction")
print("-" * 30)

workflow_steps = [
    "Collect Student Data",
    "Clean Data",
    "Create Features",
    "Split Dataset",
    "Train Model",
    "Evaluate Model",
    "Deploy Model",
    "Monitor Results"
]

for i, step in enumerate(
        workflow_steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Workflow Diagram
# ----------------------------------------------------------

print("\nWorkflow Diagram")
print("-" * 30)

print("""
Problem Definition
        ↓
Data Collection
        ↓
Data Exploration
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Model Selection
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Cross Validation
        ↓
Hyperparameter Tuning
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
    "Organized Process",
    "Better Accuracy",
    "Improved Reliability",
    "Scalable Solutions",
    "Industry Standard Workflow"
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
    "Deployment Complexity",
    "Maintenance Cost"
]

for item in challenges:
    print("✗", item)

# ----------------------------------------------------------
# Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Healthcare",
    "Finance",
    "Education",
    "E-Commerce",
    "Agriculture",
    "Manufacturing"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

completed_steps = 12
total_steps = 13

progress = (
    completed_steps /
    total_steps
) * 100

print("Workflow Progress =",
      round(progress, 2),
      "%")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

Which step comes after
Model Evaluation?

Answer:

Cross Validation
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is an End-to-End ML Workflow?

2. Why is Data Preprocessing important?

3. What is Feature Engineering?

4. Why do we deploy models?

5. Why is Monitoring required?
""")

print("""
Answers:

1. Complete ML project process
2. Improve data quality
3. Create useful features
4. Allow users to use the model
5. Track model performance
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 58 Summary")
print("-" * 30)

print("""
1. End-to-End Workflow covers
   the complete ML lifecycle.

2. Main Stages:

   ✓ Problem Definition
   ✓ Data Collection
   ✓ Data Exploration
   ✓ Data Preprocessing
   ✓ Feature Engineering
   ✓ Train-Test Split
   ✓ Model Selection
   ✓ Model Training
   ✓ Model Evaluation
   ✓ Cross Validation
   ✓ Hyperparameter Tuning
   ✓ Deployment
   ✓ Monitoring

3. Every stage contributes to
   successful model development.

4. This workflow is widely used
   in industry and research.

5. Understanding the complete
   workflow is essential for
   Machine Learning Engineers
   and Data Scientists.
""")

print("\nDay 58 Completed Successfully!")
print("=" * 60)