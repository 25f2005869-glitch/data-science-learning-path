/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 08
Description : ER Diagrams and ER Notations
*/

-- =====================================
-- DAY 08 : ER DIAGRAMS
-- =====================================

-- What is an ER Diagram?

-- ER Diagram stands for
-- Entity Relationship Diagram.

-- It is a graphical representation
-- of entities, attributes, and
-- relationships in a database.

-- ER Diagrams help us visualize
-- database structure before creating
-- actual tables.

-- =====================================
-- BASIC COMPONENTS OF ER DIAGRAM
-- =====================================

-- 1. Entity
-- 2. Attribute
-- 3. Relationship

-- =====================================
-- ENTITY SYMBOL
-- =====================================

-- Rectangle

-- Example:

-- +-----------+
-- |  STUDENT  |
-- +-----------+

-- Represents an Entity.

-- Examples:

-- Student
-- Teacher
-- Course

-- =====================================
-- ATTRIBUTE SYMBOL
-- =====================================

-- Oval (Ellipse)

-- Example:

-- (Name)
-- (Age)
-- (Roll_No)

-- Attributes describe entities.

-- =====================================
-- RELATIONSHIP SYMBOL
-- =====================================

-- Diamond Shape

-- Example:

-- Student ---- Enrolls ---- Course

-- "Enrolls" is the Relationship.

-- =====================================
-- STRONG ENTITY
-- =====================================

-- Single Rectangle

-- Example:

-- +-----------+
-- | STUDENT   |
-- +-----------+

-- Has its own Primary Key.

-- =====================================
-- WEAK ENTITY
-- =====================================

-- Double Rectangle

-- Example:

-- =================
-- || DEPENDENT ||
-- =================

-- Depends on another entity.

-- =====================================
-- MULTI-VALUED ATTRIBUTE
-- =====================================

-- Double Oval

-- Example:

-- ((Phone_Number))

-- Can contain multiple values.

-- =====================================
-- DERIVED ATTRIBUTE
-- =====================================

-- Dashed Oval

-- Example:

-- - - (Age) - -

-- Derived from another attribute.

-- Example:

-- Date_of_Birth --> Age

-- =====================================
-- KEY ATTRIBUTE
-- =====================================

-- Underlined Attribute

-- Example:

-- __Roll_No__

-- Used to uniquely identify entities.

-- =====================================
-- SIMPLE ER EXAMPLE
-- =====================================

-- STUDENT
-- Attributes:
-- Roll_No
-- Name
-- Age

-- COURSE
-- Attributes:
-- Course_ID
-- Course_Name

-- Relationship:

-- Student ---- Enrolls ---- Course

-- =====================================
-- ADVANTAGES OF ER DIAGRAMS
-- =====================================

-- 1. Easy Visualization
-- 2. Better Database Design
-- 3. Easy Communication
-- 4. Reduces Design Errors
-- 5. Helps Convert ER Model to Tables

-- =====================================
-- DAY 08 SUMMARY
-- =====================================

-- Rectangle  --> Entity

-- Oval       --> Attribute

-- Diamond    --> Relationship

-- Double Rectangle
-- --> Weak Entity

-- Double Oval
-- --> Multi-Valued Attribute

-- Dashed Oval
-- --> Derived Attribute

-- Underlined Attribute
-- --> Key Attribute