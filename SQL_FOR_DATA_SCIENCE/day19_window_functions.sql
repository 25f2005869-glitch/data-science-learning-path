-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Window Functions
-- Day         : 19
-- Description : Running calculations without grouping
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
INSERT INTO students VALUES (3,'Aman',70);
INSERT INTO students VALUES (4,'Neha',85);
INSERT INTO students VALUES (5,'Riya',90);

-- ==========================================
-- Window Function : Average Marks
-- ==========================================

SELECT
    id,
    name,
    marks,
    AVG(marks) OVER () AS Average_Marks
FROM students;

-- ==========================================
-- Window Function : Total Marks
-- ==========================================

SELECT
    id,
    name,
    marks,
    SUM(marks) OVER () AS Total_Marks
FROM students;

-- ==========================================
-- Running Total
-- ==========================================

SELECT
    id,
    name,
    marks,
    SUM(marks) OVER (
        ORDER BY id
    ) AS Running_Total
FROM students;