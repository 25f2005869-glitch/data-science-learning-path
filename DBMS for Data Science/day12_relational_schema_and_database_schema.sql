/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 12
Description : Relational Schema and Database Schema
*/

-- =====================================
-- DAY 12 : RELATIONAL SCHEMA
-- =====================================

-- What is a Schema?

-- A Schema is the overall structure
-- or blueprint of a database.

-- It defines:

-- Tables
-- Attributes
-- Relationships
-- Constraints

-- Schema tells us how data
-- will be organized.

-- =====================================
-- RELATIONAL SCHEMA
-- =====================================

-- Relational Schema describes
-- the structure of a Relation
-- (Table).

-- Example:

-- STUDENT
-- (Roll_No, Name, Age)

-- Here:

-- STUDENT = Relation Name

-- Roll_No
-- Name
-- Age

-- are Attributes.

-- Relational Schema:

-- STUDENT(Roll_No, Name, Age)

-- =====================================
-- ANOTHER EXAMPLE
-- =====================================

-- COURSE(Course_ID, Course_Name)

-- STUDENT(Roll_No, Name, Age)

-- ENROLLMENT(Roll_No, Course_ID)

-- These are Relational Schemas.

-- =====================================
-- DATABASE SCHEMA
-- =====================================

-- Database Schema is a collection
-- of all Relational Schemas.

-- Example:

-- STUDENT(Roll_No, Name, Age)

-- COURSE(Course_ID, Course_Name)

-- ENROLLMENT(Roll_No, Course_ID)

-- Together they form
-- a Database Schema.

-- =====================================
-- SCHEMA VS INSTANCE
-- =====================================

-- Schema:
-- Structure of Database

-- Instance:
-- Actual Data stored at a
-- particular moment.

-- =====================================
-- EXAMPLE
-- =====================================

-- Schema:

-- STUDENT(Roll_No, Name, Age)

-- Instance:

-- 101 | Saloni | 20
-- 102 | Rahul  | 21

-- Schema remains same.

-- Data may change.

-- =====================================
-- CHARACTERISTICS OF SCHEMA
-- =====================================

-- 1. Defines Database Structure
-- 2. Changes Rarely
-- 3. Created During Design Phase
-- 4. Independent of Actual Data

-- =====================================
-- CHARACTERISTICS OF INSTANCE
-- =====================================

-- 1. Actual Data
-- 2. Changes Frequently
-- 3. Depends on User Operations
-- 4. Dynamic in Nature

-- =====================================
-- DAY 12 SUMMARY
-- =====================================

-- Schema
-- --> Blueprint of Database

-- Relational Schema
-- --> Structure of a Table

-- Database Schema
-- --> Collection of All Tables

-- Instance
-- --> Actual Data

-- Schema = Design

-- Instance = Current Data