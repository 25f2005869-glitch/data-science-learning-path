/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 56
Description : Lock-Based Protocols
*/

-- =====================================
-- DAY 56 : LOCK-BASED PROTOCOLS
-- =====================================

-- What is a Lock?

-- A Lock is a mechanism used by
-- DBMS to control concurrent access
-- to data items.

-- Locks prevent conflicts between
-- transactions.

-- Goal:

-- Maintain Isolation

-- Maintain Consistency

-- Prevent Concurrent Access Problems

-- =====================================
-- WHY LOCKS?
-- =====================================

-- Multiple transactions may try
-- to access the same data item.

-- Example:

-- Account Balance = 1000

-- T1 updates balance.

-- T2 updates balance.

-- Without locks:

-- Lost Update may occur.

-- =====================================
-- LOCK TYPES
-- =====================================

-- 1. Shared Lock (S-Lock)

-- 2. Exclusive Lock (X-Lock)

-- =====================================
-- 1. SHARED LOCK
-- =====================================

-- Also called:

-- Read Lock

-- Symbol:

-- S

-- =====================================

-- Purpose:

-- Allows Reading

-- Does NOT allow Writing

-- =====================================

-- Example:

-- T1 reads Account A

-- T1 acquires:

-- S(A)

-- -------------------------------------

-- T2 also wants to read A

-- Allowed

-- S(A) + S(A)

-- Compatible

-- =====================================

-- Multiple Shared Locks
-- can exist simultaneously.

-- =====================================
-- 2. EXCLUSIVE LOCK
-- =====================================

-- Also called:

-- Write Lock

-- Symbol:

-- X

-- =====================================

-- Purpose:

-- Allows Reading

-- Allows Writing

-- Prevents others from
-- Reading or Writing.

-- =====================================

-- Example:

-- T1 updates Account A

-- T1 acquires:

-- X(A)

-- -------------------------------------

-- T2 wants to read A

-- Not Allowed

-- Must Wait

-- =====================================

-- Only one Exclusive Lock
-- allowed at a time.

-- =====================================
-- LOCK COMPATIBILITY TABLE
-- =====================================

-- Requested Lock

--      S     X

-- S   Yes   No

-- X   No    No

-- =====================================

-- S + S

-- Allowed

-- -------------------------------------

-- S + X

-- Not Allowed

-- -------------------------------------

-- X + X

-- Not Allowed

-- =====================================
-- TWO-PHASE LOCKING (2PL)
-- =====================================

-- Most Important Lock Protocol

-- Guarantees:

-- Conflict Serializability

-- =====================================

-- Rule:

-- Transaction executes in
-- two phases.

-- =====================================
-- PHASE 1
-- GROWING PHASE
-- =====================================

-- Transaction can:

-- Acquire Locks

-- -------------------------------------

-- Transaction cannot:

-- Release Locks

-- =====================================
-- PHASE 2
-- SHRINKING PHASE
-- =====================================

-- Transaction can:

-- Release Locks

-- -------------------------------------

-- Transaction cannot:

-- Acquire New Locks

-- =====================================
-- EXAMPLE
-- =====================================

-- T1

-- Acquire S(A)

-- Acquire X(B)

-- Acquire S(C)

-- --------------------

-- Release S(A)

-- Release X(B)

-- Release S(C)

-- =====================================

-- Valid 2PL

-- All acquisitions happen first.

-- All releases happen later.

-- =====================================
-- INVALID EXAMPLE
-- =====================================

-- Acquire S(A)

-- Release S(A)

-- Acquire X(B)

-- =====================================

-- Not Valid 2PL

-- Because lock acquired
-- after release.

-- =====================================
-- ADVANTAGES OF 2PL
-- =====================================

-- Ensures Serializability

-- Maintains Consistency

-- Prevents Lost Updates

-- Easy to Implement

-- =====================================
-- DISADVANTAGES OF 2PL
-- =====================================

-- May Cause Deadlocks

-- Reduced Concurrency

-- Waiting Time Increases

-- =====================================
-- STRICT 2PL
-- =====================================

-- Special Version of 2PL

-- Rule:

-- All Exclusive Locks held
-- until Commit or Abort.

-- Benefits:

-- Prevents Cascading Rollbacks

-- Improves Recovery

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which lock is used
-- for reading?

-- Answer:

-- Shared Lock

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which lock allows writing?

-- Answer:

-- Exclusive Lock

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which protocol guarantees
-- Conflict Serializability?

-- Answer:

-- Two-Phase Locking (2PL)

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is a Shared Lock?

-- Answer:

-- Allows reading but
-- prevents writing.

-- -------------------------------------

-- Q2. What is an Exclusive Lock?

-- Answer:

-- Allows reading and writing,
-- blocks all other access.

-- -------------------------------------

-- Q3. What is 2PL?

-- Answer:

-- A locking protocol with:

-- Growing Phase

-- Shrinking Phase

-- guaranteeing Conflict
-- Serializability.

-- =====================================
-- DAY 56 SUMMARY
-- =====================================

-- Lock

-- Controls Concurrent Access

-- -------------------------------------

-- Shared Lock (S)

-- Read Only

-- -------------------------------------

-- Exclusive Lock (X)

-- Read + Write

-- -------------------------------------

-- Two-Phase Locking (2PL)

-- Growing Phase

-- Shrinking Phase

-- -------------------------------------

-- Strict 2PL

-- Hold X-Locks until Commit

-- -------------------------------------

-- Locks are the primary tool
-- used by DBMS to prevent
-- concurrency problems.