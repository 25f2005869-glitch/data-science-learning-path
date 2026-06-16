/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 45
Description : Comparison of 1NF, 2NF, 3NF and BCNF
*/

-- =====================================
-- DAY 45 : COMPARISON OF
-- 1NF, 2NF, 3NF AND BCNF
-- =====================================

-- Normalization is a process used
-- to reduce redundancy and improve
-- database design.

-- =====================================
-- NORMALIZATION HIERARCHY
-- =====================================

-- UNF

-- ↓

-- 1NF

-- ↓

-- 2NF

-- ↓

-- 3NF

-- ↓

-- BCNF

-- =====================================
-- FIRST NORMAL FORM (1NF)
-- =====================================

-- Rule:

-- Every attribute must contain
-- atomic (single) values.

-- Removes:

-- Repeating Groups

-- Multi-Valued Attributes

-- Example:

-- NOT IN 1NF

-- Student_ID | Phone_Numbers

-- 101        | 9876,8765

-- -------------------------------------

-- IN 1NF

-- Student_ID | Phone_Number

-- 101        | 9876

-- 101        | 8765

-- =====================================
-- SECOND NORMAL FORM (2NF)
-- =====================================

-- Rule:

-- Must be in 1NF

-- No Partial Dependency

-- Removes:

-- Partial Dependency

-- Example:

-- Student_ID
-- Course_ID
-- Student_Name

-- (Student_ID, Course_ID)
-- →
-- Student_Name

-- Student_Name depends only on
-- Student_ID.

-- Therefore:

-- Partial Dependency Exists.

-- =====================================
-- THIRD NORMAL FORM (3NF)
-- =====================================

-- Rule:

-- Must be in 2NF

-- No Transitive Dependency

-- Removes:

-- Transitive Dependency

-- Example:

-- Emp_ID
-- →
-- Dept_ID

-- Dept_ID
-- →
-- Dept_Name

-- Therefore:

-- Emp_ID
-- →
-- Dept_Name

-- Transitive Dependency Exists.

-- =====================================
-- BOYCE CODD NORMAL FORM
-- =====================================

-- Rule:

-- For every FD

-- X → Y

-- X must be a Super Key.

-- Stronger version of 3NF.

-- Removes:

-- Remaining Redundancy

-- Remaining Anomalies

-- =====================================
-- COMPARISON TABLE
-- =====================================

-- 1NF

-- Removes:

-- Multi-Valued Attributes

-- Main Rule:

-- Atomic Values

-- -------------------------------------

-- 2NF

-- Removes:

-- Partial Dependency

-- Main Rule:

-- Full Functional Dependency

-- -------------------------------------

-- 3NF

-- Removes:

-- Transitive Dependency

-- Main Rule:

-- No Non-Key to Non-Key Dependency

-- -------------------------------------

-- BCNF

-- Removes:

-- All FD-Based Redundancy

-- Main Rule:

-- Determinant must be Super Key

-- =====================================
-- PRACTICAL EXAMPLE
-- =====================================

-- Relation:

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Student_Name
-- Instructor_Name

-- Candidate Key:

-- (Student_ID, Course_ID)

-- Student_ID
-- →
-- Student_Name

-- Course_ID
-- →
-- Instructor_Name

-- =====================================

-- Problem:

-- Partial Dependency Exists

-- Therefore:

-- Not in 2NF

-- =====================================

-- After Decomposition

-- STUDENT

-- Student_ID
-- Student_Name

-- COURSE

-- Course_ID
-- Instructor_Name

-- ENROLLMENT

-- Student_ID
-- Course_ID

-- =====================================

-- Relation becomes closer
-- to higher normal forms.

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is 1NF?

-- Answer:

-- Atomic values only.

-- -------------------------------------

-- Q2. What is removed in 2NF?

-- Answer:

-- Partial Dependency.

-- -------------------------------------

-- Q3. What is removed in 3NF?

-- Answer:

-- Transitive Dependency.

-- -------------------------------------

-- Q4. What is BCNF?

-- Answer:

-- For every FD:

-- X → Y

-- X must be a Super Key.

-- -------------------------------------

-- Q5. Is every BCNF relation
-- in 3NF?

-- Answer:

-- Yes.

-- =====================================
-- DAY 45 SUMMARY
-- =====================================

-- 1NF

-- Atomic Values

-- -------------------------------------

-- 2NF

-- No Partial Dependency

-- -------------------------------------

-- 3NF

-- No Transitive Dependency

-- -------------------------------------

-- BCNF

-- Determinant is Super Key

-- -------------------------------------

-- Progression:

-- 1NF
-- ↓
-- 2NF
-- ↓
-- 3NF
-- ↓
-- BCNF

-- Each level reduces redundancy
-- and improves database design.