/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 58
Description : Timestamp-Based Concurrency Control
*/

-- =====================================
-- DAY 58 : TIMESTAMP ORDERING PROTOCOL
-- =====================================

-- What is Timestamp Ordering?

-- Timestamp Ordering (TO) is a
-- concurrency control method that
-- uses timestamps to determine the
-- execution order of transactions.

-- Goal:

-- Ensure Conflict Serializability

-- Avoid Deadlocks

-- =====================================
-- BASIC IDEA
-- =====================================

-- Every transaction receives a
-- unique timestamp when it starts.

-- Example:

-- T1 = 100

-- T2 = 200

-- Since:

-- 100 < 200

-- T1 is older than T2

-- =====================================
-- TIMESTAMP RULE
-- =====================================

-- Older Transaction

-- Must appear before

-- Newer Transaction

-- =====================================
-- DATA ITEM INFORMATION
-- =====================================

-- For each data item X:

-- Read_TS(X)

-- Write_TS(X)

-- =====================================

-- Read_TS(X)

-- Largest timestamp of any
-- transaction that successfully
-- read X.

-- =====================================

-- Write_TS(X)

-- Largest timestamp of any
-- transaction that successfully
-- wrote X.

-- =====================================
-- READ RULE
-- =====================================

-- Transaction T wants Read(X)

-- If:

-- TS(T) < Write_TS(X)

-- Then:

-- Read Rejected

-- Transaction Rolled Back

-- =====================================

-- Otherwise:

-- Read Allowed

-- Update:

-- Read_TS(X)

-- =====================================
-- WRITE RULE
-- =====================================

-- Transaction T wants Write(X)

-- If:

-- TS(T) < Read_TS(X)

-- Then:

-- Write Rejected

-- Rollback Transaction

-- =====================================

-- If:

-- TS(T) < Write_TS(X)

-- Then:

-- Write Rejected

-- Rollback Transaction

-- =====================================

-- Otherwise:

-- Write Allowed

-- Update:

-- Write_TS(X)

-- =====================================
-- EXAMPLE 1
-- =====================================

-- T1

-- Timestamp = 10

-- T2

-- Timestamp = 20

-- =====================================

-- T1 writes A

-- Write_TS(A) = 10

-- =====================================

-- T2 reads A

-- Allowed

-- Read_TS(A) = 20

-- =====================================

-- Serializable Order:

-- T1 → T2

-- =====================================
-- ADVANTAGES
-- =====================================

-- Deadlock Free

-- High Concurrency

-- Guarantees Serializability

-- =====================================
-- DISADVANTAGES
-- =====================================

-- Frequent Rollbacks

-- Possible Starvation

-- More Overhead

-- =====================================
-- THOMAS WRITE RULE
-- =====================================

-- Improvement over basic
-- Timestamp Ordering.

-- =====================================

-- Problem:

-- Some writes are unnecessarily
-- rejected.

-- =====================================

-- Basic TO:

-- If:

-- TS(T) < Write_TS(X)

-- Transaction Aborted

-- =====================================

-- Thomas Write Rule:

-- Ignore Obsolete Writes

-- Instead of aborting.

-- =====================================
-- RULE
-- =====================================

-- If:

-- TS(T) < Write_TS(X)

-- Then:

-- Ignore Write

-- Continue Transaction

-- =====================================

-- Example:

-- Write_TS(A) = 50

-- Transaction T

-- Timestamp = 40

-- Wants Write(A)

-- =====================================

-- Basic TO:

-- Abort T

-- =====================================

-- Thomas Write Rule:

-- Ignore Write

-- Continue T

-- =====================================
-- BENEFITS OF THOMAS RULE
-- =====================================

-- Fewer Rollbacks

-- Better Performance

-- Higher Throughput

-- =====================================
-- TIMESTAMP ORDERING VS 2PL
-- =====================================

-- Timestamp Ordering

-- Deadlock Free

-- More Rollbacks

-- -------------------------------------

-- Two-Phase Locking

-- Possible Deadlocks

-- Fewer Rollbacks

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- What information is maintained
-- for each data item?

-- Answer:

-- Read_TS

-- Write_TS

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which protocol is deadlock free?

-- Answer:

-- Timestamp Ordering

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- What does Thomas Write Rule do?

-- Answer:

-- Ignores obsolete writes.

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Timestamp Ordering?

-- Answer:

-- Concurrency control protocol
-- based on transaction timestamps.

-- -------------------------------------

-- Q2. Why is TO deadlock free?

-- Answer:

-- No locks are used.

-- -------------------------------------

-- Q3. What is Thomas Write Rule?

-- Answer:

-- Optimization that ignores
-- outdated write operations
-- instead of aborting transactions.

-- =====================================
-- DAY 58 SUMMARY
-- =====================================

-- Timestamp Ordering Protocol

-- Uses Timestamps

-- Guarantees Serializability

-- -------------------------------------

-- Read_TS(X)

-- Last Successful Read Timestamp

-- -------------------------------------

-- Write_TS(X)

-- Last Successful Write Timestamp

-- -------------------------------------

-- Advantages

-- Deadlock Free

-- High Concurrency

-- -------------------------------------

-- Thomas Write Rule

-- Ignore Obsolete Writes

-- Reduce Rollbacks

-- Improve 