/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 15
Description : Keys in DBMS
*/

-- =====================================
-- DAY 15 : KEYS IN DBMS
-- =====================================

-- What is a Key?

-- A Key is an attribute or a set of
-- attributes used to uniquely identify
-- a tuple (row) in a relation (table).

-- Keys help maintain data integrity
-- and establish relationships between
-- tables.

-- =====================================
-- TYPES OF KEYS
-- =====================================

-- 1. Super Key
-- 2. Candidate Key
-- 3. Primary Key
-- 4. Alternate Key
-- 5. Foreign Key

-- =====================================
-- EXAMPLE TABLE
-- =====================================

-- STUDENT

-- Roll_No | Email              | Name
-- ----------------------------------------
-- 101     | saloni@gmail.com   | Saloni
-- 102     | rahul@gmail.com    | Rahul

-- =====================================
-- 1. SUPER KEY
-- =====================================

-- A Super Key is any attribute or
-- combination of attributes that can
-- uniquely identify a row.

-- Examples:

-- Roll_No

-- Email

-- Roll_No + Name

-- Email + Name

-- All of the above are Super Keys.

-- =====================================
-- 2. CANDIDATE KEY
-- =====================================

-- A Candidate Key is a minimal
-- Super Key.

-- It contains no unnecessary
-- attributes.

-- Examples:

-- Roll_No

-- Email

-- These are Candidate Keys because
-- each alone can uniquely identify
-- a student.

-- =====================================
-- 3. PRIMARY KEY
-- =====================================

-- A Primary Key is the Candidate Key
-- selected to uniquely identify rows.

-- Example:

-- Roll_No

-- Properties:

-- Unique
-- Cannot be NULL
-- Only one Primary Key per table

-- =====================================
-- 4. ALTERNATE KEY
-- =====================================

-- Candidate Keys that are not chosen
-- as Primary Key become Alternate Keys.

-- Example:

-- Primary Key:
-- Roll_No

-- Alternate Key:
-- Email

-- =====================================
-- 5. FOREIGN KEY
-- =====================================

-- A Foreign Key creates a relationship
-- between two tables.

-- Example:

-- STUDENT

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul

-- ENROLLMENT

-- Roll_No | Course
-- --------------------
-- 101     | DBMS
-- 102     | Python

-- ENROLLMENT.Roll_No is a
-- Foreign Key.

-- It refers to STUDENT.Roll_No.

-- =====================================
-- BENEFITS OF KEYS
-- =====================================

-- 1. Unique Identification
-- 2. Maintain Integrity
-- 3. Avoid Duplicate Records
-- 4. Establish Relationships
-- 5. Improve Data Consistency

-- =====================================
-- DAY 15 SUMMARY
-- =====================================

-- Super Key
-- --> Uniquely Identifies Rows

-- Candidate Key
-- --> Minimal Super Key

-- Primary Key
-- --> Selected Candidate Key

-- Alternate Key
-- --> Candidate Key not chosen
--     as Primary Key

-- Foreign Key
-- --> Creates Relationship
--     Between Tables