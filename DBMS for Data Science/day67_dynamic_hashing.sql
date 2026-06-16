/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 67
Description : Dynamic Hashing (Extendible Hashing and Linear Hashing)
*/

-- =====================================
-- DAY 67 : DYNAMIC HASHING
-- =====================================

-- What is Dynamic Hashing?

-- Dynamic Hashing is a hashing
-- technique in which the number
-- of buckets can grow or shrink
-- dynamically as data changes.

-- It overcomes the limitations
-- of Static Hashing.

-- =====================================
-- WHY DYNAMIC HASHING?
-- =====================================

-- Static Hashing Problems:

-- Fixed Number Of Buckets

-- More Collisions

-- Overflow Chains

-- Poor Scalability

-- =====================================

-- Dynamic Hashing Solution:

-- Buckets Expand Automatically

-- Better Performance

-- Fewer Collisions

-- =====================================
-- TYPES OF DYNAMIC HASHING
-- =====================================

-- 1. Extendible Hashing

-- 2. Linear Hashing

-- =====================================
-- 1. EXTENDIBLE HASHING
-- =====================================

-- Uses:

-- Directory

-- Buckets

-- Hash Function

-- =====================================

-- Directory stores pointers
-- to buckets.

-- Directory size can grow
-- dynamically.

-- =====================================
-- GLOBAL DEPTH
-- =====================================

-- Number of bits used
-- from hash value.

-- Example:

-- Global Depth = 2

-- Directory Entries:

-- 00

-- 01

-- 10

-- 11

-- =====================================
-- LOCAL DEPTH
-- =====================================

-- Number of bits identifying
-- a particular bucket.

-- Each bucket maintains its
-- own Local Depth.

-- =====================================
-- INSERTION
-- =====================================

-- Step 1:

-- Compute Hash Value

-- Step 2:

-- Use Global Depth bits

-- Step 3:

-- Locate Bucket

-- Step 4:

-- Insert Record

-- =====================================

-- If Bucket Full:

-- Split Bucket

-- Increase Local Depth

-- =====================================

-- If Local Depth becomes
-- greater than Global Depth

-- Double Directory Size

-- Increase Global Depth

-- =====================================
-- EXAMPLE
-- =====================================

-- Global Depth = 2

-- Directory

-- 00

-- 01

-- 10

-- 11

-- =====================================

-- Bucket Overflow Occurs

-- Split Bucket

-- Local Depth Increases

-- Directory May Double

-- =====================================
-- ADVANTAGES
-- =====================================

-- Fast Search

-- Dynamic Expansion

-- Fewer Collisions

-- No Long Overflow Chains

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Directory Maintenance

-- Extra Memory Usage

-- More Complex

-- =====================================
-- 2. LINEAR HASHING
-- =====================================

-- Dynamic Hashing without
-- a directory.

-- =====================================

-- Buckets split gradually
-- as database grows.

-- =====================================

-- Uses:

-- Hash Functions

-- Split Pointer

-- =====================================
-- BASIC IDEA
-- =====================================

-- Start with few buckets.

-- Example:

-- Bucket 0

-- Bucket 1

-- =====================================

-- As records increase:

-- Create New Bucket

-- Split Existing Bucket

-- =====================================

-- Growth is gradual.

-- No sudden doubling.

-- =====================================
-- SPLIT POINTER
-- =====================================

-- Indicates next bucket
-- to be split.

-- =====================================

-- Example

-- Split Pointer = 0

-- Split Bucket 0

-- Move Pointer To 1

-- =====================================

-- Continue Splitting
-- Sequentially.

-- =====================================
-- ADVANTAGES
-- =====================================

-- No Directory Needed

-- Gradual Expansion

-- Efficient Storage

-- Good Performance

-- =====================================
-- DISADVANTAGES
-- =====================================

-- More Complex Search Logic

-- Split Management Required

-- =====================================
-- EXTENDIBLE VS LINEAR HASHING
-- =====================================

-- Extendible Hashing

-- Uses Directory

-- -------------------------------------

-- Linear Hashing

-- No Directory

-- =====================================

-- Extendible Hashing

-- Directory Doubles

-- =====================================

-- Linear Hashing

-- Gradual Bucket Growth

-- =====================================

-- Extendible Hashing

-- Faster Lookup

-- =====================================

-- Linear Hashing

-- Better Space Utilization

-- =====================================
-- APPLICATIONS
-- =====================================

-- Database Indexing

-- Large Data Storage

-- Dynamic Databases

-- High Performance Systems

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Why is Dynamic Hashing used?

-- Answer:

-- To overcome fixed bucket
-- limitations of Static Hashing.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which Dynamic Hashing method
-- uses a directory?

-- Answer:

-- Extendible Hashing

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which method uses
-- a Split Pointer?

-- Answer:

-- Linear Hashing

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Difference between
-- Static and Dynamic Hashing?

-- Answer:

-- Static:

-- Fixed Buckets

-- -------------------------------------

-- Dynamic:

-- Buckets Grow Automatically

-- -------------------------------------

-- Q2. What is Global Depth?

-- Answer:

-- Number of bits used by
-- the directory.

-- -------------------------------------

-- Q3. What is Local Depth?

-- Answer:

-- Number of bits identifying
-- a bucket.

-- -------------------------------------

-- Q4. What is the advantage of
-- Linear Hashing?

-- Answer:

-- Gradual bucket expansion
-- without a directory.

-- =====================================
-- DAY 67 SUMMARY
-- =====================================

-- Dynamic Hashing

-- Buckets Grow Dynamically

-- -------------------------------------

-- Extendible Hashing

-- Uses Directory

-- Uses Global Depth

-- Uses Local Depth

-- -------------------------------------

-- Linear Hashing

-- No Directory

-- Uses Split Pointer

-- Gradual Expansion

-- -------------------------------------

-- Advantages

-- Better Scalability

-- Fewer Collisions

-- Better Performance

-- -------------------------------------

-- Dynamic Hashing solves the
-- major limitations of
-- Static Hashing.