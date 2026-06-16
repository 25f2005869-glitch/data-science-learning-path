/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 20
Description : Complete Revision of Keys in DBMS
*/

-- =====================================
-- DAY 20 : KEYS REVISION
-- =====================================

-- This day is dedicated to the
-- revision of all key concepts
-- studied from Day 15 to Day 19.

-- =====================================
-- WHAT IS A KEY?
-- =====================================

-- A Key is an attribute or set of
-- attributes used to uniquely
-- identify records in a table.

-- =====================================
-- TYPES OF KEYS
-- =====================================

-- 1. Super Key
-- 2. Candidate Key
-- 3. Primary Key
-- 4. Alternate Key
-- 5. Composite Key
-- 6. Foreign Key

-- =====================================
-- SUPER KEY
-- =====================================

-- Any attribute or combination of
-- attributes that uniquely identifies
-- a tuple.

-- Example:

-- STUDENT

-- Roll_No
-- Email
-- Name

-- Super Keys:

-- Roll_No

-- Email

-- Roll_No + Name

-- Email + Name

-- Roll_No + Email

-- =====================================
-- CANDIDATE KEY
-- =====================================

-- Minimal Super Key.

-- No unnecessary attributes.

-- Example:

-- Roll_No

-- Email

-- =====================================
-- PRIMARY KEY
-- =====================================

-- Selected Candidate Key.

-- Properties:

-- Unique
-- Cannot be NULL

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

-- Combination of multiple
-- attributes.

-- Example:

-- ENROLLMENT

-- Roll_No
-- Course_ID

-- Composite Key:

-- (Roll_No, Course_ID)

-- =====================================
-- FOREIGN KEY
-- =====================================

-- Refers to Primary Key of
-- another table.

-- Used to establish relationships.

-- Example:

-- STUDENT.Roll_No

-- referenced by

-- ENROLLMENT.Roll_No

-- =====================================
-- HIERARCHY OF KEYS
-- =====================================

-- Super Key

-- Candidate Key

-- Primary Key

-- Alternate Key

-- =====================================
-- IMPORTANT FACTS
-- =====================================

-- Every Candidate Key is
-- a Super Key.

-- Every Primary Key is
-- a Candidate Key.

-- Every Primary Key is
-- a Super Key.

-- Every Super Key is NOT
-- a Candidate Key.

-- Foreign Key is used
-- for Relationships.

-- Composite Key can be
-- a Primary Key.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- STUDENT

-- Roll_No
-- Email
-- Phone
-- Name

-- Find:

-- Candidate Keys

-- Answer:

-- Roll_No
-- Email
-- Phone

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- ENROLLMENT

-- Roll_No
-- Course_ID

-- Identify Key:

-- Answer:

-- Composite Key

-- (Roll_No, Course_ID)

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- STUDENT

-- Roll_No

-- ENROLLMENT

-- Roll_No

-- Identify:

-- Answer:

-- Foreign Key

-- ENROLLMENT.Roll_No

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Difference between
-- Super Key and Candidate Key?

-- Answer:
-- Candidate Key is a minimal
-- Super Key.

-- Q2. Can a table have multiple
-- Candidate Keys?

-- Answer:
-- Yes.

-- Q3. Can a table have multiple
-- Primary Keys?

-- Answer:
-- No.

-- Q4. Can a Foreign Key contain NULL?

-- Answer:
-- Yes, depending on design.

-- Q5. Can a Composite Key be
-- a Primary Key?

-- Answer:
-- Yes.

-- =====================================
-- DAY 20 SUMMARY
-- =====================================

-- Super Key
-- --> Unique Identifier

-- Candidate Key
-- --> Minimal Super Key

-- Primary Key
-- --> Selected Candidate Key

-- Alternate Key
-- --> Unselected Candidate Key

-- Composite Key
-- --> Multiple Attributes Together

-- Foreign Key
-- --> Connects Tables

-- Keys are essential for:

-- Uniqueness
-- Integrity
-- Relationships
-- Efficient Database Design