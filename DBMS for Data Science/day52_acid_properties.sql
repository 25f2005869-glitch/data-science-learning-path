/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 52
Description : ACID Properties of Transactions
*/

-- =====================================
-- DAY 52 : ACID PROPERTIES
-- =====================================

-- What are ACID Properties?

-- ACID properties ensure that
-- database transactions are
-- processed reliably.

-- ACID stands for:

-- A -> Atomicity

-- C -> Consistency

-- I -> Isolation

-- D -> Durability

-- =====================================
-- 1. ATOMICITY
-- =====================================

-- Meaning:

-- All operations of a transaction
-- are executed completely or
-- none are executed.

-- Rule:

-- All or Nothing

-- =====================================
-- EXAMPLE
-- =====================================

-- Transfer Rs.1000

-- Account A -> Account B

-- Step 1:

-- Deduct Rs.1000 from A

-- Step 2:

-- Add Rs.1000 to B

-- If Step 2 fails:

-- Step 1 is undone.

-- Entire transaction rolls back.

-- =====================================
-- BENEFIT
-- =====================================

-- Prevents Partial Updates

-- Prevents Data Loss

-- =====================================
-- 2. CONSISTENCY
-- =====================================

-- Meaning:

-- A transaction must move
-- the database from one
-- valid state to another
-- valid state.

-- =====================================
-- EXAMPLE
-- =====================================

-- Total Money Before:

-- A = 5000

-- B = 2000

-- Total = 7000

-- After Transfer:

-- A = 4000

-- B = 3000

-- Total = 7000

-- Consistency Maintained.

-- =====================================
-- BENEFIT
-- =====================================

-- Database Rules Always Followed

-- Data Remains Correct

-- =====================================
-- 3. ISOLATION
-- =====================================

-- Meaning:

-- Multiple transactions
-- should not interfere
-- with each other.

-- Each transaction behaves
-- as if it is running alone.

-- =====================================
-- EXAMPLE
-- =====================================

-- Transaction T1

-- Reads Balance

-- Transaction T2

-- Updates Balance

-- Isolation ensures that
-- inconsistent intermediate
-- values are not visible.

-- =====================================
-- BENEFIT
-- =====================================

-- Prevents Concurrency Problems

-- Maintains Correct Results

-- =====================================
-- 4. DURABILITY
-- =====================================

-- Meaning:

-- Once a transaction commits,
-- its changes become permanent.

-- Even if:

-- Power Failure Occurs

-- System Crash Occurs

-- Data Remains Safe.

-- =====================================
-- EXAMPLE
-- =====================================

-- COMMIT;

-- Transaction Successful.

-- System crashes immediately.

-- Data is still preserved.

-- =====================================
-- BENEFIT
-- =====================================

-- Reliable Data Storage

-- Crash Recovery Support

-- =====================================
-- COMPLETE EXAMPLE
-- =====================================

-- BEGIN;

-- UPDATE Account
-- SET Balance = Balance - 1000
-- WHERE ID = 1;

-- UPDATE Account
-- SET Balance = Balance + 1000
-- WHERE ID = 2;

-- COMMIT;

-- Atomicity:
-- Both Updates or None

-- Consistency:
-- Total Money Preserved

-- Isolation:
-- Other Transactions
-- Cannot See Partial State

-- Durability:
-- Changes Permanent After Commit

-- =====================================
-- ACID SUMMARY TABLE
-- =====================================

-- Atomicity

-- All or Nothing

-- -------------------------------------

-- Consistency

-- Valid State to Valid State

-- -------------------------------------

-- Isolation

-- Transactions Work Independently

-- -------------------------------------

-- Durability

-- Changes Remain Permanent

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which ACID property ensures
-- all operations succeed or fail?

-- Answer:

-- Atomicity

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which ACID property keeps data
-- permanent after commit?

-- Answer:

-- Durability

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which ACID property prevents
-- interference among transactions?

-- Answer:

-- Isolation

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What does ACID stand for?

-- Answer:

-- Atomicity
-- Consistency
-- Isolation
-- Durability

-- -------------------------------------

-- Q2. Which ACID property is
-- "All or Nothing"?

-- Answer:

-- Atomicity

-- -------------------------------------

-- Q3. Which ACID property ensures
-- committed data survives crashes?

-- Answer:

-- Durability

-- =====================================
-- DAY 52 SUMMARY
-- =====================================

-- ACID Properties

-- Atomicity
-- --> All or Nothing

-- Consistency
-- --> Valid State Maintained

-- Isolation
-- --> Transactions Independent

-- Durability
-- --> Permanent Changes

-- ACID properties ensure
-- reliable and safe database
-- transaction processing.