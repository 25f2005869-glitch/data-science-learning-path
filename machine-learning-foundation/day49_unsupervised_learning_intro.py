# ==========================================================
# Day 49 : Introduction to Unsupervised Learning
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 49")
print("=" * 60)

print("\nIntroduction to Unsupervised Learning")
print("-" * 30)

print("""
Unsupervised Learning is a Machine Learning
approach where the model learns patterns
from unlabeled data.

Unlike Supervised Learning:

✓ No Target Variable
✓ No Labels
✓ No Correct Answers

Goal:

Discover hidden structures,
patterns, and relationships
within data.
""")

# ----------------------------------------------------------
# What is Unsupervised Learning?
# ----------------------------------------------------------

print("\nWhat is Unsupervised Learning?")
print("-" * 30)

print("""
In Unsupervised Learning:

Input Data → Available

Output Labels → Not Available

The algorithm tries to find
patterns on its own.

Examples:

✓ Customer Segmentation
✓ Market Basket Analysis
✓ Recommendation Systems
✓ Anomaly Detection
""")

# ----------------------------------------------------------
# Supervised vs Unsupervised Learning
# ----------------------------------------------------------

print("\nSupervised vs Unsupervised Learning")
print("-" * 30)

print("""
Supervised Learning:

✓ Uses Labeled Data
✓ Predicts Outputs

Example:
Study Hours → Marks

Unsupervised Learning:

✓ Uses Unlabeled Data
✓ Finds Hidden Patterns

Example:
Group Similar Students
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

students = [
    [18, 70],
    [19, 75],
    [20, 90],
    [21, 95],
    [18, 72],
    [22, 96]
]

print("Age | Score")

for student in students:
    print(student[0], "|", student[1])

print("""
Notice:

No labels are available.

The algorithm must discover
patterns automatically.
""")

# ----------------------------------------------------------
# Main Types of Unsupervised Learning
# ----------------------------------------------------------

print("\nMain Types")
print("-" * 30)

types = [
    "Clustering",
    "Association Rule Learning",
    "Dimensionality Reduction"
]

for item in types:
    print("✓", item)

# ----------------------------------------------------------
# Clustering
# ----------------------------------------------------------

print("\n1. Clustering")
print("-" * 30)

print("""
Clustering groups similar
data points together.

Goal:

Create clusters where members
inside a cluster are similar.

Examples:

✓ Customer Segmentation
✓ Student Grouping
✓ Image Segmentation
""")

# Example Clusters

cluster_1 = [
    "Student A",
    "Student B",
    "Student C"
]

cluster_2 = [
    "Student D",
    "Student E"
]

print("Cluster 1 =", cluster_1)
print("Cluster 2 =", cluster_2)

# ----------------------------------------------------------
# Association Rule Learning
# ----------------------------------------------------------

print("\n2. Association Rule Learning")
print("-" * 30)

print("""
Association Learning discovers
relationships between items.

Example:

People who buy Bread
often buy Butter.

Applications:

✓ Market Basket Analysis
✓ Product Recommendations
""")

basket = [
    "Bread",
    "Butter",
    "Milk"
]

print("Shopping Basket =", basket)

# ----------------------------------------------------------
# Dimensionality Reduction
# ----------------------------------------------------------

print("\n3. Dimensionality Reduction")
print("-" * 30)

print("""
Real-world datasets may contain
many features.

Dimensionality Reduction:

✓ Removes Redundant Features
✓ Simplifies Data
✓ Speeds Up Computation

Popular Technique:

✓ PCA (Principal Component Analysis)
""")

# ----------------------------------------------------------
# Clustering Example
# ----------------------------------------------------------

print("\nClustering Example")
print("-" * 30)

customers = [
    [25, 20000],
    [28, 22000],
    [45, 80000],
    [48, 85000]
]

print("""
Features:

Age
Income

Possible Clusters:

Cluster 1:
Young Customers

Cluster 2:
High Income Customers
""")

for customer in customers:
    print(customer)

# ----------------------------------------------------------
# Why Unsupervised Learning?
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Works Without Labels",
    "Finds Hidden Patterns",
    "Useful for Exploration",
    "Handles Large Datasets",
    "Discovers Relationships"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Results May Be Difficult To Interpret",
    "No Guaranteed Correct Answer",
    "Evaluation Can Be Challenging",
    "Sensitive To Data Quality"
]

for item in limitations:
    print("✗", item)

# ----------------------------------------------------------
# Real-World Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Customer Segmentation",
    "Fraud Detection",
    "Recommendation Systems",
    "Market Basket Analysis",
    "Image Compression",
    "Social Network Analysis"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Recommendation Systems
# ----------------------------------------------------------

print("\nRecommendation Systems")
print("-" * 30)

print("""
Streaming platforms and
online stores use patterns
in user behavior.

Examples:

✓ Movie Recommendations
✓ Product Recommendations
✓ Music Recommendations
""")

# ----------------------------------------------------------
# Anomaly Detection
# ----------------------------------------------------------

print("\nAnomaly Detection")
print("-" * 30)

print("""
Anomaly Detection identifies
unusual observations.

Applications:

✓ Fraud Detection
✓ Network Security
✓ Equipment Monitoring
""")

transactions = [
    500,
    600,
    700,
    800,
    25000
]

print("Transactions =", transactions)

print("""
25000 may be considered
an anomaly.
""")

# ----------------------------------------------------------
# Popular Algorithms
# ----------------------------------------------------------

print("\nPopular Unsupervised Algorithms")
print("-" * 30)

algorithms = [
    "K-Means Clustering",
    "Hierarchical Clustering",
    "DBSCAN",
    "PCA",
    "Apriori Algorithm"
]

for algorithm in algorithms:
    print("✓", algorithm)

# ----------------------------------------------------------
# Machine Learning Workflow
# ----------------------------------------------------------

print("\nWorkflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Preprocess Data",
    "Select Algorithm",
    "Discover Patterns",
    "Analyze Results",
    "Take Action"
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

scores = [
    45,
    50,
    48,
    92,
    95,
    97
]

print("Scores =", scores)

print("""
Possible Clusters:

Cluster 1:
45, 50, 48

Cluster 2:
92, 95, 97
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

Which type of learning
uses unlabeled data?

Answer:

Unsupervised Learning
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Unsupervised Learning?

2. Does it require labels?

3. What is Clustering?

4. Name one Dimensionality
   Reduction technique.

5. Give one application of
   Unsupervised Learning.
""")

print("""
Answers:

1. Learning from unlabeled data
2. No
3. Grouping similar data points
4. PCA
5. Customer Segmentation
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 49 Summary")
print("-" * 30)

print("""
1. Unsupervised Learning works
   with unlabeled data.

2. It discovers hidden patterns
   and relationships.

3. Main categories:

   ✓ Clustering
   ✓ Association Learning
   ✓ Dimensionality Reduction

4. Popular Algorithms:

   ✓ K-Means
   ✓ Hierarchical Clustering
   ✓ DBSCAN
   ✓ PCA

5. It is widely used for
   customer segmentation,
   recommendation systems,
   and anomaly detection.

6. Unsupervised Learning is
   essential for exploratory
   data analysis.
""")

print("\nDay 49 Completed Successfully!")
print("=" * 60)