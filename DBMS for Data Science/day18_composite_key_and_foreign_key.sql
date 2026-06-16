/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 18
Description : Composite Key and Foreign Key
*/

-- =====================================
-- DAY 18 : COMPOSITE KEY AND FOREIGN KEY
-- =====================================

-- What is a Composite Key?

-- A Composite Key is a Primary Key
-- formed using two or more attributes.

-- A single attribute alone cannot
-- uniquely identify a record.

-- Therefore multiple attributes
-- are combined.

-- =====================================
-- EXAMPLE OF COMPOSITE KEY
-- =====================================

-- ENROLLMENT

-- Roll_No | Course_ID
-- --------------------
-- 101     | DBMS
-- 101     | Python
-- 102     | DBMS

-- Roll_No alone is not unique.

-- Course_ID alone is not unique.

-- Combination:

-- (Roll_No, Course_ID)

-- uniquely identifies each record.

-- Therefore:

-- Composite Key =
-- (Roll_No, Course_ID)

-- =====================================
-- ANOTHER EXAMPLE
-- =====================================

-- ORDER_DETAILS

-- Order_ID | Product_ID | Quantity
-- ---------------------------------
-- 1001     | P101       | 2
-- 1001     | P102       | 1

-- Composite Key:

-- (Order_ID, Product_ID)

-- =====================================
-- ADVANTAGES OF COMPOSITE KEY
-- =====================================

-- 1. Ensures Uniqueness
-- 2. Avoids Duplicate Records
-- 3. Useful in Many-to-Many Relationships

-- =====================================
-- FOREIGN KEY
-- =====================================

-- A Foreign Key is an attribute
-- that creates a relationship
-- between two tables.

-- A Foreign Key refers to the
-- Primary Key of another table.

-- =====================================
-- EXAMPLE
-- =====================================

-- STUDENT

-- Roll_No | Name
-- ----------------
-- 101     | Saloni
-- 102     | Rahul

-- Primary Key:

-- Roll_No

-- =====================================

-- ENROLLMENT

-- Roll_No | Course
-- -------------------
-- 101     | DBMS
-- 102     | Python

-- Here:

-- ENROLLMENT.Roll_No

-- is a Foreign Key.

-- It refers to:

-- STUDENT.Roll_No

-- =====================================
-- WHY FOREIGN KEYS?
-- =====================================

-- 1. Maintain Relationships
-- 2. Ensure Data Consistency
-- 3. Enforce Referential Integrity
-- 4. Prevent Invalid References

-- =====================================
-- VALID FOREIGN KEY EXAMPLE
-- =====================================

-- STUDENT

-- Roll_No
-- 101
-- 102

-- ENROLLMENT

-- Roll_No
-- 101

-- Valid because 101 exists
-- in STUDENT table.

-- =====================================
-- INVALID FOREIGN KEY EXAMPLE
-- =====================================

-- ENROLLMENT

-- Roll_No
-- 999

-- Invalid because 999 does not exist
-- in STUDENT table.

-- Referential Integrity is violated.

-- =====================================
-- COMPOSITE KEY VS FOREIGN KEY
-- =====================================

-- Composite Key

-- Combination of multiple attributes
-- used to uniquely identify records.

-- Foreign Key

-- Attribute used to establish
-- relationships between tables.

-- =====================================
-- DAY 18 SUMMARY
-- =====================================

-- Composite Key

-- Two or more attributes together
-- uniquely identify a record.

-- Example:

-- (Roll_No, Course_ID)

-- Foreign Key

-- Refers to Primary Key
-- of another table.

-- Used to connect tables.

-- Composite Key:
-- Identification

-- Foreign Key:
-- Relationship