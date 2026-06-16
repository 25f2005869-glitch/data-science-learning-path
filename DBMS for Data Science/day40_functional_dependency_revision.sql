/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 40
Description : Complete Revision of Functional Dependency Concepts
*/

-- =====================================
-- DAY 40 : FUNCTIONAL DEPENDENCY
-- COMPLETE REVISION
-- =====================================

-- This day is dedicated to revising
-- all concepts covered from
-- Day 31 to Day 39.

-- =====================================
-- TOPICS COVERED
-- =====================================

-- 1. Functional Dependency

-- 2. Types of Functional Dependency

-- 3. Attribute Closure

-- 4. Armstrong's Axioms

-- 5. Minimal Cover

-- 6. Dependency Preservation

-- 7. Lossless Join

-- 8. Candidate Key Finding

-- 9. Full, Partial and
--    Transitive Dependency

-- =====================================
-- FUNCTIONAL DEPENDENCY
-- =====================================

-- Notation:

-- X → Y

-- Meaning:

-- X determines Y

-- Example:

-- Roll_No → Name

-- Roll_No → Age

-- =====================================
-- TYPES OF FUNCTIONAL DEPENDENCY
-- =====================================

-- Trivial FD

-- X → Y

-- where Y ⊆ X

-- Example:

-- AB → A

-- -------------------------------------

-- Non-Trivial FD

-- Y is not a subset of X

-- Example:

-- A → B

-- -------------------------------------

-- Completely Non-Trivial FD

-- X ∩ Y = ∅

-- Example:

-- A → B

-- =====================================
-- ATTRIBUTE CLOSURE
-- =====================================

-- Notation:

-- X+

-- Meaning:

-- Set of all attributes
-- determined by X

-- Example:

-- A → B

-- B → C

-- Then:

-- A+ = {A, B, C}

-- =====================================
-- SUPER KEY TEST
-- =====================================

-- If:

-- X+ contains all attributes
-- of relation

-- Then:

-- X is a Super Key

-- =====================================
-- CANDIDATE KEY TEST
-- =====================================

-- If:

-- X is a Super Key

-- and

-- No attribute can be removed

-- Then:

-- X is a Candidate Key

-- =====================================
-- ARMSTRONG'S AXIOMS
-- =====================================

-- 1. Reflexivity

-- If Y ⊆ X

-- Then:

-- X → Y

-- -------------------------------------

-- 2. Augmentation

-- If X → Y

-- Then:

-- XZ → YZ

-- -------------------------------------

-- 3. Transitivity

-- If X → Y

-- Y → Z

-- Then:

-- X → Z

-- =====================================
-- DERIVED RULES
-- =====================================

-- Union Rule

-- If:

-- X → Y

-- X → Z

-- Then:

-- X → YZ

-- -------------------------------------

-- Decomposition Rule

-- If:

-- X → YZ

-- Then:

-- X → Y

-- X → Z

-- -------------------------------------

-- Pseudotransitivity

-- If:

-- X → Y

-- WY → Z

-- Then:

-- WX → Z

-- =====================================
-- MINIMAL COVER
-- =====================================

-- Smallest equivalent set
-- of Functional Dependencies.

-- Rules:

-- 1. Single Attribute RHS

-- 2. Remove Extraneous Attributes

-- 3. Remove Redundant FDs

-- =====================================
-- DEPENDENCY PRESERVATION
-- =====================================

-- All Functional Dependencies
-- remain enforceable after
-- decomposition.

-- No Join required
-- to verify dependencies.

-- =====================================
-- LOSSLESS JOIN
-- =====================================

-- Original relation can be
-- reconstructed exactly
-- after decomposition.

-- No Information Loss.

-- =====================================
-- ADVANCED DEPENDENCIES
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

-- Removed in:

-- 2NF

-- -------------------------------------

-- Transitive Dependency

-- Example:

-- Emp_ID
-- →
-- Dept_ID

-- Dept_ID
-- →
-- Dept_Name

-- Removed in:

-- 3NF

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- R(A, B, C)

-- A → B

-- B → C

-- Find A+

-- Answer:

-- {A, B, C}

-- Candidate Key = A

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Given:

-- A → B

-- B → C

-- Find:

-- A → ?

-- Answer:

-- A → C

-- By Transitivity

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Given:

-- A → BC

-- Find Minimal Cover

-- Answer:

-- A → B

-- A → C

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Functional Dependency?

-- Relationship between attributes
-- where one attribute determines
-- another.

-- -------------------------------------

-- Q2. What is Attribute Closure?

-- Set of all attributes determined
-- by a given attribute set.

-- -------------------------------------

-- Q3. What is a Candidate Key?

-- Minimal Super Key.

-- -------------------------------------

-- Q4. What is Dependency Preservation?

-- All FDs remain enforceable
-- after decomposition.

-- -------------------------------------

-- Q5. What is Lossless Join?

-- Original relation can be
-- reconstructed without
-- losing information.

-- =====================================
-- DAY 40 SUMMARY
-- =====================================

-- Functional Dependency

-- Attribute Closure

-- Candidate Key

-- Armstrong's Axioms

-- Minimal Cover

-- Dependency Preservation

-- Lossless Join

-- Full Dependency

-- Partial Dependency

-- Transitive Dependency

-- These concepts form the
-- foundation of Normalization
-- and advanced DBMS design.