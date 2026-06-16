/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 38
Description : Functional Dependency Practice Problems and Candidate Key Finding
*/

-- =====================================
-- DAY 38 : FUNCTIONAL DEPENDENCY
-- PRACTICE PROBLEMS
-- =====================================

-- Goal:

-- 1. Practice Functional Dependencies

-- 2. Find Attribute Closure

-- 3. Identify Super Keys

-- 4. Find Candidate Keys

-- =====================================
-- PROBLEM 1
-- =====================================

-- Relation:

-- R(A, B, C)

-- Functional Dependencies:

-- A → B

-- B → C

-- Find:

-- A+

-- -------------------------------------

-- Step 1:

-- Start:

-- A+ = {A}

-- Step 2:

-- A → B

-- A+ = {A, B}

-- Step 3:

-- B → C

-- A+ = {A, B, C}

-- Final Answer:

-- A+ = {A, B, C}

-- Since closure contains all attributes,

-- A is a Super Key.

-- Candidate Key = A

-- =====================================
-- PROBLEM 2
-- =====================================

-- Relation:

-- R(A, B, C, D)

-- Functional Dependencies:

-- A → B

-- B → C

-- C → D

-- Find:

-- A+

-- -------------------------------------

-- A+ = {A}

-- A → B

-- A+ = {A, B}

-- B → C

-- A+ = {A, B, C}

-- C → D

-- A+ = {A, B, C, D}

-- Final Answer:

-- A+ = {A, B, C, D}

-- Candidate Key = A

-- =====================================
-- PROBLEM 3
-- =====================================

-- Relation:

-- R(A, B, C)

-- Functional Dependencies:

-- AB → C

-- Find:

-- AB+

-- -------------------------------------

-- Start:

-- AB+ = {A, B}

-- AB → C

-- AB+ = {A, B, C}

-- Final Answer:

-- AB+ = {A, B, C}

-- Candidate Key = AB

-- =====================================
-- PROBLEM 4
-- =====================================

-- Relation:

-- R(A, B, C, D)

-- Functional Dependencies:

-- A → B

-- A → C

-- C → D

-- Find:

-- A+

-- -------------------------------------

-- A+ = {A}

-- A → B

-- {A, B}

-- A → C

-- {A, B, C}

-- C → D

-- {A, B, C, D}

-- Final Answer:

-- A+ = {A, B, C, D}

-- Candidate Key = A

-- =====================================
-- SUPER KEY IDENTIFICATION
-- =====================================

-- Relation:

-- R(A, B, C)

-- FD:

-- A → B

-- B → C

-- Candidate Key:

-- A

-- Super Keys:

-- A

-- AB

-- AC

-- ABC

-- =====================================
-- CANDIDATE KEY RULE
-- =====================================

-- If Closure contains all
-- attributes of relation:

-- X+ = R

-- Then:

-- X is a Super Key

-- -------------------------------------

-- If no attribute can be removed
-- from X:

-- Then X is a Candidate Key

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- R(A, B, C)

-- FD:

-- A → B

-- B → C

-- Find:

-- A+

-- Answer:

-- {A, B, C}

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- R(A, B, C, D)

-- FD:

-- A → B

-- B → C

-- C → D

-- Find:

-- Candidate Key

-- Answer:

-- A

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- R(A, B, C)

-- FD:

-- AB → C

-- Find:

-- Candidate Key

-- Answer:

-- AB

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Attribute Closure?

-- Answer:

-- Set of all attributes
-- functionally determined by
-- a given attribute set.

-- -------------------------------------

-- Q2. How do we identify
-- a Candidate Key?

-- Answer:

-- Find closure.

-- If closure contains all
-- attributes and is minimal,
-- it is a Candidate Key.

-- -------------------------------------

-- Q3. Difference between
-- Super Key and Candidate Key?

-- Answer:

-- Candidate Key is a minimal
-- Super Key.

-- =====================================
-- DAY 38 SUMMARY
-- =====================================

-- Attribute Closure

-- Used to Find:

-- Super Keys

-- Candidate Keys

-- Functional Dependencies

-- Rules:

-- X+ = All Attributes

-- ⇒ Super Key

-- Minimal Super Key

-- ⇒ Candidate Key