/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 75
Description : Cost-Based Query Optimization
*/

-- =====================================
-- DAY 75 : COST-BASED QUERY OPTIMIZATION
-- =====================================

-- What is Cost-Based Optimization?

-- Cost-Based Query Optimization (CBO)
-- is a technique where the DBMS
-- evaluates multiple execution plans
-- and selects the one with the
-- lowest estimated cost.

-- =====================================
-- GOAL
-- =====================================

-- Minimize:

-- Disk I/O

-- CPU Usage

-- Memory Usage

-- Network Cost

-- Query Execution Time

-- =====================================
-- WHY COST-BASED OPTIMIZATION?
-- =====================================

-- A query can be executed using
-- different strategies.

-- Example:

-- Full Table Scan

-- Index Scan

-- Hash Access

-- =====================================

-- DBMS estimates the cost of
-- each strategy.

-- Chooses the cheapest plan.

-- =====================================
-- EXAMPLE QUERY
-- =====================================

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Plan A

-- Full Table Scan

-- Estimated Cost = 500

-- -------------------------------------

-- Plan B

-- Index Scan

-- Estimated Cost = 50

-- =====================================

-- Optimizer Chooses

-- Plan B

-- =====================================
-- COST ESTIMATION
-- =====================================

-- Cost Estimation predicts
-- resources needed to execute
-- a query.

-- =====================================

-- Factors Considered

-- Number Of Rows

-- Number Of Blocks

-- Available Indexes

-- Join Operations

-- Memory Availability

-- =====================================
-- DATABASE STATISTICS
-- =====================================

-- Optimizer uses Statistics
-- stored by DBMS.

-- =====================================

-- Examples

-- Number Of Rows

-- Number Of Pages

-- Distinct Values

-- Index Information

-- =====================================

-- Statistics help estimate
-- query execution cost.

-- =====================================
-- CARDINALITY
-- =====================================

-- Cardinality means:

-- Number Of Rows

-- =====================================

-- Example

-- STUDENT Table

-- Total Rows = 100000

-- =====================================

-- Cardinality

-- = 100000

-- =====================================

-- Used to estimate result size.

-- =====================================
-- SELECTIVITY
-- =====================================

-- Selectivity measures how many
-- rows satisfy a condition.

-- =====================================

-- Formula

-- Selectivity

-- = Matching Rows

--   --------------

--   Total Rows

-- =====================================

-- Example

-- Total Rows = 100000

-- Matching Rows = 100

-- =====================================

-- Selectivity

-- = 100 / 100000

-- = 0.001

-- =====================================

-- Low Selectivity

-- Better Index Usage

-- =====================================
-- HIGH VS LOW SELECTIVITY
-- =====================================

-- High Selectivity

-- Few Rows Match

-- Excellent For Indexes

-- -------------------------------------

-- Low Selectivity

-- Many Rows Match

-- Full Scan May Be Better

-- =====================================
-- ACCESS PATH SELECTION
-- =====================================

-- Optimizer chooses between:

-- Full Table Scan

-- Index Scan

-- Hash Access

-- =====================================

-- Based On

-- Estimated Cost

-- =====================================
-- JOIN COST ESTIMATION
-- =====================================

-- Joins are expensive operations.

-- =====================================

-- Optimizer estimates:

-- Input Sizes

-- Join Method Cost

-- Intermediate Results

-- =====================================

-- Chooses Best Join Strategy

-- =====================================
-- QUERY PLAN
-- =====================================

-- Query Plan

-- Sequence of operations chosen
-- by the optimizer.

-- =====================================

-- Example

-- Index Scan

-- ↓

-- Selection

-- ↓

-- Join

-- ↓

-- Projection

-- =====================================

-- Different plans

-- Different costs.

-- =====================================
-- HEURISTIC VS COST-BASED
-- =====================================

-- Heuristic Optimization

-- Rule-Based

-- Fast

-- =====================================

-- Cost-Based Optimization

-- Uses Statistics

-- Calculates Cost

-- More Accurate

-- =====================================
-- ADVANTAGES
-- =====================================

-- Better Execution Plans

-- Lower Query Cost

-- Better Performance

-- Efficient Resource Usage

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Optimization Overhead

-- Requires Statistics

-- More Complex

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is Cardinality?

-- Answer:

-- Number of rows in a relation.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- What is Selectivity?

-- Answer:

-- Fraction of rows satisfying
-- a condition.

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Why are statistics important?

-- Answer:

-- Used for cost estimation.

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Cost-Based
-- Query Optimization?

-- Answer:

-- Technique that chooses the
-- lowest-cost execution plan.

-- -------------------------------------

-- Q2. What is Cardinality?

-- Answer:

-- Number of tuples (rows)
-- in a relation.

-- -------------------------------------

-- Q3. What is Selectivity?

-- Answer:

-- Measure of how restrictive
-- a condition is.

-- -------------------------------------

-- Q4. Why does DBMS maintain
-- statistics?

-- Answer:

-- To estimate query cost and
-- select the best execution plan.

-- =====================================
-- DAY 75 SUMMARY
-- =====================================

-- Cost-Based Optimization

-- Uses Estimated Costs

-- -------------------------------------

-- Statistics

-- Used By Optimizer

-- -------------------------------------

-- Cardinality

-- Number Of Rows

-- -------------------------------------

-- Selectivity

-- Fraction Of Matching Rows

-- -------------------------------------

-- Goal

-- Lowest Cost Plan

-- Fastest Query Execution

-- -------------------------------------

-- Cost-Based Optimization is
-- the core technique used by
-- modern DBMS optimizers to
-- achieve high performance.