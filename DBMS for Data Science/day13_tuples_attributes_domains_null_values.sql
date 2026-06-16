/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 13
Description : Tuples, Attributes, Domains and Null Values
*/

-- =====================================
-- DAY 13 : TUPLES, ATTRIBUTES,
-- DOMAINS AND NULL VALUES
-- =====================================

-- Revision

-- Relation   --> Table
-- Tuple      --> Row
-- Attribute  --> Column

-- =====================================
-- TUPLES
-- =====================================

-- A Tuple represents a single row
-- in a relation.

-- Example:

-- STUDENT

-- +---------+--------+-----+
-- | Roll_No | Name   | Age |
-- +---------+--------+-----+
-- | 101     | Saloni | 20  |
-- | 102     | Rahul  | 21  |
-- +---------+--------+-----+

-- Tuple 1:

-- (101, Saloni, 20)

-- Tuple 2:

-- (102, Rahul, 21)

-- Each row is called a Tuple.

-- =====================================
-- ATTRIBUTES
-- =====================================

-- Attributes represent columns
-- in a relation.

-- Example:

-- Roll_No
-- Name
-- Age

-- These columns are Attributes.

-- Attributes describe properties
-- of an entity.

-- =====================================
-- DOMAIN
-- =====================================

-- Domain is the set of all valid
-- values that an attribute can have.

-- Example:

-- Age

-- Domain:

-- 0 to 120

-- Gender

-- Domain:

-- Male
-- Female
-- Other

-- Roll_No

-- Domain:

-- Positive Integers

-- =====================================
-- IMPORTANCE OF DOMAIN
-- =====================================

-- 1. Ensures Data Validity
-- 2. Reduces Errors
-- 3. Improves Consistency
-- 4. Maintains Data Integrity

-- =====================================
-- NULL VALUE
-- =====================================

-- NULL means:

-- Unknown Value
-- Missing Value
-- Not Available Value

-- NULL does NOT mean:

-- Zero (0)
-- Empty String ('')
-- False

-- =====================================
-- EXAMPLE OF NULL
-- =====================================

-- STUDENT

-- +---------+--------+------+
-- | Roll_No | Name   | Phone|
-- +---------+--------+------+
-- | 101     | Saloni | NULL |
-- +---------+--------+------+

-- Phone Number is not available.

-- Therefore NULL is stored.

-- =====================================
-- TYPES OF NULL SITUATIONS
-- =====================================

-- 1. Value Unknown

-- Example:
-- Student's phone number is unknown.

-- 2. Value Missing

-- Example:
-- Data not entered yet.

-- 3. Value Not Applicable

-- Example:
-- Spouse_Name for an unmarried person.

-- =====================================
-- PROBLEMS WITH NULL VALUES
-- =====================================

-- 1. Difficult Calculations
-- 2. Complex Comparisons
-- 3. Special Handling Required

-- Example:

-- NULL = NULL

-- Result:
-- Unknown

-- Not True

-- =====================================
-- DAY 13 SUMMARY
-- =====================================

-- Tuple
-- --> Row of a Table

-- Attribute
-- --> Column of a Table

-- Domain
-- --> Valid Set of Values

-- NULL
-- --> Unknown / Missing Value

-- NULL is different from:
-- 0
-- Empty String
-- False