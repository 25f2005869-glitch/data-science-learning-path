/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 16
Description : Super Key and Candidate Key
*/

-- =====================================
-- DAY 16 : SUPER KEY AND CANDIDATE KEY
-- =====================================

-- What is a Super Key?

-- A Super Key is a set of one or more
-- attributes that can uniquely identify
-- each tuple in a relation.

-- A Super Key may contain
-- extra attributes.

-- =====================================
-- EXAMPLE TABLE
-- =====================================

-- STUDENT

-- Roll_No | Email            | Name
-- -------------------------------------
-- 101     | saloni@gmail.com | Saloni
-- 102     | rahul@gmail.com  | Rahul

-- =====================================
-- SUPER KEYS
-- =====================================

-- Roll_No

-- Email

-- Roll_No + Name

-- Email + Name

-- Roll_No + Email

-- Roll_No + Email + Name

-- All of the above are Super Keys.

-- Why?

-- Because each combination can
-- uniquely identify a student.

-- =====================================
-- PROBLEM WITH SUPER KEYS
-- =====================================

-- Some Super Keys contain
-- unnecessary attributes.

-- Example:

-- Roll_No + Name

-- Roll_No alone is sufficient.

-- Therefore Name is unnecessary.

-- =====================================
-- CANDIDATE KEY
-- =====================================

-- A Candidate Key is a minimal
-- Super Key.

-- Minimal means:

-- No attribute can be removed
-- without losing uniqueness.

-- =====================================
-- CANDIDATE KEYS
-- =====================================

-- Roll_No

-- Email

-- These are Candidate Keys because:

-- 1. Unique
-- 2. Minimal

-- =====================================
-- NOT CANDIDATE KEYS
-- =====================================

-- Roll_No + Name

-- Email + Name

-- Roll_No + Email

-- These contain extra attributes.

-- Therefore they are not
-- Candidate Keys.

-- =====================================
-- SUPER KEY VS CANDIDATE KEY
-- =====================================

-- Super Key

-- Uniquely identifies records.
-- May contain extra attributes.

-- Candidate Key

-- Uniquely identifies records.
-- Contains no extra attributes.

-- =====================================
-- EXAMPLE 2
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Email
-- Aadhaar_No
-- Name

-- Candidate Keys:

-- Emp_ID

-- Email

-- Aadhaar_No

-- Super Keys:

-- Emp_ID + Name

-- Email + Name

-- Aadhaar_No + Name

-- Emp_ID + Email

-- And many more combinations.

-- =====================================
-- ADVANTAGES OF CANDIDATE KEYS
-- =====================================

-- 1. Remove Redundancy
-- 2. Better Database Design
-- 3. Easier Identification
-- 4. Basis for Primary Key Selection

-- =====================================
-- DAY 16 SUMMARY
-- =====================================

-- Super Key

-- Any attribute or combination
-- that uniquely identifies rows.

-- Candidate Key

-- Minimal Super Key.

-- Every Candidate Key is
-- a Super Key.

-- Every Super Key is NOT
-- a Candidate Key.