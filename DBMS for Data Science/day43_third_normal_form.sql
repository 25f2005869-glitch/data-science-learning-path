/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 43
Description : Third Normal Form (3NF)
*/

-- =====================================
-- DAY 43 : THIRD NORMAL FORM (3NF)
-- =====================================

-- What is 3NF?

-- A relation is in Third Normal Form
-- if:

-- 1. It is already in 2NF

-- AND

-- 2. It contains NO Transitive Dependency

-- =====================================
-- WHAT IS TRANSITIVE DEPENDENCY?
-- =====================================

-- Transitive Dependency occurs when
-- a non-key attribute depends on
-- another non-key attribute.

-- General Form:

-- A → B

-- B → C

-- Therefore:

-- A → C

-- Here:

-- C is transitively dependent on A.

-- =====================================
-- EXAMPLE
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Emp_Name
-- Dept_ID
-- Dept_Name

-- Primary Key:

-- Emp_ID

-- Functional Dependencies:

-- Emp_ID → Emp_Name

-- Emp_ID → Dept_ID

-- Dept_ID → Dept_Name

-- =====================================
-- ANALYSIS
-- =====================================

-- Emp_ID determines Dept_ID

-- Dept_ID determines Dept_Name

-- Therefore:

-- Emp_ID determines Dept_Name

-- through Dept_ID

-- This is:

-- Transitive Dependency

-- Relation is NOT in 3NF.

-- =====================================
-- CONVERT TO 3NF
-- =====================================

-- Split Relation

-- EMPLOYEE

-- Emp_ID
-- Emp_Name
-- Dept_ID

-- -------------------------------------

-- DEPARTMENT

-- Dept_ID
-- Dept_Name

-- =====================================
-- RESULT
-- =====================================

-- EMPLOYEE

-- Emp_ID → Emp_Name

-- Emp_ID → Dept_ID

-- -------------------------------------

-- DEPARTMENT

-- Dept_ID → Dept_Name

-- No Transitive Dependency Exists.

-- Therefore:

-- Relation is in 3NF.

-- =====================================
-- WHY REMOVE TRANSITIVE DEPENDENCY?
-- =====================================

-- Reduces Redundancy

-- Eliminates Update Anomalies

-- Improves Consistency

-- Better Database Structure

-- =====================================
-- 2NF VS 3NF
-- =====================================

-- 2NF

-- Removes Partial Dependency

-- -------------------------------------

-- 3NF

-- Removes Transitive Dependency

-- =====================================
-- IMPORTANT RULE
-- =====================================

-- For every Functional Dependency:

-- X → A

-- One of the following must be true:

-- 1. X is a Super Key

-- OR

-- 2. A is a Prime Attribute

-- Then relation is in 3NF.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Dept_ID
-- Dept_Name

-- FD:

-- Emp_ID → Dept_ID

-- Dept_ID → Dept_Name

-- Answer:

-- Transitive Dependency Exists

-- Not in 3NF

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- STUDENT

-- Roll_No
-- Name

-- FD:

-- Roll_No → Name

-- Answer:

-- No Transitive Dependency

-- Can be in 3NF

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is Third Normal Form?

-- Answer:

-- A relation is in 3NF if it is
-- already in 2NF and contains
-- no Transitive Dependency.

-- =====================================
-- DAY 43 SUMMARY
-- =====================================

-- 3NF

-- Must satisfy 2NF

-- No Transitive Dependency

-- Removes Redundancy

-- Improves Integrity

-- Example:

-- Emp_ID → Dept_ID

-- Dept_ID → Dept_Name

-- Causes Transitive Dependency

-- 3NF removes such dependencies.