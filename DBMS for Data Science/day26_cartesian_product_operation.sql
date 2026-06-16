/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 26
Description : Cartesian Product Operation (×) in Relational Algebra
*/

-- =====================================
-- DAY 26 : CARTESIAN PRODUCT (×)
-- =====================================

-- What is Cartesian Product?

-- Cartesian Product is a binary
-- operation that combines every tuple
-- of the first relation with every
-- tuple of the second relation.

-- Symbol:

-- ×

-- Result:

-- Every row of Relation A is paired
-- with every row of Relation B.

-- =====================================
-- FORMULA
-- =====================================

-- If:

-- Relation A has m rows

-- Relation B has n rows

-- Then:

-- A × B

-- Total Rows = m × n

-- =====================================
-- EXAMPLE TABLES
-- =====================================

-- STUDENT

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul

-- COURSE

-- Course_ID | Course_Name
-- ------------------------
-- C1        | DBMS
-- C2        | Python

-- =====================================
-- CARTESIAN PRODUCT
-- =====================================

-- STUDENT × COURSE

-- Result:

-- Roll_No | Name   | Course_ID | Course_Name
-- -------------------------------------------
-- 101     | Saloni | C1        | DBMS
-- 101     | Saloni | C2        | Python
-- 102     | Rahul  | C1        | DBMS
-- 102     | Rahul  | C2        | Python

-- Total Rows:

-- 2 × 2 = 4

-- =====================================
-- ANOTHER EXAMPLE
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- -------
-- E1
-- E2
-- E3

-- DEPARTMENT

-- Dept_ID
-- --------
-- D1
-- D2

-- EMPLOYEE × DEPARTMENT

-- Total Rows:

-- 3 × 2 = 6

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Binary Operation

-- No Matching Condition Required

-- Produces All Possible Combinations

-- Output is a Relation

-- =====================================
-- IMPORTANCE
-- =====================================

-- Cartesian Product forms the
-- basis of Join Operations.

-- Join = Cartesian Product
--       + Selection Condition

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Relational Algebra:

-- STUDENT × COURSE

-- SQL:

-- SELECT *
-- FROM STUDENT, COURSE;

-- or

-- SELECT *
-- FROM STUDENT
-- CROSS JOIN COURSE;

-- =====================================
-- DISADVANTAGES
-- =====================================

-- 1. Produces Large Results

-- 2. Many Unnecessary Tuples

-- 3. High Storage Cost

-- Therefore usually followed by
-- Selection conditions.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Relation A

-- 2 Rows

-- Relation B

-- 5 Rows

-- A × B

-- Answer:

-- 10 Rows

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Relation X

-- 4 Rows

-- Relation Y

-- 3 Rows

-- X × Y

-- Answer:

-- 12 Rows

-- =====================================
-- DAY 26 SUMMARY
-- =====================================

-- Cartesian Product (×)

-- Combines every tuple of
-- first relation with every tuple
-- of second relation.

-- Total Rows:

-- m × n

-- Forms the basis of Joins.

-- Input  : Two Relations
-- Output : One Relation

-- Cartesian Product is a
-- Binary Operation.