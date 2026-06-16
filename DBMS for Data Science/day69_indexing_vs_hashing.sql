/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 69
Description : Indexing vs Hashing
*/

-- =====================================
-- DAY 69 : INDEXING VS HASHING
-- =====================================

-- Both Indexing and Hashing are
-- techniques used to improve
-- database search performance.

-- However, they work differently
-- and are suitable for different
-- types of queries.

-- =====================================
-- INDEXING
-- =====================================

-- Indexing uses a special data
-- structure such as:

-- B-Tree

-- B+ Tree

-- =====================================

-- Records are organized
-- in sorted order.

-- =====================================

-- Example

-- Student_ID

-- 101

-- 102

-- 103

-- 104

-- =====================================

-- Search performed using
-- tree traversal.

-- =====================================

-- Search Complexity

-- O(log n)

-- =====================================
-- HASHING
-- =====================================

-- Hashing uses a Hash Function
-- to directly locate records.

-- =====================================

-- Example

-- h(k) = k MOD 10

-- Key = 25

-- Bucket = 5

-- =====================================

-- Search Complexity

-- O(1) Average

-- =====================================
-- RANGE QUERY EXAMPLE
-- =====================================

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID

-- BETWEEN 100 AND 200;

-- =====================================

-- Indexing

-- Very Efficient

-- =====================================

-- Hashing

-- Poor Performance

-- Must Check Multiple Buckets

-- =====================================
-- EQUALITY QUERY EXAMPLE
-- =====================================

-- SELECT *

-- FROM STUDENT

-- WHERE Student_ID = 105;

-- =====================================

-- Indexing

-- Good Performance

-- =====================================

-- Hashing

-- Excellent Performance

-- Direct Access

-- =====================================
-- INDEXING VS HASHING
-- =====================================

-- Indexing

-- Search Complexity

-- O(log n)

-- -------------------------------------

-- Hashing

-- Search Complexity

-- O(1) Average

-- =====================================

-- Indexing

-- Supports Range Queries

-- -------------------------------------

-- Hashing

-- Poor Range Query Support

-- =====================================

-- Indexing

-- Data Stored In Order

-- -------------------------------------

-- Hashing

-- Data Stored By Hash Function

-- =====================================

-- Indexing

-- Uses Trees

-- B-Tree

-- B+ Tree

-- -------------------------------------

-- Hashing

-- Uses Buckets

-- Hash Tables

-- =====================================

-- Indexing

-- Sequential Access Easy

-- -------------------------------------

-- Hashing

-- Sequential Access Difficult

-- =====================================
-- B+ TREE VS HASHING
-- =====================================

-- B+ Tree

-- O(log n)

-- =====================================

-- Supports

-- Equality Search

-- Range Search

-- Ordered Traversal

-- =====================================

-- Hashing

-- O(1)

-- =====================================

-- Supports

-- Equality Search

-- =====================================

-- Poor For

-- Range Queries

-- Ordered Traversal

-- =====================================
-- WHEN TO USE INDEXING?
-- =====================================

-- Range Queries

-- ORDER BY

-- GROUP BY

-- Sorted Reports

-- Sequential Access

-- =====================================
-- WHEN TO USE HASHING?
-- =====================================

-- Exact Match Queries

-- Primary Key Lookup

-- Fast Equality Search

-- =====================================
-- REAL DATABASES
-- =====================================

-- MySQL

-- Uses B+ Tree Indexes

-- =====================================

-- PostgreSQL

-- Uses B+ Tree Indexes

-- =====================================

-- Oracle

-- Uses B+ Tree Indexes

-- =====================================

-- Hash Indexes used in
-- special situations.

-- =====================================
-- ADVANTAGES OF INDEXING
-- =====================================

-- Supports Range Queries

-- Ordered Data Access

-- Good Flexibility

-- =====================================
-- ADVANTAGES OF HASHING
-- =====================================

-- Extremely Fast Equality Search

-- Direct Access

-- O(1) Average Search

-- =====================================
-- DISADVANTAGES OF INDEXING
-- =====================================

-- Slightly Slower Than Hashing

-- More Tree Maintenance

-- =====================================
-- DISADVANTAGES OF HASHING
-- =====================================

-- Collision Problems

-- Poor Range Queries

-- No Ordering

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which technique is best for
-- range queries?

-- Answer:

-- Indexing

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which technique provides
-- O(1) average search?

-- Answer:

-- Hashing

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which structure is commonly
-- used in DBMS indexes?

-- Answer:

-- B+ Tree

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Difference between
-- Indexing and Hashing?

-- Answer:

-- Indexing:

-- Tree-Based

-- Supports Range Queries

-- -------------------------------------

-- Hashing:

-- Bucket-Based

-- Supports Fast Equality Search

-- -------------------------------------

-- Q2. Why do databases prefer
-- B+ Trees?

-- Answer:

-- Efficient range queries and
-- sequential access.

-- -------------------------------------

-- Q3. Which is faster for
-- exact key lookup?

-- Answer:

-- Hashing

-- =====================================
-- DAY 69 SUMMARY
-- =====================================

-- Indexing

-- Uses B+ Tree

-- O(log n)

-- Supports Range Queries

-- -------------------------------------

-- Hashing

-- Uses Buckets

-- O(1) Average

-- Best For Equality Search

-- -------------------------------------

-- B+ Tree

-- Preferred In Most DBMS

-- -------------------------------------

-- Hashing

-- Preferred For Exact Match Queries

-- Understanding the strengths
-- and weaknesses of both helps
-- in selecting the right access
-- method for database systems.