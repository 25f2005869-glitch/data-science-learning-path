/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 46
Description : Fourth Normal Form (4NF)
*/

-- =====================================
-- DAY 46 : FOURTH NORMAL FORM (4NF)
-- =====================================

-- What is 4NF?

-- Fourth Normal Form (4NF) is a
-- higher level of normalization
-- that removes Multivalued
-- Dependencies (MVDs).

-- A relation is in 4NF if:

-- 1. It is already in BCNF

-- AND

-- 2. It contains no non-trivial
--    Multivalued Dependency.

-- =====================================
-- WHAT IS A MULTIVALUED
-- DEPENDENCY (MVD)?
-- =====================================

-- Notation:

-- A ↠ B

-- Read as:

-- A Multidetermines B

-- Meaning:

-- For one value of A,
-- multiple independent values
-- of B may exist.

-- =====================================
-- EXAMPLE
-- =====================================

-- STUDENT

-- Student_ID
-- Hobby
-- Language

-- Example Data:

-- Student_ID | Hobby  | Language
-- -------------------------------
-- S1         | Music  | English
-- S1         | Music  | Hindi
-- S1         | Dance  | English
-- S1         | Dance  | Hindi

-- =====================================
-- ANALYSIS
-- =====================================

-- Student S1 has:

-- Hobbies:

-- Music
-- Dance

-- Languages:

-- English
-- Hindi

-- Hobby and Language are
-- independent of each other.

-- Therefore:

-- Student_ID ↠ Hobby

-- Student_ID ↠ Language

-- Multivalued Dependencies exist.

-- =====================================
-- PROBLEM
-- =====================================

-- Data Redundancy

-- Repeated Combinations

-- Storage Wastage

-- Update Anomalies

-- =====================================
-- CONVERT TO 4NF
-- =====================================

-- Split into:

-- STUDENT_HOBBY

-- Student_ID
-- Hobby

-- ----------------

-- S1
-- Music

-- S1
-- Dance

-- =====================================

-- STUDENT_LANGUAGE

-- Student_ID
-- Language

-- ----------------

-- S1
-- English

-- S1
-- Hindi

-- =====================================

-- Now:

-- No Multivalued Dependency
-- problem remains.

-- Relation satisfies 4NF.

-- =====================================
-- TRIVIAL MVD
-- =====================================

-- A ↠ B is Trivial if:

-- B ⊆ A

-- OR

-- A ∪ B = Relation

-- Such MVDs do not violate 4NF.

-- =====================================
-- BCNF VS 4NF
-- =====================================

-- BCNF

-- Handles Functional Dependencies

-- -------------------------------------

-- 4NF

-- Handles Multivalued Dependencies

-- =====================================
-- BENEFITS OF 4NF
-- =====================================

-- 1. Eliminates Redundancy

-- 2. Improves Consistency

-- 3. Reduces Storage Waste

-- 4. Better Database Design

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- STUDENT

-- Student_ID
-- Hobby
-- Language

-- Student_ID ↠ Hobby

-- Student_ID ↠ Language

-- Answer:

-- Not in 4NF

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Split into:

-- STUDENT_HOBBY

-- STUDENT_LANGUAGE

-- Answer:

-- 4NF Achieved

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is 4NF?

-- Answer:

-- A relation is in Fourth
-- Normal Form if it is in BCNF
-- and contains no non-trivial
-- Multivalued Dependency.

-- =====================================
-- DAY 46 SUMMARY
-- =====================================

-- 4NF

-- Must satisfy BCNF

-- Removes:

-- Multivalued Dependency (MVD)

-- Notation:

-- A ↠ B

-- Solution:

-- Decompose relation into
-- smaller independent relations.

-- 4NF reduces redundancy caused
-- by multiple independent values.