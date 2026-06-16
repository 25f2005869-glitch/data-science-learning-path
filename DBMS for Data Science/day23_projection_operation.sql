/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 23
Description : Projection Operation (π) in Relational Algebra
*/

-- =====================================
-- DAY 23 : PROJECTION OPERATION (π)
-- =====================================

-- What is Projection?

-- Projection is a unary operation
-- used to select specific columns
-- from a relation.

-- Symbol:

-- π (Pi)

-- Projection works on Columns.

-- =====================================
-- GENERAL FORM
-- =====================================

-- π Attribute_List (Relation)

-- Example:

-- π Name (STUDENT)

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

-- Select only Name column.

-- π Name (STUDENT)

-- Result:

-- Name
-- ------
-- Saloni
-- Rahul
-- Priya
-- Amit

-- =====================================
-- EXAMPLE 2
-- =====================================

-- Select Roll_No and Name.

-- π Roll_No, Name (STUDENT)

-- Result:

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul
-- 103     | Priya
-- 104     | Amit

-- =====================================
-- EXAMPLE 3
-- =====================================

-- Select only Age.

-- π Age (STUDENT)

-- Result:

-- Age
-- ----
-- 20
-- 21
-- 19
-- 22

-- =====================================
-- DUPLICATE ELIMINATION
-- =====================================

-- Projection automatically removes
-- duplicate rows.

-- Example:

-- EMPLOYEE

-- Emp_ID | Department
-- --------------------
-- 1      | HR
-- 2      | HR
-- 3      | IT

-- π Department (EMPLOYEE)

-- Result:

-- HR
-- IT

-- Duplicate HR is removed.

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Projection:

-- Works on Columns

-- Reduces Number of Columns

-- Number of Rows usually remains same

-- Removes Duplicate Rows

-- Output is always a Relation

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Relational Algebra:

-- π Name (STUDENT)

-- SQL:

-- SELECT Name
-- FROM STUDENT;

-- =====================================
-- SELECTION VS PROJECTION
-- =====================================

-- Selection (σ)

-- Selects Rows

-- Uses Conditions

-- Example:

-- σ Age > 20 (STUDENT)

-- Projection (π)

-- Selects Columns

-- Uses Attribute Names

-- Example:

-- π Name (STUDENT)

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Display only Roll_No.

-- Answer:

-- π Roll_No (STUDENT)

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Display Name and Age.

-- Answer:

-- π Name, Age (STUDENT)

-- =====================================
-- DAY 23 SUMMARY
-- =====================================

-- Projection (π)

-- Used to Select Columns

-- Syntax:

-- π Attribute_List (Relation)

-- Removes Duplicate Rows

-- Input  : Relation
-- Output : Relation

-- Projection is a Unary Operation.