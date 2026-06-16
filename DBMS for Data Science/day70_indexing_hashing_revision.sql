/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 70
Description : Complete Revision of Indexing, Hashing and File Organization
*/

-- =====================================
-- DAY 70 : COMPLETE REVISION
-- INDEXING, HASHING AND FILE ORGANIZATION
-- =====================================

-- This day revises all concepts
-- covered from Day 61 to Day 69.

-- =====================================
-- TOPICS COVERED
-- =====================================

-- 1. Introduction to Indexing

-- 2. Ordered Indices

-- 3. B-Tree

-- 4. B+ Tree

-- 5. Hashing

-- 6. Static Hashing

-- 7. Dynamic Hashing

-- 8. File Organization

-- 9. Indexing vs Hashing

-- =====================================
-- INDEXING
-- =====================================

-- Purpose:

-- Faster Data Retrieval

-- Avoid Full Table Scan

-- =====================================

-- Components

-- Search Key

-- Pointer

-- =====================================

-- SQL Command

-- CREATE INDEX idx_name

-- ON STUDENT(Student_ID);

-- =====================================
-- ORDERED INDICES
-- =====================================

-- Types

-- Primary Index

-- Secondary Index

-- Dense Index

-- Sparse Index

-- =====================================

-- Primary Index

-- Built On Ordering Key

-- Usually Sparse

-- =====================================

-- Secondary Index

-- Built On Non-Ordering Key

-- Usually Dense

-- =====================================

-- Dense Index

-- Entry For Every Record

-- Faster Search

-- More Storage

-- =====================================

-- Sparse Index

-- Entry For Some Records

-- Less Storage

-- =====================================
-- B-TREE
-- =====================================

-- Balanced Multi-Way Tree

-- =====================================

-- Properties

-- Sorted Keys

-- Multiple Keys Per Node

-- Balanced Height

-- =====================================

-- Operations

-- Search

-- Insert

-- Delete

-- =====================================

-- Search Complexity

-- O(log n)

-- =====================================
-- B+ TREE
-- =====================================

-- Advanced Form Of B-Tree

-- =====================================

-- Actual Data Stored Only
-- In Leaf Nodes

-- =====================================

-- Leaf Nodes Linked Together

-- =====================================

-- Advantages

-- Fast Range Queries

-- Sequential Access

-- Efficient Disk Access

-- =====================================

-- Used By

-- MySQL

-- PostgreSQL

-- Oracle

-- SQL Server

-- =====================================
-- HASHING
-- =====================================

-- Direct Record Access

-- Using Hash Function

-- =====================================

-- Example

-- h(k) = k MOD 10

-- =====================================

-- Components

-- Hash Function

-- Bucket

-- Collision Handling

-- =====================================

-- Average Search

-- O(1)

-- =====================================
-- COLLISION RESOLUTION
-- =====================================

-- Chaining

-- Open Addressing

-- =====================================
-- STATIC HASHING
-- =====================================

-- Fixed Number Of Buckets

-- =====================================

-- Advantages

-- Simple

-- Easy To Implement

-- =====================================

-- Disadvantages

-- Overflow Chains

-- Poor Scalability

-- =====================================
-- DYNAMIC HASHING
-- =====================================

-- Buckets Grow Dynamically

-- =====================================

-- Types

-- Extendible Hashing

-- Linear Hashing

-- =====================================

-- Extendible Hashing

-- Uses Directory

-- Global Depth

-- Local Depth

-- =====================================

-- Linear Hashing

-- No Directory

-- Split Pointer

-- Gradual Expansion

-- =====================================
-- FILE ORGANIZATION
-- =====================================

-- Heap File

-- Sequential File

-- Hash File

-- =====================================

-- Heap File

-- Unordered Storage

-- Fast Insert

-- Slow Search

-- =====================================

-- Sequential File

-- Sorted Storage

-- Good Range Queries

-- =====================================

-- Hash File

-- Hash-Based Storage

-- Fast Equality Search

-- =====================================
-- INDEXING VS HASHING
-- =====================================

-- Indexing

-- O(log n)

-- =====================================

-- Supports

-- Equality Search

-- Range Search

-- Ordered Traversal

-- =====================================

-- Hashing

-- O(1) Average

-- =====================================

-- Supports

-- Equality Search

-- =====================================

-- Poor For

-- Range Queries

-- Ordered Traversal

-- =====================================
-- QUICK COMPARISON TABLE
-- =====================================

-- B-Tree

-- Balanced Tree

-- -------------------------------------

-- B+ Tree

-- Data In Leaves Only

-- -------------------------------------

-- Static Hashing

-- Fixed Buckets

-- -------------------------------------

-- Dynamic Hashing

-- Growing Buckets

-- -------------------------------------

-- Heap File

-- Unordered

-- -------------------------------------

-- Sequential File

-- Sorted

-- -------------------------------------

-- Hash File

-- Hash-Based

-- =====================================
-- IMPORTANT INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Indexing?

-- Answer:

-- Technique used to improve
-- search performance.

-- -------------------------------------

-- Q2. Difference between
-- Dense and Sparse Index?

-- Answer:

-- Dense:

-- Entry For Every Record

-- Sparse:

-- Entry For Some Records

-- -------------------------------------

-- Q3. Why is B+ Tree preferred
-- over B-Tree?

-- Answer:

-- Better Range Queries and
-- Sequential Access.

-- -------------------------------------

-- Q4. What is Collision?

-- Answer:

-- Multiple keys mapping
-- to same bucket.

-- -------------------------------------

-- Q5. Difference between
-- Static and Dynamic Hashing?

-- Answer:

-- Static:

-- Fixed Buckets

-- Dynamic:

-- Buckets Expand Automatically

-- -------------------------------------

-- Q6. Which file organization
-- is best for equality search?

-- Answer:

-- Hash File Organization

-- -------------------------------------

-- Q7. Which technique supports
-- range queries?

-- Answer:

-- B+ Tree Indexing

-- =====================================
-- DAY 70 SUMMARY
-- =====================================

-- Indexing

-- Ordered Indices

-- B-Tree

-- B+ Tree

-- Hashing

-- Static Hashing

-- Dynamic Hashing

-- File Organization

-- Indexing vs Hashing

-- =====================================

-- UNIT COMPLETE

-- Day 61 → Introduction to Indexing

-- Day 62 → Ordered Indices

-- Day 63 → B-Tree

-- Day 64 → B+ Tree

-- Day 65 → Hashing

-- Day 66 → Static Hashing

-- Day 67 → Dynamic Hashing

-- Day 68 → File Organization

-- Day 69 → Indexing vs Hashing

-- Day 70 → Complete Revision

-- =====================================

-- END OF INDEXING & FILE
-- ORGANIZATION UNIT