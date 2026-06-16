/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 27
Description : Rename Operation (ρ) in Relational Algebra
*/

-- =====================================
-- DAY 27 : RENAME OPERATION (ρ)
-- =====================================

-- What is Rename Operation?

-- Rename is a unary operation used
-- to rename a relation or attributes.

-- Symbol:

-- ρ (Rho)

-- Rename improves readability
-- and simplifies complex queries.

-- =====================================
-- WHY RENAME IS NEEDED?
-- =====================================

-- 1. Shorten Relation Names

-- 2. Avoid Ambiguity

-- 3. Improve Query Readability

-- 4. Useful in Self-Joins

-- =====================================
-- RENAME A RELATION
-- =====================================

-- Example:

-- STUDENT

-- Roll_No
-- Name
-- Age

-- Rename STUDENT as S

-- ρ S (STUDENT)

-- Result:

-- Relation Name:

-- S

-- =====================================
-- RENAME ATTRIBUTES
-- =====================================

-- Example:

-- STUDENT

-- Roll_No
-- Name
-- Age

-- Rename Attributes

-- ρ S(RNo, Student_Name, Student_Age)
-- (STUDENT)

-- Result:

-- RNo
-- Student_Name
-- Student_Age

-- =====================================
-- GENERAL FORMS
-- =====================================

-- Rename Relation

-- ρ New_Name(Relation)

-- Example:

-- ρ S(STUDENT)

-- -------------------------------------

-- Rename Attributes

-- ρ New_Name(Attribute1, Attribute2...)
-- (Relation)

-- Example:

-- ρ S(RNo, Name, Age)(STUDENT)

-- =====================================
-- PRACTICAL EXAMPLE
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Name
-- Salary

-- Rename Relation

-- ρ E(EMPLOYEE)

-- New Relation Name:

-- E

-- =====================================
-- SELF JOIN APPLICATION
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Name
-- Manager_ID

-- To compare employee records
-- with manager records from
-- same table:

-- ρ E1(EMPLOYEE)

-- ρ E2(EMPLOYEE)

-- Rename helps distinguish
-- between two copies of
-- the same relation.

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Unary Operation

-- Changes Names Only

-- Does Not Change Data

-- Output is a Relation

-- =====================================
-- SQL EQUIVALENT
-- =====================================

-- Relational Algebra:

-- ρ S(STUDENT)

-- SQL:

-- SELECT *
-- FROM STUDENT AS S;

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Relation:

-- COURSE

-- Rename as C

-- Answer:

-- ρ C(COURSE)

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Relation:

-- EMPLOYEE

-- Attributes:

-- Emp_ID
-- Name
-- Salary

-- Rename:

-- ID
-- Employee_Name
-- Income

-- Answer:

-- ρ E(ID, Employee_Name, Income)
-- (EMPLOYEE)

-- =====================================
-- DAY 27 SUMMARY
-- =====================================

-- Rename (ρ)

-- Used to Rename:

-- Relations

-- Attributes

-- Does Not Modify Data

-- Improves Readability

-- Useful in Self Joins

-- Input  : Relation
-- Output : Relation

-- Rename is a Unary Operation.