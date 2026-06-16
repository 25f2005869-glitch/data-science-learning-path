/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 72
Description : Query Processing Architecture
*/

-- =====================================
-- DAY 72 : QUERY PROCESSING
-- ARCHITECTURE
-- =====================================

-- What is Query Processing Architecture?

-- Query Processing Architecture
-- describes the internal components
-- of a DBMS that process and execute
-- SQL queries.

-- Goal:

-- Efficient Query Execution

-- Minimum Resource Usage

-- Faster Response Time

-- =====================================
-- MAJOR COMPONENTS
-- =====================================

-- 1. Parser

-- 2. Query Translator

-- 3. Query Optimizer

-- 4. Execution Engine

-- 5. Storage Manager

-- =====================================
-- OVERALL FLOW
-- =====================================

-- SQL Query

-- ↓

-- Parser

-- ↓

-- Query Translator

-- ↓

-- Query Optimizer

-- ↓

-- Execution Engine

-- ↓

-- Storage Manager

-- ↓

-- Result

-- =====================================
-- 1. PARSER
-- =====================================

-- First component of
-- Query Processing.

-- =====================================

-- Responsibilities

-- Check Syntax

-- Check SQL Grammar

-- Validate Table Names

-- Validate Column Names

-- =====================================

-- Example

-- SELECT Name

-- FROM STUDENT;

-- Valid Query

-- =====================================

-- Example

-- SELCT Name

-- FROM STUDENT;

-- Syntax Error

-- =====================================

-- Output:

-- Parse Tree

-- =====================================
-- 2. QUERY TRANSLATOR
-- =====================================

-- Converts SQL into
-- Relational Algebra.

-- =====================================

-- Example

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Relational Algebra

-- σ(Student_ID=101)(STUDENT)

-- =====================================

-- Output:

-- Internal Query Representation

-- =====================================
-- 3. QUERY OPTIMIZER
-- =====================================

-- Most Important Component

-- =====================================

-- Goal:

-- Choose Best Execution Plan

-- =====================================

-- Optimizer Evaluates

-- Full Table Scan

-- Index Scan

-- Join Methods

-- Access Paths

-- =====================================

-- Chooses Lowest Cost Plan

-- =====================================

-- Example

-- Table Size

-- 1,000,000 Rows

-- =====================================

-- Full Scan

-- Expensive

-- =====================================

-- Index Scan

-- Cheaper

-- =====================================

-- Optimizer Chooses

-- Index Scan

-- =====================================
-- 4. EXECUTION ENGINE
-- =====================================

-- Executes the selected plan.

-- =====================================

-- Responsibilities

-- Perform Searches

-- Execute Joins

-- Apply Filters

-- Return Results

-- =====================================

-- Example

-- Read Matching Records

-- Return Output

-- =====================================
-- 5. STORAGE MANAGER
-- =====================================

-- Responsible for
-- Physical Data Access.

-- =====================================

-- Handles

-- Files

-- Pages

-- Buffers

-- Indexes

-- Disk Access

-- =====================================

-- Provides Data To

-- Execution Engine

-- =====================================
-- ARCHITECTURE SUMMARY
-- =====================================

-- Parser

-- Syntax Checking

-- -------------------------------------

-- Query Translator

-- SQL → Relational Algebra

-- -------------------------------------

-- Query Optimizer

-- Select Best Plan

-- -------------------------------------

-- Execution Engine

-- Execute Plan

-- -------------------------------------

-- Storage Manager

-- Access Physical Data

-- =====================================
-- EXAMPLE WALKTHROUGH
-- =====================================

-- Query

-- SELECT Name

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Parser

-- Validates Query

-- =====================================

-- Translator

-- Creates Relational Algebra

-- =====================================

-- Optimizer

-- Chooses Index Scan

-- =====================================

-- Execution Engine

-- Executes Search

-- =====================================

-- Storage Manager

-- Reads Data From Disk

-- =====================================

-- Result Returned

-- =====================================
-- BENEFITS
-- =====================================

-- Faster Queries

-- Better Resource Usage

-- Lower Disk Access

-- Improved Performance

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which component checks
-- SQL syntax?

-- Answer:

-- Parser

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which component chooses
-- the best execution plan?

-- Answer:

-- Query Optimizer

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which component accesses
-- physical storage?

-- Answer:

-- Storage Manager

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is the role of
-- Query Optimizer?

-- Answer:

-- Select the lowest-cost
-- execution plan.

-- -------------------------------------

-- Q2. What does Query Translator do?

-- Answer:

-- Converts SQL into
-- Relational Algebra.

-- -------------------------------------

-- Q3. Which component actually
-- executes the query?

-- Answer:

-- Execution Engine

-- =====================================
-- DAY 72 SUMMARY
-- =====================================

-- Query Processing Architecture

-- -------------------------------------

-- Parser

-- Checks Syntax

-- -------------------------------------

-- Query Translator

-- SQL → Relational Algebra

-- -------------------------------------

-- Query Optimizer

-- Chooses Best Plan

-- -------------------------------------

-- Execution Engine

-- Executes Query

-- -------------------------------------

-- Storage Manager

-- Accesses Physical Data

-- -------------------------------------

-- These components work together
-- to execute SQL queries efficiently
-- in a DBMS.