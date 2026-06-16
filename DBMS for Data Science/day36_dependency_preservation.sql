/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 36
Description : Dependency Preservation
*/

-- =====================================
-- DAY 36 : DEPENDENCY PRESERVATION
-- =====================================

-- What is Dependency Preservation?

-- Dependency Preservation ensures that
-- all Functional Dependencies (FDs)
-- can be enforced after decomposing
-- a relation.

-- =====================================
-- WHY DEPENDENCY PRESERVATION?
-- =====================================

-- During Normalization, a relation
-- is often decomposed into smaller
-- relations.

-- After decomposition, we should
-- still be able to enforce all
-- original Functional Dependencies.

-- =====================================
-- DEFINITION
-- =====================================

-- A decomposition is Dependency
-- Preserving if all original FDs
-- can be checked using the
-- decomposed relations only.

-- No need to join relations
-- to verify dependencies.

-- =====================================
-- EXAMPLE 1
-- =====================================

-- Relation:

-- R(A, B, C)

-- Functional Dependencies:

-- A → B

-- B → C

-- -------------------------------------

-- Decompose into:

-- R1(A, B)

-- R2(B, C)

-- -------------------------------------

-- Check Dependencies:

-- A → B exists in R1

-- B → C exists in R2

-- All FDs preserved.

-- Therefore:

-- Dependency Preserving
-- Decomposition

-- =====================================
-- EXAMPLE 2
-- =====================================

-- Relation:

-- R(A, B, C)

-- Functional Dependencies:

-- A → B

-- B → C

-- -------------------------------------

-- Decompose into:

-- R1(A, B)

-- R2(A, C)

-- -------------------------------------

-- A → B exists in R1

-- But:

-- B → C cannot be checked directly.

-- Need Join Operation.

-- Therefore:

-- Not Dependency Preserving

-- =====================================
-- IMPORTANCE
-- =====================================

-- 1. Easy Constraint Enforcement

-- 2. Better Data Integrity

-- 3. Efficient Database Design

-- 4. Reduces Query Complexity

-- =====================================
-- DEPENDENCY PRESERVING VS
-- NON-DEPENDENCY PRESERVING
-- =====================================

-- Dependency Preserving

-- Original FDs remain available.

-- No Join required.

-- Easy Validation.

-- -------------------------------------

-- Non Dependency Preserving

-- Some FDs are lost.

-- Join required.

-- Difficult Validation.

-- =====================================
-- RELATION TO NORMALIZATION
-- =====================================

-- During Normalization:

-- We aim for:

-- 1. Lossless Join

-- 2. Dependency Preservation

-- Good decomposition should
-- satisfy both conditions.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- R(A, B, C)

-- FDs:

-- A → B

-- B → C

-- Decompose:

-- R1(A, B)

-- R2(B, C)

-- Answer:

-- Dependency Preserving

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- R(A, B, C)

-- FDs:

-- A → B

-- B → C

-- Decompose:

-- R1(A, B)

-- R2(A, C)

-- Answer:

-- Not Dependency Preserving

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is Dependency Preservation?

-- Answer:

-- A decomposition is Dependency
-- Preserving if all original
-- Functional Dependencies can be
-- enforced without joining the
-- decomposed relations.

-- =====================================
-- DAY 36 SUMMARY
-- =====================================

-- Dependency Preservation

-- Ensures all Functional
-- Dependencies remain valid
-- after decomposition.

-- Benefits:

-- Easy Constraint Checking

-- Better Integrity

-- Efficient Design

-- Goal of Normalization:

-- Lossless Join

-- Dependency Preservation