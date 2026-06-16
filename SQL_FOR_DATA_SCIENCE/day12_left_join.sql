-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : LEFT JOIN
-- Day         : 12
-- Description : Display all records from the left table
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
INSERT INTO students VALUES (4, 'Neha', 'Mumbai', 2);

-- Student without matching course

INSERT INTO students VALUES (5, 'Riya', 'Patna', 10);


-- ==========================================
-- LEFT JOIN
-- ==========================================

SELECT
    s.id,
    s.name,
    s.city,
    c.course_name
FROM students s
LEFT JOIN courses c
ON s.course_id = c.course_id;