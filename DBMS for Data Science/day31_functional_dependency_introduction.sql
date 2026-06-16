/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 31
Description : Introduction to Functional Dependency
*/

-- =====================================
-- DAY 31 : FUNCTIONAL DEPENDENCY (FD)
-- =====================================

-- What is Functional Dependency?

-- Functional Dependency (FD) is a
-- relationship between attributes
-- in a relation.

-- It describes how one attribute
-- determines another attribute.

-- Functional Dependency is the
-- foundation of Normalization.

-- =====================================
-- NOTATION
-- =====================================

-- X → Y

-- Read as:

-- X determines Y

-- or

-- Y is functionally dependent on X

-- =====================================
-- EXAMPLE 1
-- =====================================

-- STUDENT

-- Roll_No | Name   | Age
-- ------------------------
-- 101     | Saloni | 20
-- 102     | Rahul  | 21

-- Here:

-- Roll_No → Name

-- Roll_No → Age

-- Because one Roll_No uniquely
-- determines one Name and one Age.

-- =====================================
-- DETERMINANT
-- =====================================

-- The attribute on the left side
-- of FD is called Determinant.

-- Example:

-- Roll_No → Name

-- Determinant:

-- Roll_No

-- =====================================
-- DEPENDENT ATTRIBUTE
-- =====================================

-- The attribute on the right side
-- of FD is called Dependent Attribute.

-- Example:

-- Roll_No → Name

-- Dependent Attribute:

-- Name

-- =====================================
-- EXAMPLE 2
-- =====================================

-- EMPLOYEE

-- Emp_ID | Name | Department
-- ---------------------------
-- E101   | Ram  | HR
-- E102   | Ravi | IT

-- Functional Dependencies:

-- Emp_ID → Name

-- Emp_ID → Department

-- =====================================
-- VALID FUNCTIONAL DEPENDENCY
-- =====================================

-- STUDENT

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul

-- Roll_No uniquely identifies
-- each Name.

-- Therefore:

-- Roll_No → Name

-- Valid FD

-- =====================================
-- INVALID FUNCTIONAL DEPENDENCY
-- =====================================

-- STUDENT

-- Roll_No | Department
-- ---------------------
-- 101     | CSE
-- 102     | CSE
-- 103     | IT

-- Department does not uniquely
-- determine Roll_No.

-- Therefore:

-- Department → Roll_No

-- Invalid FD

-- =====================================
-- IMPORTANCE OF FD
-- =====================================

-- 1. Database Design

-- 2. Normalization

-- 3. Remove Redundancy

-- 4. Maintain Consistency

-- 5. Improve Data Integrity

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Functional Dependency:

-- Expresses Relationship
-- Between Attributes

-- Helps Identify Keys

-- Helps Normalize Tables

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- STUDENT

-- Roll_No | Name

-- Identify FD

-- Answer:

-- Roll_No → Name

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- EMPLOYEE

-- Emp_ID | Salary

-- Answer:

-- Emp_ID → Salary

-- =====================================
-- DAY 31 SUMMARY
-- =====================================

-- Functional Dependency (FD)

-- X → Y

-- Means:

-- X determines Y

-- Left Side:
-- Determinant

-- Right Side:
-- Dependent Attribute

-- Functional Dependency is
-- the foundation of
-- Normalization in DBMS.