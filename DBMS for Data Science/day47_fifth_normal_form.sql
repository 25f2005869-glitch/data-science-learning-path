/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 47
Description : Fifth Normal Form (5NF)
*/

-- =====================================
-- DAY 47 : FIFTH NORMAL FORM (5NF)
-- =====================================

-- What is 5NF?

-- Fifth Normal Form (5NF) is the
-- highest commonly discussed
-- normal form in DBMS.

-- It deals with:

-- Join Dependency (JD)

-- =====================================
-- DEFINITION
-- =====================================

-- A relation is in 5NF if:

-- 1. It is already in 4NF

-- AND

-- 2. Every Join Dependency is
--    implied by Candidate Keys.

-- =====================================
-- WHAT IS JOIN DEPENDENCY?
-- =====================================

-- Join Dependency occurs when
-- a relation can be decomposed
-- into multiple smaller relations
-- and reconstructed correctly
-- using joins.

-- Notation:

-- JD(R1, R2, R3)

-- =====================================
-- WHY 5NF?
-- =====================================

-- Some redundancy still exists
-- even after reaching 4NF.

-- Such redundancy can be removed
-- using Join Dependency analysis.

-- =====================================
-- EXAMPLE
-- =====================================

-- SUPPLIER_PROJECT_PART

-- Supplier
-- Project
-- Part

-- Example Data:

-- S1 | P1 | A

-- S1 | P2 | A

-- S2 | P1 | A

-- =====================================
-- ANALYSIS
-- =====================================

-- Supplier works on Projects.

-- Supplier supplies Parts.

-- Project uses Parts.

-- These relationships are
-- independent.

-- Therefore storing all three
-- together may create redundancy.

-- =====================================
-- DECOMPOSITION
-- =====================================

-- SP (Supplier, Project)

-- Supplier | Project

-- S1       | P1

-- S1       | P2

-- S2       | P1

-- =====================================

-- SJ (Supplier, Part)

-- Supplier | Part

-- S1       | A

-- S2       | A

-- =====================================

-- PJ (Project, Part)

-- Project | Part

-- P1      | A

-- P2      | A

-- =====================================

-- Original relation can be
-- reconstructed through joins.

-- Therefore:

-- Relation can be converted
-- into 5NF.

-- =====================================
-- BENEFITS OF 5NF
-- =====================================

-- 1. Removes Remaining Redundancy

-- 2. Improves Consistency

-- 3. Eliminates Join Anomalies

-- 4. Better Database Design

-- =====================================
-- 4NF VS 5NF
-- =====================================

-- 4NF

-- Removes:

-- Multivalued Dependency

-- -------------------------------------

-- 5NF

-- Removes:

-- Join Dependency

-- =====================================
-- IMPORTANT FACT
-- =====================================

-- 5NF is rarely required
-- in practical databases.

-- Most real-world systems
-- stop at:

-- 3NF

-- or

-- BCNF

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which dependency is handled
-- by 5NF?

-- Answer:

-- Join Dependency

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Must a relation be in 4NF
-- before reaching 5NF?

-- Answer:

-- Yes

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is Fifth Normal Form?

-- Answer:

-- A relation is in 5NF if it is
-- in 4NF and every Join Dependency
-- is implied by Candidate Keys.

-- =====================================
-- DAY 47 SUMMARY
-- =====================================

-- 5NF

-- Must satisfy 4NF

-- Removes:

-- Join Dependency

-- Goal:

-- Eliminate Remaining Redundancy

-- Improve Database Design

-- Highest commonly studied
-- Normal Form in DBMS.