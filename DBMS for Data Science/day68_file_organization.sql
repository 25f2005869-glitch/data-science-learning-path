/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 68
Description : File Organization in DBMS
*/

-- =====================================
-- DAY 68 : FILE ORGANIZATION
-- =====================================

-- What is File Organization?

-- File Organization refers to the
-- way records are physically stored
-- in secondary storage.

-- It determines how records are:

-- Stored

-- Retrieved

-- Updated

-- Deleted

-- =====================================
-- WHY FILE ORGANIZATION?
-- =====================================

-- Efficient Storage

-- Faster Searching

-- Better Retrieval

-- Reduced Access Time

-- =====================================
-- TYPES OF FILE ORGANIZATION
-- =====================================

-- 1. Heap File Organization

-- 2. Sequential File Organization

-- 3. Hash File Organization

-- =====================================
-- 1. HEAP FILE ORGANIZATION
-- =====================================

-- Also Called:

-- Unordered File Organization

-- =====================================

-- Records are stored in the order
-- they arrive.

-- No sorting is maintained.

-- =====================================

-- Example

-- Record 1

-- Record 2

-- Record 3

-- Record 4

-- =====================================

-- New Record

-- Added At End

-- =====================================

-- Advantages

-- Simple

-- Fast Insertions

-- =====================================

-- Disadvantages

-- Slow Searching

-- Full Table Scan Needed

-- =====================================

-- Search Complexity

-- O(n)

-- =====================================
-- 2. SEQUENTIAL FILE ORGANIZATION
-- =====================================

-- Records stored in sorted order
-- based on a search key.

-- =====================================

-- Example

-- Student_ID

-- 101

-- 102

-- 103

-- 104

-- =====================================

-- Data remains ordered.

-- =====================================

-- Advantages

-- Efficient Range Queries

-- Faster Sequential Access

-- =====================================

-- Disadvantages

-- Insertions Costly

-- Deletions Costly

-- Reorganization Required

-- =====================================

-- Search Complexity

-- O(log n)

-- Using Binary Search

-- =====================================
-- 3. HASH FILE ORGANIZATION
-- =====================================

-- Uses Hash Function

-- To determine storage location.

-- =====================================

-- Example

-- h(k) = k MOD 10

-- Key = 25

-- h(25)

-- = 5

-- =====================================

-- Store Record

-- In Bucket 5

-- =====================================

-- Advantages

-- Very Fast Equality Search

-- Direct Record Access

-- =====================================

-- Disadvantages

-- Collision Problems

-- Poor Range Queries

-- =====================================

-- Search Complexity

-- O(1) Average

-- =====================================
-- FILE ORGANIZATION COMPARISON
-- =====================================

-- Heap File

-- Storage:

-- Unordered

-- -------------------------------------

-- Search:

-- Slow

-- -------------------------------------

-- Insert:

-- Fast

-- =====================================

-- Sequential File

-- Storage:

-- Sorted

-- -------------------------------------

-- Search:

-- Fast

-- -------------------------------------

-- Insert:

-- Slow

-- =====================================

-- Hash File

-- Storage:

-- Hash Based

-- -------------------------------------

-- Search:

-- Very Fast

-- -------------------------------------

-- Insert:

-- Fast

-- =====================================
-- WHEN TO USE HEAP FILE?
-- =====================================

-- Frequent Insertions

-- Small Databases

-- Temporary Data

-- =====================================
-- WHEN TO USE SEQUENTIAL FILE?
-- =====================================

-- Range Queries

-- Ordered Reports

-- Batch Processing

-- =====================================
-- WHEN TO USE HASH FILE?
-- =====================================

-- Equality Search

-- Exact Match Queries

-- Fast Retrieval Required

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which file organization
-- stores records unordered?

-- Answer:

-- Heap File

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which file organization
-- supports fast range queries?

-- Answer:

-- Sequential File

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which file organization
-- uses a hash function?

-- Answer:

-- Hash File

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is File Organization?

-- Answer:

-- Method of storing records
-- physically on disk.

-- -------------------------------------

-- Q2. Which file organization
-- provides fastest equality search?

-- Answer:

-- Hash File Organization

-- -------------------------------------

-- Q3. Which file organization
-- is best for range queries?

-- Answer:

-- Sequential File Organization

-- -------------------------------------

-- Q4. Which file organization
-- provides fastest insertion?

-- Answer:

-- Heap File Organization

-- =====================================
-- DAY 68 SUMMARY
-- =====================================

-- File Organization

-- Physical Storage Of Records

-- -------------------------------------

-- Heap File

-- Unordered

-- Fast Insert

-- Slow Search

-- -------------------------------------

-- Sequential File

-- Sorted

-- Fast Search

-- Good For Range Queries

-- -------------------------------------

-- Hash File

-- Hash-Based Storage

-- O(1) Average Search

-- Best For Equality Search

-- -------------------------------------

-- File Organization plays a
-- major role in database
-- performance and storage
-- efficiency.