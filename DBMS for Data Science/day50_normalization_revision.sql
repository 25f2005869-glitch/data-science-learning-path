/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 50
Description : Complete Revision of Normalization (1NF to 5NF)
*/

-- =====================================
-- DAY 50 : NORMALIZATION REVISION
-- =====================================

-- This day is dedicated to revising
-- all Normalization concepts covered
-- from Day 41 to Day 49.

-- =====================================
-- WHY NORMALIZATION?
-- =====================================

-- Normalization helps:

-- 1. Reduce Redundancy

-- 2. Improve Consistency

-- 3. Improve Data Integrity

-- 4. Eliminate Anomalies

-- 5. Improve Database Design

-- =====================================
-- TYPES OF ANOMALIES
-- =====================================

-- 1. Insertion Anomaly

-- Cannot insert information
-- independently.

-- -------------------------------------

-- 2. Update Anomaly

-- Same data repeated in multiple rows.

-- Updating one row may cause
-- inconsistency.

-- -------------------------------------

-- 3. Deletion Anomaly

-- Deleting one record may remove
-- useful information.

-- =====================================
-- NORMALIZATION HIERARCHY
-- =====================================

-- UNF

-- ↓

-- 1NF

-- ↓

-- 2NF

-- ↓

-- 3NF

-- ↓

-- BCNF

-- ↓

-- 4NF

-- ↓

-- 5NF

-- =====================================
-- FIRST NORMAL FORM (1NF)
-- =====================================

-- Rule:

-- Atomic Values Only

-- Removes:

-- Multi-Valued Attributes

-- Repeating Groups

-- Example:

-- Phone = 9876,8765

-- Not in 1NF

-- -------------------------------------

-- Phone = 9876

-- Phone = 8765

-- In 1NF

-- =====================================
-- SECOND NORMAL FORM (2NF)
-- =====================================

-- Rule:

-- Must be in 1NF

-- No Partial Dependency

-- Removes:

-- Partial Dependency

-- Example:

-- Student_ID
-- →
-- Student_Name

-- while key is:

-- (Student_ID, Course_ID)

-- Not in 2NF

-- =====================================
-- THIRD NORMAL FORM (3NF)
-- =====================================

-- Rule:

-- Must be in 2NF

-- No Transitive Dependency

-- Example:

-- Emp_ID
-- →
-- Dept_ID

-- Dept_ID
-- →
-- Dept_Name

-- Therefore:

-- Emp_ID
-- →
-- Dept_Name

-- Not in 3NF

-- =====================================
-- BCNF
-- =====================================

-- Rule:

-- For every FD:

-- X → Y

-- X must be Super Key

-- Stronger than 3NF

-- Removes:

-- Remaining FD-based Redundancy

-- =====================================
-- FOURTH NORMAL FORM (4NF)
-- =====================================

-- Rule:

-- Must be in BCNF

-- No Multivalued Dependency

-- Notation:

-- A ↠ B

-- Example:

-- Student_ID ↠ Hobby

-- Student_ID ↠ Language

-- Not in 4NF

-- =====================================
-- FIFTH NORMAL FORM (5NF)
-- =====================================

-- Rule:

-- Must be in 4NF

-- No Join Dependency

-- Removes:

-- Join Dependency

-- Improves decomposition quality.

-- =====================================
-- COMPARISON TABLE
-- =====================================

-- 1NF

-- Removes:

-- Multi-Valued Attributes

-- -------------------------------------

-- 2NF

-- Removes:

-- Partial Dependency

-- -------------------------------------

-- 3NF

-- Removes:

-- Transitive Dependency

-- -------------------------------------

-- BCNF

-- Removes:

-- FD-Based Redundancy

-- -------------------------------------

-- 4NF

-- Removes:

-- Multivalued Dependency

-- -------------------------------------

-- 5NF

-- Removes:

-- Join Dependency

-- =====================================
-- COMPLETE NORMALIZATION FLOW
-- =====================================

-- UNF

-- Multi-Valued Attributes

-- ↓

-- 1NF

-- Atomic Values

-- ↓

-- 2NF

-- No Partial Dependency

-- ↓

-- 3NF

-- No Transitive Dependency

-- ↓

-- BCNF

-- Determinant is Super Key

-- ↓

-- 4NF

-- No Multivalued Dependency

-- ↓

-- 5NF

-- No Join Dependency

-- =====================================
-- IMPORTANT INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Normalization?

-- Answer:

-- Process of organizing data
-- to reduce redundancy and
-- improve integrity.

-- -------------------------------------

-- Q2. Which Normal Form removes
-- Partial Dependency?

-- Answer:

-- 2NF

-- -------------------------------------

-- Q3. Which Normal Form removes
-- Transitive Dependency?

-- Answer:

-- 3NF

-- -------------------------------------

-- Q4. Which Normal Form removes
-- Multivalued Dependency?

-- Answer:

-- 4NF

-- -------------------------------------

-- Q5. Which Normal Form removes
-- Join Dependency?

-- Answer:

-- 5NF

-- -------------------------------------

-- Q6. Which is stronger:
-- 3NF or BCNF?

-- Answer:

-- BCNF

-- -------------------------------------

-- Q7. Is every BCNF relation
-- in 3NF?

-- Answer:

-- Yes

-- =====================================
-- FINAL DAY 50 SUMMARY
-- =====================================

-- 1NF

-- Atomic Values

-- -------------------------------------

-- 2NF

-- No Partial Dependency

-- -------------------------------------

-- 3NF

-- No Transitive Dependency

-- -------------------------------------

-- BCNF

-- Determinant is Super Key

-- -------------------------------------

-- 4NF

-- No Multivalued Dependency

-- -------------------------------------

-- 5NF

-- No Join Dependency

-- =====================================

-- NORMALIZATION UNIT COMPLETE

-- Day 41 → 1NF

-- Day 42 → 2NF

-- Day 43 → 3NF

-- Day 44 → BCNF

-- Day 46 → 4NF

-- Day 47 → 5NF

-- Day 48 → Complete Example

-- Day 49 → Practice Problems

-- Day 50 → Revision

-- =====================================

-- END OF NORMALIZATION UNIT