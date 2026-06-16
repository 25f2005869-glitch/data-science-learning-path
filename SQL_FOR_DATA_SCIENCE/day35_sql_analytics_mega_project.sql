-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : SQL Analytics Mega Project
-- Day         : 35
-- Description : Student Performance Analytics System
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
-- Sample Data
-- ==========================================

INSERT INTO students VALUES
(1,'Saloni','Patna',95),
(2,'Rahul','Delhi',80),
(3,'Aman','Patna',70),
(4,'Neha','Mumbai',85),
(5,'Riya','Patna',90);

INSERT INTO courses VALUES
(101,'SQL'),
(102,'Python'),
(103,'Data Science');

INSERT INTO enrollments VALUES
(1001,1,101),
(1002,1,102),
(1003,2,102),
(1004,3,101),
(1005,4,103),
(1006,5,103);

-- ==========================================
-- Query 1 : Student Course Report
-- ==========================================

SELECT
    s.student_name,
    s.city,
    c.course_name,
    s.marks
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
JOIN courses c
ON e.course_id = c.course_id;

-- ==========================================
-- Query 2 : City-wise Student Count
-- ==========================================

SELECT
    city,
    COUNT(*) AS total_students
FROM students
GROUP BY city;

-- ==========================================
-- Query 3 : Above Average Students
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

-- ==========================================
-- Query 4 : Student Ranking
-- ==========================================

SELECT
    student_name,
    marks,
    DENSE_RANK() OVER
    (
        ORDER BY marks DESC
    ) AS rank_position
FROM students;

-- ==========================================
-- Query 5 : High Scorers View
-- ==========================================

CREATE VIEW high_scorers AS

SELECT *
FROM students
WHERE marks >= 85;

SELECT *
FROM high_scorers;

-- ==========================================
-- Query 6 : Course Enrollment Count
-- ==========================================

SELECT
    c.course_name,
    COUNT(*) AS total_enrollments
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_name;

-- ==========================================
-- Query 7 : Top Performer
-- ==========================================

SELECT *
FROM students
WHERE marks =
(
    SELECT MAX(marks)
    FROM students
);