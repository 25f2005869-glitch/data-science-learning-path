-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Database Design & Normalization
-- Day         : 29
-- Description : 1NF, 2NF, 3NF and Table Design
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
    city TEXT
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
-- Insert Sample Data
-- ==========================================

INSERT INTO students
VALUES (1,'Saloni','Patna');

INSERT INTO students
VALUES (2,'Rahul','Delhi');

INSERT INTO courses
VALUES (101,'SQL');

INSERT INTO courses
VALUES (102,'Python');

INSERT INTO enrollments
VALUES (1001,1,101);

INSERT INTO enrollments
VALUES (1002,2,102);

-- ==========================================
-- View Data
-- ==========================================

SELECT *
FROM students;

SELECT *
FROM courses;

SELECT *
FROM enrollments;