/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 06
Description : Entities and Entity Sets
*/

-- =====================================
-- DAY 06 : ENTITIES AND ENTITY SETS
-- =====================================

-- What is an Entity?

-- An Entity is any real-world object
-- that can be uniquely identified.

-- Examples:

-- Student
-- Teacher
-- Course
-- Department

-- Example:

-- Student:
-- Roll No : 101
-- Name    : Saloni
-- Age     : 20

-- Here Student is an Entity.

-- =====================================
-- ENTITY SET
-- =====================================

-- An Entity Set is a collection of
-- similar entities.

-- Example:

-- Student Entity Set

-- Student 1
-- Student 2
-- Student 3
-- Student 4

-- All students together form
-- an Entity Set.

-- =====================================
-- TYPES OF ENTITIES
-- =====================================

-- 1. Strong Entity
-- 2. Weak Entity

-- =====================================
-- STRONG ENTITY
-- =====================================

-- A Strong Entity can be uniquely
-- identified using its own attributes.

-- Example:

-- STUDENT

-- Roll_No
-- Name
-- Age

-- Roll_No uniquely identifies
-- each student.

-- Therefore Student is a
-- Strong Entity.

-- =====================================
-- WEAK ENTITY
-- =====================================

-- A Weak Entity cannot be uniquely
-- identified by its own attributes.

-- It depends on another entity.

-- Example:

-- DEPENDENT

-- Dependent_Name
-- Age

-- A dependent cannot be identified
-- without Employee information.

-- Employee + Dependent together
-- identify the dependent.

-- Therefore Dependent is a
-- Weak Entity.

-- =====================================
-- OWNER ENTITY
-- =====================================

-- The Strong Entity that supports
-- a Weak Entity is called
-- Owner Entity.

-- Example:

-- Employee --> Owner Entity

-- Dependent --> Weak Entity

-- =====================================
-- EXAMPLE
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Name
-- Salary

-- DEPENDENT

-- Dependent_Name
-- Age

-- Relationship:

-- Employee ---- Has ---- Dependent

-- Employee = Strong Entity
-- Dependent = Weak Entity

-- =====================================
-- ADVANTAGES OF ENTITY SETS
-- =====================================

-- 1. Better Organization
-- 2. Easy Database Design
-- 3. Reduced Complexity
-- 4. Improved Understanding

-- =====================================
-- DAY 06 SUMMARY
-- =====================================

-- Entity:
-- Real-world object.

-- Entity Set:
-- Collection of similar entities.

-- Strong Entity:
-- Has its own primary key.

-- Weak Entity:
-- Depends on another entity.

-- Owner Entity:
-- Supports Weak Entity.