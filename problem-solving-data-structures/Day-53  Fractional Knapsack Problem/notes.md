Day 53 – Fractional Knapsack Problem
Objective

The goal of this session is to understand the Fractional Knapsack Problem and solve it using a Greedy Algorithm.

What is the Fractional Knapsack Problem?

Given:

A knapsack with limited capacity.
Items having:
Weight
Value

The objective is:

Maximize Total Value

while keeping total weight within the knapsack capacity.

Difference from 0/1 Knapsack
0/1 Knapsack
Take Entire Item

or

Leave Entire Item
Fractional Knapsack
Item can be divided

Example:

Take 50% of an Item

or

Take 25% of an Item
Example

Knapsack Capacity:

50

Items:

Item	Value	Weight
A	60	10
B	100	20
C	120	30
Step 1: Calculate Value Per Weight

Formula:

Weight
Value
	​


Item	Value/Weight
A	6
B	5
C	4
Step 2: Sort Descending
A → B → C
Step 3: Fill Knapsack

Take Item A:

Weight = 10

Value = 60

Remaining Capacity:

40

Take Item B:

Weight = 20

Value = 100

Remaining Capacity:

20

Take Fraction of Item C:

20/30

Fraction Taken:

2/3

Value Obtained:

120 × (20/30)

= 80
Final Answer

Total Value:

60 + 100 + 80

Result:

240
Why Greedy Works?

Always select the item with:

Highest Value Per Unit Weight

This guarantees the optimal solution for the Fractional Knapsack Problem.

Algorithm
Compute Value/Weight ratio.
Sort items by ratio in descending order.
Take highest ratio items first.
If item does not fit:
Take fraction.
Continue until capacity becomes zero.
Pseudocode
Sort by Value/Weight Ratio

FOR each item

    IF item fits

        Take Entire Item

    ELSE

        Take Fraction

        BREAK
Applications
Cargo Loading
Resource Allocation
Investment Planning
Budget Optimization
Logistics Systems
Time Complexity

Sorting:

O(n log n)

Traversal:

O(n)

Overall:

O(n log n)
Space Complexity
O(1)

(extra space ignored)

Key Concepts Learned
Fractional Knapsack
Greedy Algorithm
Value Density
Optimization
Resource Allocation
Summary

The Fractional Knapsack Problem is a classic Greedy Algorithm problem where items are selected according to their value-to-weight ratio to maximize total profit.