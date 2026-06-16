-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : DELETE Statement
-- Day         : 27
-- Description : Removing records from a table
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
-- Delete One Record
-- ==========================================

DELETE FROM students
WHERE id = 3;

-- ==========================================
-- Delete Students with Marks < 85
-- ==========================================

DELETE FROM students
WHERE marks < 85;

-- ==========================================
-- View Remaining Records
-- ==========================================

SELECT * FROM students;