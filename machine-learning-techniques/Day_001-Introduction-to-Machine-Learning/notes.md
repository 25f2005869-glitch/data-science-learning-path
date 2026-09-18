![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Programme](https://img.shields.io/badge/Programme-Diploma%20Level-blue?style=for-the-badge)
![Subject](https://img.shields.io/badge/Subject-MLT-green?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Introduction%20to%20Machine%20Learning-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-001-purple?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-Saloni%20Tiwari-pink?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Learning-success?style=for-the-badge)
![Tools](https://img.shields.io/badge/Tools-Concepts%20%7C%20Python-lightgrey?style=for-the-badge)

# Introduction to Machine Learning

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Subject:** Machine Learning Techniques (MLT)  
**Day:** 001  
**Topic:** Introduction to Machine Learning

---

## 1. What is Machine Learning?

Machine Learning (ML) is a field of computer science and artificial intelligence where computers learn useful patterns from data.

In traditional programming, we explicitly write rules for the computer. In Machine Learning, an algorithm learns a model from examples and uses that model to make predictions or decisions.

A simple view is:

    Data
      ↓
    Learning Algorithm
      ↓
    Model
      ↓
    Prediction / Decision

Machine Learning is mainly about learning a useful relationship or pattern from available data.

---

## 2. Why Do We Need Machine Learning?

Many real-world problems are difficult to solve using manually written rules.

For example, consider email spam detection.

It may be difficult to manually write every possible rule that identifies spam because:

- New spam messages appear regularly.
- Spam messages can use different words.
- The structure of messages can change.
- The number of possible patterns can be very large.

A Machine Learning model can learn patterns from previously observed emails and use those patterns to classify new emails.

Other applications include:

- House price prediction
- Recommendation systems
- Fraud detection
- Image classification
- Customer segmentation
- Speech recognition
- Search systems
- Text classification

---

## 3. Traditional Programming

In traditional programming, the programmer provides the rules and the data.

    Rules + Data
         ↓
      Program
         ↓
       Output

For example:

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

Here, the rule is explicitly written by the programmer.

---

## 4. Machine Learning Approach

In Machine Learning, examples are provided to a learning algorithm.

    Data + Examples
          ↓
    Learning Algorithm
          ↓
         Model

The trained model can then be used with new data.

    New Data
       ↓
    Trained Model
       ↓
    Prediction

The important difference is that the model learns patterns from data instead of depending entirely on manually written rules.

---

## 5. Example: House Price Prediction

Suppose we have information about houses.

    Area
    Number of Rooms
    Location
    Age of House

These values can be used as input features.

The known selling price can be the target.

The model learns from previous examples:

    House Features
          ↓
    Machine Learning Model
          ↓
      House Price

After training, the model can estimate the price of a new house.

Because the target is a numerical value, this is an example of a regression problem.

---

## 6. Dataset

A dataset is a collection of examples or observations used for analysis or Machine Learning.

Example:

| Area | Rooms | Age | Price |
|---:|---:|---:|---:|
| 1200 | 3 | 5 | 5000000 |
| 1500 | 4 | 3 | 6500000 |
| 900 | 2 | 8 | 3800000 |

Each row represents one observation.

---

## 7. Feature

A feature is an input variable used by a Machine Learning model.

In the house-price example:

    Area
    Rooms
    Age

are features.

Features may also be called:

- Input variables
- Attributes
- Predictors

The choice and representation of useful features can have an important effect on model performance.

---

## 8. Target

The target is the output that the model is expected to predict.

In the house-price example:

    Price

is the target.

The target is also commonly called:

- Output variable
- Response variable
- Label, in classification settings

---

## 9. Sample or Instance

A single row in a dataset generally represents one sample or instance.

For example:

    Area = 1200
    Rooms = 3
    Age = 5
    Price = 5000000

represents one house example.

A Machine Learning dataset normally contains many such examples.

---

## 10. Model

A Machine Learning model is a learned representation of a relationship or pattern in data.

A simplified representation is:

    Input
      ↓
    Model
      ↓
    Output

For example:

    House Features
          ↓
    Price Prediction Model
          ↓
    Predicted Price

The model is learned from training data.

---

## 11. Learning from Examples

Suppose we have many examples:

    Input → Output

The learning algorithm tries to find a suitable relationship between the inputs and outputs.

Conceptually:

    Training Examples
          ↓
    Learning Algorithm
          ↓
    Learned Model

The learned model is then applied to new inputs.

    New Input
        ↓
    Learned Model
        ↓
    Prediction

---

## 12. Main Machine Learning Paradigms

Machine Learning can be studied through different learning paradigms.

The three major categories are:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

Each paradigm has a different way of learning from data or interaction.

---

## 13. Supervised Learning

In supervised learning, the training examples contain inputs along with known outputs.

    Input + Known Output
            ↓
      Learning Algorithm
            ↓
           Model

The model learns to predict the output for new inputs.

Two important supervised learning tasks are:

### Regression

Regression predicts a continuous numerical value.

Example:

    House Features → House Price

### Classification

Classification predicts a category or class.

Example:

    Email → Spam / Not Spam

---

## 14. Unsupervised Learning

In unsupervised learning, the training data does not have predefined target labels.

The algorithm attempts to discover useful structures or patterns in the data.

Example:

    Customer Data
         ↓
    Clustering Algorithm
         ↓
    Customer Groups

K-Means clustering is an example of an unsupervised learning algorithm.

Clustering will be studied later in the MLT course.

---

## 15. Reinforcement Learning

In reinforcement learning, an agent interacts with an environment.

The agent takes actions and receives feedback in the form of rewards or penalties.

    Agent
      ↓
    Action
      ↓
    Environment
      ↓
    Reward
      ↓
    Learning

The agent learns how its actions affect future rewards.

Reinforcement Learning is different from supervised and unsupervised learning because learning happens through interaction and feedback.

---

## 16. Regression vs Classification

### Regression

The output is generally a numerical value.

Examples:

- House price
- Temperature
- Sales amount
- Demand

Example:

    Input → House Features
    Output → ₹50,00,000

### Classification

The output belongs to a class or category.

Examples:

- Spam / Not Spam
- Pass / Fail
- Fraud / Not Fraud
- Cat / Dog

Example:

    Input → Email Features
    Output → Spam

---

## 17. Training Data

Training data is the data used by the learning algorithm to learn the model.

    Training Data
          ↓
    Learning Algorithm
          ↓
    Trained Model

The model learns patterns from the training examples.

---

## 18. Test Data

Test data is used to evaluate the trained model on data that was not used for learning the model.

    Training Data
          ↓
    Train Model
          ↓
    Trained Model
          ↓
    Test Data
          ↓
    Evaluation

Testing on unseen data helps us understand how the model may perform beyond the examples it learned from.

---

## 19. Generalization

Generalization is the ability of a trained model to perform well on new, unseen data.

The goal is not simply to memorize the training examples.

Instead, the model should learn patterns that are useful for new examples.

    Training Data
         ↓
       Model
         ↓
    Unseen Data
         ↓
      Prediction

Generalization is an important concept in Machine Learning.

---

## 20. Machine Learning as Function Learning

A Machine Learning problem can often be viewed as learning an unknown relationship.

Suppose:

    y = f(x)

where:

- x represents input.
- y represents output.
- f represents an unknown relationship.

The learning algorithm tries to estimate this relationship from data.

A learned model can be represented as:

    ŷ = f̂(x)

where:

- ŷ is the predicted output.
- f̂ is the learned approximation of the unknown function.

---

## 21. Example: Spam Detection

Suppose we have emails with information such as:

- Words used
- Number of links
- Message length
- Sender information

Previously labelled examples can be used for learning.

    Email Features
          ↓
    Classification Model
          ↓
    Spam / Not Spam

This is a classification problem because the output belongs to a category.

---

## 22. Example: Customer Segmentation

Suppose a company has information about customers:

- Age
- Spending
- Purchase frequency
- Product preferences

There may be no predefined customer group labels.

A clustering algorithm can discover groups with similar characteristics.

    Customer Data
         ↓
      Clustering
         ↓
    Customer Groups

This is an example of unsupervised learning.

---

## 23. Artificial Intelligence and Machine Learning

Artificial Intelligence (AI) is a broad field concerned with building systems that perform tasks associated with intelligent behaviour.

Machine Learning is an important approach within AI.

A simplified relationship is:

    Artificial Intelligence
             ↓
      Machine Learning
             ↓
       Learning from Data

Deep Learning is a subfield of Machine Learning that uses neural networks with multiple layers.

---

## 24. Machine Learning Workflow

A basic Machine Learning workflow can be represented as:

    Problem Definition
          ↓
    Data Collection
          ↓
    Data Preparation
          ↓
    Feature Representation
          ↓
    Model Selection
          ↓
    Model Training
          ↓
    Model Evaluation
          ↓
    Prediction

The exact workflow can vary depending on the problem.

Some steps may need to be repeated during development.

---

## 25. Important Terminology

| Term | Meaning |
|---|---|
| Dataset | Collection of examples |
| Sample | One observation |
| Feature | Input variable |
| Target | Output to be predicted |
| Model | Learned representation |
| Training | Learning from data |
| Prediction | Output produced for new input |
| Classification | Predicting a class |
| Regression | Predicting a numerical value |
| Generalization | Performance on unseen data |

---

## 26. Important Ideas

### Data is central

Machine Learning algorithms learn from data.

### Representation matters

The way data is represented can affect learning.

### Learning is not memorization

A useful model should generalize to unseen examples.

### Evaluation is necessary

A model needs to be evaluated to understand its performance.

### Different problems need different approaches

Regression, classification, clustering, and other problems may require different algorithms and models.

---

## 27. What I Learned Today

After Day 001, I should be able to explain:

- What Machine Learning means.
- Why Machine Learning is useful.
- Difference between traditional programming and Machine Learning.
- What a dataset is.
- What features are.
- What a target is.
- What a Machine Learning model is.
- What supervised learning means.
- What unsupervised learning means.
- What reinforcement learning means.
- Difference between regression and classification.
- Difference between training and test data.
- Meaning of generalization.
- Basic Machine Learning workflow.

---

## 28. Quick Revision

    Machine Learning
           ↓
    Data + Learning Algorithm
           ↓
         Model
           ↓
    New Data
           ↓
    Prediction / Decision

### Basic Terms

    Feature → Input
    Target  → Expected Output
    Model   → Learned Relationship
    Training → Learning Process
    Testing  → Evaluation on Unseen Data
    Generalization → Performance on New Data

---

## 29. Self-Check Questions

1. What is Machine Learning?
2. How is Machine Learning different from traditional programming?
3. What is a dataset?
4. What is a feature?
5. What is a target variable?
6. What is a sample?
7. What is a Machine Learning model?
8. What is supervised learning?
9. What is unsupervised learning?
10. What is reinforcement learning?
11. What is regression?
12. What is classification?
13. Why is training data used?
14. Why is test data used?
15. What is generalization?
16. How is Machine Learning related to Artificial Intelligence?

---

## 30. Day 001 Summary

Day 001 introduces the fundamental idea of Machine Learning.

The key concept is that a Machine Learning algorithm can learn useful patterns or relationships from data and use the learned model to make predictions or decisions on new data.

The basic learning process can be summarized as:

    Data
      ↓
    Learning
      ↓
    Model
      ↓
    Prediction

The next lectures will build on these foundations and explain different Machine Learning paradigms and ways of representing data.

---

## Day 001 Learning Checklist

- [ ] Understand Machine Learning
- [ ] Understand traditional programming vs ML
- [ ] Understand datasets
- [ ] Understand features
- [ ] Understand targets
- [ ] Understand samples
- [ ] Understand models
- [ ] Understand supervised learning
- [ ] Understand unsupervised learning
- [ ] Understand reinforcement learning
- [ ] Understand regression
- [ ] Understand classification
- [ ] Understand training and test data
- [ ] Understand generalization
- [ ] Understand the basic ML workflow

**End of Day 001**