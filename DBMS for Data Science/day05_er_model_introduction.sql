/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 05
Description : Introduction to Entity Relationship (ER) Model
*/

-- =====================================
-- DAY 05 : ER MODEL INTRODUCTION
-- =====================================

-- What is an ER Model?

-- ER stands for Entity Relationship Model.

-- It is a conceptual model used to
-- design and visualize a database.

-- The ER Model was proposed by
-- Peter Chen in 1976.

-- Why do we use ER Models?

-- 1. Easy Database Planning
-- 2. Better Visualization
-- 3. Easy Communication
-- 4. Reduces Design Errors

-- =====================================
-- BASIC COMPONENTS OF ER MODEL
-- =====================================

-- 1. Entity
-- 2. Attribute
-- 3. Relationship

-- =====================================
-- ENTITY
-- =====================================

-- An Entity is a real-world object
-- about which data is stored.

-- Examples:

-- Student
-- Teacher
-- Course
-- Department

-- Example:

-- Student
-- Roll No : 101
-- Name    : Saloni
-- Age     : 20

-- Here Student is an Entity.

-- =====================================
-- ATTRIBUTE
-- =====================================

-- Attributes describe the properties
-- of an Entity.

-- Examples of Student Attributes:

-- Roll Number
-- Name
-- Age
-- Email

-- Example:

-- STUDENT

-- Roll No
-- Name
-- Age
-- Email

-- These are Attributes.

-- =====================================
-- RELATIONSHIP
-- =====================================

-- Relationship shows how entities
-- are connected.

-- Example:

-- Student ---- Enrolls ---- Course

-- Here "Enrolls" is the Relationship.

-- Another Example:

-- Teacher ---- Teaches ---- Course

-- =====================================
-- SIMPLE ER EXAMPLE
-- =====================================

-- ENTITY 1 : Student
-- Attributes:
-- Roll_No
-- Name
-- Age

-- ENTITY 2 : Course
-- Attributes:
-- Course_ID
-- Course_Name

-- RELATIONSHIP:
-- Student Enrolls in Course

-- =====================================
-- ADVANTAGES OF ER MODEL
-- =====================================

-- 1. Easy to Understand
-- 2. Visual Representation
-- 3. Better Database Design
-- 4. Reduces Redundancy
-- 5. Easy Maintenance

-- =====================================
-- DAY 05 SUMMARY
-- =====================================

-- ER = Entity Relationship Model

-- Main Components:

-- Entity
-- Attribute
-- Relationship

-- Example:

-- Student ---- Enrolls ---- Course

-- ER Model is used before creating
-- actual database tables.