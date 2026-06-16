-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Common Table Expression (CTE)
-- Day         : 18
-- Description : Using WITH clause for temporary tables
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
-- CTE Example 1
-- Students with marks above 80
-- ==========================================

WITH high_scorers AS
(
    SELECT *
    FROM students
    WHERE marks > 80
)

SELECT *
FROM high_scorers;

-- ==========================================
-- CTE Example 2
-- Average Marks
-- ==========================================

WITH avg_marks AS
(
    SELECT AVG(marks) AS average_score
    FROM students
)

SELECT *
FROM avg_marks;

-- ==========================================
-- CTE Example 3
-- Students Above Average
-- ==========================================

WITH avg_marks AS
(
    SELECT AVG(marks) AS average_score
    FROM students
)

SELECT *
FROM students
WHERE marks >
(
    SELECT average_score
    FROM avg_marks
);