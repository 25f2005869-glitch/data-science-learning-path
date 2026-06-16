/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 03
Description : Database System Architecture
*/

-- =====================================
-- DAY 03 : DATABASE SYSTEM ARCHITECTURE
-- =====================================

-- What is Database Architecture?
-- Database Architecture defines how data is
-- stored, managed, and accessed in a DBMS.

-- Why do we need Database Architecture?

-- 1. Data Independence
-- 2. Better Security
-- 3. Easy Maintenance
-- 4. Efficient Data Management

-- Three-Level Architecture

-- 1. External Level
-- 2. Conceptual Level
-- 3. Internal Level

-- =====================================
-- 1. EXTERNAL LEVEL
-- =====================================

-- Also called View Level.

-- This level is closest to users.

-- Different users can see different views
-- of the same database.

-- Example:
-- Student sees marks only.
-- Teacher sees marks and attendance.
-- Admin sees complete records.

-- =====================================
-- 2. CONCEPTUAL LEVEL
-- =====================================

-- Also called Logical Level.

-- Describes the entire database structure.

-- Contains:
-- Tables
-- Attributes
-- Relationships
-- Constraints

-- Example:
-- Student(ID, Name, Marks)

-- =====================================
-- 3. INTERNAL LEVEL
-- =====================================

-- Also called Physical Level.

-- Describes how data is actually stored
-- inside the storage device.

-- Includes:
-- File Structures
-- Indexes
-- Storage Methods

-- Users generally do not interact
-- with this level directly.

-- =====================================
-- DATA INDEPENDENCE
-- =====================================

-- Ability to modify one level without
-- affecting another level.

-- Types:

-- 1. Physical Data Independence
-- Changes in Internal Level do not affect
-- Conceptual Level.

-- Example:
-- Changing storage structure.

-- 2. Logical Data Independence
-- Changes in Conceptual Level do not affect
-- External Level.

-- Example:
-- Adding a new column in a table.

-- =====================================
-- DAY 03 SUMMARY
-- =====================================

-- Database Architecture consists of:

-- External Level (View Level)
-- Conceptual Level (Logical Level)
-- Internal Level (Physical Level)

-- Benefits:
-- Data Independence
-- Security
-- Easy Maintenance
-- Efficient Data Access