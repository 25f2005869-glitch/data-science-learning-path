/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 53
Description : Transaction States
*/

-- =====================================
-- DAY 53 : TRANSACTION STATES
-- =====================================

-- What are Transaction States?

-- During execution, a transaction
-- passes through different states.

-- These states describe the
-- lifecycle of a transaction.

-- =====================================
-- TRANSACTION STATE DIAGRAM
-- =====================================

-- Active
--   |
--   v
-- Partially Committed
--   |
--   v
-- Committed
--   |
--   v
-- Terminated

-- If Error Occurs:

-- Active
--   |
--   v
-- Failed
--   |
--   v
-- Aborted
--   |
--   v
-- Terminated

-- =====================================
-- 1. ACTIVE STATE
-- =====================================

-- A transaction starts in
-- the Active State.

-- Operations are being executed.

-- Example:

-- Read(A)

-- Write(A)

-- Read(B)

-- Write(B)

-- Transaction is currently running.

-- =====================================
-- EXAMPLE
-- =====================================

-- BEGIN;

-- UPDATE Account
-- SET Balance = Balance - 1000
-- WHERE ID = 1;

-- Transaction is Active.

-- =====================================
-- 2. PARTIALLY COMMITTED STATE
-- =====================================

-- Transaction has completed
-- all operations successfully.

-- But changes are not yet
-- permanently stored.

-- Waiting for COMMIT.

-- =====================================

-- Example:

-- All SQL statements executed.

-- COMMIT operation about
-- to occur.

-- =====================================
-- 3. COMMITTED STATE
-- =====================================

-- Transaction completed successfully.

-- COMMIT executed.

-- Changes become permanent.

-- =====================================

-- Example:

-- COMMIT;

-- Data saved permanently.

-- =====================================
-- 4. FAILED STATE
-- =====================================

-- Transaction cannot continue.

-- Error occurred.

-- Causes:

-- Hardware Failure

-- Software Failure

-- Deadlock

-- Invalid Operation

-- System Crash

-- =====================================

-- Example:

-- Divide by zero error

-- Disk failure

-- Network failure

-- =====================================
-- 5. ABORTED STATE
-- =====================================

-- Transaction is rolled back.

-- Database restored to
-- previous consistent state.

-- All changes undone.

-- =====================================

-- Example:

-- ROLLBACK;

-- Transaction aborted.

-- =====================================
-- 6. TERMINATED STATE
-- =====================================

-- Final state of transaction.

-- Resources released.

-- Transaction removed
-- from system.

-- =====================================

-- Reached after:

-- COMMITTED

-- OR

-- ABORTED

-- =====================================
-- COMPLETE EXAMPLE
-- =====================================

-- BEGIN;

-- Read(A)

-- A = A - 1000

-- Write(A)

-- Read(B)

-- B = B + 1000

-- Write(B)

-- COMMIT;

-- State Flow:

-- Active

-- →

-- Partially Committed

-- →

-- Committed

-- →

-- Terminated

-- =====================================
-- FAILURE EXAMPLE
-- =====================================

-- BEGIN;

-- Read(A)

-- Write(A)

-- System Crash

-- State Flow:

-- Active

-- →

-- Failed

-- →

-- Aborted

-- →

-- Terminated

-- =====================================
-- SUMMARY TABLE
-- =====================================

-- Active

-- Transaction Running

-- -------------------------------------

-- Partially Committed

-- Operations Completed

-- Waiting for Commit

-- -------------------------------------

-- Committed

-- Changes Permanent

-- -------------------------------------

-- Failed

-- Error Occurred

-- -------------------------------------

-- Aborted

-- Rollback Performed

-- -------------------------------------

-- Terminated

-- Transaction Finished

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which state comes first?

-- Answer:

-- Active

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which state occurs after
-- successful COMMIT?

-- Answer:

-- Committed

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which state performs rollback?

-- Answer:

-- Aborted

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is the first state
-- of a transaction?

-- Answer:

-- Active

-- -------------------------------------

-- Q2. What happens in
-- Partially Committed state?

-- Answer:

-- Execution completed but
-- commit not finalized.

-- -------------------------------------

-- Q3. Difference between
-- Failed and Aborted?

-- Answer:

-- Failed:
-- Error detected.

-- Aborted:
-- Rollback completed.

-- =====================================
-- DAY 53 SUMMARY
-- =====================================

-- Transaction States

-- Active
-- --> Executing

-- Partially Committed
-- --> Waiting for Commit

-- Committed
-- --> Changes Permanent

-- Failed
-- --> Error Occurred

-- Aborted
-- --> Rollback Done

-- Terminated
-- --> Transaction Ends

-- Transaction States help
-- manage execution and recovery
-- in DBMS.