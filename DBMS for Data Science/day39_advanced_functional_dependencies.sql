/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 39
Description : Full Functional Dependency, Partial Dependency and Transitive Dependency
*/

-- =====================================
-- DAY 39 : ADVANCED FUNCTIONAL
-- DEPENDENCY CONCEPTS
-- =====================================

-- These concepts are important for:

-- 1. Normalization

-- 2. Database Design

-- 3. Removing Redundancy

-- 4. Improving Data Integrity

-- =====================================
-- TYPES OF DEPENDENCIES
-- =====================================

-- 1. Full Functional Dependency

-- 2. Partial Dependency

-- 3. Transitive Dependency

-- =====================================
-- 1. FULL FUNCTIONAL DEPENDENCY
-- =====================================

-- Definition:

-- Y is Fully Functionally Dependent
-- on X if Y depends on the whole X
-- and not on any subset of X.

-- Example:

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Grade

-- Functional Dependency:

-- (Student_ID, Course_ID) → Grade

-- Grade depends on both
-- Student_ID and Course_ID.

-- Removing either attribute
-- breaks the dependency.

-- Therefore:

-- Full Functional Dependency.

-- =====================================
-- 2. PARTIAL DEPENDENCY
-- =====================================

-- Definition:

-- Y is Partially Dependent on X
-- if Y depends on only a part
-- of the composite key.

-- Example:

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Student_Name

-- Functional Dependency:

-- (Student_ID, Course_ID)
-- →
-- Student_Name

-- But:

-- Student_ID
-- →
-- Student_Name

-- Student_Name depends only on
-- Student_ID.

-- Therefore:

-- Partial Dependency exists.

-- =====================================
-- WHY PARTIAL DEPENDENCY IS BAD?
-- =====================================

-- Causes:

-- Data Redundancy

-- Update Anomalies

-- Insertion Anomalies

-- Deletion Anomalies

-- Removed in:

-- Second Normal Form (2NF)

-- =====================================
-- 3. TRANSITIVE DEPENDENCY
-- =====================================

-- Definition:

-- If:

-- A → B

-- B → C

-- Then:

-- A → C

-- C is transitively dependent on A.

-- =====================================
-- EXAMPLE
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Dept_ID
-- Dept_Name

-- Functional Dependencies:

-- Emp_ID → Dept_ID

-- Dept_ID → Dept_Name

-- Therefore:

-- Emp_ID → Dept_Name

-- This is a Transitive Dependency.

-- =====================================
-- WHY TRANSITIVE DEPENDENCY IS BAD?
-- =====================================

-- Causes:

-- Data Redundancy

-- Update Problems

-- Inconsistent Data

-- Removed in:

-- Third Normal Form (3NF)

-- =====================================
-- COMPARISON
-- =====================================

-- Full Functional Dependency

-- Depends on complete key.

-- Example:

-- (Student_ID, Course_ID)
-- →
-- Grade

-- -------------------------------------

-- Partial Dependency

-- Depends on part of key.

-- Example:

-- Student_ID
-- →
-- Student_Name

-- -------------------------------------

-- Transitive Dependency

-- Depends through another attribute.

-- Example:

-- Emp_ID
-- →
-- Dept_ID
-- →
-- Dept_Name

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Relation:

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Grade

-- FD:

-- (Student_ID, Course_ID)
-- →
-- Grade

-- Answer:

-- Full Functional Dependency

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Relation:

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Student_Name

-- FD:

-- Student_ID
-- →
-- Student_Name

-- Answer:

-- Partial Dependency

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Relation:

-- EMPLOYEE

-- Emp_ID
-- Dept_ID
-- Dept_Name

-- FD:

-- Emp_ID → Dept_ID

-- Dept_ID → Dept_Name

-- Answer:

-- Transitive Dependency

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Full Functional Dependency?

-- Answer:

-- Dependency on entire key.

-- -------------------------------------

-- Q2. What is Partial Dependency?

-- Answer:

-- Dependency on part of a
-- composite key.

-- -------------------------------------

-- Q3. What is Transitive Dependency?

-- Answer:

-- Dependency through another
-- non-key attribute.

-- =====================================
-- DAY 39 SUMMARY
-- =====================================

-- Full Functional Dependency

-- Depends on complete key.

-- Removed Issues:
-- None

-- -------------------------------------

-- Partial Dependency

-- Depends on part of key.

-- Removed in:
-- 2NF

-- -------------------------------------

-- Transitive Dependency

-- Depends through another attribute.

-- Removed in:
-- 3NF

-- These dependencies form the
-- foundation of Normalization.