# ==========================================================
# Day 04 : Machine Learning Workflow
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 04")
print("=" * 60)

print("\nWhat is a Machine Learning Workflow?")
print("-" * 30)

print("""
A Machine Learning Workflow is a step-by-step process
used to build, train, evaluate, and deploy a machine
learning model.

Every successful ML project follows a structured workflow.
""")

# ----------------------------------------------------------
# ML Workflow Steps
# ----------------------------------------------------------

print("\nMachine Learning Workflow")
print("-" * 30)

workflow_steps = [
    "1. Problem Definition",
    "2. Data Collection",
    "3. Data Cleaning",
    "4. Exploratory Data Analysis (EDA)",
    "5. Feature Engineering",
    "6. Train-Test Split",
    "7. Model Selection",
    "8. Model Training",
    "9. Model Evaluation",
    "10. Model Deployment",
    "11. Monitoring and Improvement"
]

for step in workflow_steps:
    print(step)

# ----------------------------------------------------------
# Step 1 : Problem Definition
# ----------------------------------------------------------

print("\nStep 1 : Problem Definition")
print("-" * 30)

print("""
Example:

A school wants to predict student marks
based on study hours.

Input  -> Study Hours
Output -> Expected Marks
""")

# ----------------------------------------------------------
# Step 2 : Data Collection
# ----------------------------------------------------------

print("\nStep 2 : Data Collection")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]

print("Collected Dataset")
print("Study Hours :", study_hours)
print("Marks       :", marks)

# ----------------------------------------------------------
# Step 3 : Data Cleaning
# ----------------------------------------------------------

print("\nStep 3 : Data Cleaning")
print("-" * 30)

print("""
Data Cleaning includes:

✓ Handling missing values
✓ Removing duplicates
✓ Correcting errors
✓ Standardizing formats
""")

# ----------------------------------------------------------
# Step 4 : Exploratory Data Analysis
# ----------------------------------------------------------

print("\nStep 4 : Exploratory Data Analysis (EDA)")
print("-" * 30)

average_marks = sum(marks) / len(marks)

print("Average Marks:", average_marks)

print("""
EDA helps us understand patterns,
trends, and relationships in data.
""")

# ----------------------------------------------------------
# Step 5 : Feature Engineering
# ----------------------------------------------------------

print("\nStep 5 : Feature Engineering")
print("-" * 30)

print("""
Features are input variables used
for prediction.

Example:
Feature -> Study Hours
Target  -> Marks
""")

# ----------------------------------------------------------
# Step 6 : Train-Test Split
# ----------------------------------------------------------

print("\nStep 6 : Train-Test Split")
print("-" * 30)

print("""
Training Data -> Used to train model
Testing Data  -> Used to evaluate model

Common Split:
80% Training
20% Testing
""")

# ----------------------------------------------------------
# Step 7 : Model Selection
# ----------------------------------------------------------

print("\nStep 7 : Model Selection")
print("-" * 30)

models = [
    "Linear Regression",
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "KNN",
    "SVM"
]

for model in models:
    print(f"✓ {model}")

# ----------------------------------------------------------
# Step 8 : Model Training
# ----------------------------------------------------------

print("\nStep 8 : Model Training")
print("-" * 30)

print("""
The selected algorithm learns patterns
from the training data.
""")

# ----------------------------------------------------------
# Step 9 : Model Evaluation
# ----------------------------------------------------------

print("\nStep 9 : Model Evaluation")
print("-" * 30)

print("""
Common Evaluation Metrics:

Regression:
✓ MAE
✓ MSE
✓ RMSE
✓ R² Score

Classification:
✓ Accuracy
✓ Precision
✓ Recall
✓ F1 Score
""")

# ----------------------------------------------------------
# Step 10 : Deployment
# ----------------------------------------------------------

print("\nStep 10 : Model Deployment")
print("-" * 30)

print("""
Deployment means making the model
available for real-world use.

Examples:
✓ Web Applications
✓ Mobile Applications
✓ Business Dashboards
✓ AI Assistants
""")

# ----------------------------------------------------------
# Step 11 : Monitoring
# ----------------------------------------------------------

print("\nStep 11 : Monitoring and Improvement")
print("-" * 30)

print("""
After deployment, the model must be
continuously monitored and updated
using new data.
""")

# ----------------------------------------------------------
# Workflow Diagram
# ----------------------------------------------------------

print("\nML Workflow Diagram")
print("-" * 30)

print("""
Problem Definition
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
EDA
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
# Summary
# ----------------------------------------------------------

print("\nDay 04 Summary")
print("-" * 30)

print("""
1. Every ML project follows a workflow.
2. Data collection and cleaning are critical.
3. Models learn from training data.
4. Evaluation measures model performance.
5. Deployment brings ML models into real-world use.
6. Monitoring keeps models effective over time.
""")

print("\nDay 04 Completed Successfully!")
print("=" * 60)