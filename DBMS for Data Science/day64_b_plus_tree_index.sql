/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 64
Description : B+ Tree Index Structure
*/

-- =====================================
-- DAY 64 : B+ TREE INDEX
-- =====================================

-- What is a B+ Tree?

-- B+ Tree is an advanced version
-- of B-Tree used extensively in
-- modern DBMS systems.

-- Examples:

-- MySQL

-- PostgreSQL

-- Oracle

-- SQL Server

-- =====================================
-- WHY B+ TREE?
-- =====================================

-- B-Tree stores data in both:

-- Internal Nodes

-- Leaf Nodes

-- -------------------------------------

-- B+ Tree stores actual data
-- only in Leaf Nodes.

-- Internal Nodes contain
-- only search keys.

-- =====================================
-- BASIC STRUCTURE
-- =====================================

--              [30]

--           /        \

--      [10,20]     [40,50]

--        |             |

-- -------------------------------------

-- Leaf Nodes

-- [10,20] <-> [30,40] <-> [50,60]

-- =====================================

-- Important:

-- All Leaf Nodes are linked
-- together using pointers.

-- =====================================
-- PROPERTIES OF B+ TREE
-- =====================================

-- 1. Balanced Tree

-- All leaves are at same level.

-- -------------------------------------

-- 2. Data Stored Only In Leaves

-- Internal nodes contain keys only.

-- -------------------------------------

-- 3. Linked Leaf Nodes

-- Supports fast sequential access.

-- -------------------------------------

-- 4. Dynamic Structure

-- Automatically grows and shrinks.

-- =====================================
-- SEARCH OPERATION
-- =====================================

-- Search Key = 40

-- Step 1:

-- Start at Root

-- -------------------------------------

-- Step 2:

-- Follow Appropriate Child

-- -------------------------------------

-- Step 3:

-- Reach Leaf Node

-- -------------------------------------

-- Step 4:

-- Find Record

-- =====================================

-- Search Complexity

-- O(log n)

-- =====================================
-- INSERTION
-- =====================================

-- Insert New Key

-- Place Key In Correct Leaf Node

-- =====================================

-- Example:

-- Leaf Node

-- [10,20,30]

-- Insert:

-- 25

-- Result:

-- [10,20,25,30]

-- =====================================
-- OVERFLOW
-- =====================================

-- If Node Becomes Full

-- Split Node

-- =====================================

-- Example:

-- [10,20,30,40]

-- Overflow

-- =====================================

-- Split Into

-- [10,20]

-- [30,40]

-- =====================================

-- Parent Updated

-- Tree Remains Balanced

-- =====================================
-- DELETION
-- =====================================

-- Delete Key

-- =====================================

-- If Underflow Occurs

-- Borrow From Sibling

-- OR

-- Merge Nodes

-- =====================================

-- Balance Maintained

-- =====================================
-- LEAF NODE LINKING
-- =====================================

-- Example

-- [10,20]

--     ↔

-- [30,40]

--     ↔

-- [50,60]

-- =====================================

-- Benefit

-- Fast Range Queries

-- Fast Sequential Access

-- =====================================
-- RANGE QUERY EXAMPLE
-- =====================================

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID

-- BETWEEN 20 AND 60;

-- =====================================

-- B+ Tree directly traverses
-- linked leaf nodes.

-- Very Efficient.

-- =====================================
-- B-TREE VS B+ TREE
-- =====================================

-- B-Tree

-- Data In Internal Nodes

-- Data In Leaf Nodes

-- -------------------------------------

-- B+ Tree

-- Data Only In Leaf Nodes

-- Internal Nodes Store Keys Only

-- -------------------------------------

-- B-Tree

-- Sequential Access Slower

-- -------------------------------------

-- B+ Tree

-- Sequential Access Faster

-- =====================================
-- ADVANTAGES OF B+ TREE
-- =====================================

-- Faster Search

-- Efficient Range Queries

-- Better Disk Utilization

-- Smaller Tree Height

-- Sequential Traversal Easy

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Slightly More Complex

-- Extra Leaf-Level Pointers

-- =====================================
-- APPLICATIONS
-- =====================================

-- Database Indexes

-- File Systems

-- Storage Engines

-- Query Optimization

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Where is actual data stored
-- in B+ Tree?

-- Answer:

-- Leaf Nodes

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Why are linked leaves useful?

-- Answer:

-- Fast Sequential Access

-- Fast Range Queries

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Search Complexity?

-- Answer:

-- O(log n)

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Difference between
-- B-Tree and B+ Tree?

-- Answer:

-- B-Tree:

-- Data in Internal and Leaf Nodes

-- -------------------------------------

-- B+ Tree:

-- Data only in Leaf Nodes

-- -------------------------------------

-- Q2. Why is B+ Tree preferred
-- in DBMS?

-- Answer:

-- Better range queries and
-- efficient disk access.

-- -------------------------------------

-- Q3. What is the major advantage
-- of linked leaf nodes?

-- Answer:

-- Fast sequential traversal.

-- =====================================
-- DAY 64 SUMMARY
-- =====================================

-- B+ Tree

-- Advanced Form of B-Tree

-- -------------------------------------

-- Data Stored Only
-- In Leaf Nodes

-- -------------------------------------

-- Linked Leaf Nodes

-- Fast Range Queries

-- -------------------------------------

-- Search

-- O(log n)

-- -------------------------------------

-- Insert

-- Split On Overflow

-- -------------------------------------

-- Delete

-- Borrow Or Merge

-- -------------------------------------

-- Used By

-- MySQL

-- PostgreSQL

-- Oracle

-- SQL Server

-- B+ Tree is the most widely used
-- indexing structure in modern DBMS.