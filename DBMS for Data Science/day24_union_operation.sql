/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 24
Description : Union Operation (∪) in Relational Algebra
*/

-- =====================================
-- DAY 24 : UNION OPERATION (∪)
-- =====================================

-- What is Union?

-- Union is a binary operation
-- used to combine tuples from
-- two relations.

-- Symbol:

-- ∪

-- The result contains all tuples
-- from both relations.

-- Duplicate tuples are removed.

-- =====================================
-- CONDITIONS FOR UNION
-- =====================================

-- Two relations must be
-- Union Compatible.

-- Requirements:

-- 1. Same Number of Attributes

-- 2. Same Domain of Attributes

-- 3. Compatible Data Types

-- =====================================
-- EXAMPLE TABLES
-- =====================================

-- STUDENT_A

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul

-- STUDENT_B

-- Roll_No | Name
-- ----------------
-- 103     | Priya
-- 104     | Amit

-- =====================================
-- UNION OPERATION
-- =====================================

-- STUDENT_A ∪ STUDENT_B

-- Result:

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul
-- 103     | Priya
-- 104     | Amit

-- =====================================
-- DUPLICATE REMOVAL
-- =====================================

-- STUDENT_A

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul

-- STUDENT_B

-- Roll_No | Name
-- ----------------
-- 102     | Rahul
-- 103     | Priya

-- STUDENT_A ∪ STUDENT_B

-- Result:

-- 101     | Saloni
-- 102     | Rahul
-- 103     | Priya

-- Duplicate tuple removed.

-- =====================================
-- INVALID UNION EXAMPLE
-- =====================================

-- STUDENT

-- Roll_No | Name

-- COURSE

-- Course_ID | Course_Name | Credits

-- Different number of attributes.

-- Therefore:

-- STUDENT ∪ COURSE

-- Invalid

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Union:

-- Works on Two Relations

-- Removes Duplicate Tuples

-- Requires Union Compatibility

-- Output is a Relation

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Relational Algebra:

-- STUDENT_A ∪ STUDENT_B

-- SQL:

-- SELECT *
-- FROM STUDENT_A

-- UNION

-- SELECT *
-- FROM STUDENT_B;

-- =====================================
-- UNION VS UNION ALL
-- =====================================

-- Relational Algebra:

-- Always removes duplicates.

-- SQL UNION:

-- Removes duplicates.

-- SQL UNION ALL:

-- Keeps duplicates.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- EMPLOYEE_A

-- Emp_ID
-- 1
-- 2

-- EMPLOYEE_B

-- Emp_ID
-- 2
-- 3

-- EMPLOYEE_A ∪ EMPLOYEE_B

-- Result:

-- 1
-- 2
-- 3

-- =====================================
-- DAY 24 SUMMARY
-- =====================================

-- Union (∪)

-- Combines Two Relations

-- Removes Duplicate Tuples

-- Requires:

-- Same Number of Attributes

-- Same Domains

-- Same Data Types

-- Input  : Two Relations
-- Output : One Relation

-- Union is a Binary Operation.