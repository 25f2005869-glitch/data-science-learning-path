/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 28
Description : Introduction to Join Operations
*/

-- =====================================
-- DAY 28 : JOIN OPERATIONS
-- =====================================

-- What is a Join?

-- A Join operation combines rows
-- from two or more relations
-- based on a related attribute.

-- Joins are among the most important
-- operations in Relational Algebra
-- and SQL.

-- =====================================
-- WHY JOINS?
-- =====================================

-- 1. Combine Data from Multiple Tables

-- 2. Reduce Redundancy

-- 3. Retrieve Related Information

-- 4. Support Complex Queries

-- =====================================
-- SAMPLE TABLES
-- =====================================

-- STUDENT

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul

-- ENROLLMENT

-- Roll_No | Course
-- -------------------
-- 101     | DBMS
-- 102     | Python

-- =====================================
-- JOIN TYPES
-- =====================================

-- 1. Theta Join (θ Join)

-- 2. Equi Join

-- 3. Natural Join

-- =====================================
-- 1. THETA JOIN (θ)
-- =====================================

-- Join using any comparison operator.

-- Operators:

-- =
-- <
-- >
-- <=
-- >=
-- !=

-- General Form:

-- STUDENT θ Condition ENROLLMENT

-- Example:

-- STUDENT.Roll_No =
-- ENROLLMENT.Roll_No

-- =====================================
-- 2. EQUI JOIN
-- =====================================

-- Special case of Theta Join.

-- Uses only "=" operator.

-- Example:

-- STUDENT ⋈
-- STUDENT.Roll_No =
-- ENROLLMENT.Roll_No
-- ENROLLMENT

-- Result:

-- Roll_No | Name   | Course
-- --------------------------
-- 101     | Saloni | DBMS
-- 102     | Rahul  | Python

-- =====================================
-- 3. NATURAL JOIN
-- =====================================

-- Automatically joins tables
-- using common attribute names.

-- Common attribute appears
-- only once in result.

-- Example:

-- STUDENT

-- Roll_No | Name

-- ENROLLMENT

-- Roll_No | Course

-- STUDENT ⋈ ENROLLMENT

-- Result:

-- Roll_No | Name   | Course
-- --------------------------
-- 101     | Saloni | DBMS
-- 102     | Rahul  | Python

-- =====================================
-- THETA JOIN VS EQUI JOIN
-- =====================================

-- Theta Join

-- Uses:
-- =, <, >, <=, >=, !=

-- Equi Join

-- Uses:
-- = only

-- Every Equi Join is a Theta Join.

-- Every Theta Join is NOT
-- an Equi Join.

-- =====================================
-- EQUI JOIN VS NATURAL JOIN
-- =====================================

-- Equi Join

-- Duplicate join columns may appear.

-- Natural Join

-- Duplicate join columns are removed.

-- Common attributes matched automatically.

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Equi Join

-- SELECT *
-- FROM STUDENT S
-- JOIN ENROLLMENT E
-- ON S.Roll_No = E.Roll_No;

-- Natural Join

-- SELECT *
-- FROM STUDENT
-- NATURAL JOIN ENROLLMENT;

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- STUDENT

-- Roll_No | Name

-- COURSE_REG

-- Roll_No | Course

-- Find student names with courses.

-- Answer:

-- Natural Join or Equi Join

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Can Natural Join work without
-- common attribute names?

-- Answer:

-- No

-- =====================================
-- DAY 28 SUMMARY
-- =====================================

-- Join

-- Combines Multiple Relations

-- Types:

-- Theta Join (θ)

-- Equi Join

-- Natural Join

-- Theta Join:
-- Any Comparison Operator

-- Equi Join:
-- Equal (=) Only

-- Natural Join:
-- Automatic Matching of
-- Common Attributes

-- Join is one of the most
-- important operations in DBMS.