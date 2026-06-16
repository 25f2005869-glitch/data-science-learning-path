/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 74
Description : Heuristic Query Optimization
*/

-- =====================================
-- DAY 74 : HEURISTIC QUERY OPTIMIZATION
-- =====================================

-- What is Heuristic Query Optimization?

-- Heuristic Query Optimization
-- uses predefined rules to improve
-- query execution plans.

-- Goal:

-- Reduce Intermediate Results

-- Reduce Disk Access

-- Improve Query Performance

-- =====================================
-- WHY HEURISTICS?
-- =====================================

-- Instead of calculating exact cost,

-- DBMS applies optimization rules
-- that usually lead to better
-- execution plans.

-- =====================================
-- COMMON HEURISTIC RULES
-- =====================================

-- 1. Selection Pushdown

-- 2. Projection Pushdown

-- 3. Join Optimization

-- 4. Query Tree Optimization

-- =====================================
-- 1. SELECTION PUSHDOWN
-- =====================================

-- Apply Selection As Early
-- As Possible.

-- =====================================

-- Example

-- SELECT *

-- FROM STUDENT

-- WHERE Department = 'CSE';

-- =====================================

-- Relational Algebra

-- σ(Department='CSE')(STUDENT)

-- =====================================

-- Selection reduces number
-- of records early.

-- =====================================

-- Benefit:

-- Smaller Intermediate Results

-- Less Processing

-- =====================================
-- EXAMPLE
-- =====================================

-- Before Optimization

-- JOIN

-- ↓

-- SELECTION

-- =====================================

-- After Optimization

-- SELECTION

-- ↓

-- JOIN

-- =====================================

-- Better Performance

-- =====================================
-- 2. PROJECTION PUSHDOWN
-- =====================================

-- Apply Projection Early.

-- =====================================

-- Projection selects only
-- required columns.

-- =====================================

-- Example

-- SELECT Name

-- FROM STUDENT;

-- =====================================

-- Relational Algebra

-- π(Name)(STUDENT)

-- =====================================

-- Unnecessary columns removed
-- immediately.

-- =====================================

-- Benefit:

-- Less Data Transfer

-- Less Memory Usage

-- =====================================
-- EXAMPLE
-- =====================================

-- Before

-- Entire Table Processed

-- =====================================

-- After

-- Only Required Columns

-- Processed

-- =====================================
-- 3. JOIN OPTIMIZATION
-- =====================================

-- Join operations are expensive.

-- =====================================

-- Heuristic Rule:

-- Reduce relation size before join.

-- =====================================

-- Example

-- STUDENT

-- JOIN

-- ENROLLMENT

-- =====================================

-- First Apply:

-- Selection

-- Projection

-- Then Join

-- =====================================

-- Smaller Inputs

-- Faster Join

-- =====================================
-- 4. QUERY TREE OPTIMIZATION
-- =====================================

-- Query represented as
-- a Query Tree.

-- =====================================

-- Example

--          π(Name)

--              |

--      σ(Dept='CSE')

--              |

--         STUDENT

-- =====================================

-- Optimizer rearranges nodes
-- using heuristic rules.

-- =====================================

-- Goal:

-- Reduce Processing Cost

-- =====================================
-- HEURISTIC STRATEGIES
-- =====================================

-- Perform Selections Early

-- Perform Projections Early

-- Reduce Join Inputs

-- Avoid Large Intermediate Results

-- =====================================
-- EXAMPLE QUERY
-- =====================================

-- SELECT Name

-- FROM STUDENT

-- WHERE Department='CSE';

-- =====================================

-- Relational Algebra

-- π(Name)

-- (

-- σ(Department='CSE')

-- (STUDENT)

-- )

-- =====================================

-- Selection First

-- Then Projection

-- Efficient Plan

-- =====================================
-- ADVANTAGES
-- =====================================

-- Simple Optimization

-- Fast Decision Making

-- Reduced Query Cost

-- Better Performance

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Does Not Guarantee

-- Optimal Plan

-- =====================================

-- Uses General Rules Only

-- =====================================
-- HEURISTIC VS COST-BASED
-- =====================================

-- Heuristic Optimization

-- Rule-Based

-- Fast

-- =====================================

-- Cost-Based Optimization

-- Cost Calculation

-- More Accurate

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is Selection Pushdown?

-- Answer:

-- Apply selection as early
-- as possible.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Why use Projection Pushdown?

-- Answer:

-- Reduce unnecessary columns.

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Why optimize joins?

-- Answer:

-- Joins are expensive operations.

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Heuristic
-- Query Optimization?

-- Answer:

-- Rule-based query optimization
-- using predefined strategies.

-- -------------------------------------

-- Q2. What is Selection Pushdown?

-- Answer:

-- Moving selection closer
-- to base relations.

-- -------------------------------------

-- Q3. Why are joins optimized?

-- Answer:

-- To reduce processing cost
-- and intermediate results.

-- =====================================
-- DAY 74 SUMMARY
-- =====================================

-- Heuristic Optimization

-- Rule-Based Optimization

-- -------------------------------------

-- Selection Pushdown

-- Apply Filters Early

-- -------------------------------------

-- Projection Pushdown

-- Remove Extra Columns Early

-- -------------------------------------

-- Join Optimization

-- Reduce Join Inputs

-- -------------------------------------

-- Query Tree Optimization

-- Rearrange Operations

-- -------------------------------------

-- Goal

-- Reduce Intermediate Results

-- Improve Query Performance

-- Heuristic optimization is a
-- fast and practical technique
-- used by DBMS optimizers.