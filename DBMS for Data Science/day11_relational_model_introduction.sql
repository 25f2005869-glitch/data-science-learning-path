/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 11
Description : Introduction to Relational Model
*/

-- =====================================
-- DAY 11 : RELATIONAL MODEL
-- =====================================

-- What is a Relational Model?

-- The Relational Model was proposed
-- by E. F. Codd in 1970.

-- It is the most widely used
-- database model today.

-- In the Relational Model,
-- data is stored in tables.

-- Examples:

-- Student Table
-- Employee Table
-- Course Table

-- =====================================
-- RELATION
-- =====================================

-- A Relation is another name
-- for a Table.

-- Example:

-- STUDENT

-- +---------+--------+-----+
-- | Roll_No | Name   | Age |
-- +---------+--------+-----+
-- | 101     | Saloni | 20  |
-- | 102     | Rahul  | 21  |
-- +---------+--------+-----+

-- Here STUDENT is a Relation.

-- =====================================
-- TUPLE
-- =====================================

-- A Tuple represents a Row
-- in a table.

-- Example:

-- 101 | Saloni | 20

-- This complete row is a Tuple.

-- =====================================
-- ATTRIBUTE
-- =====================================

-- Attributes represent Columns
-- in a table.

-- Example:

-- Roll_No
-- Name
-- Age

-- These are Attributes.

-- =====================================
-- DOMAIN
-- =====================================

-- Domain is the set of all
-- possible values an attribute
-- can have.

-- Example:

-- Age:

-- 0 to 120

-- Gender:

-- Male
-- Female
-- Other

-- =====================================
-- DEGREE OF A RELATION
-- =====================================

-- Degree = Number of Columns

-- Example:

-- Roll_No
-- Name
-- Age

-- Total Columns = 3

-- Degree = 3

-- =====================================
-- CARDINALITY OF A RELATION
-- =====================================

-- Cardinality = Number of Rows

-- Example:

-- 101 | Saloni | 20
-- 102 | Rahul  | 21

-- Total Rows = 2

-- Cardinality = 2

-- =====================================
-- ADVANTAGES OF RELATIONAL MODEL
-- =====================================

-- 1. Simple Structure
-- 2. Easy Data Retrieval
-- 3. Reduced Redundancy
-- 4. Data Independence
-- 5. Better Security

-- =====================================
-- DAY 11 SUMMARY
-- =====================================

-- Relation   --> Table

-- Tuple      --> Row

-- Attribute  --> Column

-- Domain     --> Possible Values

-- Degree     --> Number of Columns

-- Cardinality --> Number of Rows

-- Relational Model is the
-- foundation of modern DBMS.