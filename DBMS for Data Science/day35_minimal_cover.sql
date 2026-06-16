/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 35
Description : Minimal Cover (Canonical Cover)
*/

-- =====================================
-- DAY 35 : MINIMAL COVER
-- =====================================

-- What is a Minimal Cover?

-- A Minimal Cover (also called
-- Canonical Cover) is the smallest
-- set of Functional Dependencies
-- that is equivalent to the original
-- set of Functional Dependencies.

-- Goal:

-- Remove unnecessary attributes
-- and redundant dependencies.

-- =====================================
-- WHY MINIMAL COVER?
-- =====================================

-- 1. Simplifies Functional Dependencies

-- 2. Helps in Normalization

-- 3. Reduces Redundancy

-- 4. Improves Database Design

-- =====================================
-- PROPERTIES OF MINIMAL COVER
-- =====================================

-- A Minimal Cover must satisfy:

-- 1. Right side contains
--    only one attribute.

-- 2. No extraneous attribute
--    on left side.

-- 3. No redundant dependency.

-- =====================================
-- STEP 1
-- SPLIT RIGHT SIDE ATTRIBUTES
-- =====================================

-- Example:

-- A → BC

-- Convert into:

-- A → B

-- A → C

-- =====================================
-- EXAMPLE
-- =====================================

-- Given FD Set:

-- A → BC

-- B → C

-- Convert:

-- A → B

-- A → C

-- B → C

-- =====================================
-- STEP 2
-- REMOVE EXTRANEOUS ATTRIBUTES
-- =====================================

-- Example:

-- AB → C

-- If A alone determines C

-- Then B is unnecessary.

-- Therefore:

-- A → C

-- Extraneous attribute removed.

-- =====================================
-- STEP 3
-- REMOVE REDUNDANT FDs
-- =====================================

-- Example:

-- A → B

-- B → C

-- A → C

-- Here:

-- A → C

-- can be derived from:

-- A → B

-- B → C

-- Therefore:

-- A → C

-- is redundant.

-- Remove it.

-- =====================================
-- COMPLETE EXAMPLE
-- =====================================

-- Given:

-- A → BC

-- B → C

-- A → C

-- -------------------------------------

-- Step 1:

-- Split

-- A → B

-- A → C

-- B → C

-- A → C

-- -------------------------------------

-- Step 2:

-- Check redundancy

-- A → C

-- already obtained through

-- A → B

-- B → C

-- -------------------------------------

-- Step 3:

-- Remove redundant FD

-- Final Minimal Cover:

-- A → B

-- B → C

-- =====================================
-- PRACTICAL IMPORTANCE
-- =====================================

-- Used in:

-- 1. Normalization

-- 2. Database Design

-- 3. Dependency Preservation

-- 4. Schema Decomposition

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Given:

-- A → BC

-- Convert to:

-- A → B

-- A → C

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Given:

-- A → B

-- B → C

-- A → C

-- Find Redundant FD.

-- Answer:

-- A → C

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Given:

-- AB → C

-- A → C

-- Which attribute is extraneous?

-- Answer:

-- B

-- =====================================
-- DAY 35 SUMMARY
-- =====================================

-- Minimal Cover

-- Smallest Equivalent Set
-- of Functional Dependencies.

-- Rules:

-- 1. Single Attribute on RHS

-- 2. Remove Extraneous Attributes

-- 3. Remove Redundant Dependencies

-- Benefits:

-- Simplifies FD Analysis

-- Helps Normalization

-- Improves Database Design

-- Minimal Cover is a key step
-- before schema decomposition.