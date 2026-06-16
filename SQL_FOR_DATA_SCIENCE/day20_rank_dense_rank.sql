-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : ROW_NUMBER, RANK, DENSE_RANK
-- Day         : 20
-- Description : Ranking students based on marks
-- ==================================================

DROP TABLE IF EXISTS students;

-- ==========================================
-- Create Students Table
-- ==========================================

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    marks INTEGER
);

INSERT INTO students VALUES (1,'Saloni',95);
INSERT INTO students VALUES (2,'Rahul',80);
INSERT INTO students VALUES (3,'Aman',95);
INSERT INTO students VALUES (4,'Neha',85);
INSERT INTO students VALUES (5,'Riya',80);

-- ==========================================
-- ROW_NUMBER()
-- ==========================================

SELECT
    id,
    name,
    marks,
    ROW_NUMBER() OVER (
        ORDER BY marks DESC
    ) AS Row_Num
FROM students;

-- ==========================================
-- RANK()
-- ==========================================

SELECT
    id,
    name,
    marks,
    RANK() OVER (
        ORDER BY marks DESC
    ) AS Student_Rank
FROM students;

-- ==========================================
-- DENSE_RANK()
-- ==========================================

SELECT
    id,
    name,
    marks,
    DENSE_RANK() OVER (
        ORDER BY marks DESC
    ) AS Dense_Rank
FROM students;