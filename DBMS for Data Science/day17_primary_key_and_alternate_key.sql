/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 17
Description : Primary Key and Alternate Key
*/

-- =====================================
-- DAY 17 : PRIMARY KEY AND ALTERNATE KEY
-- =====================================

-- What is a Primary Key?

-- A Primary Key is a Candidate Key
-- selected to uniquely identify
-- each row in a table.

-- Every table should have
-- one Primary Key.

-- Properties of Primary Key:

-- 1. Unique
-- 2. Cannot be NULL
-- 3. Only one Primary Key per table
-- 4. Identifies each record uniquely

-- =====================================
-- EXAMPLE
-- =====================================

-- STUDENT

-- Roll_No | Email            | Name
-- -------------------------------------
-- 101     | saloni@gmail.com | Saloni
-- 102     | rahul@gmail.com  | Rahul

-- Candidate Keys:

-- Roll_No

-- Email

-- Suppose we select Roll_No.

-- Primary Key:

-- Roll_No

-- =====================================
-- WHY PRIMARY KEY?
-- =====================================

-- Without Primary Key:

-- Duplicate records may occur.

-- Difficult to identify records.

-- Data integrity may be lost.

-- =====================================
-- ALTERNATE KEY
-- =====================================

-- Alternate Key is a Candidate Key
-- that was NOT selected as
-- Primary Key.

-- Example:

-- Candidate Keys:

-- Roll_No

-- Email

-- Primary Key:

-- Roll_No

-- Alternate Key:

-- Email

-- =====================================
-- EXAMPLE 2
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Aadhaar_No
-- Email
-- Name

-- Candidate Keys:

-- Emp_ID

-- Aadhaar_No

-- Email

-- Suppose:

-- Primary Key = Emp_ID

-- Alternate Keys:

-- Aadhaar_No
-- Email

-- =====================================
-- PRIMARY KEY VS ALTERNATE KEY
-- =====================================

-- Primary Key

-- Selected Candidate Key

-- Cannot be NULL

-- Only One

-- Alternate Key

-- Remaining Candidate Keys

-- Usually Unique

-- Can become Primary Key
-- if required

-- =====================================
-- ADVANTAGES OF PRIMARY KEY
-- =====================================

-- 1. Prevents Duplicate Records
-- 2. Ensures Data Integrity
-- 3. Improves Searching
-- 4. Establishes Relationships

-- =====================================
-- ADVANTAGES OF ALTERNATE KEY
-- =====================================

-- 1. Additional Unique Identifiers
-- 2. Better Flexibility
-- 3. Useful for Future Design Changes

-- =====================================
-- DAY 17 SUMMARY
-- =====================================

-- Candidate Key
-- --> Minimal Super Key

-- Primary Key
-- --> Selected Candidate Key

-- Alternate Key
-- --> Candidate Key not selected
--     as Primary Key

-- Every Primary Key is a
-- Candidate Key.

-- Every Alternate Key is also
-- a Candidate Key.