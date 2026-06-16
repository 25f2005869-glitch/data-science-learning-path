-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Indexes
-- Day         : 22
-- Description : Improving Query Performance
-- ==================================================

DROP TABLE IF EXISTS students;

-- ==========================================
-- Create Students Table
-- ==========================================

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    city TEXT,
    marks INTEGER
);

INSERT INTO students VALUES (1,'Saloni','Patna',95);
INSERT INTO students VALUES (2,'Rahul','Delhi',80);
INSERT INTO students VALUES (3,'Aman','Patna',70);
INSERT INTO students VALUES (4,'Neha','Mumbai',85);
INSERT INTO students VALUES (5,'Riya','Patna',90);

-- ==========================================
-- Create Index on Name
-- ==========================================

CREATE INDEX idx_student_name
ON students(name);

-- ==========================================
-- Create Index on City
-- ==========================================

CREATE INDEX idx_student_city
ON students(city);

-- ==========================================
-- Queries Using Indexed Columns
-- ==========================================

SELECT *
FROM students
WHERE name = 'Saloni';

SELECT *
FROM students
WHERE city = 'Patna';