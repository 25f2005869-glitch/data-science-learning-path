/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 44
Description : Boyce-Codd Normal Form (BCNF)
*/

-- =====================================
-- DAY 44 : BOYCE-CODD NORMAL FORM
-- =====================================

-- What is BCNF?

-- BCNF stands for:

-- Boyce-Codd Normal Form

-- It is a stronger version
-- of Third Normal Form (3NF).

-- Proposed by:

-- Raymond Boyce
-- Edgar F. Codd

-- =====================================
-- WHY BCNF?
-- =====================================

-- Some relations satisfy 3NF
-- but still contain redundancy.

-- BCNF removes such anomalies.

-- =====================================
-- BCNF RULE
-- =====================================

-- A relation is in BCNF if:

-- For every Functional Dependency

-- X → Y

-- X must be a Super Key.

-- =====================================
-- SIMPLE EXAMPLE
-- =====================================

-- STUDENT

-- Roll_No
-- Name

-- FD:

-- Roll_No → Name

-- Roll_No is a Super Key.

-- Therefore:

-- Relation is in BCNF.

-- =====================================
-- EXAMPLE WHERE 3NF EXISTS
-- BUT BCNF FAILS
-- =====================================

-- Relation:

-- R(Student, Course, Instructor)

-- Functional Dependencies:

-- (Student, Course)
-- →
-- Instructor

-- Instructor
-- →
-- Course

-- =====================================
-- CANDIDATE KEYS
-- =====================================

-- Candidate Key:

-- (Student, Course)

-- =====================================
-- ANALYSIS
-- =====================================

-- Instructor → Course

-- Here:

-- Instructor is NOT a Super Key.

-- Therefore:

-- BCNF Violated.

-- Relation is NOT in BCNF.

-- =====================================
-- WHY PROBLEM OCCURS?
-- =====================================

-- Redundant Data

-- Update Anomalies

-- Insertion Anomalies

-- Deletion Anomalies

-- =====================================
-- DECOMPOSITION INTO BCNF
-- =====================================

-- R1(Instructor, Course)

-- R2(Student, Instructor)

-- Now:

-- Instructor → Course

-- Instructor is Key in R1.

-- No BCNF Violation.

-- =====================================
-- 3NF VS BCNF
-- =====================================

-- 3NF

-- For X → Y

-- X is Super Key

-- OR

-- Y is Prime Attribute

-- -------------------------------------

-- BCNF

-- For X → Y

-- X MUST be Super Key

-- No Exception.

-- =====================================
-- IMPORTANT FACT
-- =====================================

-- Every BCNF Relation
-- is in 3NF.

-- But

-- Every 3NF Relation
-- is NOT necessarily in BCNF.

-- =====================================
-- BENEFITS OF BCNF
-- =====================================

-- 1. Removes Redundancy

-- 2. Eliminates Anomalies

-- 3. Better Database Design

-- 4. Stronger Integrity

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- FD:

-- Roll_No → Name

-- Roll_No is Super Key.

-- Answer:

-- BCNF Satisfied.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- FD:

-- Instructor → Course

-- Instructor is NOT Super Key.

-- Answer:

-- BCNF Violated.

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is BCNF?

-- Answer:

-- A relation is in BCNF if
-- for every Functional Dependency
-- X → Y, X is a Super Key.

-- =====================================
-- DAY 44 SUMMARY
-- =====================================

-- BCNF

-- Stronger than 3NF

-- Rule:

-- X → Y

-- X must be Super Key

-- Every BCNF is 3NF

-- Every 3NF is NOT BCNF

-- BCNF removes remaining
-- redundancy and anomalies.