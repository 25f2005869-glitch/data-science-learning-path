/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 76
Description : Join Processing Techniques
*/

-- =====================================
-- DAY 76 : JOIN PROCESSING TECHNIQUES
-- =====================================

-- What is Join Processing?

-- Join Processing refers to the
-- methods used by a DBMS to
-- execute JOIN operations
-- efficiently.

-- =====================================

-- Joins are among the most
-- expensive operations in DBMS.

-- Therefore:

-- Optimizing joins is critical
-- for query performance.

-- =====================================
-- WHY JOIN PROCESSING?
-- =====================================

-- Multiple tables often contain
-- related information.

-- Example:

-- STUDENT

-- Student_ID

-- Name

-- -------------------------------------

-- ENROLLMENT

-- Student_ID

-- Course_ID

-- =====================================

-- Query:

-- Find student names and courses.

-- =====================================

-- Requires JOIN operation.

-- =====================================
-- JOIN OPERATION
-- =====================================

-- Example

-- SELECT Name, Course_ID

-- FROM STUDENT S

-- JOIN ENROLLMENT E

-- ON S.Student_ID = E.Student_ID;

-- =====================================

-- DBMS must decide:

-- How to perform the join?

-- Which algorithm to use?

-- =====================================
-- COMMON JOIN TECHNIQUES
-- =====================================

-- 1. Nested Loop Join

-- 2. Sort-Merge Join

-- 3. Hash Join

-- =====================================
-- JOIN COST FACTORS
-- =====================================

-- Number Of Records

-- Table Size

-- Available Indexes

-- Memory Size

-- Disk I/O

-- =====================================

-- Optimizer selects join
-- technique with lowest cost.

-- =====================================
-- NESTED LOOP JOIN
-- =====================================

-- Basic Idea

-- Compare every row of one table
-- with every row of another table.

-- =====================================

-- Example

-- For each STUDENT row

-- Check every ENROLLMENT row

-- =====================================

-- Pseudocode

-- For each row in STUDENT

-- For each row in ENROLLMENT

-- Compare Student_ID

-- =====================================

-- Advantages

-- Simple

-- Easy To Implement

-- =====================================

-- Disadvantages

-- Expensive For Large Tables

-- =====================================

-- Complexity

-- O(n × m)

-- =====================================
-- SORT-MERGE JOIN
-- =====================================

-- Basic Idea

-- Sort both relations on
-- join attribute.

-- Then merge them.

-- =====================================

-- Example

-- Sort STUDENT by Student_ID

-- Sort ENROLLMENT by Student_ID

-- =====================================

-- Merge Matching Records

-- =====================================

-- Advantages

-- Good For Large Sorted Data

-- Supports Range Conditions

-- =====================================

-- Disadvantages

-- Sorting Cost

-- =====================================
-- HASH JOIN
-- =====================================

-- Basic Idea

-- Use Hash Function on
-- join attribute.

-- =====================================

-- Build Phase

-- Create Hash Table

-- =====================================

-- Probe Phase

-- Search Matching Records

-- =====================================

-- Example

-- Hash STUDENT.Student_ID

-- Search ENROLLMENT.Student_ID

-- =====================================

-- Advantages

-- Very Fast Equality Joins

-- =====================================

-- Disadvantages

-- Poor For Range Joins

-- Additional Memory Required

-- =====================================
-- JOIN METHOD SELECTION
-- =====================================

-- Small Tables

-- Nested Loop Join

-- =====================================

-- Sorted Data

-- Sort-Merge Join

-- =====================================

-- Equality Join

-- Hash Join

-- =====================================

-- Large Relations

-- Hash Join

-- Sort-Merge Join

-- =====================================
-- COMPARISON TABLE
-- =====================================

-- Nested Loop Join

-- Simple

-- O(n × m)

-- -------------------------------------

-- Sort-Merge Join

-- Requires Sorting

-- Efficient For Sorted Data

-- -------------------------------------

-- Hash Join

-- Uses Hash Function

-- Excellent For Equality Join

-- =====================================
-- OPTIMIZER DECISION
-- =====================================

-- Query Optimizer evaluates

-- Table Size

-- Available Memory

-- Indexes

-- Join Condition

-- =====================================

-- Then chooses lowest-cost
-- join algorithm.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which join algorithm compares
-- every row with every row?

-- Answer:

-- Nested Loop Join

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which join algorithm uses
-- a hash table?

-- Answer:

-- Hash Join

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which join algorithm requires
-- sorted inputs?

-- Answer:

-- Sort-Merge Join

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Why are joins expensive?

-- Answer:

-- Multiple relations must be
-- compared and combined.

-- -------------------------------------

-- Q2. Which join is best for
-- equality conditions?

-- Answer:

-- Hash Join

-- -------------------------------------

-- Q3. Which join works well on
-- sorted relations?

-- Answer:

-- Sort-Merge Join

-- -------------------------------------

-- Q4. Which join is simplest?

-- Answer:

-- Nested Loop Join

-- =====================================
-- DAY 76 SUMMARY
-- =====================================

-- Join Processing

-- Executes JOIN Operations

-- -------------------------------------

-- Nested Loop Join

-- Simple

-- O(n × m)

-- -------------------------------------

-- Sort-Merge Join

-- Sort + Merge

-- Good For Sorted Data

-- -------------------------------------

-- Hash Join

-- Uses Hash Table

-- Best For Equality Joins

-- -------------------------------------

-- Query Optimizer selects
-- the join technique with
-- the lowest estimated cost.

-- Join processing is one of
-- the most important topics
-- in query optimization.