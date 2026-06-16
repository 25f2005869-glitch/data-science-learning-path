-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Subqueries
-- Day         : 17
-- Description : Query inside another query
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
-- Subquery 1
-- Students with highest marks
-- ==========================================

SELECT *
FROM students
WHERE marks = (
    SELECT MAX(marks)
    FROM students
);

-- ==========================================
-- Subquery 2
-- Students above average marks
-- ==========================================

SELECT *
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);

-- ==========================================
-- Subquery 3
-- Students below average marks
-- ==========================================

SELECT *
FROM students
WHERE marks < (
    SELECT AVG(marks)
    FROM students
);