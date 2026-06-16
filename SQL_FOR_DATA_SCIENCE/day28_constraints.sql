-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Constraints
-- Day         : 28
-- Description : PRIMARY KEY, FOREIGN KEY,
--               UNIQUE and NOT NULL
-- ==================================================

DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;

-- ==========================================
-- Students Table
-- ==========================================

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    city TEXT
);

-- ==========================================
-- Insert Records
-- ==========================================

INSERT INTO students
VALUES (1,'Saloni','saloni@gmail.com','Patna');

INSERT INTO students
VALUES (2,'Rahul','rahul@gmail.com','Delhi');

-- ==========================================
-- Courses Table
-- ==========================================

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT NOT NULL,

    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
);

-- ==========================================
-- Insert Enrollment Data
-- ==========================================

INSERT INTO enrollments
VALUES (101,1,'SQL');

INSERT INTO enrollments
VALUES (102,2,'Python');

-- ==========================================
-- View Data
-- ==========================================

SELECT * FROM students;

SELECT * FROM enrollments;