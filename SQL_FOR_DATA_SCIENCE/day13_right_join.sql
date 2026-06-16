-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : RIGHT JOIN
-- Day         : 13
-- Description : Understanding RIGHT JOIN using SQLite
-- ==================================================


-- ==========================================
-- Create Courses Table
-- ==========================================

DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id INTEGER,
    course_name TEXT
);

INSERT INTO courses VALUES (1, 'Data Science');
INSERT INTO courses VALUES (2, 'Python');
INSERT INTO courses VALUES (3, 'SQL');
INSERT INTO courses VALUES (4, 'Machine Learning');


-- ==========================================
-- Create Students Table
-- ==========================================

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    city TEXT,
    course_id INTEGER
);

INSERT INTO students VALUES (1, 'Saloni', 'Patna', 1);
INSERT INTO students VALUES (2, 'Rahul', 'Delhi', 2);
INSERT INTO students VALUES (3, 'Aman', 'Patna', 3);


-- ==========================================
-- RIGHT JOIN Equivalent
-- ==========================================

SELECT
    s.id,
    s.name,
    c.course_name
FROM courses c
LEFT JOIN students s
ON c.course_id = s.course_id;