/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 21
Description : Introduction to Relational Algebra
*/

-- =====================================
-- DAY 21 : RELATIONAL ALGEBRA
-- =====================================

-- What is Relational Algebra?

-- Relational Algebra is a procedural
-- query language used to retrieve
-- and manipulate data from relations
-- (tables).

-- It forms the theoretical foundation
-- of SQL.

-- Relational Algebra tells:

-- What data is required
-- AND
-- How to retrieve it

-- =====================================
-- WHY RELATIONAL ALGEBRA?
-- =====================================

-- 1. Query Processing
-- 2. Database Operations
-- 3. SQL Foundation
-- 4. Data Manipulation

-- =====================================
-- BASIC OPERATIONS
-- =====================================

-- 1. Selection (σ)
-- 2. Projection (π)
-- 3. Union (∪)
-- 4. Set Difference (-)
-- 5. Cartesian Product (×)
-- 6. Rename (ρ)

-- =====================================
-- SAMPLE TABLE
-- =====================================

-- STUDENT

-- Roll_No | Name   | Age
-- ------------------------
-- 101     | Saloni | 20
-- 102     | Rahul  | 21
-- 103     | Priya  | 19

-- =====================================
-- SELECTION (σ)
-- =====================================

-- Used to select rows.

-- Symbol:

-- σ

-- Example:

-- Select students whose age is 20.

-- σ Age=20 (STUDENT)

-- Result:

-- 101 | Saloni | 20

-- =====================================
-- PROJECTION (π)
-- =====================================

-- Used to select columns.

-- Symbol:

-- π

-- Example:

-- π Name (STUDENT)

-- Result:

-- Saloni
-- Rahul
-- Priya

-- =====================================
-- UNION (∪)
-- =====================================

-- Combines tuples from
-- two compatible relations.

-- Example:

-- STUDENT_A ∪ STUDENT_B

-- Conditions:

-- Same number of attributes
-- Same domains

-- =====================================
-- SET DIFFERENCE (-)
-- =====================================

-- Returns tuples present in
-- first relation but not in second.

-- Example:

-- STUDENT_A - STUDENT_B

-- =====================================
-- CARTESIAN PRODUCT (×)
-- =====================================

-- Combines every row of first
-- relation with every row
-- of second relation.

-- Example:

-- STUDENT × COURSE

-- If:

-- STUDENT = 3 rows

-- COURSE = 2 rows

-- Result:

-- 3 × 2 = 6 rows

-- =====================================
-- RENAME (ρ)
-- =====================================

-- Used to rename a relation
-- or attribute.

-- Example:

-- ρ S(STUDENT)

-- STUDENT becomes S

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Input:
-- One or More Relations

-- Output:
-- A Relation

-- Therefore Relational Algebra
-- is called a Closed System.

-- =====================================
-- DAY 21 SUMMARY
-- =====================================

-- Relational Algebra
-- --> Foundation of SQL

-- Main Operations:

-- Selection (σ)
-- Projection (π)
-- Union (∪)
-- Difference (-)
-- Cartesian Product (×)
-- Rename (ρ)

-- Input  : Relation
-- Output : Relation

-- Relational Algebra is
-- a Procedural Query Language.