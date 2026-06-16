/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 25
Description : Set Difference Operation (-) in Relational Algebra
*/

-- =====================================
-- DAY 25 : SET DIFFERENCE OPERATION (-)
-- =====================================

-- What is Set Difference?

-- Set Difference is a binary operation
-- used to find tuples that exist in
-- one relation but not in another.

-- Symbol:

-- -

-- Result:

-- Tuples present in first relation
-- but absent in second relation.

-- =====================================
-- CONDITIONS
-- =====================================

-- Relations must be
-- Union Compatible.

-- Requirements:

-- 1. Same Number of Attributes

-- 2. Same Domains

-- 3. Same Data Types

-- =====================================
-- EXAMPLE TABLES
-- =====================================

-- STUDENT_A

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul
-- 103     | Priya

-- STUDENT_B

-- Roll_No | Name
-- ----------------
-- 102     | Rahul
-- 103     | Priya

-- =====================================
-- DIFFERENCE OPERATION
-- =====================================

-- STUDENT_A - STUDENT_B

-- Result:

-- Roll_No | Name
-- ----------------
-- 101     | Saloni

-- Because:

-- 101 exists in STUDENT_A
-- but not in STUDENT_B

-- =====================================
-- REVERSE DIFFERENCE
-- =====================================

-- STUDENT_B - STUDENT_A

-- Result:

-- Empty Relation

-- Because every tuple in
-- STUDENT_B already exists
-- in STUDENT_A

-- =====================================
-- IMPORTANT PROPERTY
-- =====================================

-- Difference is NOT Commutative.

-- A - B ≠ B - A

-- Example:

-- STUDENT_A - STUDENT_B

-- Result:

-- Saloni

-- STUDENT_B - STUDENT_A

-- Result:

-- Empty

-- Therefore:

-- A - B ≠ B - A

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Relational Algebra:

-- STUDENT_A - STUDENT_B

-- SQL:

-- SELECT *
-- FROM STUDENT_A

-- EXCEPT

-- SELECT *
-- FROM STUDENT_B;

-- =====================================
-- PRACTICAL EXAMPLE
-- =====================================

-- REGISTERED_STUDENTS

-- 101
-- 102
-- 103
-- 104

-- EXAM_APPEARED

-- 101
-- 103

-- REGISTERED_STUDENTS
-- -
-- EXAM_APPEARED

-- Result:

-- 102
-- 104

-- Students who did not
-- appear in exam.

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Binary Operation

-- Requires Union Compatibility

-- Removes Common Tuples

-- Returns Unique Tuples

-- Output is a Relation

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- A

-- 1
-- 2
-- 3

-- B

-- 2
-- 3

-- A - B

-- Result:

-- 1

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- EMPLOYEE

-- 1
-- 2
-- 3
-- 4

-- MANAGERS

-- 2
-- 4

-- EMPLOYEE - MANAGERS

-- Result:

-- 1
-- 3

-- =====================================
-- DAY 25 SUMMARY
-- =====================================

-- Difference (-)

-- Returns tuples present
-- in first relation but not
-- in second relation.

-- Requires:

-- Same Number of Attributes

-- Same Domains

-- Same Data Types

-- A - B ≠ B - A

-- Input  : Two Relations
-- Output : One Relation

-- Difference is a
-- Binary Operation.