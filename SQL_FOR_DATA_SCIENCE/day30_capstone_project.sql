-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : SQL Capstone Project
-- Day         : 30
-- Description : Student Database Management System
-- ==================================================

DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;

-- ==========================================
-- Students Table
-- ==========================================

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    city TEXT,
    marks INTEGER
);

-- ==========================================
-- Courses Table
-- ==========================================

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL
);

-- ==========================================
-- Enrollments Table
-- ==========================================

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,

    FOREIGN KEY(student_id)
    REFERENCES students(student_id),

    FOREIGN KEY(course_id)
    REFERENCES courses(course_id)
);

-- ==========================================
-- Insert Students
-- ==========================================

INSERT INTO students VALUES (1,'Saloni','Patna',95);
INSERT INTO students VALUES (2,'Rahul','Delhi',80);
INSERT INTO students VALUES (3,'Aman','Patna',70);
INSERT INTO students VALUES (4,'Neha','Mumbai',85);
INSERT INTO students VALUES (5,'Riya','Patna',90);

-- ==========================================
-- Insert Courses
-- ==========================================

INSERT INTO courses VALUES (101,'SQL');
INSERT INTO courses VALUES (102,'Python');
INSERT INTO courses VALUES (103,'Data Science');

-- ==========================================
-- Insert Enrollments
-- ==========================================

INSERT INTO enrollments VALUES (1001,1,101);
INSERT INTO enrollments VALUES (1002,2,102);
INSERT INTO enrollments VALUES (1003,3,101);
INSERT INTO enrollments VALUES (1004,4,103);
INSERT INTO enrollments VALUES (1005,5,103);

-- ==========================================
-- INNER JOIN
-- ==========================================

SELECT
    s.student_name,
    c.course_name,
    s.marks
FROM students s
INNER JOIN enrollments e
ON s.student_id = e.student_id
INNER JOIN courses c
ON e.course_id = c.course_id;

-- ==========================================
-- GROUP BY
-- ==========================================

SELECT
    city,
    COUNT(*) AS Total_Students
FROM students
GROUP BY city;

-- ==========================================
-- HAVING
-- ==========================================

SELECT
    city,
    COUNT(*) AS Total_Students
FROM students
GROUP BY city
HAVING COUNT(*) > 1;

-- ==========================================
-- VIEW
-- ==========================================

CREATE VIEW high_scorers AS
SELECT *
FROM students
WHERE marks >= 85;

SELECT * FROM high_scorers;

-- ==========================================
-- WINDOW FUNCTION
-- ==========================================

SELECT
    student_name,
    marks,
    RANK() OVER (
        ORDER BY marks DESC
    ) AS Student_Rank
FROM students;

-- ==========================================
-- CTE
-- ==========================================

WITH avg_marks AS
(
    SELECT AVG(marks) AS avg_score
    FROM students
)

SELECT *
FROM students
WHERE marks >
(
    SELECT avg_score
    FROM avg_marks
);