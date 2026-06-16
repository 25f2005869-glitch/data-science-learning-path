/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 60
Description : Complete Revision of Transaction Management and Recovery
*/

-- =====================================
-- DAY 60 : COMPLETE REVISION
-- TRANSACTION MANAGEMENT
-- =====================================

-- This day revises all concepts
-- covered from Day 51 to Day 59.

-- =====================================
-- TOPICS COVERED
-- =====================================

-- 1. Transactions

-- 2. ACID Properties

-- 3. Transaction States

-- 4. Schedules

-- 5. Serializability

-- 6. Concurrency Control

-- 7. Lock-Based Protocols

-- 8. Deadlocks

-- 9. Timestamp Ordering

-- 10. Recovery Techniques

-- =====================================
-- TRANSACTIONS
-- =====================================

-- Transaction:

-- Logical Unit of Work

-- Example:

-- Bank Transfer

-- Deduct Money

-- Add Money

-- Both operations must succeed.

-- =====================================

-- Transaction Commands

-- BEGIN

-- COMMIT

-- ROLLBACK

-- =====================================
-- ACID PROPERTIES
-- =====================================

-- Atomicity

-- All or Nothing

-- -------------------------------------

-- Consistency

-- Valid State to Valid State

-- -------------------------------------

-- Isolation

-- Transactions Independent

-- -------------------------------------

-- Durability

-- Permanent Changes

-- =====================================
-- TRANSACTION STATES
-- =====================================

-- Active

-- ↓

-- Partially Committed

-- ↓

-- Committed

-- ↓

-- Terminated

-- =====================================

-- Failure Path

-- Active

-- ↓

-- Failed

-- ↓

-- Aborted

-- ↓

-- Terminated

-- =====================================
-- SCHEDULES
-- =====================================

-- Schedule:

-- Order of execution of
-- transaction operations.

-- =====================================

-- Types

-- Serial Schedule

-- Concurrent Schedule

-- =====================================
-- SERIALIZABILITY
-- =====================================

-- Ensures concurrent execution
-- behaves like serial execution.

-- =====================================

-- Types

-- Conflict Serializability

-- View Serializability

-- =====================================

-- Conflict Serializable

-- Precedence Graph has NO Cycle

-- =====================================
-- CONCURRENCY PROBLEMS
-- =====================================

-- Lost Update

-- One update overwrites another

-- -------------------------------------

-- Dirty Read

-- Reads uncommitted data

-- -------------------------------------

-- Unrepeatable Read

-- Same row different values

-- -------------------------------------

-- Phantom Read

-- Same query different rows

-- =====================================
-- LOCK-BASED PROTOCOLS
-- =====================================

-- Shared Lock (S)

-- Read Only

-- -------------------------------------

-- Exclusive Lock (X)

-- Read + Write

-- =====================================

-- Compatibility

-- S + S

-- Allowed

-- -------------------------------------

-- S + X

-- Not Allowed

-- -------------------------------------

-- X + X

-- Not Allowed

-- =====================================
-- TWO PHASE LOCKING (2PL)
-- =====================================

-- Growing Phase

-- Acquire Locks

-- -------------------------------------

-- Shrinking Phase

-- Release Locks

-- =====================================

-- Guarantees

-- Conflict Serializability

-- =====================================
-- STRICT 2PL
-- =====================================

-- Hold all Exclusive Locks

-- Until Commit or Abort

-- =====================================
-- DEADLOCKS
-- =====================================

-- Deadlock:

-- Transactions wait indefinitely
-- for each other.

-- =====================================

-- Coffman Conditions

-- Mutual Exclusion

-- Hold and Wait

-- No Preemption

-- Circular Wait

-- =====================================

-- Detection

-- Wait-For Graph

-- Cycle

-- ⇒ Deadlock

-- =====================================
-- TIMESTAMP ORDERING
-- =====================================

-- Uses timestamps to order
-- transactions.

-- =====================================

-- Read_TS(X)

-- Latest Read Timestamp

-- -------------------------------------

-- Write_TS(X)

-- Latest Write Timestamp

-- =====================================

-- Advantages

-- Deadlock Free

-- High Concurrency

-- =====================================
-- THOMAS WRITE RULE
-- =====================================

-- Ignore obsolete writes

-- Reduce rollbacks

-- Improve performance

-- =====================================
-- RECOVERY TECHNIQUES
-- =====================================

-- Recovery

-- Restores database after failure

-- =====================================

-- Techniques

-- Log-Based Recovery

-- Deferred Update

-- Immediate Update

-- Checkpoints

-- =====================================
-- WRITE AHEAD LOGGING
-- =====================================

-- WAL Rule

-- Write Log First

-- Then Database

-- =====================================
-- REDO
-- =====================================

-- Reapply committed changes

-- =====================================
-- UNDO
-- =====================================

-- Reverse uncommitted changes

-- =====================================
-- CHECKPOINT
-- =====================================

-- Recovery Marker

-- Speeds up recovery

-- =====================================
-- QUICK REVISION TABLE
-- =====================================

-- Transaction

-- Logical Unit of Work

-- -------------------------------------

-- ACID

-- Reliability Properties

-- -------------------------------------

-- Schedule

-- Execution Order

-- -------------------------------------

-- Serializability

-- Correct Concurrent Execution

-- -------------------------------------

-- Locks

-- Concurrency Control

-- -------------------------------------

-- Deadlock

-- Infinite Waiting

-- -------------------------------------

-- Timestamp Ordering

-- Deadlock-Free Protocol

-- -------------------------------------

-- Recovery

-- Restore Database

-- -------------------------------------

-- REDO

-- Reapply Changes

-- -------------------------------------

-- UNDO

-- Reverse Changes

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

-- Q2. Which lock is used for reading?

-- Answer:

-- Shared Lock

-- -------------------------------------

-- Q3. Which protocol guarantees
-- Conflict Serializability?

-- Answer:

-- Two Phase Locking

-- -------------------------------------

-- Q4. What indicates a deadlock?

-- Answer:

-- Cycle in Wait-For Graph

-- -------------------------------------

-- Q5. Which protocol is
-- deadlock free?

-- Answer:

-- Timestamp Ordering

-- -------------------------------------

-- Q6. Difference between
-- REDO and UNDO?

-- Answer:

-- REDO:

-- Reapply committed changes

-- UNDO:

-- Reverse uncommitted changes

-- =====================================
-- DAY 60 SUMMARY
-- =====================================

-- Transactions

-- ACID Properties

-- Transaction States

-- Schedules

-- Serializability

-- Concurrency Control

-- Locking Protocols

-- Deadlocks

-- Timestamp Ordering

-- Recovery Techniques

-- =====================================

-- UNIT COMPLETE

-- Day 51 → Transactions

-- Day 52 → ACID

-- Day 53 → Transaction States

-- Day 54 → Schedules & Serializability

-- Day 55 → Concurrency Problems

-- Day 56 → Lock-Based Protocols

-- Day 57 → Deadlocks

-- Day 58 → Timestamp Ordering

-- Day 59 → Recovery Techniques

-- Day 60 → Revision

-- =====================================

-- END OF TRANSACTION MANAGEMENT UNIT