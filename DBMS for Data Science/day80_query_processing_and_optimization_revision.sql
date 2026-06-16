/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 80
Description : Complete Revision of Query Processing and Query Optimization
*/

-- =====================================
-- DAY 80 : COMPLETE REVISION
-- QUERY PROCESSING & OPTIMIZATION
-- =====================================

-- This day revises all concepts
-- covered from Day 71 to Day 79.

-- =====================================
-- TOPICS COVERED
-- =====================================

-- 1. Query Processing

-- 2. Query Processing Architecture

-- 3. Query Optimization Basics

-- 4. Heuristic Optimization

-- 5. Cost-Based Optimization

-- 6. Join Processing

-- 7. Nested Loop Join

-- 8. Sort-Merge Join

-- 9. Hash Join

-- 10. Query Execution Plans

-- =====================================
-- QUERY PROCESSING
-- =====================================

-- Query Processing converts
-- SQL queries into efficient
-- execution operations.

-- =====================================

-- Main Goal

-- Fast Execution

-- Low Cost

-- Efficient Resource Usage

-- =====================================
-- PHASES OF QUERY PROCESSING
-- =====================================

-- SQL Query

-- ↓

-- Parsing

-- ↓

-- Translation

-- ↓

-- Optimization

-- ↓

-- Evaluation

-- ↓

-- Result

-- =====================================
-- QUERY PROCESSING ARCHITECTURE
-- =====================================

-- Parser

-- Checks Syntax

-- =====================================

-- Query Translator

-- SQL → Relational Algebra

-- =====================================

-- Query Optimizer

-- Chooses Best Plan

-- =====================================

-- Execution Engine

-- Executes Plan

-- =====================================

-- Storage Manager

-- Accesses Physical Data

-- =====================================
-- QUERY OPTIMIZATION
-- =====================================

-- Goal:

-- Select Lowest Cost
-- Execution Plan

-- =====================================

-- Reduce

-- Disk I/O

-- CPU Cost

-- Memory Usage

-- =====================================
-- ACCESS PATHS
-- =====================================

-- Full Table Scan

-- Index Scan

-- Hash Access

-- =====================================

-- Optimizer chooses best
-- access path.

-- =====================================
-- HEURISTIC OPTIMIZATION
-- =====================================

-- Rule-Based Optimization

-- =====================================

-- Important Rules

-- Selection Pushdown

-- Projection Pushdown

-- Join Optimization

-- Query Tree Optimization

-- =====================================

-- Goal

-- Reduce Intermediate Results

-- =====================================
-- SELECTION PUSHDOWN
-- =====================================

-- Apply Selection Early

-- =====================================

-- Example

-- σ(Dept='CSE')

-- Before Join

-- =====================================

-- Benefit

-- Smaller Relations

-- Faster Processing

-- =====================================
-- PROJECTION PUSHDOWN
-- =====================================

-- Apply Projection Early

-- =====================================

-- Remove Unnecessary Columns

-- =====================================

-- Benefit

-- Less Memory

-- Less Data Transfer

-- =====================================
-- COST-BASED OPTIMIZATION
-- =====================================

-- Uses Statistics

-- Estimates Query Cost

-- =====================================

-- Chooses Plan With

-- Lowest Cost

-- =====================================
-- IMPORTANT TERMS
-- =====================================

-- Cardinality

-- Number Of Rows

-- =====================================

-- Selectivity

-- Matching Rows

-- ----------------

-- Total Rows

-- =====================================

-- Statistics

-- Used For Cost Estimation

-- =====================================
-- JOIN PROCESSING
-- =====================================

-- Join Operations Are Expensive

-- =====================================

-- Optimizer Chooses

-- Best Join Algorithm

-- =====================================
-- JOIN ALGORITHMS
-- =====================================

-- Nested Loop Join

-- Sort-Merge Join

-- Hash Join

-- =====================================
-- NESTED LOOP JOIN
-- =====================================

-- Compare Every Row

-- With Every Row

-- =====================================

-- Complexity

-- O(n × m)

-- =====================================

-- Advantage

-- Simple

-- =====================================

-- Best For

-- Small Tables

-- =====================================
-- SORT-MERGE JOIN
-- =====================================

-- Sort Relations

-- Then Merge

-- =====================================

-- Complexity

-- Sorting + Merging

-- =====================================

-- Best For

-- Large Sorted Data

-- Range Conditions

-- =====================================
-- HASH JOIN
-- =====================================

-- Build Phase

-- Create Hash Table

-- =====================================

-- Probe Phase

-- Find Matches

-- =====================================

-- Complexity

-- O(n + m)

-- =====================================

-- Best For

-- Equality Joins

-- =====================================
-- JOIN COMPARISON
-- =====================================

-- Nested Loop Join

-- O(n × m)

-- =====================================

-- Sort-Merge Join

-- Requires Sorting

-- =====================================

-- Hash Join

-- O(n + m)

-- =====================================

-- Fastest For Equality Joins

-- =====================================
-- QUERY EXECUTION PLAN
-- =====================================

-- Execution Strategy Chosen
-- By Optimizer

-- =====================================

-- Components

-- Execution Tree

-- Operator Tree

-- =====================================

-- Generated After

-- Optimization Phase

-- =====================================
-- EXECUTION TREE
-- =====================================

-- Represents Actual
-- Execution Operations

-- =====================================

-- Root Node

-- Final Result

-- =====================================

-- Leaf Nodes

-- Base Relations

-- =====================================
-- OPERATOR TREE
-- =====================================

-- Represents Relational
-- Algebra Operations

-- =====================================

-- Common Operators

-- Selection

-- Projection

-- Join

-- Sort

-- Aggregate

-- =====================================
-- EXPLAIN COMMAND
-- =====================================

-- Displays Query Plan

-- =====================================

-- Example

-- EXPLAIN

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Shows

-- Access Path

-- Estimated Cost

-- Number Of Rows

-- Operations Used

-- =====================================
-- QUICK REVISION TABLE
-- =====================================

-- Parsing

-- Syntax Checking

-- -------------------------------------

-- Translation

-- SQL → Relational Algebra

-- -------------------------------------

-- Optimization

-- Select Best Plan

-- -------------------------------------

-- Evaluation

-- Execute Query

-- -------------------------------------

-- Cardinality

-- Number Of Rows

-- -------------------------------------

-- Selectivity

-- Fraction Of Matching Rows

-- -------------------------------------

-- Nested Loop

-- O(n × m)

-- -------------------------------------

-- Sort-Merge

-- Sort + Merge

-- -------------------------------------

-- Hash Join

-- O(n + m)

-- -------------------------------------

-- EXPLAIN

-- Show Query Plan

-- =====================================
-- IMPORTANT INTERVIEW QUESTIONS
-- =====================================

-- Q1. What are the phases of
-- Query Processing?

-- Answer:

-- Parsing

-- Translation

-- Optimization

-- Evaluation

-- -------------------------------------

-- Q2. Difference between
-- Heuristic and Cost-Based
-- Optimization?

-- Answer:

-- Heuristic:

-- Rule-Based

-- -------------------------------------

-- Cost-Based:

-- Statistics + Cost Estimation

-- -------------------------------------

-- Q3. What is Cardinality?

-- Answer:

-- Number Of Rows In A Relation

-- -------------------------------------

-- Q4. Which join is best for
-- equality conditions?

-- Answer:

-- Hash Join

-- -------------------------------------

-- Q5. Which command displays
-- execution plans?

-- Answer:

-- EXPLAIN

-- =====================================
-- DAY 80 SUMMARY
-- =====================================

-- Query Processing

-- Query Optimization

-- Query Architecture

-- Heuristic Optimization

-- Cost-Based Optimization

-- Join Processing

-- Nested Loop Join

-- Sort-Merge Join

-- Hash Join

-- Query Execution Plans

-- =====================================

-- UNIT COMPLETE

-- Day 71 → Query Processing

-- Day 72 → Query Processing Architecture

-- Day 73 → Query Optimization Basics

-- Day 74 → Heuristic Optimization

-- Day 75 → Cost-Based Optimization

-- Day 76 → Join Processing

-- Day 77 → Nested Loop & Sort-Merge

-- Day 78 → Hash Join

-- Day 79 → Query Execution Plans

-- Day 80 → Complete Revision

-- =====================================

-- END OF QUERY PROCESSING
-- & QUERY OPTIMIZATION UNIT