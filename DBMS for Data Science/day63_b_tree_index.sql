/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 63
Description : B-Tree Index Structure
*/

-- =====================================
-- DAY 63 : B-TREE INDEX
-- =====================================

-- What is a B-Tree?

-- B-Tree (Balanced Tree) is a
-- self-balancing search tree used
-- in DBMS for efficient searching,
-- insertion and deletion.

-- It keeps data sorted and allows
-- operations in logarithmic time.

-- =====================================
-- WHY B-TREE?
-- =====================================

-- Sequential Search

-- Time Complexity:

-- O(n)

-- -------------------------------------

-- B-Tree Search

-- Time Complexity:

-- O(log n)

-- =====================================

-- Therefore:

-- Much Faster For Large Databases

-- =====================================
-- BASIC STRUCTURE
-- =====================================

-- Example:

--          [30]

--        /      \

--   [10,20]   [40,50]

-- =====================================

-- Root Node:

-- [30]

-- -------------------------------------

-- Child Nodes:

-- [10,20]

-- [40,50]

-- =====================================
-- PROPERTIES OF B-TREE
-- =====================================

-- 1. Balanced Tree

-- All leaf nodes are at
-- the same level.

-- -------------------------------------

-- 2. Multiple Keys Per Node

-- One node may store
-- several keys.

-- -------------------------------------

-- 3. Sorted Keys

-- Keys stored in sorted order.

-- -------------------------------------

-- 4. Dynamic Structure

-- Grows and shrinks automatically.

-- =====================================
-- ORDER OF B-TREE
-- =====================================

-- Let Order = m

-- Maximum Children

-- = m

-- Maximum Keys

-- = m - 1

-- Minimum Children

-- = ceil(m/2)

-- =====================================

-- Example:

-- Order = 4

-- Maximum Children = 4

-- Maximum Keys = 3

-- =====================================
-- SEARCH OPERATION
-- =====================================

-- Search Key = 40

-- Tree:

--          [30]

--        /      \

--   [10,20]   [40,50]

-- =====================================

-- Step 1:

-- Compare with 30

-- 40 > 30

-- Move Right

-- -------------------------------------

-- Step 2:

-- Find 40

-- Search Successful

-- =====================================

-- Complexity:

-- O(log n)

-- =====================================
-- INSERTION
-- =====================================

-- Insert New Key

-- Place Key In Sorted Position

-- =====================================

-- Example:

-- Node:

-- [10,20]

-- Insert:

-- 15

-- Result:

-- [10,15,20]

-- =====================================
-- NODE OVERFLOW
-- =====================================

-- If Node Becomes Full:

-- Split Node

-- Promote Middle Key

-- =====================================

-- Example:

-- Order = 4

-- Node:

-- [10,20,30,40]

-- Overflow

-- =====================================

-- Split

-- Middle Key:

-- 20

-- Promoted Up

-- =====================================

-- Result

--        [20]

--       /    \

--    [10]  [30,40]

-- =====================================
-- DELETION
-- =====================================

-- Delete Key

-- Maintain B-Tree Properties

-- =====================================

-- If Underflow Occurs

-- Borrow From Sibling

-- OR

-- Merge Nodes

-- =====================================
-- ADVANTAGES
-- =====================================

-- Fast Searching

-- Fast Insertion

-- Fast Deletion

-- Balanced Structure

-- Suitable For Disk Storage

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Complex Implementation

-- Extra Rebalancing Required

-- More Memory Overhead

-- =====================================
-- APPLICATIONS
-- =====================================

-- Database Indexing

-- File Systems

-- Multi-Level Indexing

-- Storage Engines

-- =====================================
-- B-TREE VS BINARY SEARCH TREE
-- =====================================

-- BST

-- One Key Per Node

-- Can Become Unbalanced

-- -------------------------------------

-- B-Tree

-- Multiple Keys Per Node

-- Always Balanced

-- Better For Databases

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Why is B-Tree preferred
-- over Binary Search Tree?

-- Answer:

-- B-Tree remains balanced
-- and supports efficient
-- disk access.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Time Complexity of Search?

-- Answer:

-- O(log n)

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- What happens when a node
-- overflows?

-- Answer:

-- Node Split Occurs

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is a B-Tree?

-- Answer:

-- A balanced multi-way search tree
-- used for indexing in DBMS.

-- -------------------------------------

-- Q2. Why is B-Tree efficient?

-- Answer:

-- It keeps height small and
-- provides O(log n) operations.

-- -------------------------------------

-- Q3. What happens during overflow?

-- Answer:

-- Node is split and the
-- middle key is promoted.

-- =====================================
-- DAY 63 SUMMARY
-- =====================================

-- B-Tree

-- Balanced Multi-Way Tree

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

-- Advantages

-- Fast Access

-- Balanced Structure

-- Efficient Disk Usage

-- B-Tree is one of the most
-- important indexing structures
-- used in DBMS.