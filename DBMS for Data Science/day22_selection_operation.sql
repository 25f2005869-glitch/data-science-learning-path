/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 22
Description : Selection Operation (σ) in Relational Algebra
*/

-- =====================================
-- DAY 22 : SELECTION OPERATION (σ)
-- =====================================

-- What is Selection?

-- Selection is a unary operation
-- used to select specific rows
-- from a relation based on a condition.

-- Symbol:

-- σ (Sigma)

-- Selection works on Rows.

-- =====================================
-- GENERAL FORM
-- =====================================

-- σ Condition (Relation)

-- Example:

-- σ Age > 20 (STUDENT)

-- =====================================
-- SAMPLE TABLE
-- =====================================

-- STUDENT

-- Roll_No | Name   | Age
-- ------------------------
-- 101     | Saloni | 20
-- 102     | Rahul  | 21
-- 103     | Priya  | 19
-- 104     | Amit   | 22

-- =====================================
-- EXAMPLE 1
-- =====================================

-- Select students whose age is 20.

-- σ Age = 20 (STUDENT)

-- Result:

-- 101 | Saloni | 20

-- =====================================
-- EXAMPLE 2
-- =====================================

-- Select students whose age is
-- greater than 20.

-- σ Age > 20 (STUDENT)

-- Result:

-- 102 | Rahul | 21
-- 104 | Amit  | 22

-- =====================================
-- EXAMPLE 3
-- =====================================

-- Select student whose Roll_No is 103.

-- σ Roll_No = 103 (STUDENT)

-- Result:

-- 103 | Priya | 19

-- =====================================
-- COMPARISON OPERATORS
-- =====================================

-- =   Equal To

-- >   Greater Than

-- <   Less Than

-- >=  Greater Than Equal To

-- <=  Less Than Equal To

-- !=  Not Equal To

-- =====================================
-- LOGICAL OPERATORS
-- =====================================

-- AND (∧)

-- OR (∨)

-- NOT (¬)

-- =====================================
-- EXAMPLE 4
-- =====================================

-- σ Age > 20 AND Roll_No = 104
-- (STUDENT)

-- Result:

-- 104 | Amit | 22

-- =====================================
-- EXAMPLE 5
-- =====================================

-- σ Age = 20 OR Age = 22
-- (STUDENT)

-- Result:

-- 101 | Saloni | 20
-- 104 | Amit   | 22

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Selection:

-- Works on Rows

-- Reduces Number of Rows

-- Number of Columns remains same

-- Output is always a Relation

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Relational Algebra:

-- σ Age > 20 (STUDENT)

-- SQL:

-- SELECT *
-- FROM STUDENT
-- WHERE Age > 20;

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Find students whose age is 19.

-- Answer:

-- σ Age = 19 (STUDENT)

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Find students whose Roll_No > 102.

-- Answer:

-- σ Roll_No > 102 (STUDENT)

-- =====================================
-- DAY 22 SUMMARY
-- =====================================

-- Selection (σ)

-- Used to Select Rows

-- Syntax:

-- σ Condition (Relation)

-- Uses:

-- Comparison Operators
-- Logical Operators

-- Input  : Relation
-- Output : Relation

-- Selection is a Unary Operation.