# ==========================================================
# Day 50 : K-Means Clustering
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 50")
print("=" * 60)

print("\nK-Means Clustering")
print("-" * 30)

print("""
K-Means is one of the most popular
Unsupervised Learning algorithms.

It is used to group similar data points
into clusters.

Goal:

✓ Find Hidden Patterns
✓ Group Similar Data
✓ Discover Natural Clusters

Applications:

✓ Customer Segmentation
✓ Market Analysis
✓ Image Segmentation
✓ Recommendation Systems
""")

# ----------------------------------------------------------
# What is K-Means?
# ----------------------------------------------------------

print("\nWhat is K-Means?")
print("-" * 30)

print("""
K-Means divides data into K clusters.

K = Number of Clusters

The algorithm groups data points
based on similarity.

Example:

K = 2

Cluster 1
Cluster 2
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
    [48, 85000],
    [50, 90000]
]

print("Age | Income")

for customer in customers:
    print(customer[0], "|", customer[1])

# ----------------------------------------------------------
# Understanding Clusters
# ----------------------------------------------------------

print("\nUnderstanding Clusters")
print("-" * 30)

print("""
Cluster 1:

Young Customers
Lower Income

Cluster 2:

Older Customers
Higher Income

K-Means automatically discovers
these groups.
""")

# ----------------------------------------------------------
# Step 1 : Choose K
# ----------------------------------------------------------

print("\nStep 1 : Choose K")
print("-" * 30)

k = 2

print("Number of Clusters =", k)

print("""
K is chosen before training.

Example:

K = 2
K = 3
K = 4
""")

# ----------------------------------------------------------
# Step 2 : Initialize Centroids
# ----------------------------------------------------------

print("\nStep 2 : Initialize Centroids")
print("-" * 30)

centroid_1 = [25, 20000]
centroid_2 = [50, 90000]

print("Centroid 1 =", centroid_1)
print("Centroid 2 =", centroid_2)

print("""
Centroids are the centers
of clusters.
""")

# ----------------------------------------------------------
# Step 3 : Assign Data Points
# ----------------------------------------------------------

print("\nStep 3 : Assign Data Points")
print("-" * 30)

cluster_1 = [
    [25, 20000],
    [28, 22000],
    [30, 25000]
]

cluster_2 = [
    [45, 80000],
    [48, 85000],
    [50, 90000]
]

print("Cluster 1")

for point in cluster_1:
    print(point)

print("\nCluster 2")

for point in cluster_2:
    print(point)

# ----------------------------------------------------------
# Step 4 : Update Centroids
# ----------------------------------------------------------

print("\nStep 4 : Update Centroids")
print("-" * 30)

new_centroid_1_age = (
    25 + 28 + 30
) / 3

new_centroid_1_income = (
    20000 + 22000 + 25000
) / 3

print("Updated Centroid 1 =",
      [round(new_centroid_1_age, 2),
       round(new_centroid_1_income, 2)])

new_centroid_2_age = (
    45 + 48 + 50
) / 3

new_centroid_2_income = (
    80000 + 85000 + 90000
) / 3

print("Updated Centroid 2 =",
      [round(new_centroid_2_age, 2),
       round(new_centroid_2_income, 2)])

# ----------------------------------------------------------
# Step 5 : Repeat Until Convergence
# ----------------------------------------------------------

print("\nStep 5 : Convergence")
print("-" * 30)

print("""
The algorithm repeatedly:

1. Assigns points to clusters
2. Updates centroids

Until centroids stop changing.

This state is called:

Convergence
""")

# ----------------------------------------------------------
# Distance Calculation
# ----------------------------------------------------------

print("\nDistance Calculation")
print("-" * 30)

print("""
K-Means usually uses
Euclidean Distance.

Formula:

Distance =
√((x2 - x1)^2 + (y2 - y1)^2)
""")

x1 = 25
y1 = 20000

x2 = 28
y2 = 22000

distance = (
    ((x2 - x1) ** 2) +
    ((y2 - y1) ** 2)
) ** 0.5

print("Distance =",
      round(distance, 2))

# ----------------------------------------------------------
# Visual Cluster Example
# ----------------------------------------------------------

print("\nVisual Cluster Example")
print("-" * 30)

print("""
Cluster 1

● ● ●

Cluster 2

▲ ▲ ▲

Each symbol represents
a different cluster.
""")

# ----------------------------------------------------------
# Customer Segmentation Example
# ----------------------------------------------------------

print("\nCustomer Segmentation")
print("-" * 30)

print("""
Businesses use K-Means to group:

✓ High-Value Customers
✓ Medium-Value Customers
✓ Low-Value Customers

This helps targeted marketing.
""")

# ----------------------------------------------------------
# Image Segmentation
# ----------------------------------------------------------

print("\nImage Segmentation")
print("-" * 30)

print("""
K-Means can group similar pixels.

Applications:

✓ Image Compression
✓ Object Detection
✓ Medical Imaging
""")

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Simple and Fast",
    "Easy to Understand",
    "Scales Well",
    "Works on Large Datasets",
    "Useful for Clustering"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Must Choose K",
    "Sensitive to Outliers",
    "Sensitive to Initial Centroids",
    "Works Best for Spherical Clusters"
]

for item in limitations:
    print("✗", item)

# ----------------------------------------------------------
# Choosing K
# ----------------------------------------------------------

print("\nChoosing K")
print("-" * 30)

print("""
Selecting the correct K
is important.

Common Method:

Elbow Method

The elbow point often indicates
the optimal number of clusters.
""")

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Customer Segmentation",
    "Image Segmentation",
    "Fraud Detection",
    "Recommendation Systems",
    "Market Research",
    "Document Clustering"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nK-Means Workflow")
print("-" * 30)

steps = [
    "Choose K",
    "Initialize Centroids",
    "Assign Data Points",
    "Update Centroids",
    "Repeat Process",
    "Obtain Final Clusters"
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
    48,
    50,
    90,
    92,
    95
]

print("Scores =", scores)

print("""
Possible Clusters:

Cluster 1:
45, 48, 50

Cluster 2:
90, 92, 95
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

k = 3

print("""
Question:

What does K represent?

Answer:

Number of Clusters
""")

print("K =", k)

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is K-Means?

2. Is K-Means supervised or
   unsupervised?

3. What does K represent?

4. What is a centroid?

5. Give one application of K-Means.
""")

print("""
Answers:

1. Clustering Algorithm
2. Unsupervised Learning
3. Number of Clusters
4. Center of a Cluster
5. Customer Segmentation
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 50 Summary")
print("-" * 30)

print("""
1. K-Means is a clustering algorithm.

2. It belongs to Unsupervised Learning.

3. K represents the number of clusters.

4. Centroids are cluster centers.

5. The algorithm repeatedly:

   ✓ Assigns Data Points
   ✓ Updates Centroids

6. It stops when convergence occurs.

7. K-Means is widely used in
   customer segmentation,
   image processing,
   and recommendation systems.
""")

print("\nDay 50 Completed Successfully!")
print("=" * 60)