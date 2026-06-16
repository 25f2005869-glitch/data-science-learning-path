-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Advanced Window Functions
-- Day         : 34
-- Description : LAG, LEAD, FIRST_VALUE,
--               LAST_VALUE and NTILE
-- ==================================================

DROP TABLE IF EXISTS students;

-- ==========================================
-- Create Students Table
-- ==========================================

CREATE TABLE students (
    student_id INTEGER,
    student_name TEXT,
    marks INTEGER
);

INSERT INTO students VALUES (1,'Saloni',95);
INSERT INTO students VALUES (2,'Rahul',80);
INSERT INTO students VALUES (3,'Aman',70);
INSERT INTO students VALUES (4,'Neha',85);
INSERT INTO students VALUES (5,'Riya',90);

-- ==========================================
-- LAG()
-- Previous Student Marks
-- ==========================================

SELECT
    student_name,
    marks,
    LAG(marks) OVER (
        ORDER BY marks
    ) AS Previous_Marks
FROM students;

-- ==========================================
-- LEAD()
-- Next Student Marks
-- ==========================================

SELECT
    student_name,
    marks,
    LEAD(marks) OVER (
        ORDER BY marks
    ) AS Next_Marks
FROM students;

-- ==========================================
-- FIRST_VALUE()
-- Top Marks
-- ==========================================

SELECT
    student_name,
    marks,
    FIRST_VALUE(marks) OVER (
        ORDER BY marks DESC
    ) AS Highest_Marks
FROM students;

-- ==========================================
-- LAST_VALUE()
-- Lowest Marks
-- ==========================================

SELECT
    student_name,
    marks,
    LAST_VALUE(marks) OVER (
        ORDER BY marks DESC
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND UNBOUNDED FOLLOWING
    ) AS Lowest_Marks
FROM students;

-- ==========================================
-- NTILE()
-- Divide into 3 Groups
-- ==========================================

SELECT
    student_name,
    marks,
    NTILE(3) OVER (
        ORDER BY marks DESC
    ) AS Performance_Group
FROM students;