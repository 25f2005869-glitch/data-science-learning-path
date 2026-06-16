-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : FULL JOIN
-- Day         : 14
-- Description : Combining all records from both tables
-- ==================================================

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

-- ==========================================
-- Create Students Table
-- ==========================================

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    course_id INTEGER
);

INSERT INTO students VALUES (1,'Saloni',1);
INSERT INTO students VALUES (2,'Rahul',2);
INSERT INTO students VALUES (3,'Aman',3);
INSERT INTO students VALUES (4,'Neha',10);

-- ==========================================
-- Create Courses Table
-- ==========================================

CREATE TABLE courses (
    course_id INTEGER,
    course_name TEXT
);

INSERT INTO courses VALUES (1,'Data Science');
INSERT INTO courses VALUES (2,'Python');
INSERT INTO courses VALUES (3,'SQL');
INSERT INTO courses VALUES (5,'Machine Learning');

-- ==========================================
-- FULL JOIN Simulation
-- ==========================================

SELECT
    s.id,
    s.name,
    c.course_name
FROM students s
LEFT JOIN courses c
ON s.course_id = c.course_id

UNION

SELECT
    s.id,
    s.name,
    c.course_name
FROM courses c
LEFT JOIN students s
ON c.course_id = s.course_id;