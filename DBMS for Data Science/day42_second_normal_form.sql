/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 42
Description : Second Normal Form (2NF)
*/

-- =====================================
-- DAY 42 : SECOND NORMAL FORM (2NF)
-- =====================================

-- What is 2NF?

-- A relation is in Second Normal Form
-- if:

-- 1. It is already in 1NF

-- AND

-- 2. It contains NO Partial Dependency

-- =====================================
-- WHAT IS PARTIAL DEPENDENCY?
-- =====================================

-- Partial Dependency occurs when
-- a non-prime attribute depends
-- on only a part of a composite key.

-- =====================================
-- EXAMPLE
-- =====================================

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Student_Name
-- Grade

-- Composite Key:

-- (Student_ID, Course_ID)

-- Functional Dependencies:

-- Student_ID
-- →
-- Student_Name

-- (Student_ID, Course_ID)
-- →
-- Grade

-- =====================================
-- ANALYSIS
-- =====================================

-- Student_Name depends only on
-- Student_ID.

-- It does NOT depend on the
-- entire composite key.

-- Therefore:

-- Partial Dependency Exists.

-- Relation is NOT in 2NF.

-- =====================================
-- CONVERT TO 2NF
-- =====================================

-- Split Relation

-- STUDENT

-- Student_ID
-- Student_Name

-- -------------------------------------

-- ENROLLMENT

-- Student_ID
-- Course_ID
-- Grade

-- =====================================
-- RESULT
-- =====================================

-- Student_Name now depends
-- completely on Student_ID.

-- Grade depends on:

-- (Student_ID, Course_ID)

-- No Partial Dependency exists.

-- Therefore:

-- Relation is in 2NF.

-- =====================================
-- WHY REMOVE PARTIAL DEPENDENCY?
-- =====================================

-- Reduces Redundancy

-- Improves Consistency

-- Eliminates Update Anomalies

-- Improves Database Design

-- =====================================
-- 1NF VS 2NF
-- =====================================

-- 1NF

-- Atomic Values

-- No Multi-Valued Attributes

-- -------------------------------------

-- 2NF

-- Must be in 1NF

-- No Partial Dependency

-- =====================================
-- IMPORTANT POINT
-- =====================================

-- Partial Dependency can occur only
-- when a Composite Key exists.

-- If a table has only one
-- Candidate Key attribute,

-- Partial Dependency cannot occur.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- STUDENT

-- Student_ID
-- Course_ID
-- Student_Name

-- FD:

-- Student_ID
-- →
-- Student_Name

-- Answer:

-- Partial Dependency Exists

-- Not in 2NF

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- STUDENT

-- Student_ID
-- Name

-- Primary Key:

-- Student_ID

-- Answer:

-- Partial Dependency impossible

-- Table can satisfy 2NF

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is Second Normal Form?

-- Answer:

-- A relation is in 2NF if it is
-- already in 1NF and contains
-- no Partial Dependency.

-- =====================================
-- DAY 42 SUMMARY
-- =====================================

-- 2NF

-- Must satisfy 1NF

-- No Partial Dependency

-- Removes Redundancy

-- Improves Integrity

-- Partial Dependency occurs when
-- a non-key attribute depends on
-- part of a composite key.

-- 2NF removes Partial Dependency.