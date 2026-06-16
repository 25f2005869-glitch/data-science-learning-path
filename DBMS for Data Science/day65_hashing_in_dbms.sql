/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 65
Description : Hashing in DBMS
*/

-- =====================================
-- DAY 65 : HASHING IN DBMS
-- =====================================

-- What is Hashing?

-- Hashing is a technique used
-- to directly locate records
-- using a hash function.

-- Unlike B-Tree and B+ Tree,

-- Hashing does not search
-- through tree levels.

-- It directly computes
-- the storage location.

-- =====================================
-- WHY HASHING?
-- =====================================

-- Faster Data Retrieval

-- Direct Record Access

-- Efficient Equality Search

-- =====================================

-- Example Query

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 101;

-- =====================================

-- Hashing can directly find
-- the record location.

-- =====================================
-- BASIC COMPONENTS
-- =====================================

-- 1. Hash Function

-- 2. Hash Value

-- 3. Bucket

-- 4. Collision Handling

-- =====================================
-- HASH FUNCTION
-- =====================================

-- A mathematical function
-- used to convert a search key
-- into a bucket address.

-- =====================================

-- Example

-- h(k) = k MOD 10

-- =====================================

-- Key = 25

-- h(25)

-- = 25 MOD 10

-- = 5

-- =====================================

-- Record stored in

-- Bucket 5

-- =====================================
-- HASH TABLE
-- =====================================

-- Bucket 0

-- Bucket 1

-- Bucket 2

-- Bucket 3

-- Bucket 4

-- Bucket 5

-- Bucket 6

-- Bucket 7

-- Bucket 8

-- Bucket 9

-- =====================================

-- Key 25

-- Goes To Bucket 5

-- =====================================
-- BUCKET
-- =====================================

-- Bucket is a storage location
-- where records are placed.

-- =====================================

-- Example

-- Bucket 5

-- 25

-- 35

-- 45

-- =====================================

-- Multiple records may exist
-- inside one bucket.

-- =====================================
-- COLLISION
-- =====================================

-- Collision occurs when
-- multiple keys generate
-- the same hash value.

-- =====================================

-- Example

-- h(k) = k MOD 10

-- Key 25

-- 25 MOD 10 = 5

-- -------------------------------------

-- Key 35

-- 35 MOD 10 = 5

-- =====================================

-- Both map to Bucket 5

-- Collision Occurs

-- =====================================
-- COLLISION RESOLUTION
-- =====================================

-- Common Techniques

-- 1. Chaining

-- 2. Open Addressing

-- =====================================
-- CHAINING
-- =====================================

-- Store colliding records
-- in a linked list.

-- =====================================

-- Bucket 5

-- 25

-- ↓

-- 35

-- ↓

-- 45

-- =====================================

-- Easy Implementation

-- =====================================
-- OPEN ADDRESSING
-- =====================================

-- Find another free bucket.

-- =====================================

-- Example

-- Bucket 5 Occupied

-- Store Record In

-- Bucket 6

-- =====================================

-- Popular Method:

-- Linear Probing

-- =====================================
-- HASH SEARCH
-- =====================================

-- Example

-- Search Key = 25

-- h(25)

-- = 5

-- =====================================

-- Directly Access

-- Bucket 5

-- =====================================

-- Very Fast Search

-- =====================================
-- ADVANTAGES OF HASHING
-- =====================================

-- Fast Equality Search

-- Direct Record Access

-- Average Search:

-- O(1)

-- Simple Retrieval

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Collision Problem

-- Poor Range Queries

-- Rehashing Overhead

-- Extra Space Usage

-- =====================================
-- HASHING VS B+ TREE
-- =====================================

-- Hashing

-- Equality Search Excellent

-- Range Query Poor

-- -------------------------------------

-- B+ Tree

-- Equality Search Good

-- Range Query Excellent

-- =====================================
-- APPLICATIONS
-- =====================================

-- Database Indexing

-- Symbol Tables

-- Caches

-- Hash Maps

-- Storage Systems

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is a Hash Function?

-- Answer:

-- Function that converts
-- a key into a bucket address.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- What is Collision?

-- Answer:

-- Multiple keys map to
-- the same bucket.

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Average Search Complexity?

-- Answer:

-- O(1)

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Hashing?

-- Answer:

-- Technique for direct record
-- access using a hash function.

-- -------------------------------------

-- Q2. What is a Bucket?

-- Answer:

-- Storage location used
-- to store records.

-- -------------------------------------

-- Q3. Difference between
-- Hashing and B+ Tree?

-- Answer:

-- Hashing:

-- Better for equality search.

-- -------------------------------------

-- B+ Tree:

-- Better for range queries.

-- =====================================
-- DAY 65 SUMMARY
-- =====================================

-- Hashing

-- Direct Record Access

-- -------------------------------------

-- Hash Function

-- Computes Bucket Address

-- -------------------------------------

-- Bucket

-- Storage Location

-- -------------------------------------

-- Collision

-- Multiple Keys Same Bucket

-- -------------------------------------

-- Collision Resolution

-- Chaining

-- Open Addressing

-- -------------------------------------

-- Search Complexity

-- O(1) Average

-- -------------------------------------

-- Best For

-- Equality Searches

-- Hashing is one of the fastest
-- access methods used in DBMS.