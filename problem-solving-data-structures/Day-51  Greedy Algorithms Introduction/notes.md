Day 51 – Greedy Algorithms Introduction
Objective

The goal of this session is to understand Greedy Algorithms and how they make locally optimal choices to solve optimization problems.

What is a Greedy Algorithm?

A Greedy Algorithm builds a solution step by step by always choosing the best available option at the current moment.

It never revisits previous decisions.

Greedy Principle
Choose Best Now

The algorithm assumes that making the locally optimal choice will eventually lead to a globally optimal solution.

Real Life Example

Suppose you need ₹67.

Available coins:

₹10, ₹5, ₹2, ₹1

Greedy Approach:

Take Largest Coin First

Solution:

67

→ 10
→ 10
→ 10
→ 10
→ 10
→ 10
→ 5
→ 2

Total Coins:

8
Characteristics of Greedy Algorithms
Greedy Choice Property

A globally optimal solution can be reached by choosing local optimum choices.

Optimal Substructure

An optimal solution contains optimal solutions to subproblems.

General Strategy
Identify all possible choices.
Select the best choice.
Add it to the solution.
Never reconsider the choice.
Repeat until solution is complete.
Greedy vs Dynamic Programming
Feature	Greedy	Dynamic Programming
Decision	Local Best	Global Best
Reconsider Choices	No	Yes
Speed	Faster	Slower
Memory	Less	More
Example Problems
Coin Change

Choose largest coin first.

Activity Selection

Choose activity that finishes earliest.

Fractional Knapsack

Choose item with highest profit per weight.

Huffman Coding

Choose lowest frequency nodes first.

Minimum Spanning Tree

Used in:

Prim's Algorithm

Kruskal's Algorithm
When Greedy Works

Greedy works only when:

Greedy Choice Property

and

Optimal Substructure

are satisfied.

Advantages
Easy to implement
Fast execution
Low memory usage
Often produces optimal solutions
Limitations

Greedy does not always produce the best answer.

Example:

Some Coin Systems

require Dynamic Programming instead.

Time Complexity

Depends on the problem.

Many Greedy Algorithms run in:

O(n log n)

because sorting is often required.

Applications
Scheduling Systems
Network Routing
Data Compression
Resource Allocation
Job Sequencing
Transportation Systems
Key Concepts Learned
Greedy Algorithm
Local Optimum
Global Optimum
Greedy Choice Property
Optimal Substructure
Summary

Greedy Algorithms make the best immediate choice at each step. They are efficient and widely used in optimization problems where local decisions lead to globally optimal solutions.