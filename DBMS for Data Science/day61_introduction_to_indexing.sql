/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 61
Description : Introduction to Indexing
*/

-- =====================================
-- DAY 61 : INTRODUCTION TO INDEXING
-- =====================================

-- What is Indexing?

-- Indexing is a technique used
-- to speed up data retrieval
-- operations in a database.

-- It helps DBMS locate records
-- quickly without scanning
-- the entire table.

-- =====================================
-- WHY INDEXING?
-- =====================================

-- Without Index:

-- DBMS performs Full Table Scan.

-- Time Complexity:

-- O(n)

-- =====================================

-- With Index:

-- DBMS directly locates records.

-- Faster Search Performance.

-- =====================================
-- REAL LIFE EXAMPLE
-- =====================================

-- Book Index

-- Instead of reading entire book,

-- We check the index page and
-- directly go to required topic.

-- Database Index works similarly.

-- =====================================
-- EXAMPLE TABLE
-- =====================================

-- STUDENT

-- Student_ID | Name
-- -----------------
-- 101        | Saloni
-- 102        | Rahul
-- 103        | Priya
-- 104        | Aman

-- =====================================

-- Query:

-- SELECT *
-- FROM STUDENT
-- WHERE Student_ID = 103;

-- =====================================

-- Without Index:

-- Check Row 1

-- Check Row 2

-- Check Row 3

-- Record Found

-- =====================================

-- With Index:

-- Directly locate Student_ID 103

-- Faster Access

-- =====================================
-- INDEX STRUCTURE
-- =====================================

-- Index Entry

-- Search Key

-- Pointer

-- =====================================

-- Example:

-- Student_ID | Address
-- ---------------------
-- 101        | Row 1

-- 102        | Row 2

-- 103        | Row 3

-- =====================================

-- Search Key:

-- Student_ID

-- Pointer:

-- Location of Record

-- =====================================
-- BENEFITS OF INDEXING
-- =====================================

-- Faster Searching

-- Faster Retrieval

-- Improved Query Performance

-- Efficient Range Queries

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Extra Storage Required

-- Slower INSERT

-- Slower UPDATE

-- Slower DELETE

-- Because index must also
-- be maintained.

-- =====================================
-- TYPES OF INDICES
-- =====================================

-- Primary Index

-- Secondary Index

-- Clustered Index

-- Non-Clustered Index

-- Dense Index

-- Sparse Index

-- B-Tree Index

-- B+ Tree Index

-- Hash Index

-- =====================================
-- CREATE INDEX IN SQL
-- =====================================

-- Syntax

-- CREATE INDEX index_name

-- ON table_name(column_name);

-- =====================================

-- Example

-- CREATE INDEX idx_student

-- ON STUDENT(Student_ID);

-- =====================================

-- Now queries using Student_ID
-- become faster.

-- =====================================
-- DROP INDEX
-- =====================================

-- Syntax

-- DROP INDEX index_name;

-- =====================================
-- EXAMPLE

-- DROP INDEX idx_student;

-- =====================================
-- WHEN TO CREATE INDEX?
-- =====================================

-- Frequently Searched Columns

-- Primary Keys

-- Foreign Keys

-- Columns Used in WHERE Clause

-- Columns Used in JOIN

-- =====================================
-- WHEN NOT TO CREATE INDEX?
-- =====================================

-- Small Tables

-- Frequently Updated Columns

-- Low Selectivity Columns

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is the main purpose
-- of Indexing?

-- Answer:

-- Faster Data Retrieval

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Does indexing require
-- extra storage?

-- Answer:

-- Yes

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which SQL command creates
-- an index?

-- Answer:

-- CREATE INDEX

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Indexing?

-- Answer:

-- Technique used to improve
-- search performance in DBMS.

-- -------------------------------------

-- Q2. What is the drawback
-- of indexing?

-- Answer:

-- Extra storage and maintenance cost.

-- -------------------------------------

-- Q3. Why is indexing faster?

-- Answer:

-- It avoids full table scans.

-- =====================================
-- DAY 61 SUMMARY
-- =====================================

-- Indexing

-- Speeds Up Searches

-- -------------------------------------

-- Uses:

-- Search Key

-- Pointer

-- -------------------------------------

-- Benefits

-- Faster Queries

-- Better Performance

-- -------------------------------------

-- Drawbacks

-- Extra Storage

-- Slower Updates

-- -------------------------------------

-- SQL Commands

-- CREATE INDEX

-- DROP INDEX

-- Indexing is one of the most
-- important optimization techniques
-- in DBMS.