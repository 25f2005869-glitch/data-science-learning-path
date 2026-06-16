/*
Author      : Saloni Tiwari
Topic       : DBMS
Day         : 34
Description : Armstrong's Axioms
*/

-- =====================================
-- DAY 34 : ARMSTRONG'S AXIOMS
-- =====================================

-- What are Armstrong's Axioms?

-- Armstrong's Axioms are a set of
-- inference rules used to derive
-- Functional Dependencies.

-- Proposed by:

-- William W. Armstrong

-- These rules help determine
-- whether a Functional Dependency
-- is logically implied by others.

-- =====================================
-- MAIN ARMSTRONG'S AXIOMS
-- =====================================

-- 1. Reflexivity Rule

-- 2. Augmentation Rule

-- 3. Transitivity Rule

-- =====================================
-- 1. REFLEXIVITY RULE
-- =====================================

-- If:

-- Y ⊆ X

-- Then:

-- X → Y

-- Meaning:

-- Any set of attributes determines
-- itself and its subsets.

-- Example:

-- {A, B} → A

-- {A, B} → B

-- {A, B} → {A, B}

-- Valid because:

-- A is a subset of {A, B}

-- B is a subset of {A, B}

-- =====================================
-- 2. AUGMENTATION RULE
-- =====================================

-- If:

-- X → Y

-- Then:

-- XZ → YZ

-- Meaning:

-- Adding the same attribute(s)
-- to both sides preserves
-- the dependency.

-- Example:

-- A → B

-- Add C to both sides

-- AC → BC

-- Valid by Augmentation Rule.

-- =====================================
-- 3. TRANSITIVITY RULE
-- =====================================

-- If:

-- X → Y

-- Y → Z

-- Then:

-- X → Z

-- Meaning:

-- Dependency can pass through
-- an intermediate attribute.

-- Example:

-- A → B

-- B → C

-- Therefore:

-- A → C

-- =====================================
-- SECONDARY RULES
-- =====================================

-- Derived from the three
-- basic Armstrong's Axioms.

-- 1. Union Rule

-- 2. Decomposition Rule

-- 3. Pseudotransitivity Rule

-- =====================================
-- UNION RULE
-- =====================================

-- If:

-- X → Y

-- X → Z

-- Then:

-- X → YZ

-- Example:

-- A → B

-- A → C

-- Therefore:

-- A → BC

-- =====================================
-- DECOMPOSITION RULE
-- =====================================

-- If:

-- X → YZ

-- Then:

-- X → Y

-- X → Z

-- Example:

-- A → BC

-- Therefore:

-- A → B

-- A → C

-- =====================================
-- PSEUDOTRANSITIVITY RULE
-- =====================================

-- If:

-- X → Y

-- WY → Z

-- Then:

-- WX → Z

-- Example:

-- A → B

-- CB → D

-- Therefore:

-- AC → D

-- =====================================
-- PRACTICE QUESTION 1
-- =====================================

-- Given:

-- A → B

-- B → C

-- Find:

-- A → ?

-- Answer:

-- A → C

-- By Transitivity

-- =====================================
-- PRACTICE QUESTION 2
-- =====================================

-- Given:

-- A → B

-- Apply Augmentation with C

-- Answer:

-- AC → BC

-- =====================================
-- PRACTICE QUESTION 3
-- =====================================

-- Given:

-- A → B

-- A → C

-- Find Combined FD

-- Answer:

-- A → BC

-- By Union Rule

-- =====================================
-- DAY 34 SUMMARY
-- =====================================

-- Armstrong's Axioms:

-- 1. Reflexivity

-- If Y ⊆ X

-- Then X → Y

-- -------------------------------------

-- 2. Augmentation

-- If X → Y

-- Then XZ → YZ

-- -------------------------------------

-- 3. Transitivity

-- If X → Y

-- Y → Z

-- Then X → Z

-- -------------------------------------

-- Derived Rules:

-- Union

-- Decomposition

-- Pseudotransitivity

-- Armstrong's Axioms are the
-- foundation of Functional
-- Dependency analysis and
-- Normalization.