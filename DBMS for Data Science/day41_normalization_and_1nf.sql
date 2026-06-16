/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 41
Description : Introduction to Normalization and First Normal Form (1NF)
*/

-- =====================================
-- DAY 41 : NORMALIZATION AND 1NF
-- =====================================

-- What is Normalization?

-- Normalization is the process of
-- organizing data in a database to:

-- 1. Reduce Data Redundancy

-- 2. Eliminate Anomalies

-- 3. Improve Data Integrity

-- 4. Improve Database Design

-- =====================================
-- WHY NORMALIZATION?
-- =====================================

-- Without Normalization:

-- Duplicate Data Exists

-- Storage Wastage Occurs

-- Update Problems Occur

-- Insertion Problems Occur

-- Deletion Problems Occur

-- =====================================
-- TYPES OF ANOMALIES
-- =====================================

-- 1. Insertion Anomaly

-- 2. Update Anomaly

-- 3. Deletion Anomaly

-- =====================================
-- INSERTION ANOMALY
-- =====================================

-- Cannot insert data without
-- inserting unnecessary information.

-- Example:

-- Student and Course information
-- stored in same table.

-- New Course cannot be added
-- until a student enrolls.

-- =====================================
-- UPDATE ANOMALY
-- =====================================

-- Same data appears in multiple rows.

-- Updating one row and forgetting
-- another creates inconsistency.

-- Example:

-- Department name stored
-- repeatedly for many students.

-- =====================================
-- DELETION ANOMALY
-- =====================================

-- Deleting one record may remove
-- important information.

-- Example:

-- Deleting the last student of a
-- course may also remove course data.

-- =====================================
-- NORMAL FORMS
-- =====================================

-- 1NF  --> First Normal Form

-- 2NF  --> Second Normal Form

-- 3NF  --> Third Normal Form

-- BCNF --> Boyce Codd Normal Form

-- 4NF  --> Fourth Normal Form

-- 5NF  --> Fifth Normal Form

-- =====================================
-- FIRST NORMAL FORM (1NF)
-- =====================================

-- Definition:

-- A relation is in 1NF if:

-- Every attribute contains
-- Atomic Values.

-- Atomic means:

-- Indivisible

-- Single Value

-- =====================================
-- NOT IN 1NF
-- =====================================

-- STUDENT

-- Roll_No | Name   | Phone_Numbers
-- -----------------------------------
-- 101     | Saloni | 9876,8765
-- 102     | Rahul  | 7654,6543

-- Phone_Numbers contains
-- multiple values.

-- Therefore:

-- NOT in 1NF

-- =====================================
-- CONVERT TO 1NF
-- =====================================

-- STUDENT

-- Roll_No | Name   | Phone_Number
-- ---------------------------------
-- 101     | Saloni | 9876
-- 101     | Saloni | 8765
-- 102     | Rahul  | 7654
-- 102     | Rahul  | 6543

-- Now every cell contains
-- a single value.

-- Therefore:

-- Relation is in 1NF

-- =====================================
-- RULES OF 1NF
-- =====================================

-- 1. No Multi-Valued Attributes

-- 2. No Repeating Groups

-- 3. Each Cell Contains One Value

-- 4. Rows Must Be Unique

-- =====================================
-- BENEFITS OF 1NF
-- =====================================

-- 1. Better Data Organization

-- 2. Easier Query Processing

-- 3. Removes Repeating Groups

-- 4. Foundation for Higher NFs

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- STUDENT

-- Roll_No | Subject
-- ------------------
-- 101     | DBMS,SQL

-- Is it in 1NF?

-- Answer:

-- No

-- Multi-Valued Attribute Exists

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- EMPLOYEE

-- Emp_ID | Name
-- ----------------
-- E1     | Ram

-- One value per cell.

-- Answer:

-- Relation is in 1NF

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is 1NF?

-- Answer:

-- A relation is in First Normal Form
-- if every attribute contains only
-- atomic (single) values.

-- =====================================
-- DAY 41 SUMMARY
-- =====================================

-- Normalization

-- Reduces Redundancy

-- Removes Anomalies

-- Improves Integrity

-- -------------------------------------

-- 1NF

-- Atomic Values Only

-- No Repeating Groups

-- No Multi-Valued Attributes

-- 1NF is the first step
-- toward a well-designed database.