/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 73
Description : Query Optimization Basics
*/

-- =====================================
-- DAY 73 : QUERY OPTIMIZATION BASICS
-- =====================================

-- What is Query Optimization?

-- Query Optimization is the process
-- of selecting the most efficient
-- execution plan for a query.

-- Goal:

-- Minimize Query Cost

-- Minimize Disk Access

-- Minimize CPU Usage

-- Improve Performance

-- =====================================
-- WHY QUERY OPTIMIZATION?
-- =====================================

-- A SQL query can often be
-- executed in multiple ways.

-- DBMS must choose the
-- best execution strategy.

-- =====================================
-- EXAMPLE
-- =====================================

-- Query

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Possible Plans

-- Plan 1

-- Full Table Scan

-- -------------------------------------

-- Plan 2

-- Index Scan

-- =====================================

-- Optimizer chooses:

-- Lower Cost Plan

-- Usually Index Scan

-- =====================================
-- QUERY COST
-- =====================================

-- Query Cost represents the
-- resources required to execute
-- a query.

-- =====================================

-- Cost Factors

-- Disk I/O

-- CPU Time

-- Memory Usage

-- Network Cost

-- =====================================

-- Most Expensive:

-- Disk Access

-- =====================================
-- ACCESS PATHS
-- =====================================

-- Access Path means the method
-- used to retrieve records.

-- =====================================

-- Common Access Paths

-- Full Table Scan

-- Index Scan

-- Hash Access

-- =====================================
-- 1. FULL TABLE SCAN
-- =====================================

-- Reads every row in table.

-- =====================================

-- Example

-- SELECT *

-- FROM STUDENT;

-- =====================================

-- Advantages

-- Simple

-- =====================================

-- Disadvantages

-- Expensive For Large Tables

-- =====================================
-- 2. INDEX SCAN
-- =====================================

-- Uses Index Structure

-- Example:

-- B+ Tree

-- =====================================

-- Faster Search

-- Less Disk Access

-- =====================================

-- Example

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Index Used

-- Faster Retrieval

-- =====================================
-- 3. HASH ACCESS
-- =====================================

-- Uses Hash Index

-- =====================================

-- Best For

-- Equality Search

-- =====================================

-- Example

-- WHERE Student_ID = 101

-- =====================================

-- Average Search

-- O(1)

-- =====================================
-- EVALUATION PLAN
-- =====================================

-- Evaluation Plan is the
-- sequence of operations chosen
-- by the optimizer.

-- =====================================

-- Example Plan

-- Use Index

-- Apply Selection

-- Return Results

-- =====================================

-- Different Plans

-- Different Costs

-- =====================================
-- OPTIMIZER OBJECTIVE
-- =====================================

-- Find Lowest Cost Plan

-- =====================================

-- Example

-- Plan A

-- Cost = 500

-- -------------------------------------

-- Plan B

-- Cost = 100

-- =====================================

-- Choose Plan B

-- =====================================
-- FACTORS AFFECTING COST
-- =====================================

-- Table Size

-- Number Of Records

-- Available Indexes

-- Memory Availability

-- Join Operations

-- Disk Blocks

-- =====================================
-- EXAMPLE WALKTHROUGH
-- =====================================

-- Query

-- SELECT Name

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Parser

-- Checks Syntax

-- =====================================

-- Translator

-- Creates Relational Algebra

-- =====================================

-- Optimizer

-- Compares Plans

-- =====================================

-- Chooses Index Scan

-- =====================================

-- Execution Engine

-- Executes Query

-- =====================================
-- BENEFITS
-- =====================================

-- Faster Queries

-- Better Performance

-- Lower Resource Usage

-- Improved Scalability

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is Query Optimization?

-- Answer:

-- Process of selecting the
-- most efficient execution plan.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which operation usually has
-- highest cost?

-- Answer:

-- Disk I/O

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which access path uses
-- B+ Tree indexes?

-- Answer:

-- Index Scan

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Why is Query Optimization
-- important?

-- Answer:

-- It improves query performance
-- by selecting the lowest-cost plan.

-- -------------------------------------

-- Q2. What is Query Cost?

-- Answer:

-- Measure of resources needed
-- to execute a query.

-- -------------------------------------

-- Q3. What are common
-- access paths?

-- Answer:

-- Full Table Scan

-- Index Scan

-- Hash Access

-- =====================================
-- DAY 73 SUMMARY
-- =====================================

-- Query Optimization

-- Select Best Execution Plan

-- -------------------------------------

-- Query Cost

-- Disk I/O

-- CPU

-- Memory

-- -------------------------------------

-- Access Paths

-- Full Table Scan

-- Index Scan

-- Hash Access

-- -------------------------------------

-- Evaluation Plan

-- Sequence Of Operations

-- -------------------------------------

-- Goal

-- Lowest Cost

-- Fastest Execution

-- Query Optimization is the key
-- technique used by DBMS to
-- achieve high performance.