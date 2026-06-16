/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 32
Description : Minimal Cover (Canonical Cover)
*/

-- =====================================
-- DAY 32 : MINIMAL COVER
-- =====================================

-- What is Minimal Cover?

-- Minimal Cover (Canonical Cover)
-- is the smallest set of Functional
-- Dependencies equivalent to the
-- original set.

-- Goal:

-- Remove Redundancy

-- Simplify Functional Dependencies

-- =====================================
-- PROPERTIES OF MINIMAL COVER
-- =====================================

-- 1. Right side contains
-- only one attribute.

-- 2. No extraneous attribute
-- exists.

-- 3. No redundant dependency
-- exists.

-- =====================================
-- STEP 1
-- SPLIT RIGHT HAND SIDE
-- =====================================

-- Example

-- A → BC

-- Convert To

-- A → B

-- A → C

-- =====================================
-- STEP 2
-- REMOVE EXTRANEOUS ATTRIBUTES
-- =====================================

-- Example

-- AB → C

-- If A alone determines C

-- Then B is extraneous.

-- Result:

-- A → C

-- =====================================
-- STEP 3
-- REMOVE REDUNDANT FD
-- =====================================

-- Example

-- A → B

-- B → C

-- A → C

-- =====================================

-- A → C is redundant because
-- it can be derived from:

-- A → B

-- B → C

-- =====================================
-- EXAMPLE
-- =====================================

-- F =

-- A → BC

-- B → C

-- A → B

-- AB → C

-- =====================================

-- Step 1

-- A → B

-- A → C

-- B → C

-- A → B

-- AB → C

-- =====================================

-- Step 2

-- Remove Duplicate

-- A → B

-- A → C

-- B → C

-- AB → C

-- =====================================

-- Step 3

-- AB → C is redundant

-- Because:

-- A → B

-- B → C

-- Therefore:

-- A → C

-- =====================================

-- Minimal Cover

-- A → B

-- B → C

-- =====================================
-- WHY MINIMAL COVER?
-- =====================================

-- Used in:

-- Normalization

-- Schema Design

-- Candidate Key Analysis

-- Dependency Preservation

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- A → BC

-- Convert To?

-- Answer:

-- A → B

-- A → C

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Why remove redundant FDs?

-- Answer:

-- To obtain smallest equivalent set.

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is Minimal Cover?

-- Answer:

-- Smallest equivalent set of
-- Functional Dependencies with
-- no redundancy and no
-- extraneous attributes.

-- =====================================
-- DAY 32 SUMMARY
-- =====================================

-- Minimal Cover

-- Canonical Cover

-- -------------------------------------

-- Split RHS

-- Remove Extraneous Attributes

-- Remove Redundant FDs

-- -------------------------------------

-- Used in Normalization

-- Schema Design

-- Dependency Analysis