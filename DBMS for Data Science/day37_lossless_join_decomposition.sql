/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 37
Description : Lossless Join Decomposition
*/

-- =====================================
-- DAY 37 : LOSSLESS JOIN DECOMPOSITION
-- =====================================

-- What is Decomposition?

-- Decomposition is the process of
-- breaking a large relation into
-- smaller relations.

-- It is commonly performed during
-- Normalization.

-- =====================================
-- PROBLEM WITH DECOMPOSITION
-- =====================================

-- While decomposing relations,
-- information should not be lost.

-- After decomposition, we should be
-- able to reconstruct the original
-- relation using JOIN operations.

-- =====================================
-- LOSSLESS JOIN DECOMPOSITION
-- =====================================

-- A decomposition is called
-- Lossless Join Decomposition if
-- the original relation can be
-- reconstructed exactly by joining
-- the decomposed relations.

-- No information is lost.

-- =====================================
-- EXAMPLE 1
-- =====================================

-- Relation:

-- STUDENT

-- Roll_No | Name | Department
-- ----------------------------
-- 101     | Saloni | CSE
-- 102     | Rahul  | IT

-- Decompose into:

-- R1(Roll_No, Name)

-- R2(Roll_No, Department)

-- =====================================

-- Common Attribute:

-- Roll_No

-- Join:

-- R1 ⋈ R2

-- Result:

-- Original STUDENT relation obtained.

-- Therefore:

-- Lossless Join Decomposition

-- =====================================
-- CONDITION FOR LOSSLESS JOIN
-- =====================================

-- Let:

-- R → R1 and R2

-- Common Attributes:

-- R1 ∩ R2

-- Decomposition is Lossless if:

-- (R1 ∩ R2) → R1

-- OR

-- (R1 ∩ R2) → R2

-- =====================================
-- EXAMPLE 2
-- =====================================

-- Relation:

-- R(A, B, C)

-- Functional Dependency:

-- A → B

-- Decompose:

-- R1(A, B)

-- R2(A, C)

-- Common Attribute:

-- A

-- Since:

-- A → B

-- Common attribute determines R1

-- Therefore:

-- Lossless Join

-- =====================================
-- LOSSY DECOMPOSITION
-- =====================================

-- A decomposition is called Lossy
-- if extra tuples appear after JOIN.

-- Original relation cannot be
-- reconstructed correctly.

-- =====================================
-- EXAMPLE OF LOSSY JOIN
-- =====================================

-- R(A, B, C)

-- Decompose:

-- R1(A, B)

-- R2(B, C)

-- Without proper dependencies,
-- joining may create incorrect tuples.

-- Such decomposition is Lossy.

-- =====================================
-- LOSSLESS VS LOSSY
-- =====================================

-- Lossless Join

-- No Information Lost

-- Original Relation Recoverable

-- Preferred in Normalization

-- -------------------------------------

-- Lossy Join

-- Information Lost

-- Incorrect Tuples Generated

-- Not Preferred

-- =====================================
-- IMPORTANCE
-- =====================================

-- 1. Preserves Data

-- 2. Ensures Correct Reconstruction

-- 3. Improves Database Design

-- 4. Required for Normalization

-- =====================================
-- RELATION TO NORMALIZATION
-- =====================================

-- Good Normalization requires:

-- 1. Lossless Join

-- 2. Dependency Preservation

-- Both should be satisfied.

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- R(A, B, C)

-- FD:

-- A → B

-- Decompose:

-- R1(A, B)

-- R2(A, C)

-- Answer:

-- Lossless Join

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Why is Lossless Join important?

-- Answer:

-- To ensure no information is lost
-- after decomposition.

-- =====================================
-- INTERVIEW QUESTION
-- =====================================

-- Q. What is Lossless Join Decomposition?

-- Answer:

-- A decomposition in which the
-- original relation can be
-- reconstructed exactly using JOIN
-- operations without loss of data.

-- =====================================
-- DAY 37 SUMMARY
-- =====================================

-- Lossless Join Decomposition

-- No Information Loss

-- Original Relation Recoverable

-- Important for Normalization

-- Good Decomposition:

-- Lossless Join

-- +
-- Dependency Preservation