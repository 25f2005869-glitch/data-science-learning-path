/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 48
Description : Complete Normalization Example (UNF → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF)
*/

-- =====================================
-- DAY 48 : COMPLETE NORMALIZATION
-- =====================================

-- Today we will normalize a relation
-- step-by-step from UNF to 5NF.

-- =====================================
-- STEP 0 : UNNORMALIZED FORM (UNF)
-- =====================================

-- STUDENT_COURSE

-- Student_ID
-- Student_Name
-- Phone_Numbers
-- Course_ID
-- Course_Name
-- Instructor

-- Example:

-- 101
-- Saloni
-- {9876,8765}
-- C1
-- DBMS
-- Dr. Kumar

-- Problem:

-- Multi-valued Attribute Exists

-- Phone_Numbers

-- Therefore:

-- Relation is in UNF.

-- =====================================
-- STEP 1 : FIRST NORMAL FORM (1NF)
-- =====================================

-- Rule:

-- Atomic Values Only

-- Convert:

-- Student_ID
-- Student_Name
-- Phone_Number
-- Course_ID
-- Course_Name
-- Instructor

-- Example:

-- 101
-- Saloni
-- 9876
-- C1
-- DBMS
-- Dr. Kumar

-- 101
-- Saloni
-- 8765
-- C1
-- DBMS
-- Dr. Kumar

-- Now:

-- One value per cell.

-- Relation is in 1NF.

-- =====================================
-- STEP 2 : SECOND NORMAL FORM (2NF)
-- =====================================

-- Candidate Key:

-- (Student_ID, Course_ID)

-- Functional Dependencies:

-- Student_ID → Student_Name

-- Course_ID → Course_Name

-- Course_ID → Instructor

-- Partial Dependencies Exist.

-- =====================================

-- Decompose into:

-- STUDENT

-- Student_ID
-- Student_Name

-- -------------------------------------

-- COURSE

-- Course_ID
-- Course_Name
-- Instructor

-- -------------------------------------

-- ENROLLMENT

-- Student_ID
-- Course_ID

-- Partial Dependency Removed.

-- Relation is now in 2NF.

-- =====================================
-- STEP 3 : THIRD NORMAL FORM (3NF)
-- =====================================

-- Assume:

-- Course_ID → Instructor_ID

-- Instructor_ID → Instructor_Name

-- Transitive Dependency Exists.

-- =====================================

-- Decompose:

-- COURSE

-- Course_ID
-- Instructor_ID

-- -------------------------------------

-- INSTRUCTOR

-- Instructor_ID
-- Instructor_Name

-- Transitive Dependency Removed.

-- Relation is now in 3NF.

-- =====================================
-- STEP 4 : BCNF
-- =====================================

-- Check every FD.

-- For every:

-- X → Y

-- X must be Super Key.

-- Assume all determinants
-- are Candidate Keys.

-- Therefore:

-- Relation satisfies BCNF.

-- =====================================
-- STEP 5 : FOURTH NORMAL FORM (4NF)
-- =====================================

-- Suppose:

-- Student_ID ↠ Hobby

-- Student_ID ↠ Language

-- Multiple independent values exist.

-- =====================================

-- Decompose:

-- STUDENT_HOBBY

-- Student_ID
-- Hobby

-- -------------------------------------

-- STUDENT_LANGUAGE

-- Student_ID
-- Language

-- MVD Removed.

-- Relation satisfies 4NF.

-- =====================================
-- STEP 6 : FIFTH NORMAL FORM (5NF)
-- =====================================

-- Suppose:

-- Supplier
-- Project
-- Part

-- Independent Relationships Exist.

-- =====================================

-- Decompose:

-- SP

-- Supplier
-- Project

-- -------------------------------------

-- SJ

-- Supplier
-- Part

-- -------------------------------------

-- PJ

-- Project
-- Part

-- Join Dependency Removed.

-- Relation satisfies 5NF.

-- =====================================
-- COMPLETE JOURNEY
-- =====================================

-- UNF

-- Multi-Valued Attributes

-- ↓

-- 1NF

-- Atomic Values

-- ↓

-- 2NF

-- No Partial Dependency

-- ↓

-- 3NF

-- No Transitive Dependency

-- ↓

-- BCNF

-- Determinants are Super Keys

-- ↓

-- 4NF

-- No Multivalued Dependency

-- ↓

-- 5NF

-- No Join Dependency

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. Which Normal Form removes
-- Partial Dependency?

-- Answer:

-- 2NF

-- -------------------------------------

-- Q. Which Normal Form removes
-- Transitive Dependency?

-- Answer:

-- 3NF

-- -------------------------------------

-- Q. Which Normal Form removes
-- Multivalued Dependency?

-- Answer:

-- 4NF

-- -------------------------------------

-- Q. Which Normal Form removes
-- Join Dependency?

-- Answer:

-- 5NF

-- =====================================
-- DAY 48 SUMMARY
-- =====================================

-- UNF
-- → Multi-Valued Attributes

-- 1NF
-- → Atomic Values

-- 2NF
-- → No Partial Dependency

-- 3NF
-- → No Transitive Dependency

-- BCNF
-- → Determinant is Super Key

-- 4NF
-- → No Multivalued Dependency

-- 5NF
-- → No Join Dependency

-- This completes the full
-- Normalization workflow in DBMS.