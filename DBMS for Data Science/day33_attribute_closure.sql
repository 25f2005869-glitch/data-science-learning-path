/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 33
Description : Attribute Closure
*/

-- =====================================
-- DAY 33 : ATTRIBUTE CLOSURE
-- =====================================

-- What is Attribute Closure?

-- Attribute Closure is the set of all
-- attributes that can be functionally
-- determined from a given attribute set.

-- Closure helps us determine:

-- 1. Candidate Keys

-- 2. Super Keys

-- 3. Functional Dependencies

-- =====================================
-- NOTATION
-- =====================================

-- Closure of X is written as:

-- X+

-- Read as:

-- X Plus

-- =====================================
-- EXAMPLE 1
-- =====================================

-- Relation:

-- R(A, B, C)

-- Functional Dependencies:

-- A → B

-- B → C

-- Find:

-- A+

-- Step 1:

-- Start with A

-- A+

-- {A}

-- Step 2:

-- A → B

-- Add B

-- A+

-- {A, B}

-- Step 3:

-- B → C

-- Add C

-- A+

-- {A, B, C}

-- Final Answer:

-- A+ = {A, B, C}

-- =====================================
-- EXAMPLE 2
-- =====================================

-- Relation:

-- R(A, B, C, D)

-- Functional Dependencies:

-- A → B

-- B → C

-- C → D

-- Find:

-- A+

-- Start:

-- {A}

-- A → B

-- {A, B}

-- B → C

-- {A, B, C}

-- C → D

-- {A, B, C, D}

-- Final Answer:

-- A+ = {A, B, C, D}

-- =====================================
-- HOW TO FIND CLOSURE?
-- =====================================

-- Step 1:

-- Start with given attribute set.

-- Step 2:

-- Apply all Functional Dependencies.

-- Step 3:

-- Add newly obtained attributes.

-- Step 4:

-- Repeat until no new attribute
-- can be added.

-- =====================================
-- USE OF ATTRIBUTE CLOSURE
-- =====================================

-- Candidate Key Detection

-- Super Key Detection

-- FD Verification

-- Normalization

-- Database Design

-- =====================================
-- SUPER KEY TEST
-- =====================================

-- If:

-- X+ contains all attributes
-- of the relation

-- Then:

-- X is a Super Key

-- Example:

-- R(A, B, C)

-- A+ = {A, B, C}

-- Therefore:

-- A is a Super Key

-- =====================================
-- CANDIDATE KEY TEST
-- =====================================

-- If:

-- X is a Super Key

-- And

-- No attribute can be removed
-- from X

-- Then:

-- X is a Candidate Key

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- R(A, B, C)

-- FD:

-- A → B

-- B → C

-- Find A+

-- Answer:

-- {A, B, C}

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- R(A, B, C, D)

-- FD:

-- A → B

-- A → C

-- C → D

-- Find A+

-- Answer:

-- {A, B, C, D}

-- =====================================
-- DAY 33 SUMMARY
-- =====================================

-- Attribute Closure:

-- X+

-- Represents all attributes
-- determined by X.

-- Uses:

-- Find Super Keys

-- Find Candidate Keys

-- Verify Functional Dependencies

-- Essential for Normalization.