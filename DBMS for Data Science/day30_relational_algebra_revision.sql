/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 30
Description : Complete Revision of Relational Algebra
*/

-- =====================================
-- DAY 30 : RELATIONAL ALGEBRA REVISION
-- =====================================

-- Relational Algebra is a procedural
-- query language used to retrieve
-- and manipulate data from relations.

-- It is the theoretical foundation
-- of SQL.

-- Input  : Relation
-- Output : Relation

-- Therefore Relational Algebra is
-- a Closed System.

-- =====================================
-- OPERATIONS COVERED
-- =====================================

-- 1. Selection (σ)

-- 2. Projection (π)

-- 3. Union (∪)

-- 4. Difference (-)

-- 5. Cartesian Product (×)

-- 6. Rename (ρ)

-- 7. Join (⋈)

-- 8. Division (÷)

-- =====================================
-- 1. SELECTION (σ)
-- =====================================

-- Purpose:

-- Select Rows

-- Syntax:

-- σ Condition(Relation)

-- Example:

-- σ Age > 20(STUDENT)

-- SQL Equivalent:

-- SELECT *
-- FROM STUDENT
-- WHERE Age > 20;

-- =====================================
-- 2. PROJECTION (π)
-- =====================================

-- Purpose:

-- Select Columns

-- Syntax:

-- π Attribute(Relation)

-- Example:

-- π Name(STUDENT)

-- SQL Equivalent:

-- SELECT Name
-- FROM STUDENT;

-- =====================================
-- 3. UNION (∪)
-- =====================================

-- Purpose:

-- Combine Two Relations

-- Syntax:

-- A ∪ B

-- Requirements:

-- Same Number of Attributes

-- Same Domains

-- Same Data Types

-- Removes Duplicates

-- SQL Equivalent:

-- UNION

-- =====================================
-- 4. DIFFERENCE (-)
-- =====================================

-- Purpose:

-- Tuples in A but not in B

-- Syntax:

-- A - B

-- Example:

-- STUDENT_A - STUDENT_B

-- SQL Equivalent:

-- EXCEPT

-- Property:

-- A - B ≠ B - A

-- =====================================
-- 5. CARTESIAN PRODUCT (×)
-- =====================================

-- Purpose:

-- All Possible Combinations

-- Syntax:

-- A × B

-- Formula:

-- Rows = m × n

-- SQL Equivalent:

-- CROSS JOIN

-- =====================================
-- 6. RENAME (ρ)
-- =====================================

-- Purpose:

-- Rename Relation or Attributes

-- Syntax:

-- ρ New_Name(Relation)

-- Example:

-- ρ S(STUDENT)

-- SQL Equivalent:

-- Alias

-- SELECT *
-- FROM STUDENT S;

-- =====================================
-- 7. JOIN (⋈)
-- =====================================

-- Purpose:

-- Combine Related Tables

-- Types:

-- Theta Join

-- Equi Join

-- Natural Join

-- Example:

-- STUDENT ⋈ ENROLLMENT

-- SQL Equivalent:

-- JOIN

-- =====================================
-- 8. DIVISION (÷)
-- =====================================

-- Purpose:

-- Solve "FOR ALL" Queries

-- Example:

-- Students enrolled in
-- all courses.

-- Employees working on
-- all projects.

-- SQL Equivalent:

-- NOT EXISTS
-- GROUP BY
-- HAVING

-- =====================================
-- IMPORTANT COMPARISONS
-- =====================================

-- Selection

-- Works on Rows

-- Projection

-- Works on Columns

-- -------------------------------------

-- Theta Join

-- Uses:
-- =, <, >, <=, >=, !=

-- Equi Join

-- Uses:
-- = only

-- Natural Join

-- Automatically matches
-- common attributes.

-- -------------------------------------

-- Union

-- Combines Relations

-- Difference

-- Removes Common Tuples

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Relational Algebra?

-- A procedural query language
-- forming the foundation of SQL.

-- -------------------------------------

-- Q2. Which operation selects rows?

-- Selection (σ)

-- -------------------------------------

-- Q3. Which operation selects columns?

-- Projection (π)

-- -------------------------------------

-- Q4. Which operation forms
-- the basis of Join?

-- Cartesian Product (×)

-- -------------------------------------

-- Q5. Which operation is used
-- for "FOR ALL" queries?

-- Division (÷)

-- =====================================
-- DAY 30 SUMMARY
-- =====================================

-- Selection (σ)
-- --> Rows

-- Projection (π)
-- --> Columns

-- Union (∪)
-- --> Combine Relations

-- Difference (-)
-- --> Tuples in A not in B

-- Cartesian Product (×)
-- --> All Combinations

-- Rename (ρ)
-- --> Rename Relations

-- Join (⋈)
-- --> Combine Related Tables

-- Division (÷)
-- --> FOR ALL Queries

-- Relational Algebra is the
-- foundation of SQL and DBMS.