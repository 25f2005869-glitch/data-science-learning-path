/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 59
Description : Recovery Techniques in DBMS
*/

-- =====================================
-- DAY 59 : RECOVERY TECHNIQUES
-- =====================================

-- What is Recovery?

-- Recovery is the process of
-- restoring the database to a
-- consistent state after failure.

-- Goal:

-- Preserve Data

-- Maintain Consistency

-- Ensure Durability

-- =====================================
-- WHY RECOVERY IS NEEDED?
-- =====================================

-- Failures may occur due to:

-- System Crash

-- Power Failure

-- Disk Failure

-- Software Error

-- Hardware Malfunction

-- =====================================
-- EXAMPLE
-- =====================================

-- Account A = 5000

-- Account B = 3000

-- Transaction:

-- Transfer 1000

-- A = 4000

-- System crashes before:

-- B = 4000

-- =====================================

-- Database becomes inconsistent.

-- Recovery is required.

-- =====================================
-- RECOVERY TECHNIQUES
-- =====================================

-- 1. Log-Based Recovery

-- 2. Deferred Update

-- 3. Immediate Update

-- 4. Checkpoints

-- =====================================
-- LOG-BASED RECOVERY
-- =====================================

-- DBMS maintains a Log File.

-- Log contains:

-- Transaction Start

-- Data Updates

-- Commit

-- Rollback

-- =====================================

-- Example Log

-- <START T1>

-- <T1, A, 5000, 4000>

-- <COMMIT T1>

-- =====================================

-- Meaning:

-- Old Value = 5000

-- New Value = 4000

-- =====================================
-- WRITE-AHEAD LOGGING (WAL)
-- =====================================

-- Important Rule:

-- Log must be written to disk

-- BEFORE

-- Actual database update.

-- =====================================

-- Ensures recovery information
-- is always available.

-- =====================================
-- DEFERRED UPDATE
-- =====================================

-- Principle:

-- Database is updated only
-- after COMMIT.

-- =====================================

-- Before Commit:

-- Changes stored in Log.

-- Database remains unchanged.

-- =====================================

-- After Commit:

-- Updates applied.

-- =====================================

-- Crash Before Commit:

-- No action needed.

-- =====================================

-- Crash After Commit:

-- REDO Transaction.

-- =====================================
-- IMMEDIATE UPDATE
-- =====================================

-- Principle:

-- Database may be updated
-- before Commit.

-- =====================================

-- Therefore:

-- Both REDO and UNDO
-- may be required.

-- =====================================

-- Crash Before Commit:

-- UNDO Transaction

-- =====================================

-- Crash After Commit:

-- REDO Transaction

-- =====================================
-- REDO OPERATION
-- =====================================

-- Reapply committed changes.

-- Used when committed updates
-- are not yet reflected
-- in database.

-- =====================================

-- Example:

-- T1 committed.

-- Crash occurs.

-- REDO T1.

-- =====================================
-- UNDO OPERATION
-- =====================================

-- Reverse uncommitted changes.

-- Used when transaction
-- did not commit.

-- =====================================

-- Example:

-- T1 updates A.

-- No Commit.

-- Crash occurs.

-- UNDO T1.

-- =====================================
-- CHECKPOINTS
-- =====================================

-- Checkpoint is a recovery marker.

-- Used to reduce recovery time.

-- =====================================

-- At Checkpoint:

-- All modified buffers written
-- to disk.

-- Log information saved.

-- =====================================

-- Example

-- ----CHECKPOINT----

-- =====================================

-- During Recovery:

-- DBMS starts from latest
-- checkpoint instead of
-- beginning of log.

-- =====================================
-- ADVANTAGES OF CHECKPOINT
-- =====================================

-- Faster Recovery

-- Less Log Scanning

-- Better Performance

-- =====================================
-- RECOVERY PROCESS
-- =====================================

-- Crash Occurs

-- ↓

-- Find Latest Checkpoint

-- ↓

-- Analyze Log

-- ↓

-- REDO Committed Transactions

-- ↓

-- UNDO Uncommitted Transactions

-- ↓

-- Database Restored

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What is the purpose of a Log?

-- Answer:

-- Store transaction history
-- for recovery.

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which operation re-applies
-- committed changes?

-- Answer:

-- REDO

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which operation reverses
-- uncommitted changes?

-- Answer:

-- UNDO

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Recovery?

-- Answer:

-- Process of restoring database
-- after failure.

-- -------------------------------------

-- Q2. What is Write-Ahead Logging?

-- Answer:

-- Log must be written before
-- database update.

-- -------------------------------------

-- Q3. Difference between
-- Deferred and Immediate Update?

-- Answer:

-- Deferred Update:

-- REDO only.

-- -------------------------------------

-- Immediate Update:

-- REDO and UNDO.

-- =====================================
-- DAY 59 SUMMARY
-- =====================================

-- Recovery

-- Restores Consistency

-- -------------------------------------

-- Log-Based Recovery

-- Uses Log File

-- -------------------------------------

-- Deferred Update

-- REDO Only

-- -------------------------------------

-- Immediate Update

-- REDO + UNDO

-- -------------------------------------

-- Checkpoint

-- Faster Recovery

-- -------------------------------------

-- WAL

-- Log Before Data Update

-- -------------------------------------

-- Recovery ensures durability
-- and reliability of DBMS.