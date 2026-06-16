/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 09
Description : Extended ER Model (EER Model)
*/

-- =====================================
-- DAY 09 : EXTENDED ER MODEL
-- =====================================

-- What is an Extended ER Model?

-- Extended ER Model (EER Model)
-- is an advanced version of the
-- Entity Relationship Model.

-- It provides additional concepts
-- for designing complex databases.

-- Main Concepts:

-- 1. Specialization
-- 2. Generalization
-- 3. Aggregation

-- =====================================
-- SPECIALIZATION
-- =====================================

-- Specialization is a Top-Down
-- approach.

-- A higher-level entity is divided
-- into lower-level entities.

-- Example:

-- PERSON

-- Student
-- Teacher

-- Here Person is divided into
-- Student and Teacher.

-- Person contains common attributes.

-- Student and Teacher contain
-- specialized attributes.

-- Advantages:

-- Better Classification
-- Easy Data Management

-- =====================================
-- GENERALIZATION
-- =====================================

-- Generalization is a Bottom-Up
-- approach.

-- Multiple lower-level entities
-- are combined into a higher-level
-- entity.

-- Example:

-- Student
-- Teacher

-- Combined into

-- PERSON

-- Common attributes are stored
-- in the Person entity.

-- Advantages:

-- Reduces Redundancy
-- Improves Organization

-- =====================================
-- SPECIALIZATION VS GENERALIZATION
-- =====================================

-- Specialization:

-- Top to Bottom

-- Person
--   |
-- Student
-- Teacher

-- Generalization:

-- Bottom to Top

-- Student
-- Teacher
--    |
-- Person

-- =====================================
-- AGGREGATION
-- =====================================

-- Aggregation is used when a
-- relationship itself needs to
-- participate in another relationship.

-- Example:

-- Employee ---- Works_On ---- Project

-- Manager ---- Monitors ---- (Works_On)

-- Here the relationship
-- "Works_On" becomes part of
-- another relationship.

-- This is called Aggregation.

-- Advantages:

-- Models Complex Relationships
-- Better Database Representation

-- =====================================
-- EER MODEL BENEFITS
-- =====================================

-- 1. Supports Complex Systems
-- 2. Better Data Representation
-- 3. Reduces Redundancy
-- 4. Improves Database Design

-- =====================================
-- DAY 09 SUMMARY
-- =====================================

-- Extended ER Model (EER)

-- Main Concepts:

-- Specialization
-- Generalization
-- Aggregation

-- Specialization:
-- Top-Down Approach

-- Generalization:
-- Bottom-Up Approach

-- Aggregation:
-- Relationship participates in
-- another Relationship