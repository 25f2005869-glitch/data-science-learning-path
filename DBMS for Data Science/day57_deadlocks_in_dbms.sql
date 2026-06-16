/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 57
Description : Deadlocks in DBMS
*/

-- =====================================
-- DAY 57 : DEADLOCKS IN DBMS
-- =====================================

-- What is a Deadlock?

-- A Deadlock occurs when two or more
-- transactions wait indefinitely
-- for each other to release locks.

-- As a result:

-- None of the transactions
-- can proceed.

-- =====================================
-- EXAMPLE
-- =====================================

-- Transaction T1

-- Holds Lock(A)

-- Requests Lock(B)

-- -------------------------------------

-- Transaction T2

-- Holds Lock(B)

-- Requests Lock(A)

-- =====================================

-- T1 waits for T2

-- T2 waits for T1

-- Neither can continue.

-- Deadlock Occurs.

-- =====================================
-- DEADLOCK CONDITIONS
-- =====================================

-- Four conditions must hold
-- simultaneously.

-- These are called:

-- Coffman Conditions

-- =====================================
-- 1. MUTUAL EXCLUSION
-- =====================================

-- Resource can be held by
-- only one transaction at a time.

-- Example:

-- Exclusive Lock

-- =====================================
-- 2. HOLD AND WAIT
-- =====================================

-- Transaction holds one resource

-- While waiting for another.

-- Example:

-- T1 holds Lock(A)

-- Requests Lock(B)

-- =====================================
-- 3. NO PREEMPTION
-- =====================================

-- Resources cannot be forcibly
-- taken away.

-- Transaction releases them
-- voluntarily.

-- =====================================
-- 4. CIRCULAR WAIT
-- =====================================

-- Circular chain of waiting exists.

-- Example:

-- T1 waits for T2

-- T2 waits for T3

-- T3 waits for T1

-- =====================================

-- All four conditions required.

-- Remove any one condition

-- Deadlock cannot occur.

-- =====================================
-- WAIT-FOR GRAPH (WFG)
-- =====================================

-- Used to detect deadlocks.

-- =====================================

-- Node

-- Transaction

-- -------------------------------------

-- Edge

-- Waiting Relationship

-- =====================================

-- Example

-- T1 → T2

-- T2 → T3

-- T3 → T1

-- =====================================

-- Cycle Exists

-- Deadlock Exists

-- =====================================

-- No Cycle

-- No Deadlock

-- =====================================
-- DEADLOCK PREVENTION
-- =====================================

-- Goal:

-- Prevent one of the
-- Coffman Conditions.

-- =====================================

-- Method 1

-- Resource Ordering

-- Request resources in
-- predefined order.

-- =====================================

-- Method 2

-- Request All Locks At Once

-- Eliminates Hold and Wait.

-- =====================================

-- Method 3

-- Allow Preemption

-- Remove resources when needed.

-- =====================================
-- DEADLOCK DETECTION
-- =====================================

-- Allow deadlock to occur.

-- Then detect it.

-- =====================================

-- Use:

-- Wait-For Graph

-- =====================================

-- If Cycle Found

-- Deadlock Detected

-- =====================================
-- DEADLOCK RECOVERY
-- =====================================

-- After detection:

-- Break the deadlock.

-- =====================================

-- Method 1

-- Abort One Transaction

-- =====================================

-- Method 2

-- Rollback Transaction

-- =====================================

-- Method 3

-- Abort Multiple Transactions

-- Until cycle disappears.

-- =====================================
-- DEADLOCK AVOIDANCE
-- =====================================

-- Avoid unsafe states.

-- Common Algorithm:

-- Banker's Algorithm

-- =====================================

-- System grants requests only
-- if resulting state remains safe.

-- =====================================
-- COMPARISON
-- =====================================

-- Prevention

-- Stop Deadlock Before It Happens

-- -------------------------------------

-- Avoidance

-- Avoid Unsafe States

-- -------------------------------------

-- Detection

-- Find Deadlock After Occurrence

-- -------------------------------------

-- Recovery

-- Break Existing Deadlock

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- T1 waits for T2

-- T2 waits for T1

-- What occurs?

-- Answer:

-- Deadlock

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- What structure is used
-- to detect deadlocks?

-- Answer:

-- Wait-For Graph

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- What indicates a deadlock
-- in Wait-For Graph?

-- Answer:

-- Cycle

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is a Deadlock?

-- Answer:

-- Situation where transactions
-- wait indefinitely for each other.

-- -------------------------------------

-- Q2. How many conditions are
-- required for deadlock?

-- Answer:

-- Four

-- Mutual Exclusion

-- Hold and Wait

-- No Preemption

-- Circular Wait

-- -------------------------------------

-- Q3. How is deadlock detected?

-- Answer:

-- Using Wait-For Graph.

-- Cycle ⇒ Deadlock

-- -------------------------------------

-- Q4. How is deadlock resolved?

-- Answer:

-- Abort or Rollback one or more
-- transactions.

-- =====================================
-- DAY 57 SUMMARY
-- =====================================

-- Deadlock

-- Infinite Waiting Situation

-- -------------------------------------

-- Conditions

-- Mutual Exclusion

-- Hold and Wait

-- No Preemption

-- Circular Wait

-- -------------------------------------

-- Detection

-- Wait-For Graph

-- Cycle ⇒ Deadlock

-- -------------------------------------

-- Recovery

-- Abort Transaction

-- Rollback Transaction

-- -------------------------------------

-- Deadlock management is a key
-- responsibility of DBMS in
-- concurrent transaction systems.