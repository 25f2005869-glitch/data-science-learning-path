/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 04
Description : Data Models in DBMS
*/

-- =====================================
-- DAY 04 : DATA MODELS IN DBMS
-- =====================================

-- What is a Data Model?

-- A Data Model is a collection of concepts
-- used to describe the structure of a database.

-- It defines:

-- 1. How data is stored
-- 2. How data is related
-- 3. How users interact with data

-- Why are Data Models Important?

-- 1. Organize Data Efficiently
-- 2. Reduce Complexity
-- 3. Improve Data Understanding
-- 4. Support Database Design

-- =====================================
-- TYPES OF DATA MODELS
-- =====================================

-- 1. Hierarchical Model
-- 2. Network Model
-- 3. Relational Model
-- 4. Entity Relationship Model

-- =====================================
-- 1. HIERARCHICAL MODEL
-- =====================================

-- Data is organized in a tree structure.

-- Parent Child Relationship

-- Example:

-- College
--   |
-- Department
--   |
-- Students

-- Advantages:

-- Simple Structure
-- Fast Access

-- Disadvantages:

-- Complex Relationships are difficult
-- Limited Flexibility

-- =====================================
-- 2. NETWORK MODEL
-- =====================================

-- Data is organized as a graph.

-- A child can have multiple parents.

-- Example:

-- Student <---> Course

-- Advantages:

-- Supports Many-to-Many Relationships
-- Flexible Structure

-- Disadvantages:

-- Complex Design
-- Difficult Maintenance

-- =====================================
-- 3. RELATIONAL MODEL
-- =====================================

-- Data is stored in tables.

-- Example:

-- STUDENT

-- ID | NAME | AGE
-- 1  | Ram  | 20
-- 2  | Shyam| 21

-- Advantages:

-- Easy to Understand
-- High Flexibility
-- Most Popular Model

-- Disadvantages:

-- Can become complex for very large systems

-- =====================================
-- 4. ENTITY RELATIONSHIP MODEL
-- =====================================

-- Used for database design.

-- Main Components:

-- Entity
-- Attribute
-- Relationship

-- Example:

-- Student ---- Enrolls ---- Course

-- Advantages:

-- Easy Visualization
-- Good for Database Planning

-- =====================================
-- DAY 04 SUMMARY
-- =====================================

-- Hierarchical Model
-- Tree Structure

-- Network Model
-- Graph Structure

-- Relational Model
-- Table Structure

-- ER Model
-- Database Design Model

-- Most Modern Databases
-- use the Relational Model.