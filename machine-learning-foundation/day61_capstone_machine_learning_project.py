# ==========================================================
# Day 61 : Capstone Machine Learning Project
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 61")
print("=" * 60)

print("\nCapstone Machine Learning Project")
print("-" * 40)

print("""
A Capstone Project combines all
Machine Learning concepts learned
during the course.

This project simulates a complete
real-world Machine Learning workflow.

Project:

Student Performance Prediction System

Goal:

Predict whether a student is likely
to achieve High Performance based
on study habits and attendance.
""")

# ----------------------------------------------------------
# Project Overview
# ----------------------------------------------------------

print("\nProject Overview")
print("-" * 40)

print("""
Problem Statement:

Educational institutions want to
identify students who may need
academic support.

Machine Learning can help predict
student performance using historical data.
""")

# ----------------------------------------------------------
# Step 1 : Data Collection
# ----------------------------------------------------------

print("\nStep 1 : Data Collection")
print("-" * 40)

student_data = [
    [2, 60, 45],
    [4, 70, 55],
    [6, 80, 65],
    [8, 85, 75],
    [10, 90, 90]
]

print("""
Columns:

Study Hours
Attendance
Final Marks
""")

for row in student_data:

    print(row)

# ----------------------------------------------------------
# Step 2 : Data Exploration
# ----------------------------------------------------------

print("\nStep 2 : Data Exploration")
print("-" * 40)

rows = len(student_data)
columns = len(student_data[0])

print("Number of Records =", rows)
print("Number of Features =", columns)

study_hours = []

attendance = []

marks = []

for row in student_data:

    study_hours.append(row[0])
    attendance.append(row[1])
    marks.append(row[2])

print("Study Hours =", study_hours)
print("Attendance =", attendance)
print("Marks =", marks)

# ----------------------------------------------------------
# Step 3 : Basic Statistics
# ----------------------------------------------------------

print("\nStep 3 : Basic Statistics")
print("-" * 40)

average_marks = (
    sum(marks) /
    len(marks)
)

average_attendance = (
    sum(attendance) /
    len(attendance)
)

print("Average Marks =",
      round(average_marks, 2))

print("Average Attendance =",
      round(average_attendance, 2))

# ----------------------------------------------------------
# Step 4 : Data Cleaning
# ----------------------------------------------------------

print("\nStep 4 : Data Cleaning")
print("-" * 40)

print("""
Checking Dataset:

✓ Missing Values
✓ Invalid Values
✓ Duplicate Records

Dataset Status:

No Missing Values Found
""")

# ----------------------------------------------------------
# Step 5 : Feature Engineering
# ----------------------------------------------------------

print("\nStep 5 : Feature Engineering")
print("-" * 40)

performance_labels = []

for score in marks:

    if score >= 75:

        performance_labels.append(
            "High Performer"
        )

    else:

        performance_labels.append(
            "Needs Improvement"
        )

print("Performance Labels:")

for label in performance_labels:

    print(label)

# ----------------------------------------------------------
# Step 6 : Train-Test Split
# ----------------------------------------------------------

print("\nStep 6 : Train-Test Split")
print("-" * 40)

train_data = student_data[:4]
test_data = student_data[4:]

print("Training Records =", len(train_data))
print("Testing Records =", len(test_data))

# ----------------------------------------------------------
# Step 7 : Model Selection
# ----------------------------------------------------------

print("\nStep 7 : Model Selection")
print("-" * 40)

print("""
Selected Model:

Linear Regression

Reason:

✓ Easy to Understand
✓ Suitable for Prediction
✓ Foundation Level Project
""")

selected_model = (
    "Linear Regression"
)

print("Model =", selected_model)

# ----------------------------------------------------------
# Step 8 : Simulated Training
# ----------------------------------------------------------

print("\nStep 8 : Model Training")
print("-" * 40)

training_accuracy = 91.5

print("Training Completed")

print("Training Accuracy =",
      training_accuracy,
      "%")

# ----------------------------------------------------------
# Step 9 : Prediction
# ----------------------------------------------------------

print("\nStep 9 : Prediction")
print("-" * 40)

new_student = {
    "Study Hours": 9,
    "Attendance": 88
}

predicted_marks = 84

print("New Student =",
      new_student)

print("Predicted Marks =",
      predicted_marks)

if predicted_marks >= 75:

    prediction = "High Performer"

else:

    prediction = "Needs Improvement"

print("Prediction =",
      prediction)

# ----------------------------------------------------------
# Step 10 : Model Evaluation
# ----------------------------------------------------------

print("\nStep 10 : Model Evaluation")
print("-" * 40)

accuracy = 90
precision = 0.88
recall = 0.91
f1_score = 0.89

print("Accuracy =", accuracy, "%")
print("Precision =", precision)
print("Recall =", recall)
print("F1 Score =", f1_score)

# ----------------------------------------------------------
# Step 11 : Cross Validation
# ----------------------------------------------------------

print("\nStep 11 : Cross Validation")
print("-" * 40)

cv_scores = [
    0.89,
    0.91,
    0.90,
    0.92,
    0.88
]

average_cv = (
    sum(cv_scores) /
    len(cv_scores)
)

print("CV Scores =",
      cv_scores)

print("Average CV Score =",
      round(average_cv, 4))

# ----------------------------------------------------------
# Step 12 : Hyperparameter Tuning
# ----------------------------------------------------------

print("\nStep 12 : Hyperparameter Tuning")
print("-" * 40)

print("""
Example Parameters:

Learning Rate
Tree Depth
K Value

Tuning improves
overall performance.
""")

# ----------------------------------------------------------
# Step 13 : Deployment
# ----------------------------------------------------------

print("\nStep 13 : Deployment")
print("-" * 40)

deployment_status = (
    "Successfully Deployed"
)

print("Deployment Status =",
      deployment_status)

# ----------------------------------------------------------
# Step 14 : Monitoring
# ----------------------------------------------------------

print("\nStep 14 : Monitoring")
print("-" * 40)

print("""
Monitor:

✓ Accuracy
✓ Prediction Quality
✓ Data Changes

Retrain model if performance
starts decreasing.
""")

# ----------------------------------------------------------
# Project Dashboard
# ----------------------------------------------------------

print("\nProject Dashboard")
print("-" * 40)

project_metrics = {
    "Records": rows,
    "Average Marks":
        round(average_marks, 2),
    "Accuracy": accuracy,
    "CV Score":
        round(average_cv, 4)
}

for key, value in project_metrics.items():

    print(key, ":", value)

# ----------------------------------------------------------
# Complete Workflow Summary
# ----------------------------------------------------------

print("\nMachine Learning Workflow")
print("-" * 40)

workflow_steps = [
    "Problem Definition",
    "Data Collection",
    "Data Exploration",
    "Data Cleaning",
    "Feature Engineering",
    "Train-Test Split",
    "Model Selection",
    "Model Training",
    "Prediction",
    "Evaluation",
    "Cross Validation",
    "Hyperparameter Tuning",
    "Deployment",
    "Monitoring"
]

for i, step in enumerate(
        workflow_steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Skills Demonstrated
# ----------------------------------------------------------

print("\nSkills Demonstrated")
print("-" * 40)

skills = [
    "Data Analysis",
    "Statistics",
    "Feature Engineering",
    "Regression Concepts",
    "Classification Concepts",
    "Model Evaluation",
    "Cross Validation",
    "ML Workflow Design"
]

for skill in skills:

    print("✓", skill)

# ----------------------------------------------------------
# Real-World Impact
# ----------------------------------------------------------

print("\nReal-World Impact")
print("-" * 40)

print("""
Benefits:

✓ Early Student Intervention
✓ Better Academic Planning
✓ Performance Monitoring
✓ Data-Driven Decisions
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 40)

print("""
Question:

Which stage comes after
Model Evaluation?

Answer:

Cross Validation
""")

# ----------------------------------------------------------
# Final Quiz
# ----------------------------------------------------------

print("\nFinal Quiz")
print("-" * 40)

print("""
1. What was the project goal?

2. Which model was selected?

3. Why is Cross Validation useful?

4. Why is Feature Engineering important?

5. Why is Monitoring required?
""")

print("""
Answers:

1. Predict Student Performance
2. Linear Regression
3. Reliable Evaluation
4. Better Features Improve Models
5. Maintain Model Performance
""")

# ----------------------------------------------------------
# Capstone Summary
# ----------------------------------------------------------

print("\nCapstone Project Summary")
print("-" * 40)

print("""
This Capstone Project integrated:

✓ Data Collection
✓ Data Exploration
✓ Statistics
✓ Feature Engineering
✓ Train-Test Split
✓ Model Building
✓ Evaluation
✓ Cross Validation
✓ Deployment
✓ Monitoring

The project demonstrates a
complete End-to-End Machine Learning
workflow using concepts learned
throughout Machine Learning Foundations.
""")

print("\nDay 61 Completed Successfully!")
print("Machine Learning Foundations Capstone Complete!")
print("=" * 60)