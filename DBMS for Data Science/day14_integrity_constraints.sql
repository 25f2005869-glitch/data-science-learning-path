/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 14
Description : Integrity Constraints in Relational Model
*/

-- =====================================
-- DAY 14 : INTEGRITY CONSTRAINTS
-- =====================================

-- What are Integrity Constraints?

-- Integrity Constraints are rules
-- that ensure the accuracy,
-- consistency, and validity of data
-- in a database.

-- They prevent invalid data from
-- entering the database.

-- =====================================
-- TYPES OF INTEGRITY CONSTRAINTS
-- =====================================

-- 1. Domain Constraint
-- 2. Key Constraint
-- 3. Entity Integrity Constraint
-- 4. Referential Integrity Constraint

-- =====================================
-- 1. DOMAIN CONSTRAINT
-- =====================================

-- Domain Constraint ensures that
-- attribute values belong to a
-- valid domain.

-- Example:

-- Age

-- Valid Values:
-- 0 to 120

-- Invalid Values:
-- -5
-- 200

-- Gender

-- Valid Values:
-- Male
-- Female
-- Other

-- Domain Constraint prevents
-- invalid values.

-- =====================================
-- 2. KEY CONSTRAINT
-- =====================================

-- Key Constraint ensures that
-- every tuple can be uniquely
-- identified.

-- Example:

-- STUDENT

-- Roll_No
-- Name
-- Age

-- Roll_No must be unique.

-- Valid:

-- 101
-- 102
-- 103

-- Invalid:

-- 101
-- 101

-- Duplicate values are not allowed.

-- =====================================
-- 3. ENTITY INTEGRITY CONSTRAINT
-- =====================================

-- Primary Key cannot be NULL.

-- Every record must have
-- a unique identifier.

-- Example:

-- STUDENT

-- Roll_No | Name

-- 101     | Saloni
-- 102     | Rahul

-- Invalid Example:

-- NULL    | Saloni

-- Primary Key cannot be NULL.

-- =====================================
-- 4. REFERENTIAL INTEGRITY
-- =====================================

-- Maintains consistency between
-- related tables.

-- Foreign Key value must exist
-- in the referenced table.

-- Example:

-- STUDENT

-- Roll_No
-- 101
-- 102

-- ENROLLMENT

-- Roll_No
-- 101

-- Valid because 101 exists
-- in STUDENT table.

-- Invalid:

-- ENROLLMENT

-- Roll_No
-- 999

-- Since 999 does not exist
-- in STUDENT table.

-- Referential Integrity is violated.

-- =====================================
-- WHY INTEGRITY CONSTRAINTS?
-- =====================================

-- 1. Ensure Correct Data
-- 2. Maintain Consistency
-- 3. Prevent Duplicate Data
-- 4. Improve Reliability
-- 5. Maintain Relationships

-- =====================================
-- DAY 14 SUMMARY
-- =====================================

-- Domain Constraint
-- --> Valid Values

-- Key Constraint
-- --> Unique Values

-- Entity Integrity
-- --> Primary Key cannot be NULL

-- Referential Integrity
-- --> Foreign Key must match
--     existing Primary Key

-- Integrity Constraints help
-- maintain a reliable database.