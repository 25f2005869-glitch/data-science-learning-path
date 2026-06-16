/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 54
Description : Schedules and Serializability
*/

-- =====================================
-- DAY 54 : SCHEDULES AND SERIALIZABILITY
-- =====================================

-- What is a Schedule?

-- A Schedule is the order in which
-- operations of multiple transactions
-- are executed.

-- It preserves the order of operations
-- within each transaction.

-- =====================================
-- WHY SCHEDULES?
-- =====================================

-- In real databases many transactions
-- run simultaneously.

-- DBMS must manage them efficiently
-- while maintaining consistency.

-- =====================================
-- EXAMPLE TRANSACTIONS
-- =====================================

-- Transaction T1

-- Read(A)

-- A = A + 100

-- Write(A)

-- -------------------------------------

-- Transaction T2

-- Read(A)

-- A = A * 2

-- Write(A)

-- =====================================
-- TYPES OF SCHEDULES
-- =====================================

-- 1. Serial Schedule

-- 2. Concurrent Schedule

-- =====================================
-- 1. SERIAL SCHEDULE
-- =====================================

-- Transactions execute one after
-- another.

-- No interleaving occurs.

-- Example:

-- T1: Read(A)

-- T1: Write(A)

-- T2: Read(A)

-- T2: Write(A)

-- =====================================

-- Advantages:

-- Simple

-- No Concurrency Problems

-- -------------------------------------

-- Disadvantages:

-- Poor Performance

-- Low Resource Utilization

-- =====================================
-- 2. CONCURRENT SCHEDULE
-- =====================================

-- Operations of transactions are
-- interleaved.

-- Example:

-- T1: Read(A)

-- T2: Read(A)

-- T1: Write(A)

-- T2: Write(A)

-- =====================================

-- Advantages:

-- Better CPU Utilization

-- Higher Throughput

-- Faster Response Time

-- =====================================
-- SERIALIZABILITY
-- =====================================

-- Serializability ensures that
-- concurrent execution produces
-- the same result as some serial
-- execution.

-- Goal:

-- Correctness + Concurrency

-- =====================================
-- TYPES OF SERIALIZABILITY
-- =====================================

-- 1. Conflict Serializability

-- 2. View Serializability

-- =====================================
-- CONFLICT SERIALIZABILITY
-- =====================================

-- Most important and commonly used.

-- A schedule is Conflict Serializable
-- if it can be transformed into a
-- Serial Schedule by swapping
-- non-conflicting operations.

-- =====================================
-- CONFLICTING OPERATIONS
-- =====================================

-- Two operations conflict if:

-- 1. They belong to different
--    transactions

-- AND

-- 2. They access the same data item

-- AND

-- 3. At least one is Write

-- =====================================
-- CONFLICT TYPES
-- =====================================

-- Read-Write (RW)

-- Write-Read (WR)

-- Write-Write (WW)

-- =====================================
-- NON-CONFLICT
-- =====================================

-- Read-Read (RR)

-- Example:

-- T1: Read(A)

-- T2: Read(A)

-- No conflict.

-- =====================================
-- EXAMPLE
-- =====================================

-- T1: Read(A)

-- T1: Write(A)

-- T2: Read(A)

-- T2: Write(A)

-- Equivalent Serial Order:

-- T1 → T2

-- Therefore:

-- Conflict Serializable

-- =====================================
-- PRECEDENCE GRAPH
-- =====================================

-- Used to test Conflict
-- Serializability.

-- Rules:

-- Each Transaction = Node

-- Conflict = Directed Edge

-- =====================================

-- If Graph has NO Cycle

-- Schedule is Conflict Serializable

-- -------------------------------------

-- If Graph has Cycle

-- Schedule is NOT
-- Conflict Serializable

-- =====================================
-- EXAMPLE GRAPH
-- =====================================

-- T1 → T2

-- No cycle.

-- Serializable.

-- =====================================

-- T1 → T2

-- T2 → T1

-- Cycle Exists.

-- Not Serializable.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which schedule executes one
-- transaction completely before
-- another starts?

-- Answer:

-- Serial Schedule

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which schedule allows
-- interleaving?

-- Answer:

-- Concurrent Schedule

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- What condition makes a schedule
-- Conflict Serializable?

-- Answer:

-- Precedence Graph must
-- be acyclic.

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is a Schedule?

-- Answer:

-- Execution order of operations
-- from multiple transactions.

-- -------------------------------------

-- Q2. What is Serializability?

-- Answer:

-- Property ensuring concurrent
-- execution behaves like a serial
-- execution.

-- -------------------------------------

-- Q3. How is Conflict
-- Serializability checked?

-- Answer:

-- Using a Precedence Graph.

-- =====================================
-- DAY 54 SUMMARY
-- =====================================

-- Schedule

-- Order of Transaction Execution

-- -------------------------------------

-- Serial Schedule

-- No Interleaving

-- -------------------------------------

-- Concurrent Schedule

-- Interleaving Allowed

-- -------------------------------------

-- Serializability

-- Ensures Correct Concurrent Execution

-- -------------------------------------

-- Conflict Serializability

-- Checked Using
-- Precedence Graph

-- Acyclic Graph

-- ⇒ Serializable

-- Cyclic Graph

-- ⇒ Not Serializable