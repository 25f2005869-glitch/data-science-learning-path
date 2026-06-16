/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 29
Description : Division Operation (÷) in Relational Algebra
*/

-- =====================================
-- DAY 29 : DIVISION OPERATION (÷)
-- =====================================

-- What is Division Operation?

-- Division is a binary operation
-- used to find values in one relation
-- that are associated with ALL values
-- in another relation.

-- Symbol:

-- ÷

-- Division is mainly used for
-- "FOR ALL" type queries.

-- =====================================
-- WHY DIVISION?
-- =====================================

-- Used when we need answers like:

-- Find students who have enrolled
-- in ALL courses.

-- Find employees who work on
-- ALL projects.

-- Find suppliers who supply
-- ALL products.

-- =====================================
-- EXAMPLE TABLES
-- =====================================

-- ENROLLMENT

-- Student | Course
-- ----------------
-- A       | DBMS
-- A       | Python
-- B       | DBMS
-- B       | Python
-- C       | DBMS

-- COURSE

-- Course
-- -------
-- DBMS
-- Python

-- =====================================
-- DIVISION OPERATION
-- =====================================

-- ENROLLMENT ÷ COURSE

-- Result:

-- Student
-- --------
-- A
-- B

-- Explanation:

-- A enrolled in all courses.

-- B enrolled in all courses.

-- C enrolled only in DBMS.

-- Therefore:

-- A and B are returned.

-- =====================================
-- GENERAL IDEA
-- =====================================

-- Relation R(A,B)

-- Relation S(B)

-- R ÷ S

-- Result:

-- Values of A associated with
-- every value of B in S.

-- =====================================
-- PRACTICAL EXAMPLE
-- =====================================

-- WORKS_ON

-- Employee | Project
-- -------------------
-- E1       | P1
-- E1       | P2
-- E2       | P1
-- E2       | P2
-- E3       | P1

-- PROJECT

-- Project
-- --------
-- P1
-- P2

-- WORKS_ON ÷ PROJECT

-- Result:

-- E1
-- E2

-- Because E1 and E2 work
-- on all projects.

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Binary Operation

-- Used for Universal Quantification

-- Solves "FOR ALL" Queries

-- Output is a Relation

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Division is not directly available
-- in SQL.

-- It is implemented using:

-- NOT EXISTS

-- Nested Queries

-- GROUP BY

-- HAVING

-- Example Idea:

-- Find students enrolled in
-- all available courses.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- SUPPLIES

-- Supplier | Product
-- -------------------
-- S1       | P1
-- S1       | P2
-- S2       | P1

-- PRODUCT

-- Product
-- --------
-- P1
-- P2

-- SUPPLIES ÷ PRODUCT

-- Result:

-- S1

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- STUDENT_COURSE

-- Student | Subject
-- ------------------
-- A       | Math
-- A       | Science
-- B       | Math

-- SUBJECT

-- Subject
-- --------
-- Math
-- Science

-- STUDENT_COURSE ÷ SUBJECT

-- Result:

-- A

-- =====================================
-- DAY 29 SUMMARY
-- =====================================

-- Division (÷)

-- Used for:

-- "FOR ALL" Queries

-- Example:

-- Students enrolled in
-- all courses.

-- Employees working on
-- all projects.

-- Suppliers supplying
-- all products.

-- Input  : Two Relations
-- Output : One Relation

-- Division is a
-- Binary Operation.