-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Advanced Subqueries
-- Day         : 32
-- Description : EXISTS, NOT EXISTS and
--               Correlated Subqueries
-- ==================================================

DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;

-- ==========================================
-- Students Table
-- ==========================================

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT,
    city TEXT
);

INSERT INTO students VALUES (1,'Saloni','Patna');
INSERT INTO students VALUES (2,'Rahul','Delhi');
INSERT INTO students VALUES (3,'Aman','Patna');
INSERT INTO students VALUES (4,'Neha','Mumbai');
INSERT INTO students VALUES (5,'Riya','Patna');

-- ==========================================
-- Enrollments Table
-- ==========================================

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT
);

INSERT INTO enrollments VALUES (101,1,'SQL');
INSERT INTO enrollments VALUES (102,2,'Python');
INSERT INTO enrollments VALUES (103,3,'Data Science');

-- ==========================================
-- EXISTS
-- Students who are enrolled
-- ==========================================

SELECT *
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.student_id
);

-- ==========================================
-- NOT EXISTS
-- Students not enrolled
-- ==========================================

SELECT *
FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.student_id
);

-- ==========================================
-- Correlated Subquery
-- Count courses per student
-- ==========================================

SELECT
    s.student_name,
    (
        SELECT COUNT(*)
        FROM enrollments e
        WHERE e.student_id = s.student_id
    ) AS Total_Courses
FROM students s;