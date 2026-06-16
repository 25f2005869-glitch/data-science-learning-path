-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Advanced Joins Challenge
-- Day         : 31
-- Description : Multi-Table Join Analytics
-- ==================================================

DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
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

-- ==========================================
-- Courses Table
-- ==========================================

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
);

INSERT INTO courses VALUES (101,'SQL');
INSERT INTO courses VALUES (102,'Python');
INSERT INTO courses VALUES (103,'Data Science');

-- ==========================================
-- Enrollments Table
-- ==========================================

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER
);

INSERT INTO enrollments VALUES (1001,1,101);
INSERT INTO enrollments VALUES (1002,1,102);
INSERT INTO enrollments VALUES (1003,2,102);
INSERT INTO enrollments VALUES (1004,3,103);
INSERT INTO enrollments VALUES (1005,4,101);

-- ==========================================
-- Multi-Table INNER JOIN
-- ==========================================

SELECT
    s.student_name,
    s.city,
    c.course_name
FROM students s
INNER JOIN enrollments e
    ON s.student_id = e.student_id
INNER JOIN courses c
    ON e.course_id = c.course_id;

-- ==========================================
-- Course-wise Student Count
-- ==========================================

SELECT
    c.course_name,
    COUNT(*) AS Total_Students
FROM courses c
INNER JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY c.course_name;

-- ==========================================
-- Students Taking Multiple Courses
-- ==========================================

SELECT
    s.student_name,
    COUNT(*) AS Total_Courses
FROM students s
INNER JOIN enrollments e
    ON s.student_id = e.student_id
GROUP BY s.student_name
HAVING COUNT(*) > 1;