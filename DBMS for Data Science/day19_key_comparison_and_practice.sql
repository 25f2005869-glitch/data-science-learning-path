/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 19
Description : Comparison of Primary Key, Foreign Key, Candidate Key and Composite Key
*/

-- =====================================
-- DAY 19 : KEY COMPARISON
-- =====================================

-- Revision

-- Super Key
-- Candidate Key
-- Primary Key
-- Alternate Key
-- Composite Key
-- Foreign Key

-- =====================================
-- CANDIDATE KEY
-- =====================================

-- A Candidate Key is a minimal
-- Super Key.

-- Properties:

-- 1. Unique
-- 2. Minimal
-- 3. Can become Primary Key

-- Example:

-- STUDENT

-- Roll_No
-- Email
-- Name

-- Candidate Keys:

-- Roll_No
-- Email

-- =====================================
-- PRIMARY KEY
-- =====================================

-- A Primary Key is the selected
-- Candidate Key.

-- Properties:

-- 1. Unique
-- 2. Cannot be NULL
-- 3. Only One per Table

-- Example:

-- Roll_No

-- =====================================
-- ALTERNATE KEY
-- =====================================

-- Candidate Key not selected
-- as Primary Key.

-- Example:

-- Email

-- =====================================
-- COMPOSITE KEY
-- =====================================

-- Combination of two or more
-- attributes.

-- Example:

-- ENROLLMENT

-- Roll_No | Course_ID

-- Composite Key:

-- (Roll_No, Course_ID)

-- =====================================
-- FOREIGN KEY
-- =====================================

-- Used to connect tables.

-- Refers to the Primary Key
-- of another table.

-- Example:

-- STUDENT

-- Roll_No

-- ENROLLMENT

-- Roll_No

-- ENROLLMENT.Roll_No
-- is a Foreign Key.

-- =====================================
-- COMPARISON TABLE
-- =====================================

-- Candidate Key
-- Minimal Super Key

-- Primary Key
-- Selected Candidate Key

-- Alternate Key
-- Unselected Candidate Key

-- Composite Key
-- Combination of Multiple Attributes

-- Foreign Key
-- Creates Relationship Between Tables

-- =====================================
-- PRACTICE EXAMPLE 1
-- =====================================

-- STUDENT

-- Roll_No
-- Email
-- Name

-- Candidate Keys:

-- Roll_No
-- Email

-- Primary Key:

-- Roll_No

-- Alternate Key:

-- Email

-- =====================================
-- PRACTICE EXAMPLE 2
-- =====================================

-- ENROLLMENT

-- Roll_No
-- Course_ID

-- Composite Key:

-- (Roll_No, Course_ID)

-- =====================================
-- PRACTICE EXAMPLE 3
-- =====================================

-- STUDENT

-- Roll_No
-- Name

-- ENROLLMENT

-- Roll_No
-- Course

-- Foreign Key:

-- ENROLLMENT.Roll_No

-- References:

-- STUDENT.Roll_No

-- =====================================
-- IMPORTANT INTERVIEW FACTS
-- =====================================

-- Every Primary Key is a
-- Candidate Key.

-- Every Candidate Key is a
-- Super Key.

-- Every Super Key is NOT a
-- Candidate Key.

-- Primary Key cannot be NULL.

-- Foreign Key may contain NULL
-- depending on design rules.

-- Composite Key may also be
-- a Primary Key.

-- =====================================
-- DAY 19 SUMMARY
-- =====================================

-- Candidate Key
-- --> Minimal Super Key

-- Primary Key
-- --> Selected Candidate Key

-- Alternate Key
-- --> Remaining Candidate Key

-- Composite Key
-- --> Multiple Attributes Together

-- Foreign Key
-- --> Connects Tables

-- Keys are essential for:
-- Uniqueness
-- Integrity
-- Relationships
-- Database Design