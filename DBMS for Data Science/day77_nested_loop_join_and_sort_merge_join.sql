/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 77
Description : Nested Loop Join and Sort-Merge Join
*/

-- =====================================
-- DAY 77 : NESTED LOOP JOIN
-- AND SORT-MERGE JOIN
-- =====================================

-- Today we study two important
-- join algorithms in detail.

-- 1. Nested Loop Join

-- 2. Sort-Merge Join

-- =====================================
-- NESTED LOOP JOIN
-- =====================================

-- What is Nested Loop Join?

-- Nested Loop Join compares every
-- row of one relation with every
-- row of another relation.

-- =====================================
-- EXAMPLE TABLES
-- =====================================

-- STUDENT

-- Student_ID | Name

-- 1          | Saloni

-- 2          | Rahul

-- =====================================

-- ENROLLMENT

-- Student_ID | Course

-- 1          | DBMS

-- 2          | SQL

-- =====================================
-- QUERY
-- =====================================

-- SELECT *

-- FROM STUDENT S

-- JOIN ENROLLMENT E

-- ON S.Student_ID = E.Student_ID;

-- =====================================
-- WORKING
-- =====================================

-- Step 1

-- Take First Row From STUDENT

-- Student_ID = 1

-- =====================================

-- Compare With All Rows
-- Of ENROLLMENT

-- =====================================

-- Match Found

-- Student_ID = 1

-- Output Result

-- =====================================

-- Step 2

-- Take Next STUDENT Row

-- Student_ID = 2

-- =====================================

-- Compare With All Rows
-- Of ENROLLMENT

-- =====================================

-- Match Found

-- Output Result

-- =====================================
-- PSEUDOCODE
-- =====================================

-- FOR each row in STUDENT

--     FOR each row in ENROLLMENT

--         IF Join Condition True

--             Output Row

-- =====================================
-- COST ANALYSIS
-- =====================================

-- Let:

-- STUDENT Rows = n

-- ENROLLMENT Rows = m

-- =====================================

-- Comparisons

-- = n × m

-- =====================================

-- Complexity

-- O(n × m)

-- =====================================
-- ADVANTAGES
-- =====================================

-- Simple Algorithm

-- Easy Implementation

-- Works For Any Join Condition

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Expensive For Large Tables

-- Large Number Of Comparisons

-- =====================================
-- SORT-MERGE JOIN
-- =====================================

-- What is Sort-Merge Join?

-- Sort-Merge Join first sorts
-- both relations on the join key.

-- Then merges matching records.

-- =====================================
-- EXAMPLE
-- =====================================

-- STUDENT

-- 1

-- 2

-- 3

-- =====================================

-- ENROLLMENT

-- 1

-- 2

-- 3

-- =====================================

-- Already Sorted

-- =====================================
-- WORKING
-- =====================================

-- Pointer 1

-- STUDENT

-- =====================================

-- Pointer 2

-- ENROLLMENT

-- =====================================

-- Compare Keys

-- =====================================

-- If Equal

-- Join Records

-- Move Both Pointers

-- =====================================

-- If Smaller

-- Move Smaller Pointer

-- =====================================

-- Continue Until End

-- =====================================
-- EXAMPLE WALKTHROUGH
-- =====================================

-- STUDENT

-- 1  2  3

-- =====================================

-- ENROLLMENT

-- 1  2  3

-- =====================================

-- Compare

-- 1 = 1

-- Join

-- =====================================

-- Compare

-- 2 = 2

-- Join

-- =====================================

-- Compare

-- 3 = 3

-- Join

-- =====================================

-- Join Complete

-- =====================================
-- COST ANALYSIS
-- =====================================

-- Sorting Cost

-- O(n log n)

-- O(m log m)

-- =====================================

-- Merge Cost

-- O(n + m)

-- =====================================

-- Total Cost

-- Sorting + Merging

-- =====================================
-- ADVANTAGES
-- =====================================

-- Efficient For Large Tables

-- Good For Sorted Relations

-- Supports Range Conditions

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Sorting Overhead

-- Requires Sorted Inputs

-- =====================================
-- NESTED LOOP VS SORT-MERGE
-- =====================================

-- Nested Loop Join

-- O(n × m)

-- =====================================

-- Sort-Merge Join

-- O(n log n)

-- + O(m log m)

-- =====================================

-- Nested Loop

-- Simple

-- =====================================

-- Sort-Merge

-- Faster For Large Data

-- =====================================

-- Nested Loop

-- No Sorting Needed

-- =====================================

-- Sort-Merge

-- Sorting Required

-- =====================================
-- WHEN TO USE?
-- =====================================

-- Small Tables

-- Nested Loop Join

-- =====================================

-- Large Sorted Tables

-- Sort-Merge Join

-- =====================================

-- Range Conditions

-- Sort-Merge Join

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which join compares every row
-- with every row?

-- Answer:

-- Nested Loop Join

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which join requires sorting?

-- Answer:

-- Sort-Merge Join

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which join is generally better
-- for large sorted tables?

-- Answer:

-- Sort-Merge Join

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Nested Loop Join?

-- Answer:

-- Join algorithm that compares
-- each row of one relation with
-- every row of another relation.

-- -------------------------------------

-- Q2. What is the complexity of
-- Nested Loop Join?

-- Answer:

-- O(n × m)

-- -------------------------------------

-- Q3. Why is Sort-Merge Join
-- efficient?

-- Answer:

-- It uses sorted data and
-- linear merge processing.

-- -------------------------------------

-- Q4. Which join supports
-- range-based conditions well?

-- Answer:

-- Sort-Merge Join

-- =====================================
-- DAY 77 SUMMARY
-- =====================================

-- Nested Loop Join

-- Compare Every Row

-- Complexity:

-- O(n × m)

-- -------------------------------------

-- Sort-Merge Join

-- Sort + Merge

-- Better For Large Data

-- -------------------------------------

-- Nested Loop

-- Simple

-- -------------------------------------

-- Sort-Merge

-- Efficient For Sorted Data

-- -------------------------------------

-- These two join algorithms are
-- fundamental building blocks of
-- query execution in DBMS.