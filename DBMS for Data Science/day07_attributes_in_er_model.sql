/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 07
Description : Attributes in ER Model
*/

-- =====================================
-- DAY 07 : ATTRIBUTES IN ER MODEL
-- =====================================

-- What is an Attribute?

-- An Attribute is a property or
-- characteristic of an Entity.

-- Example:

-- STUDENT

-- Roll_No
-- Name
-- Age
-- Email

-- These are Attributes of Student.

-- =====================================
-- TYPES OF ATTRIBUTES
-- =====================================

-- 1. Simple Attribute
-- 2. Composite Attribute
-- 3. Single-Valued Attribute
-- 4. Multi-Valued Attribute
-- 5. Derived Attribute

-- =====================================
-- 1. SIMPLE ATTRIBUTE
-- =====================================

-- Cannot be divided further.

-- Examples:

-- Age
-- Salary
-- Gender

-- Example:

-- Student Age = 20

-- Age is a Simple Attribute.

-- =====================================
-- 2. COMPOSITE ATTRIBUTE
-- =====================================

-- Can be divided into smaller parts.

-- Example:

-- Name

-- First_Name
-- Middle_Name
-- Last_Name

-- Address

-- House_No
-- City
-- State
-- PIN_Code

-- =====================================
-- 3. SINGLE-VALUED ATTRIBUTE
-- =====================================

-- Contains only one value
-- for each entity.

-- Examples:

-- Roll_No
-- Date_of_Birth

-- Student:
-- Roll_No = 101

-- Only one value exists.

-- =====================================
-- 4. MULTI-VALUED ATTRIBUTE
-- =====================================

-- Contains multiple values
-- for one entity.

-- Example:

-- Phone_Number

-- Student:

-- 9876543210
-- 8765432109

-- More than one value exists.

-- =====================================
-- 5. DERIVED ATTRIBUTE
-- =====================================

-- Derived from another attribute.

-- Example:

-- Date_of_Birth --> Age

-- If DOB is known,
-- Age can be calculated.

-- Therefore Age is a
-- Derived Attribute.

-- =====================================
-- ATTRIBUTE EXAMPLE
-- =====================================

-- STUDENT

-- Roll_No       -> Single-Valued
-- Name          -> Composite
-- Phone_Number  -> Multi-Valued
-- DOB           -> Simple
-- Age           -> Derived

-- =====================================
-- ADVANTAGES OF ATTRIBUTES
-- =====================================

-- 1. Describe Entities
-- 2. Store Information
-- 3. Improve Database Design
-- 4. Enable Data Retrieval

-- =====================================
-- DAY 07 SUMMARY
-- =====================================

-- Attribute:
-- Property of an Entity

-- Types:

-- Simple Attribute
-- Composite Attribute
-- Single-Valued Attribute
-- Multi-Valued Attribute
-- Derived Attribute

-- Example:

-- Student
-- Roll_No
-- Name
-- Phone_Number
-- DOB
-- Age