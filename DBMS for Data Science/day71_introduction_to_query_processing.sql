/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 71
Description : Introduction to Query Processing
*/

-- =====================================
-- DAY 71 : INTRODUCTION TO
-- QUERY PROCESSING
-- =====================================

-- What is Query Processing?

-- Query Processing is the process
-- by which a DBMS converts a SQL
-- query into an efficient sequence
-- of operations to retrieve data.

-- Goal:

-- Execute Queries Efficiently

-- Minimize Execution Time

-- Minimize Resource Usage

-- =====================================
-- WHY QUERY PROCESSING?
-- =====================================

-- Users write SQL queries.

-- Database cannot directly execute
-- SQL statements.

-- DBMS must:

-- Understand Query

-- Translate Query

-- Optimize Query

-- Execute Query

-- =====================================
-- EXAMPLE QUERY
-- =====================================

-- SELECT Name

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- User writes SQL.

-- DBMS converts it into
-- internal operations.

-- =====================================
-- QUERY PROCESSING PHASES
-- =====================================

-- 1. Parsing

-- 2. Translation

-- 3. Optimization

-- 4. Evaluation

-- =====================================
-- 1. PARSING
-- =====================================

-- Parser checks:

-- Syntax Errors

-- SQL Grammar

-- Table Names

-- Column Names

-- =====================================

-- Example

-- SELECT Name

-- FROM STUDENT;

-- Valid Query

-- =====================================

-- Example

-- SELCT Name

-- FROM STUDENT;

-- Invalid Query

-- Syntax Error

-- =====================================
-- OUTPUT OF PARSER
-- =====================================

-- Parse Tree

-- Represents query structure.

-- =====================================
-- 2. TRANSLATION
-- =====================================

-- SQL Query converted into

-- Relational Algebra Expression

-- =====================================

-- Example

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Relational Algebra

-- σ(Student_ID = 101)(STUDENT)

-- =====================================
-- 3. QUERY OPTIMIZATION
-- =====================================

-- Multiple execution plans
-- may exist.

-- DBMS chooses the best plan.

-- =====================================

-- Goal

-- Reduce Cost

-- Reduce Disk Access

-- Reduce CPU Usage

-- =====================================
-- EXAMPLE
-- =====================================

-- Table Size

-- 1 Million Records

-- =====================================

-- Method 1

-- Full Table Scan

-- =====================================

-- Method 2

-- Use Index

-- =====================================

-- Optimizer chooses:

-- Index Scan

-- Faster

-- =====================================
-- 4. QUERY EVALUATION
-- =====================================

-- Selected plan is executed.

-- Results returned to user.

-- =====================================

-- Example

-- Student_ID = 101

-- Record Found

-- Return Result

-- =====================================
-- QUERY PROCESSING FLOW
-- =====================================

-- SQL Query

-- ↓

-- Parser

-- ↓

-- Relational Algebra

-- ↓

-- Query Optimizer

-- ↓

-- Execution Plan

-- ↓

-- Query Evaluation

-- ↓

-- Result

-- =====================================
-- IMPORTANCE OF QUERY PROCESSING
-- =====================================

-- Faster Execution

-- Better Resource Usage

-- Lower Response Time

-- Improved Scalability

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is Query Processing?

-- Answer:

-- Process of translating and
-- executing SQL queries.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which phase checks syntax?

-- Answer:

-- Parsing

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which phase chooses the
-- best execution plan?

-- Answer:

-- Query Optimization

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What are the major phases
-- of Query Processing?

-- Answer:

-- Parsing

-- Translation

-- Optimization

-- Evaluation

-- -------------------------------------

-- Q2. Why is Query Optimization
-- important?

-- Answer:

-- It reduces execution cost
-- and improves performance.

-- -------------------------------------

-- Q3. What is produced after
-- SQL translation?

-- Answer:

-- Relational Algebra Expression

-- =====================================
-- DAY 71 SUMMARY
-- =====================================

-- Query Processing

-- Converts SQL Into Operations

-- -------------------------------------

-- Phases

-- Parsing

-- Translation

-- Optimization

-- Evaluation

-- -------------------------------------

-- Goal

-- Fast Query Execution

-- Efficient Resource Usage

-- -------------------------------------

-- Query Processing is the
-- foundation of query
-- optimization in DBMS.