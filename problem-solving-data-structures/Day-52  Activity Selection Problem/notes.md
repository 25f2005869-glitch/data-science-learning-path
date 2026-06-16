Day 52 – Activity Selection Problem
Objective

The goal of this session is to understand the Activity Selection Problem and solve it using a Greedy Algorithm.

What is the Activity Selection Problem?

Given:

N Activities

Each activity has:

Start Time
Finish Time

The objective is:

Select Maximum Number of Non-Overlapping Activities
Example

Activities:

Activity	Start	Finish
A1	1	4
A2	3	5
A3	0	6
A4	5	7
A5	8	9
A6	5	9
Visualization
Time →

0 1 2 3 4 5 6 7 8 9

A1: |---|

A2:     |---|

A3: |------|

A4:         |--|

A5:               |-|

A6:         |----|
Greedy Strategy

Choose the activity that:

Finishes Earliest

This leaves maximum time for future activities.

Step 1: Sort by Finish Time
Activity	Start	Finish
A1	1	4
A2	3	5
A3	0	6
A4	5	7
A5	8	9
A6	5	9
Step 2: Select Activities

Select:

A1

Finish Time:

4

Next Activity:

A2

Starts before 4.

Skip ❌

Next Activity:

A4

Starts at:

5

Select ✅

Next Activity:

A5

Starts at:

8

Select ✅

Final Selection

A1 → A4 → A5

Total Activities:

3
Why Greedy Works?

Choosing the earliest finishing activity ensures the maximum remaining time for future selections.

This satisfies:

Greedy Choice Property
Algorithm
Sort activities by finish time.
Select first activity.
For each remaining activity:
If start time ≥ previous finish time:
Select activity.
Continue until all activities are processed.
Pseudocode
Sort Activities by Finish Time

Select First Activity

FOR each activity

    IF start >= last_finish

        Select Activity
Applications
CPU Scheduling
Event Planning
Classroom Scheduling
Resource Allocation
Project Management
Time Complexity

Sorting:

O(n log n)

Selection:

O(n)

Overall:

O(n log n)
Space Complexity
O(1)

(ignoring output storage)

Key Concepts Learned
Activity Selection
Greedy Algorithm
Scheduling Problem
Earliest Finish Time
Greedy Choice Property
Summary

The Activity Selection Problem is a classic Greedy Algorithm problem where selecting the earliest finishing activity produces the maximum number of non-overlapping activities.