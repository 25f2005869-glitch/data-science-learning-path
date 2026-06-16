/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 10
Description : ER Model Revision and Practice Examples
*/

-- =====================================
-- DAY 10 : ER MODEL REVISION
-- =====================================

-- What is an ER Model?

-- ER Model stands for
-- Entity Relationship Model.

-- It is used to design databases
-- before creating actual tables.

-- ER Model helps represent:

-- Entities
-- Attributes
-- Relationships

-- =====================================
-- ENTITY REVISION
-- =====================================

-- Entity:
-- A real-world object about which
-- information is stored.

-- Examples:

-- Student
-- Teacher
-- Course
-- Department

-- Types:

-- Strong Entity
-- Weak Entity

-- Strong Entity:
-- Has its own Primary Key.

-- Weak Entity:
-- Depends on another entity.

-- =====================================
-- ATTRIBUTE REVISION
-- =====================================

-- Attribute:
-- Property of an Entity.

-- Examples:

-- Name
-- Age
-- Roll_No
-- Salary

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

-- =====================================
-- RELATIONSHIP REVISION
-- =====================================

-- Relationship connects entities.

-- Examples:

-- Student ---- Enrolls ---- Course

-- Teacher ---- Teaches ---- Course

-- Employee ---- Works_For ---- Company

-- =====================================
-- ER DIAGRAM SYMBOLS
-- =====================================

-- Rectangle
-- --> Entity

-- Oval
-- --> Attribute

-- Diamond
-- --> Relationship

-- Double Rectangle
-- --> Weak Entity

-- Double Oval
-- --> Multi-Valued Attribute

-- Dashed Oval
-- --> Derived Attribute

-- Underlined Attribute
-- --> Key Attribute

-- =====================================
-- EER MODEL REVISION
-- =====================================

-- Specialization

-- Person
--   |
-- Student
-- Teacher

-- Generalization

-- Student
-- Teacher
--   |
-- Person

-- Aggregation

-- Relationship participates
-- in another relationship.

-- =====================================
-- PRACTICE EXAMPLE 1
-- =====================================

-- STUDENT

-- Roll_No
-- Name
-- Age

-- COURSE

-- Course_ID
-- Course_Name

-- Relationship:

-- Student ---- Enrolls ---- Course

-- =====================================
-- PRACTICE EXAMPLE 2
-- =====================================

-- EMPLOYEE

-- Emp_ID
-- Name

-- PROJECT

-- Project_ID
-- Project_Name

-- Relationship:

-- Employee ---- Works_On ---- Project

-- =====================================
-- PRACTICE EXAMPLE 3
-- =====================================

-- CUSTOMER

-- Customer_ID
-- Name

-- ACCOUNT

-- Account_No
-- Balance

-- Relationship:

-- Customer ---- Owns ---- Account

-- =====================================
-- DAY 10 SUMMARY
-- =====================================

-- ER Model Components:

-- Entity
-- Attribute
-- Relationship

-- Advanced Concepts:

-- Specialization
-- Generalization
-- Aggregation

-- ER Model is the foundation
-- of database design.