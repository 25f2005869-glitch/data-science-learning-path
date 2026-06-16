-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Data Cleaning SQL
-- Day         : 25
-- Description : Handling duplicates, NULLs and
--               inconsistent data
-- ==================================================

DROP TABLE IF EXISTS students;

-- ==========================================
-- Create Dirty Dataset
-- ==========================================

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    city TEXT,
    marks INTEGER
);

INSERT INTO students VALUES (1,'Saloni','Patna',95);
INSERT INTO students VALUES (2,'Rahul','Delhi',80);
INSERT INTO students VALUES (3,'Aman','PATNA',70);
INSERT INTO students VALUES (4,'Neha',NULL,85);
INSERT INTO students VALUES (5,'Riya','Patna',90);
INSERT INTO students VALUES (5,'Riya','Patna',90);

-- ==========================================
-- View Original Data
-- ==========================================

SELECT *
FROM students;

-- ==========================================
-- Find Duplicate Records
-- ==========================================

SELECT
    id,
    name,
    COUNT(*) AS Duplicate_Count
FROM students
GROUP BY id, name
HAVING COUNT(*) > 1;

-- ==========================================
-- Find NULL Values
-- ==========================================

SELECT *
FROM students
WHERE city IS NULL;

-- ==========================================
-- Standardize City Names
-- ==========================================

UPDATE students
SET city = 'Patna'
WHERE city = 'PATNA';

-- ==========================================
-- Replace NULL Values
-- ==========================================

UPDATE students
SET city = 'Unknown'
WHERE city IS NULL;

-- ==========================================
-- Check Cleaned Data
-- ==========================================

SELECT *
FROM students;