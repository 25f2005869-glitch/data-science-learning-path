/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 79
Description : Query Execution Plans (Execution Tree, Operator Tree, Explain Plan)
*/

-- =====================================
-- DAY 79 : QUERY EXECUTION PLANS
-- =====================================

-- What is a Query Execution Plan?

-- A Query Execution Plan (QEP)
-- is the sequence of operations
-- chosen by the DBMS to execute
-- a SQL query.

-- =====================================

-- Query Optimizer generates
-- the execution plan.

-- =====================================

-- Goal:

-- Execute Query Efficiently

-- Minimize Cost

-- Minimize Disk I/O

-- =====================================
-- WHY EXECUTION PLANS?
-- =====================================

-- Same SQL query can be executed
-- in multiple ways.

-- =====================================

-- Example

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Possible Plans

-- Full Table Scan

-- Index Scan

-- =====================================

-- Optimizer selects

-- Lowest Cost Plan

-- =====================================
-- EXECUTION TREE
-- =====================================

-- Execution Plan is commonly
-- represented as a tree.

-- =====================================

-- Example Query

-- SELECT Name

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Execution Tree

--        Projection

--             |

--        Selection

--             |

--         STUDENT

-- =====================================

-- Leaf Node

-- Base Relation

-- =====================================

-- Internal Node

-- Operation

-- =====================================

-- Root Node

-- Final Result

-- =====================================
-- OPERATOR TREE
-- =====================================

-- Operator Tree represents
-- relational algebra operations.

-- =====================================

-- Example

-- π(Name)

--      |

-- σ(Student_ID=101)

--      |

-- STUDENT

-- =====================================

-- Operators

-- Selection

-- Projection

-- Join

-- Sort

-- Group By

-- =====================================
-- EXAMPLE WITH JOIN
-- =====================================

-- Query

-- SELECT Name, Course

-- FROM STUDENT S

-- JOIN ENROLLMENT E

-- ON S.Student_ID = E.Student_ID;

-- =====================================

-- Operator Tree

--         Projection

--              |

--            Join

--           /    \

--      STUDENT  ENROLLMENT

-- =====================================

-- Join combines records.

-- Projection returns required columns.

-- =====================================
-- QUERY EXECUTION STEPS
-- =====================================

-- Step 1

-- Parse Query

-- =====================================

-- Step 2

-- Translate To Relational Algebra

-- =====================================

-- Step 3

-- Optimize Query

-- =====================================

-- Step 4

-- Generate Execution Plan

-- =====================================

-- Step 5

-- Execute Plan

-- =====================================
-- EXPLAIN PLAN
-- =====================================

-- EXPLAIN is used to view
-- the execution plan chosen
-- by the optimizer.

-- =====================================

-- Example

-- EXPLAIN

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Output May Show

-- Index Scan

-- Estimated Cost

-- Number Of Rows

-- =====================================
-- WHY USE EXPLAIN?
-- =====================================

-- Analyze Performance

-- Detect Full Table Scans

-- Verify Index Usage

-- Improve Queries

-- =====================================
-- SAMPLE EXPLAIN OUTPUT
-- =====================================

-- Operation

-- Index Scan

-- -------------------------------------

-- Cost

-- 10

-- -------------------------------------

-- Rows

-- 1

-- =====================================

-- Indicates efficient query plan.

-- =====================================
-- COST IN EXECUTION PLAN
-- =====================================

-- Optimizer estimates:

-- Disk Access Cost

-- CPU Cost

-- Memory Cost

-- =====================================

-- Lower Cost

-- Better Plan

-- =====================================
-- COMMON OPERATORS
-- =====================================

-- Table Scan

-- Index Scan

-- Selection

-- Projection

-- Join

-- Sort

-- Aggregate

-- =====================================
-- PLAN COMPARISON
-- =====================================

-- Plan A

-- Full Table Scan

-- Cost = 500

-- =====================================

-- Plan B

-- Index Scan

-- Cost = 50

-- =====================================

-- Optimizer Chooses

-- Plan B

-- =====================================
-- ADVANTAGES
-- =====================================

-- Better Query Analysis

-- Performance Tuning

-- Detect Inefficiencies

-- Understand Optimizer Decisions

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is a Query Execution Plan?

-- Answer:

-- Sequence of operations used
-- to execute a query.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which command displays
-- the execution plan?

-- Answer:

-- EXPLAIN

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Who generates the execution plan?

-- Answer:

-- Query Optimizer

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is an Execution Tree?

-- Answer:

-- Tree representation of query
-- execution operations.

-- -------------------------------------

-- Q2. What is an Operator Tree?

-- Answer:

-- Tree containing relational
-- algebra operators.

-- -------------------------------------

-- Q3. Why is EXPLAIN important?

-- Answer:

-- It helps analyze and optimize
-- query performance.

-- -------------------------------------

-- Q4. What information does
-- EXPLAIN provide?

-- Answer:

-- Access Path

-- Estimated Cost

-- Number Of Rows

-- Operations Used

-- =====================================
-- DAY 79 SUMMARY
-- =====================================

-- Query Execution Plan

-- Execution Strategy

-- -------------------------------------

-- Execution Tree

-- Tree Of Operations

-- -------------------------------------

-- Operator Tree

-- Relational Algebra Tree

-- -------------------------------------

-- EXPLAIN

-- Displays Execution Plan

-- -------------------------------------

-- Generated By

-- Query Optimizer

-- -------------------------------------

-- Used For

-- Performance Analysis

-- Query Tuning

-- -------------------------------------

-- Understanding execution plans
-- is essential for database
-- performance optimization.