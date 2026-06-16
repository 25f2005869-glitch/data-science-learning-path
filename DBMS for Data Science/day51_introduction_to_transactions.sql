/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 51
Description : Introduction to Transactions
*/

-- =====================================
-- DAY 51 : INTRODUCTION TO TRANSACTIONS
-- =====================================

-- What is a Transaction?

-- A Transaction is a sequence of
-- one or more database operations
-- performed as a single logical unit
-- of work.

-- A transaction must either:

-- Complete Fully

-- OR

-- Fail Completely

-- =====================================
-- REAL LIFE EXAMPLE
-- =====================================

-- Bank Transfer

-- Transfer Rs.1000

-- From:

-- Account A

-- To:

-- Account B

-- Steps:

-- 1. Deduct Rs.1000 from A

-- 2. Add Rs.1000 to B

-- Both operations must succeed.

-- If one fails:

-- Entire transaction fails.

-- =====================================
-- WHY TRANSACTIONS?
-- =====================================

-- Ensure Data Consistency

-- Ensure Data Integrity

-- Prevent Partial Updates

-- Handle System Failures

-- =====================================
-- SAMPLE TRANSACTION
-- =====================================

-- Account A Balance = 5000

-- Account B Balance = 2000

-- Transaction:

-- A = A - 1000

-- B = B + 1000

-- Final Result:

-- A = 4000

-- B = 3000

-- =====================================
-- PROBLEM WITHOUT TRANSACTION
-- =====================================

-- Suppose:

-- Rs.1000 deducted from A

-- System crashes

-- Rs.1000 not added to B

-- Result:

-- Data Inconsistency

-- Money Lost

-- =====================================
-- WITH TRANSACTION
-- =====================================

-- If crash occurs:

-- Entire operation rolled back.

-- Database returns to
-- previous consistent state.

-- =====================================
-- TRANSACTION OPERATIONS
-- =====================================

-- Read(X)

-- Read data item X

-- Example:

-- Read(Account_A)

-- -------------------------------------

-- Write(X)

-- Update data item X

-- Example:

-- Write(Account_A)

-- =====================================
-- BASIC TRANSACTION MODEL
-- =====================================

-- Begin Transaction

-- Read(A)

-- A = A - 1000

-- Write(A)

-- Read(B)

-- B = B + 1000

-- Write(B)

-- Commit

-- =====================================
-- TRANSACTION BOUNDARIES
-- =====================================

-- BEGIN

-- Marks start of transaction

-- -------------------------------------

-- COMMIT

-- Makes changes permanent

-- -------------------------------------

-- ROLLBACK

-- Undo all changes

-- =====================================
-- EXAMPLE
-- =====================================

-- BEGIN;

-- UPDATE Account
-- SET Balance = Balance - 1000
-- WHERE Account_ID = 1;

-- UPDATE Account
-- SET Balance = Balance + 1000
-- WHERE Account_ID = 2;

-- COMMIT;

-- =====================================
-- CHARACTERISTICS
-- =====================================

-- Atomic Unit

-- Consistent

-- Reliable

-- Recoverable

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is a Transaction?

-- Answer:

-- A logical unit of work
-- consisting of one or more
-- database operations.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- What happens if a transaction
-- fails before commit?

-- Answer:

-- Rollback occurs.

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. Why are Transactions important?

-- Answer:

-- They ensure consistency,
-- integrity and reliability
-- of database operations.

-- =====================================
-- DAY 51 SUMMARY
-- =====================================

-- Transaction

-- Logical Unit of Work

-- Operations:

-- Read

-- Write

-- Controls:

-- BEGIN

-- COMMIT

-- ROLLBACK

-- Purpose:

-- Maintain Consistency

-- Maintain Integrity

-- Handle Failures Safely