/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 62
Description : Ordered Indices (Primary, Secondary, Dense and Sparse Index)
*/

-- =====================================
-- DAY 62 : ORDERED INDICES
-- =====================================

-- What are Ordered Indices?

-- Ordered Indices are index structures
-- in which index entries are stored
-- in sorted order according to
-- the search key.

-- Ordered indices improve
-- search efficiency.

-- =====================================
-- TYPES OF ORDERED INDICES
-- =====================================

-- 1. Primary Index

-- 2. Secondary Index

-- 3. Dense Index

-- 4. Sparse Index

-- =====================================
-- 1. PRIMARY INDEX
-- =====================================

-- Primary Index is created on
-- the ordering key of a file.

-- Data records are physically
-- stored in sorted order.

-- =====================================

-- STUDENT

-- Student_ID | Name

-- 101        | Saloni

-- 102        | Rahul

-- 103        | Priya

-- 104        | Aman

-- =====================================

-- Primary Index

-- Student_ID | Pointer

-- 101        | Block1

-- 103        | Block2

-- =====================================

-- Characteristics

-- Data File Sorted

-- Usually Sparse

-- One Primary Index Per File

-- =====================================
-- 2. SECONDARY INDEX
-- =====================================

-- Secondary Index is created on
-- a non-ordering attribute.

-- Data file remains unchanged.

-- =====================================

-- STUDENT

-- Student_ID | Name

-- 101        | Saloni

-- 102        | Rahul

-- 103        | Priya

-- 104        | Rahul

-- =====================================

-- Secondary Index on Name

-- Name   | Pointer

-- Aman   | Row4

-- Priya  | Row3

-- Rahul  | Row2, Row4

-- Saloni | Row1

-- =====================================

-- Characteristics

-- Data File Need Not Be Sorted

-- Multiple Secondary Indices Allowed

-- Usually Dense

-- =====================================
-- 3. DENSE INDEX
-- =====================================

-- Dense Index contains one index
-- entry for every search-key value.

-- =====================================

-- STUDENT

-- Student_ID | Name

-- 101        | Saloni

-- 102        | Rahul

-- 103        | Priya

-- =====================================

-- Dense Index

-- 101 → Row1

-- 102 → Row2

-- 103 → Row3

-- =====================================

-- Characteristics

-- Faster Search

-- More Storage Required

-- Every Record Indexed

-- =====================================
-- 4. SPARSE INDEX
-- =====================================

-- Sparse Index contains index
-- entries for only some records.

-- Usually first record
-- of each block.

-- =====================================

-- Block 1

-- 101

-- 102

-- -------------------------------------

-- Block 2

-- 103

-- 104

-- =====================================

-- Sparse Index

-- 101 → Block1

-- 103 → Block2

-- =====================================

-- Characteristics

-- Less Storage

-- Slower Than Dense Index

-- Data Must Be Sorted

-- =====================================
-- DENSE VS SPARSE INDEX
-- =====================================

-- Dense Index

-- Entry For Every Record

-- More Storage

-- Faster Search

-- -------------------------------------

-- Sparse Index

-- Entry For Some Records

-- Less Storage

-- Slightly Slower Search

-- =====================================
-- PRIMARY VS SECONDARY INDEX
-- =====================================

-- Primary Index

-- Built On Ordering Key

-- Data Sorted

-- Usually Sparse

-- Only One Possible

-- -------------------------------------

-- Secondary Index

-- Built On Non-Ordering Key

-- Data Need Not Be Sorted

-- Usually Dense

-- Multiple Possible

-- =====================================
-- EXAMPLE SQL
-- =====================================

-- Create Index On Name

-- CREATE INDEX idx_name

-- ON STUDENT(Name);

-- =====================================

-- Create Index On Student_ID

-- CREATE INDEX idx_sid

-- ON STUDENT(Student_ID);

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which index is built on
-- the ordering key?

-- Answer:

-- Primary Index

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which index usually contains
-- an entry for every record?

-- Answer:

-- Dense Index

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which index requires
-- sorted data?

-- Answer:

-- Primary Index
-- Sparse Index

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. Difference between
-- Dense and Sparse Index?

-- Answer:

-- Dense:

-- Entry For Every Record

-- Sparse:

-- Entry For Some Records

-- -------------------------------------

-- Q2. Difference between
-- Primary and Secondary Index?

-- Answer:

-- Primary:

-- Ordering Key

-- Secondary:

-- Non-Ordering Key

-- -------------------------------------

-- Q3. Which index uses
-- less storage?

-- Answer:

-- Sparse Index

-- =====================================
-- DAY 62 SUMMARY
-- =====================================

-- Ordered Indices

-- Stored In Sorted Order

-- -------------------------------------

-- Primary Index

-- Ordering Key

-- Usually Sparse

-- -------------------------------------

-- Secondary Index

-- Non-Ordering Key

-- Usually Dense

-- -------------------------------------

-- Dense Index

-- Entry For Every Record

-- Faster Search

-- -------------------------------------

-- Sparse Index

-- Entry For Some Records

-- Less Storage

-- Ordered Indices are the
-- foundation of advanced index
-- structures such as B-Tree
-- and B+ Tree.