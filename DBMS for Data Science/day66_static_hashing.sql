/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 66
Description : Static Hashing
*/

-- =====================================
-- DAY 66 : STATIC HASHING
-- =====================================

-- What is Static Hashing?

-- Static Hashing is a hashing
-- technique in which the number
-- of buckets remains fixed.

-- Buckets do not increase or
-- decrease dynamically.

-- =====================================
-- BASIC IDEA
-- =====================================

-- Fixed Number of Buckets

-- Example:

-- Bucket 0

-- Bucket 1

-- Bucket 2

-- Bucket 3

-- Bucket 4

-- =====================================

-- Hash Function

-- h(k) = k MOD 5

-- =====================================

-- Key = 12

-- h(12)

-- = 12 MOD 5

-- = 2

-- Store in Bucket 2

-- =====================================
-- EXAMPLE
-- =====================================

-- Number of Buckets = 5

-- Hash Function

-- h(k) = k MOD 5

-- =====================================

-- Key 7

-- Bucket 2

-- -------------------------------------

-- Key 12

-- Bucket 2

-- -------------------------------------

-- Key 17

-- Bucket 2

-- =====================================

-- Collision Occurs

-- =====================================
-- COLLISION HANDLING
-- =====================================

-- Two common methods:

-- 1. Overflow Chaining

-- 2. Open Addressing

-- =====================================
-- OVERFLOW CHAINING
-- =====================================

-- If bucket becomes full,

-- Create Overflow Bucket.

-- =====================================

-- Bucket 2

-- 7

-- 12

-- ↓

-- Overflow Bucket

-- 17

-- 22

-- =====================================

-- Linked List Structure

-- Used to store extra records.

-- =====================================
-- OPEN ADDRESSING
-- =====================================

-- If bucket is full,

-- Search another empty bucket.

-- =====================================

-- Example:

-- Bucket 2 Full

-- Store Record in Bucket 3

-- =====================================

-- Common Technique:

-- Linear Probing

-- =====================================
-- SEARCH OPERATION
-- =====================================

-- Search Key = 17

-- =====================================

-- h(17)

-- = 17 MOD 5

-- = 2

-- =====================================

-- Check Bucket 2

-- Follow Overflow Chain

-- Find 17

-- =====================================
-- INSERTION
-- =====================================

-- Step 1:

-- Compute Hash Value

-- Step 2:

-- Locate Bucket

-- Step 3:

-- Insert Record

-- Step 4:

-- Handle Collision if Needed

-- =====================================
-- DELETION
-- =====================================

-- Locate Bucket

-- Remove Record

-- Adjust Overflow Chain
-- if necessary.

-- =====================================
-- PROBLEMS OF STATIC HASHING
-- =====================================

-- Major Limitation:

-- Fixed Number of Buckets

-- =====================================

-- If Database Grows:

-- More Collisions

-- More Overflow Buckets

-- Slower Performance

-- =====================================

-- If Database Shrinks:

-- Many Buckets Remain Empty

-- Wasted Space

-- =====================================
-- PERFORMANCE ISSUES
-- =====================================

-- Large Number of Records

-- ↓

-- More Collisions

-- ↓

-- Longer Overflow Chains

-- ↓

-- Slower Searches

-- =====================================
-- ADVANTAGES
-- =====================================

-- Simple Design

-- Easy Implementation

-- Fast Equality Search

-- Low Initial Cost

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Fixed Bucket Count

-- Overflow Problems

-- Space Wastage

-- Poor Scalability

-- =====================================
-- STATIC HASHING VS
-- DYNAMIC HASHING
-- =====================================

-- Static Hashing

-- Fixed Buckets

-- -------------------------------------

-- Dynamic Hashing

-- Buckets Grow/Shrink

-- Automatically

-- =====================================
-- APPLICATIONS
-- =====================================

-- Small Databases

-- Fixed Size Data Sets

-- Temporary Storage Systems

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is Static Hashing?

-- Answer:

-- Hashing with a fixed number
-- of buckets.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- What happens when a bucket
-- becomes full?

-- Answer:

-- Overflow Handling Required.

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Major drawback?

-- Answer:

-- Fixed Bucket Count.

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Why is Static Hashing
-- called static?

-- Answer:

-- Number of buckets remains fixed.

-- -------------------------------------

-- Q2. What is Overflow Chaining?

-- Answer:

-- Using extra buckets linked
-- to the original bucket.

-- -------------------------------------

-- Q3. Why does performance degrade?

-- Answer:

-- Due to collisions and
-- overflow chains.

-- =====================================
-- DAY 66 SUMMARY
-- =====================================

-- Static Hashing

-- Fixed Number Of Buckets

-- -------------------------------------

-- Uses Hash Function

-- To Compute Bucket Address

-- -------------------------------------

-- Collision Handling

-- Overflow Chaining

-- Open Addressing

-- -------------------------------------

-- Advantages

-- Simple

-- Fast Equality Search

-- -------------------------------------

-- Disadvantages

-- Fixed Size

-- Overflow Problems

-- Poor Scalability

-- Static Hashing works well
-- for small databases but
-- struggles when data size
-- changes significantly.