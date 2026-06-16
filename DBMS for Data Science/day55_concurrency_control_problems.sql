/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 55
Description : Concurrency Control and Concurrent Execution Problems
*/

-- =====================================
-- DAY 55 : CONCURRENCY CONTROL
-- =====================================

-- What is Concurrency Control?

-- Concurrency Control is the process
-- of managing simultaneous execution
-- of multiple transactions.

-- Goal:

-- Maintain Consistency

-- Maintain Isolation

-- Prevent Data Conflicts

-- =====================================
-- WHY CONCURRENCY CONTROL?
-- =====================================

-- Multiple users may access
-- the same data simultaneously.

-- Without control:

-- Incorrect Results

-- Data Inconsistency

-- Lost Updates

-- May Occur

-- =====================================
-- EXAMPLE
-- =====================================

-- Account Balance = 1000

-- Transaction T1:

-- Add 100

-- Transaction T2:

-- Add 200

-- Correct Result:

-- 1300

-- Without Concurrency Control:

-- Incorrect result may occur.

-- =====================================
-- COMMON CONCURRENCY PROBLEMS
-- =====================================

-- 1. Lost Update

-- 2. Dirty Read

-- 3. Unrepeatable Read

-- 4. Phantom Read

-- =====================================
-- 1. LOST UPDATE
-- =====================================

-- Two transactions update
-- same data item.

-- One update overwrites
-- another update.

-- =====================================

-- Example:

-- Initial Balance = 1000

-- T1 Reads 1000

-- T2 Reads 1000

-- T1 Updates:

-- 1000 + 100 = 1100

-- T2 Updates:

-- 1000 + 200 = 1200

-- Final Balance:

-- 1200

-- Correct Balance:

-- 1300

-- T1 Update Lost.

-- =====================================
-- RESULT
-- =====================================

-- Data Inconsistency

-- Incorrect Balance

-- =====================================
-- 2. DIRTY READ
-- =====================================

-- Transaction reads data
-- written by another transaction
-- that has not committed.

-- =====================================

-- Example:

-- T1:

-- Balance = 5000

-- Update to 7000

-- Not Committed

-- -------------------------------------

-- T2 Reads:

-- 7000

-- -------------------------------------

-- T1 Rolls Back

-- Balance returns to 5000

-- =====================================

-- Problem:

-- T2 used invalid data.

-- Dirty Read Occurred.

-- =====================================
-- 3. UNREPEATABLE READ
-- =====================================

-- Same transaction reads
-- same row twice.

-- Different values obtained.

-- =====================================

-- Example:

-- T1 Reads Salary:

-- 50000

-- -------------------------------------

-- T2 Updates Salary:

-- 60000

-- Commits

-- -------------------------------------

-- T1 Reads Again:

-- 60000

-- =====================================

-- Same row

-- Different result

-- Unrepeatable Read.

-- =====================================
-- 4. PHANTOM READ
-- =====================================

-- Same query executed twice.

-- Different set of rows returned.

-- =====================================

-- Example:

-- T1:

-- SELECT *
-- FROM Employee
-- WHERE Salary > 50000;

-- Result:

-- 5 Rows

-- -------------------------------------

-- T2 Inserts New Employee

-- Salary = 70000

-- Commits

-- -------------------------------------

-- T1 Executes Same Query Again

-- Result:

-- 6 Rows

-- =====================================

-- New Row Appeared.

-- Phantom Read Occurred.

-- =====================================
-- COMPARISON TABLE
-- =====================================

-- Lost Update

-- Update Overwritten

-- -------------------------------------

-- Dirty Read

-- Read Uncommitted Data

-- -------------------------------------

-- Unrepeatable Read

-- Same Row Different Values

-- -------------------------------------

-- Phantom Read

-- Same Query Different Rows

-- =====================================
-- SOLUTION
-- =====================================

-- Concurrency Control Techniques

-- Locking

-- Timestamp Ordering

-- Serialization

-- Isolation Levels

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Which problem occurs when
-- one update overwrites another?

-- Answer:

-- Lost Update

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Which problem reads
-- uncommitted data?

-- Answer:

-- Dirty Read

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Which problem causes
-- extra rows to appear?

-- Answer:

-- Phantom Read

-- =====================================
-- INTERVIEW QUESTIONS
-- =====================================

-- Q1. What is Concurrency Control?

-- Answer:

-- Technique for managing
-- simultaneous transactions
-- safely.

-- -------------------------------------

-- Q2. What is Dirty Read?

-- Answer:

-- Reading data written by an
-- uncommitted transaction.

-- -------------------------------------

-- Q3. Difference between
-- Unrepeatable Read and Phantom Read?

-- Answer:

-- Unrepeatable Read:

-- Same Row Changes.

-- Phantom Read:

-- New/Deleted Rows Appear.

-- =====================================
-- DAY 55 SUMMARY
-- =====================================

-- Concurrency Control

-- Prevents Conflicts

-- Maintains Isolation

-- -------------------------------------

-- Lost Update

-- Update Overwritten

-- -------------------------------------

-- Dirty Read

-- Reads Uncommitted Data

-- -------------------------------------

-- Unrepeatable Read

-- Same Row Different Values

-- -------------------------------------

-- Phantom Read

-- Same Query Different Rows

-- These are the major problems
-- caused by concurrent execution.