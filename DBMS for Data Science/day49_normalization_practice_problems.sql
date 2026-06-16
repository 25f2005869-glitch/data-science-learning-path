/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 49
Description : Normalization Practice Problems and Candidate Key Based Decomposition
*/

-- =====================================
-- DAY 49 : NORMALIZATION PRACTICE
-- =====================================

-- Goal:

-- 1. Identify Candidate Keys

-- 2. Find Partial Dependencies

-- 3. Find Transitive Dependencies

-- 4. Perform Decomposition

-- 5. Apply Normal Forms

-- =====================================
-- PROBLEM 1
-- =====================================

-- Relation:

-- STUDENT_COURSE

-- Student_ID
-- Course_ID
-- Student_Name
-- Grade

-- Functional Dependencies:

-- Student_ID → Student_Name

-- (Student_ID, Course_ID)
-- →
-- Grade

-- =====================================

-- Step 1:

-- Candidate Key

-- (Student_ID, Course_ID)

-- =====================================

-- Step 2:

-- Check Partial Dependency

-- Student_ID
-- →
-- Student_Name

-- Depends on part of key.

-- Partial Dependency Exists.

-- =====================================

-- Step 3:

-- Convert to 2NF

-- STUDENT

-- Student_ID
-- Student_Name

-- -------------------------------------

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Grade

-- =====================================
-- PROBLEM 2
-- =====================================

-- Relation:

-- EMPLOYEE

-- Emp_ID
-- Emp_Name
-- Dept_ID
-- Dept_Name

-- Functional Dependencies:

-- Emp_ID → Emp_Name

-- Emp_ID → Dept_ID

-- Dept_ID → Dept_Name

-- =====================================

-- Candidate Key:

-- Emp_ID

-- =====================================

-- Transitive Dependency:

-- Emp_ID → Dept_ID

-- Dept_ID → Dept_Name

-- Therefore:

-- Emp_ID → Dept_Name

-- =====================================

-- Convert to 3NF

-- EMPLOYEE

-- Emp_ID
-- Emp_Name
-- Dept_ID

-- -------------------------------------

-- DEPARTMENT

-- Dept_ID
-- Dept_Name

-- =====================================
-- PROBLEM 3
-- =====================================

-- Relation:

-- R(A, B, C)

-- Functional Dependencies:

-- A → B

-- B → C

-- =====================================

-- Find Candidate Key

-- A+ = {A, B, C}

-- Therefore:

-- Candidate Key = A

-- =====================================
-- PROBLEM 4
-- =====================================

-- Relation:

-- R(A, B, C, D)

-- Functional Dependencies:

-- A → B

-- B → C

-- C → D

-- =====================================

-- Find A+

-- A+ = {A}

-- A → B

-- {A, B}

-- B → C

-- {A, B, C}

-- C → D

-- {A, B, C, D}

-- =====================================

-- Candidate Key:

-- A

-- =====================================
-- PROBLEM 5
-- =====================================

-- Relation:

-- STUDENT

-- Student_ID
-- Hobby
-- Language

-- Dependencies:

-- Student_ID ↠ Hobby

-- Student_ID ↠ Language

-- =====================================

-- MVD Exists

-- Not in 4NF

-- =====================================

-- Convert to:

-- STUDENT_HOBBY

-- Student_ID
-- Hobby

-- -------------------------------------

-- STUDENT_LANGUAGE

-- Student_ID
-- Language

-- =====================================

-- 4NF Achieved

-- =====================================
-- CANDIDATE KEY FINDING RULE
-- =====================================

-- Step 1:

-- Compute Closure

-- X+

-- -------------------------------------

-- Step 2:

-- If X+ contains all attributes

-- Then:

-- X is Super Key

-- -------------------------------------

-- Step 3:

-- If minimal

-- Then:

-- X is Candidate Key

-- =====================================
-- NORMALIZATION CHECKLIST
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

-- 4NF

-- No Multivalued Dependency

-- -------------------------------------

-- 5NF

-- No Join Dependency

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. How do we find a Candidate Key?

-- Answer:

-- Using Attribute Closure.

-- -------------------------------------

-- Q2. Which Normal Form removes
-- Partial Dependency?

-- Answer:

-- 2NF

-- -------------------------------------

-- Q3. Which Normal Form removes
-- Transitive Dependency?

-- Answer:

-- 3NF

-- -------------------------------------

-- Q4. Which Normal Form removes
-- Multivalued Dependency?

-- Answer:

-- 4NF

-- -------------------------------------

-- Q5. Which Normal Form removes
-- Join Dependency?

-- Answer:

-- 5NF

-- =====================================
-- DAY 49 SUMMARY
-- =====================================

-- Candidate Key Finding

-- Attribute Closure

-- 2NF Decomposition

-- 3NF Decomposition

-- 4NF Decomposition

-- Normalization Practice

-- Database Design Improvement

-- Reduction of Redundancy