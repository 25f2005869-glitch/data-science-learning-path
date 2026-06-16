/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 78
Description : Hash Join
*/

-- =====================================
-- DAY 78 : HASH JOIN
-- =====================================

-- What is Hash Join?

-- Hash Join is a join algorithm
-- that uses a hash function to
-- efficiently perform equality joins.

-- It is one of the fastest join
-- techniques for large tables.

-- =====================================
-- WHEN IS HASH JOIN USED?
-- =====================================

-- Equality Join

-- Example

-- SELECT *

-- FROM STUDENT S

-- JOIN ENROLLMENT E

-- ON S.Student_ID = E.Student_ID;

-- =====================================

-- Join Condition

-- =

-- Equality Operator

-- =====================================

-- Hash Join works best here.

-- =====================================
-- TWO PHASES OF HASH JOIN
-- =====================================

-- 1. Build Phase

-- 2. Probe Phase

-- =====================================
-- BUILD PHASE
-- =====================================

-- Choose Smaller Relation

-- Build Hash Table

-- =====================================

-- Example

-- STUDENT

-- Student_ID | Name

-- 1          | Saloni

-- 2          | Rahul

-- =====================================

-- Apply Hash Function

-- h(Student_ID)

-- =====================================

-- Hash Table

-- Bucket 1 → Saloni

-- Bucket 2 → Rahul

-- =====================================

-- Smaller table is hashed
-- to reduce memory usage.

-- =====================================
-- PROBE PHASE
-- =====================================

-- Scan Larger Relation

-- =====================================

-- ENROLLMENT

-- Student_ID | Course

-- 1          | DBMS

-- 2          | SQL

-- =====================================

-- For each record

-- Compute Hash Value

-- Search Hash Table

-- =====================================

-- Student_ID = 1

-- Match Found

-- Output Joined Record

-- =====================================

-- Student_ID = 2

-- Match Found

-- Output Joined Record

-- =====================================

-- Join Completed

-- =====================================
-- HASH JOIN WORKFLOW
-- =====================================

-- Smaller Relation

-- ↓

-- Build Hash Table

-- ↓

-- Scan Larger Relation

-- ↓

-- Probe Hash Table

-- ↓

-- Return Matches

-- =====================================
-- EXAMPLE WALKTHROUGH
-- =====================================

-- STUDENT

-- 1  Saloni

-- 2  Rahul

-- =====================================

-- Build Hash Table

-- Bucket 1 → Saloni

-- Bucket 2 → Rahul

-- =====================================

-- ENROLLMENT

-- 1 DBMS

-- 2 SQL

-- =====================================

-- Probe

-- Student_ID = 1

-- Match Bucket 1

-- =====================================

-- Student_ID = 2

-- Match Bucket 2

-- =====================================

-- Join Result Produced

-- =====================================
-- COST ANALYSIS
-- =====================================

-- Build Cost

-- O(n)

-- =====================================

-- Probe Cost

-- O(m)

-- =====================================

-- Total Cost

-- O(n + m)

-- =====================================

-- Better than

-- Nested Loop Join

-- O(n × m)

-- =====================================
-- ADVANTAGES
-- =====================================

-- Very Fast Equality Joins

-- Efficient For Large Relations

-- Low Join Cost

-- Good Performance

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Requires Additional Memory

-- Not Suitable For Range Queries

-- Hash Function Overhead

-- =====================================
-- HASH JOIN VS NESTED LOOP
-- =====================================

-- Nested Loop Join

-- O(n × m)

-- =====================================

-- Hash Join

-- O(n + m)

-- =====================================

-- Hash Join Usually Faster

-- =====================================
-- HASH JOIN VS SORT-MERGE
-- =====================================

-- Sort-Merge Join

-- Requires Sorting

-- =====================================

-- Hash Join

-- No Sorting Required

-- =====================================

-- Hash Join Faster For

-- Equality Joins

-- =====================================

-- Sort-Merge Better For

-- Range Conditions

-- =====================================
-- WHEN TO USE HASH JOIN?
-- =====================================

-- Large Tables

-- Equality Conditions

-- Available Memory

-- =====================================

-- Example

-- Customer_ID = Customer_ID

-- Student_ID = Student_ID

-- Product_ID = Product_ID

-- =====================================
-- WHEN NOT TO USE?
-- =====================================

-- Range Conditions

-- Less Available Memory

-- Ordered Output Required

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What are the two phases of
-- Hash Join?

-- Answer:

-- Build Phase

-- Probe Phase

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which relation is hashed first?

-- Answer:

-- Smaller Relation

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Time Complexity of Hash Join?

-- Answer:

-- O(n + m)

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Hash Join?

-- Answer:

-- Join algorithm that uses
-- hash tables to perform
-- equality joins efficiently.

-- -------------------------------------

-- Q2. Why is Hash Join fast?

-- Answer:

-- Uses direct hash lookups
-- instead of repeated comparisons.

-- -------------------------------------

-- Q3. When is Hash Join preferred?

-- Answer:

-- Large tables with
-- equality join conditions.

-- -------------------------------------

-- Q4. Why is Hash Join unsuitable
-- for range queries?

-- Answer:

-- Hashing does not preserve
-- ordering of values.

-- =====================================
-- DAY 78 SUMMARY
-- =====================================

-- Hash Join

-- Uses Hash Tables

-- -------------------------------------

-- Build Phase

-- Create Hash Table

-- -------------------------------------

-- Probe Phase

-- Find Matches

-- -------------------------------------

-- Complexity

-- O(n + m)

-- -------------------------------------

-- Best For

-- Equality Joins

-- Large Relations

-- -------------------------------------

-- Not Suitable For

-- Range Queries

-- Ordered Results

-- -------------------------------------

-- Hash Join is one of the most
-- important and efficient join
-- algorithms used by modern DBMS.