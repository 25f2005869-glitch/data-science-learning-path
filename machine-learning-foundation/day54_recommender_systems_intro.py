# ==========================================================
# Day 54 : Recommender Systems Introduction
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 54")
print("=" * 60)

print("\nIntroduction to Recommender Systems")
print("-" * 30)

print("""
Recommender Systems are Machine Learning
systems that suggest relevant items
to users based on their preferences
and behavior.

Goal:

✓ Personalization
✓ Better User Experience
✓ Increased Engagement
✓ Better Decision Making

Examples:

✓ Netflix Movie Recommendations
✓ Amazon Product Suggestions
✓ YouTube Video Recommendations
✓ Spotify Music Recommendations
""")

# ----------------------------------------------------------
# What is a Recommender System?
# ----------------------------------------------------------

print("\nWhat is a Recommender System?")
print("-" * 30)

print("""
A Recommender System predicts
what a user may like.

Input:

✓ User Information
✓ Preferences
✓ Past Behavior

Output:

Recommended Items

The system learns patterns and
suggests relevant content.
""")

# ----------------------------------------------------------
# Why Recommender Systems?
# ----------------------------------------------------------

print("\nWhy Recommender Systems?")
print("-" * 30)

print("""
Modern platforms contain
millions of items.

Users cannot manually search
everything.

Recommender Systems help users:

✓ Discover New Content
✓ Save Time
✓ Improve Experience
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

users = [
    "User A",
    "User B",
    "User C"
]

movies = [
    "Movie 1",
    "Movie 2",
    "Movie 3"
]

print("Users =", users)
print("Movies =", movies)

# ----------------------------------------------------------
# Types of Recommender Systems
# ----------------------------------------------------------

print("\nTypes of Recommender Systems")
print("-" * 30)

types = [
    "Content-Based Filtering",
    "Collaborative Filtering",
    "Hybrid Recommendation"
]

for item in types:
    print("✓", item)

# ----------------------------------------------------------
# Content-Based Filtering
# ----------------------------------------------------------

print("\n1. Content-Based Filtering")
print("-" * 30)

print("""
Content-Based Filtering recommends
items similar to those a user
already likes.

Example:

User likes:

✓ Action Movie A
✓ Action Movie B

Recommendation:

✓ Action Movie C

The recommendation is based on
item characteristics.
""")

# ----------------------------------------------------------
# Example Content Features
# ----------------------------------------------------------

print("\nMovie Features")
print("-" * 30)

movie_features = {
    "Movie A": "Action",
    "Movie B": "Action",
    "Movie C": "Action",
    "Movie D": "Comedy"
}

for movie, genre in movie_features.items():

    print(movie, "→", genre)

# ----------------------------------------------------------
# Collaborative Filtering
# ----------------------------------------------------------

print("\n2. Collaborative Filtering")
print("-" * 30)

print("""
Collaborative Filtering recommends
items based on user behavior.

Idea:

People with similar interests
often like similar items.

Example:

User A and User B like
similar movies.

If User B likes a new movie,
it may be recommended to User A.
""")

# ----------------------------------------------------------
# User Rating Matrix
# ----------------------------------------------------------

print("\nUser Rating Matrix")
print("-" * 30)

ratings = [
    [5, 4, 0],
    [5, 5, 4],
    [1, 2, 5]
]

print("""
Rows    → Users
Columns → Movies

0 means not rated.
""")

for row in ratings:
    print(row)

# ----------------------------------------------------------
# Hybrid Recommendation
# ----------------------------------------------------------

print("\n3. Hybrid Recommendation")
print("-" * 30)

print("""
Hybrid Systems combine:

✓ Content-Based Filtering
✓ Collaborative Filtering

Advantages:

✓ Better Accuracy
✓ Better Personalization

Used by:

✓ Netflix
✓ Amazon
✓ Spotify
""")

# ----------------------------------------------------------
# Recommendation Workflow
# ----------------------------------------------------------

print("\nRecommendation Workflow")
print("-" * 30)

steps = [
    "Collect User Data",
    "Analyze Preferences",
    "Build Recommendation Model",
    "Generate Recommendations",
    "Show Recommendations",
    "Collect Feedback"
]

for i, step in enumerate(
        steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Similarity Concept
# ----------------------------------------------------------

print("\nSimilarity")
print("-" * 30)

print("""
Recommendations often rely
on similarity.

Higher Similarity:

✓ More Relevant Recommendation

Lower Similarity:

✗ Less Relevant Recommendation
""")

similarity_score = 0.92

print("Similarity Score =",
      similarity_score)

# ----------------------------------------------------------
# Netflix Example
# ----------------------------------------------------------

print("\nNetflix Example")
print("-" * 30)

print("""
User Watches:

✓ Science Fiction Movies
✓ Space Exploration Movies

Possible Recommendation:

✓ Interstellar
✓ The Martian
✓ Gravity
""")

# ----------------------------------------------------------
# Amazon Example
# ----------------------------------------------------------

print("\nAmazon Example")
print("-" * 30)

print("""
Customers who bought:

Laptop

also bought:

✓ Mouse
✓ Keyboard
✓ Laptop Bag

This is recommendation logic.
""")

# ----------------------------------------------------------
# Spotify Example
# ----------------------------------------------------------

print("\nSpotify Example")
print("-" * 30)

print("""
User Listens To:

✓ Classical Music

Possible Recommendations:

✓ Similar Artists
✓ Similar Albums
✓ Similar Songs
""")

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Personalized Experience",
    "Improved User Satisfaction",
    "Increased Engagement",
    "Higher Sales",
    "Better Content Discovery"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Challenges
# ----------------------------------------------------------

print("\nChallenges")
print("-" * 30)

challenges = [
    "Cold Start Problem",
    "Data Sparsity",
    "Scalability Issues",
    "Privacy Concerns"
]

for item in challenges:
    print("✗", item)

# ----------------------------------------------------------
# Cold Start Problem
# ----------------------------------------------------------

print("\nCold Start Problem")
print("-" * 30)

print("""
Occurs when:

✓ New User Joins
✓ New Item Added

The system has little information
for making recommendations.
""")

# ----------------------------------------------------------
# Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Netflix",
    "Amazon",
    "Spotify",
    "YouTube",
    "E-Commerce",
    "Online Learning Platforms"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Machine Learning Connection
# ----------------------------------------------------------

print("\nMachine Learning Connection")
print("-" * 30)

print("""
Recommender Systems use:

✓ Machine Learning
✓ Data Mining
✓ Statistics
✓ User Behavior Analysis

to generate recommendations.
""")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

liked_books = [
    "Python Basics",
    "Data Science Handbook"
]

recommended_book = (
    "Machine Learning Essentials"
)

print("Liked Books =",
      liked_books)

print("Recommended Book =",
      recommended_book)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

Which recommendation method
uses similar users?

Answer:

Collaborative Filtering
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is a Recommender System?

2. Name two recommendation methods.

3. What is Collaborative Filtering?

4. What is Content-Based Filtering?

5. What is the Cold Start Problem?
""")

print("""
Answers:

1. System that suggests items
2. Content-Based and Collaborative
3. Uses similar users
4. Uses item similarity
5. Lack of information for new users/items
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 54 Summary")
print("-" * 30)

print("""
1. Recommender Systems suggest
   relevant items to users.

2. Main Types:

   ✓ Content-Based Filtering
   ✓ Collaborative Filtering
   ✓ Hybrid Systems

3. Recommendations improve
   personalization and engagement.

4. Similarity is a key concept.

5. Common applications:

   ✓ Netflix
   ✓ Amazon
   ✓ Spotify
   ✓ YouTube

6. Challenges include:

   ✓ Cold Start Problem
   ✓ Data Sparsity

7. Recommender Systems are one of
   the most important applications
   of Machine Learning.
""")

print("\nDay 54 Completed Successfully!")
print("=" * 60)