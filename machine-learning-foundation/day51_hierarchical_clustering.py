# ==========================================================
# Day 51 : Hierarchical Clustering
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 51")
print("=" * 60)

print("\nHierarchical Clustering")
print("-" * 30)

print("""
Hierarchical Clustering is an
Unsupervised Learning algorithm
used to group similar data points.

Unlike K-Means:

✓ No Need to Specify K Initially
✓ Produces a Hierarchical Structure
✓ Creates a Tree-Like Representation

Applications:

✓ Customer Segmentation
✓ Biology
✓ Document Clustering
✓ Image Analysis
""")

# ----------------------------------------------------------
# What is Hierarchical Clustering?
# ----------------------------------------------------------

print("\nWhat is Hierarchical Clustering?")
print("-" * 30)

print("""
Hierarchical Clustering creates
a hierarchy of clusters.

The result is represented using
a tree-like structure called:

Dendrogram

The algorithm groups similar
data points step by step.
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

customers = [
    [25, 20000],
    [28, 22000],
    [30, 25000],
    [45, 80000],
    [48, 85000]
]

print("Age | Income")

for customer in customers:
    print(customer[0], "|", customer[1])

# ----------------------------------------------------------
# Types of Hierarchical Clustering
# ----------------------------------------------------------

print("\nTypes of Hierarchical Clustering")
print("-" * 30)

print("""
1. Agglomerative Clustering
2. Divisive Clustering
""")

# ----------------------------------------------------------
# Agglomerative Clustering
# ----------------------------------------------------------

print("\n1. Agglomerative Clustering")
print("-" * 30)

print("""
Agglomerative means:

Bottom-Up Approach

Initially:

Each data point is its own cluster.

Then:

Nearest clusters are merged
step by step until only one
cluster remains.
""")

# Example

clusters = [
    ["A"],
    ["B"],
    ["C"],
    ["D"]
]

print("Initial Clusters =", clusters)

# ----------------------------------------------------------
# Agglomerative Process
# ----------------------------------------------------------

print("\nAgglomerative Process")
print("-" * 30)

print("""
Step 1:

[A] [B] [C] [D]

Step 2:

[A B] [C] [D]

Step 3:

[A B] [C D]

Step 4:

[A B C D]

Single Final Cluster
""")

# ----------------------------------------------------------
# Divisive Clustering
# ----------------------------------------------------------

print("\n2. Divisive Clustering")
print("-" * 30)

print("""
Divisive means:

Top-Down Approach

Initially:

All data points belong
to one cluster.

Then:

Clusters are split
until individual points remain.
""")

# ----------------------------------------------------------
# Dendrogram
# ----------------------------------------------------------

print("\nDendrogram")
print("-" * 30)

print("""
A Dendrogram is a tree diagram
used to visualize clustering.

Example:

        ABCD
       /    \\
     AB      CD
    /  \\    /  \\
   A    B  C    D

The height indicates
cluster similarity.
""")

# ----------------------------------------------------------
# Why Dendrogram?
# ----------------------------------------------------------

print("\nWhy Dendrogram?")
print("-" * 30)

print("""
Dendrogram helps:

✓ Visualize Clusters
✓ Understand Relationships
✓ Determine Optimal Clusters
✓ Analyze Similarity
""")

# ----------------------------------------------------------
# Distance Matrix
# ----------------------------------------------------------

print("\nDistance Matrix")
print("-" * 30)

print("""
Hierarchical Clustering uses
distance calculations to determine
similarity between points.

Smaller Distance:

✓ More Similar

Larger Distance:

✗ Less Similar
""")

# Example Distance Matrix

distance_matrix = [
    [0, 2, 6, 10],
    [2, 0, 5, 9],
    [6, 5, 0, 4],
    [10, 9, 4, 0]
]

for row in distance_matrix:
    print(row)

# ----------------------------------------------------------
# Linkage Methods
# ----------------------------------------------------------

print("\nLinkage Methods")
print("-" * 30)

print("""
Linkage determines how
distance between clusters
is calculated.

Common Methods:

✓ Single Linkage
✓ Complete Linkage
✓ Average Linkage
✓ Ward Linkage
""")

# ----------------------------------------------------------
# Single Linkage
# ----------------------------------------------------------

print("\nSingle Linkage")
print("-" * 30)

print("""
Uses the minimum distance
between two clusters.

Advantage:

✓ Can detect irregular shapes

Limitation:

✗ Sensitive to noise
""")

# ----------------------------------------------------------
# Complete Linkage
# ----------------------------------------------------------

print("\nComplete Linkage")
print("-" * 30)

print("""
Uses the maximum distance
between two clusters.

Advantages:

✓ Produces compact clusters

Limitation:

✗ Sensitive to outliers
""")

# ----------------------------------------------------------
# Average Linkage
# ----------------------------------------------------------

print("\nAverage Linkage")
print("-" * 30)

print("""
Uses the average distance
between cluster members.

Advantages:

✓ Balanced Approach
✓ Stable Clustering
""")

# ----------------------------------------------------------
# Ward Linkage
# ----------------------------------------------------------

print("\nWard Linkage")
print("-" * 30)

print("""
Ward's Method minimizes
within-cluster variance.

Advantages:

✓ High Quality Clusters
✓ Popular Choice
""")

# ----------------------------------------------------------
# Customer Segmentation Example
# ----------------------------------------------------------

print("\nCustomer Segmentation")
print("-" * 30)

print("""
Hierarchical Clustering can group:

Cluster 1:
Young Customers

Cluster 2:
High Income Customers

Cluster 3:
Premium Customers
""")

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "No Need to Specify K Initially",
    "Produces Dendrogram",
    "Easy Visualization",
    "Works with Small Datasets",
    "Flexible Linkage Methods"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Slow for Large Datasets",
    "High Memory Usage",
    "Sensitive to Noise",
    "Computationally Expensive"
]

for item in limitations:
    print("✗", item)

# ----------------------------------------------------------
# Hierarchical vs K-Means
# ----------------------------------------------------------

print("\nHierarchical vs K-Means")
print("-" * 30)

print("""
Hierarchical Clustering:

✓ Dendrogram Available
✓ No Initial K Required

K-Means:

✓ Faster
✓ Better for Large Data

Both are Clustering Algorithms.
""")

# ----------------------------------------------------------
# Real World Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Customer Segmentation",
    "Gene Analysis",
    "Document Clustering",
    "Image Analysis",
    "Social Network Analysis",
    "Market Research"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nHierarchical Clustering Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Compute Distances",
    "Create Clusters",
    "Merge or Split Clusters",
    "Build Dendrogram",
    "Analyze Final Clusters"
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

students = [
    45,
    48,
    50,
    92,
    95,
    97
]

print("Student Scores =", students)

print("""
Possible Clusters:

Cluster 1:
45, 48, 50

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

What is the tree-like diagram
used in Hierarchical Clustering?

Answer:

Dendrogram
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Hierarchical Clustering?

2. Is it supervised or unsupervised?

3. What is a Dendrogram?

4. Name one linkage method.

5. What is the difference between
   Agglomerative and Divisive Clustering?
""")

print("""
Answers:

1. Clustering Algorithm
2. Unsupervised Learning
3. Tree-like Cluster Diagram
4. Single Linkage
5. Bottom-Up vs Top-Down
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 51 Summary")
print("-" * 30)

print("""
1. Hierarchical Clustering is an
   Unsupervised Learning algorithm.

2. It creates a hierarchy of clusters.

3. Two major approaches:

   ✓ Agglomerative
   ✓ Divisive

4. Dendrogram visualizes
   cluster relationships.

5. Common linkage methods:

   ✓ Single
   ✓ Complete
   ✓ Average
   ✓ Ward

6. No initial K is required.

7. It is useful for clustering
   and exploratory data analysis.
""")

print("\nDay 51 Completed Successfully!")
print("=" * 60)