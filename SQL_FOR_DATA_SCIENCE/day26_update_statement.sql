-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : UPDATE Statement
-- Day         : 26
-- Description : Modifying existing records
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
-- View Original Data
-- ==========================================

SELECT * FROM students;

-- ==========================================
-- Update One Student
-- ==========================================

UPDATE students
SET marks = 88
WHERE id = 2;

-- ==========================================
-- Update City
-- ==========================================

UPDATE students
SET city = 'Bengaluru'
WHERE name = 'Neha';

-- ==========================================
-- Increase Marks by 5
-- ==========================================

UPDATE students
SET marks = marks + 5
WHERE city = 'Patna';

-- ==========================================
-- Check Updated Data
-- ==========================================

SELECT * FROM students;-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : UPDATE Statement
-- Day         : 26
-- Description : Modifying existing records
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
-- View Original Data
-- ==========================================

SELECT * FROM students;

-- ==========================================
-- Update One Student
-- ==========================================

UPDATE students
SET marks = 88
WHERE id = 2;

-- ==========================================
-- Update City
-- ==========================================

UPDATE students
SET city = 'Bengaluru'
WHERE name = 'Neha';

-- ==========================================
-- Increase Marks by 5
-- ==========================================

UPDATE students
SET marks = marks + 5
WHERE city = 'Patna';

-- ==========================================
-- Check Updated Data
-- ==========================================

SELECT * FROM students;