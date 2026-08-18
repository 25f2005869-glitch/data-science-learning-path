# ==========================================================
# Day 45 : Naive Bayes Algorithm
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 45")
print("=" * 60)

print("\nNaive Bayes Algorithm")
print("-" * 30)

print("""
Naive Bayes is a Supervised Learning
algorithm mainly used for Classification.

It is based on Bayes' Theorem from
Probability Theory.

Applications:

✓ Spam Detection
✓ Sentiment Analysis
✓ Disease Prediction
✓ Document Classification
✓ Recommendation Systems

The word 'Naive' means the algorithm
assumes all features are independent.
""")

# ----------------------------------------------------------
# What is Naive Bayes?
# ----------------------------------------------------------

print("\nWhat is Naive Bayes?")
print("-" * 30)

print("""
Naive Bayes predicts the probability
of a class based on input features.

It chooses the class with the
highest probability.

Example:

Email → Spam or Not Spam

The algorithm calculates:

P(Spam | Email Features)
P(Not Spam | Email Features)

The larger probability wins.
""")

# ----------------------------------------------------------
# Bayes Theorem
# ----------------------------------------------------------

print("\nBayes Theorem")
print("-" * 30)

print("""
Formula:

P(A|B) =
P(B|A) × P(A)
----------------
     P(B)

Where:

P(A|B) = Posterior Probability
P(B|A) = Likelihood
P(A)   = Prior Probability
P(B)   = Evidence
""")

# ----------------------------------------------------------
# Example Probabilities
# ----------------------------------------------------------

print("\nProbability Example")
print("-" * 30)

prob_spam = 0.40
prob_offer_given_spam = 0.80
prob_offer = 0.50

posterior = (
    prob_offer_given_spam *
    prob_spam
) / prob_offer

print("P(Spam) =", prob_spam)
print("P(Offer | Spam) =", prob_offer_given_spam)
print("P(Offer) =", prob_offer)

print("P(Spam | Offer) =",
      round(posterior, 2))

# ----------------------------------------------------------
# Understanding Independence
# ----------------------------------------------------------

print("\nFeature Independence")
print("-" * 30)

print("""
Naive Bayes assumes features
are independent.

Example:

Email Features:

✓ Contains Offer
✓ Contains Money
✓ Contains Free

The algorithm assumes each feature
contributes independently.
""")

# ----------------------------------------------------------
# Classification Example
# ----------------------------------------------------------

print("\nSpam Detection Example")
print("-" * 30)

emails = [
    "Free Gift",
    "Meeting Schedule",
    "Win Money",
    "Project Update"
]

labels = [
    "Spam",
    "Not Spam",
    "Spam",
    "Not Spam"
]

for email, label in zip(emails, labels):

    print(email, "→", label)

# ----------------------------------------------------------
# Training Dataset
# ----------------------------------------------------------

print("\nTraining Dataset")
print("-" * 30)

training_data = [
    ["Offer", "Spam"],
    ["Money", "Spam"],
    ["Meeting", "Not Spam"],
    ["Project", "Not Spam"]
]

for row in training_data:

    print(row)

# ----------------------------------------------------------
# Prior Probability
# ----------------------------------------------------------

print("\nPrior Probability")
print("-" * 30)

spam_count = 2
not_spam_count = 2
total_emails = 4

prior_spam = spam_count / total_emails
prior_not_spam = not_spam_count / total_emails

print("P(Spam) =", prior_spam)
print("P(Not Spam) =", prior_not_spam)

# ----------------------------------------------------------
# Likelihood
# ----------------------------------------------------------

print("\nLikelihood")
print("-" * 30)

print("""
Likelihood measures the probability
of observing a feature given a class.

Example:

P(Offer | Spam)

How often does the word
'Offer' appear in Spam emails?
""")

likelihood = 1 / 2

print("Example Likelihood =",
      likelihood)

# ----------------------------------------------------------
# Posterior Probability
# ----------------------------------------------------------

print("\nPosterior Probability")
print("-" * 30)

posterior_spam = 0.75
posterior_not_spam = 0.25

print("P(Spam | Email) =",
      posterior_spam)

print("P(Not Spam | Email) =",
      posterior_not_spam)

if posterior_spam > posterior_not_spam:

    prediction = "Spam"

else:

    prediction = "Not Spam"

print("Prediction =", prediction)

# ----------------------------------------------------------
# Types of Naive Bayes
# ----------------------------------------------------------

print("\nTypes of Naive Bayes")
print("-" * 30)

types = [
    "Gaussian Naive Bayes",
    "Multinomial Naive Bayes",
    "Bernoulli Naive Bayes"
]

for item in types:

    print("✓", item)

# ----------------------------------------------------------
# Gaussian Naive Bayes
# ----------------------------------------------------------

print("\nGaussian Naive Bayes")
print("-" * 30)

print("""
Used for continuous numerical data.

Examples:

✓ Height
✓ Weight
✓ Salary
✓ Temperature
""")

# ----------------------------------------------------------
# Multinomial Naive Bayes
# ----------------------------------------------------------

print("\nMultinomial Naive Bayes")
print("-" * 30)

print("""
Used for text classification.

Examples:

✓ Email Classification
✓ News Classification
✓ Document Analysis
""")

# ----------------------------------------------------------
# Bernoulli Naive Bayes
# ----------------------------------------------------------

print("\nBernoulli Naive Bayes")
print("-" * 30)

print("""
Used for binary features.

Examples:

Word Present?
✓ Yes
✓ No
""")

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Simple to Implement",
    "Fast Training",
    "Fast Prediction",
    "Works Well with Text Data",
    "Effective on Small Datasets"
]

for item in advantages:

    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "Strong Independence Assumption",
    "May Miss Feature Relationships",
    "Performance Depends on Data Quality"
]

for item in limitations:

    print("✗", item)

# ----------------------------------------------------------
# Disease Prediction Example
# ----------------------------------------------------------

print("\nDisease Prediction")
print("-" * 30)

symptoms = [
    "Fever",
    "Cough",
    "Fatigue"
]

print("Symptoms =", symptoms)

probability_disease = 0.85

print("Disease Probability =",
      probability_disease)

# ----------------------------------------------------------
# Sentiment Analysis Example
# ----------------------------------------------------------

print("\nSentiment Analysis")
print("-" * 30)

review = "Excellent Product"

predicted_sentiment = "Positive"

print("Review =", review)
print("Sentiment =",
      predicted_sentiment)

# ----------------------------------------------------------
# Machine Learning Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Spam Detection",
    "Sentiment Analysis",
    "Medical Diagnosis",
    "News Classification",
    "Recommendation Systems",
    "Document Categorization"
]

for app in applications:

    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nNaive Bayes Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Calculate Priors",
    "Calculate Likelihoods",
    "Apply Bayes Theorem",
    "Compute Posterior Probabilities",
    "Predict Class"
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

spam_probability = 0.82

if spam_probability > 0.5:

    email_type = "Spam"

else:

    email_type = "Not Spam"

print("Email Type =", email_type)

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

prior = 0.4
likelihood = 0.8
evidence = 0.5

posterior = (
    prior *
    likelihood
) / evidence

print("Posterior Probability =",
      round(posterior, 2))

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Naive Bayes?

2. Which theorem is it based on?

3. What does 'Naive' mean?

4. Name one type of Naive Bayes.

5. Give one application.
""")

print("""
Answers:

1. Classification Algorithm
2. Bayes Theorem
3. Features are assumed independent
4. Gaussian Naive Bayes
5. Spam Detection
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 45 Summary")
print("-" * 30)

print("""
1. Naive Bayes is a Supervised
   Learning Classification algorithm.

2. It is based on Bayes Theorem.

3. It predicts probabilities
   for different classes.

4. Features are assumed
   to be independent.

5. Common Types:

   ✓ Gaussian
   ✓ Multinomial
   ✓ Bernoulli

6. It is widely used in
   text classification tasks.

7. Naive Bayes is simple,
   fast, and effective.
""")

print("\nDay 45 Completed Successfully!")
print("=" * 60)