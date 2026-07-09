# ==========================================================
# Day 24 : Correlation
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 24")
print("=" * 60)

print("\nCorrelation")
print("-" * 30)

print("""
Correlation measures the relationship
between two variables.

It helps answer questions such as:

✓ Does study time affect marks?
✓ Does income affect spending?
✓ Does advertising affect sales?

Correlation is widely used in:

✓ Data Analysis
✓ Feature Selection
✓ Machine Learning
✓ Statistics
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]

print("Study Hours =", study_hours)
print("Marks       =", marks)

# ----------------------------------------------------------
# Mean Calculation
# ----------------------------------------------------------

print("\nStep 1 : Calculate Means")
print("-" * 30)

mean_x = sum(study_hours) / len(study_hours)
mean_y = sum(marks) / len(marks)

print("Mean Study Hours =", mean_x)
print("Mean Marks       =", mean_y)

# ----------------------------------------------------------
# Covariance Calculation
# ----------------------------------------------------------

print("\nStep 2 : Covariance")
print("-" * 30)

covariance = 0

for x, y in zip(study_hours, marks):
    covariance += (x - mean_x) * (y - mean_y)

covariance = covariance / len(study_hours)

print("Covariance =", round(covariance, 2))

# ----------------------------------------------------------
# Standard Deviations
# ----------------------------------------------------------

print("\nStep 3 : Standard Deviations")
print("-" * 30)

variance_x = sum(
    (x - mean_x) ** 2
    for x in study_hours
) / len(study_hours)

variance_y = sum(
    (y - mean_y) ** 2
    for y in marks
) / len(marks)

std_x = variance_x ** 0.5
std_y = variance_y ** 0.5

print("SD of Study Hours =", round(std_x, 2))
print("SD of Marks       =", round(std_y, 2))

# ----------------------------------------------------------
# Correlation Coefficient
# ----------------------------------------------------------

print("\nStep 4 : Correlation Coefficient")
print("-" * 30)

correlation = covariance / (std_x * std_y)

print("Correlation =", round(correlation, 4))

# ----------------------------------------------------------
# Interpretation
# ----------------------------------------------------------

print("\nInterpretation")
print("-" * 30)

print("""
Correlation Range:

+1  → Perfect Positive Correlation
 0  → No Correlation
-1  → Perfect Negative Correlation
""")

if correlation > 0:
    print("Positive Correlation Detected")
elif correlation < 0:
    print("Negative Correlation Detected")
else:
    print("No Correlation")

# ----------------------------------------------------------
# Positive Correlation Example
# ----------------------------------------------------------

print("\nPositive Correlation Example")
print("-" * 30)

hours = [1, 2, 3, 4, 5]
scores = [20, 40, 60, 80, 100]

print("Hours  =", hours)
print("Scores =", scores)

print("""
As study hours increase,
scores also increase.

Positive Correlation
""")

# ----------------------------------------------------------
# Negative Correlation Example
# ----------------------------------------------------------

print("\nNegative Correlation Example")
print("-" * 30)

speed = [20, 30, 40, 50, 60]
time_taken = [30, 25, 20, 15, 10]

print("Speed      =", speed)
print("Time Taken =", time_taken)

print("""
As speed increases,
time decreases.

Negative Correlation
""")

# ----------------------------------------------------------
# No Correlation Example
# ----------------------------------------------------------

print("\nNo Correlation Example")
print("-" * 30)

shoe_size = [6, 8, 7, 10, 9]
exam_marks = [70, 40, 90, 60, 80]

print("Shoe Size  =", shoe_size)
print("Exam Marks =", exam_marks)

print("""
No meaningful relationship.

Near Zero Correlation
""")

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nCorrelation in Machine Learning")
print("-" * 30)

applications = [
    "Feature Selection",
    "Data Analysis",
    "Exploratory Data Analysis",
    "Regression Models",
    "Predictive Analytics",
    "Data Preprocessing"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Student Dataset Example
# ----------------------------------------------------------

print("\nStudent Dataset Example")
print("-" * 30)

attendance = [60, 70, 80, 90, 100]
grades = [55, 65, 75, 85, 95]

print("Attendance =", attendance)
print("Grades     =", grades)

print("""
Higher Attendance
→ Higher Grades

Positive Correlation
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

advertising = [10, 20, 30, 40, 50]
sales = [100, 150, 200, 250, 300]

print("Advertising =", advertising)
print("Sales       =", sales)

print("""
More Advertising
→ More Sales

Positive Correlation
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

temperature = [20, 22, 24, 26, 28]
ice_cream_sales = [100, 120, 140, 170, 190]

print("Temperature     =", temperature)
print("Ice Cream Sales =", ice_cream_sales)

print("""
Question:
Positive, Negative, or No Correlation?

Answer:
Positive Correlation
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Correlation?

2. What does +1 indicate?

3. What does -1 indicate?

4. What does 0 indicate?

5. Why is Correlation useful in ML?
""")

print("""
Answers:

1. Relationship between variables
2. Perfect Positive Correlation
3. Perfect Negative Correlation
4. No Correlation
5. Helps identify useful features
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 24 Summary")
print("-" * 30)

print("""
1. Correlation measures relationships.
2. Values range from -1 to +1.
3. Positive correlation means variables
   move in the same direction.
4. Negative correlation means variables
   move in opposite directions.
5. Zero correlation means no relationship.
6. Correlation is important for
   feature selection and ML analysis.
""")

print("\nDay 24 Completed Successfully!")
print("=" * 60)