-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Views
-- Day         : 21
-- Description : Creating and Using SQL Views
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
-- Create View
-- ==========================================

CREATE VIEW high_scorers AS

SELECT
    id,
    name,
    city,
    marks
FROM students
WHERE marks >= 85;

-- ==========================================
-- Use View
-- ==========================================

SELECT *
FROM high_scorers;

-- ==========================================
-- Count High Scorers
-- ==========================================

SELECT COUNT(*) AS Total_High_Scorers
FROM high_scorers;

-- ==========================================
-- High Scorers from Patna
-- ==========================================

SELECT *
FROM high_scorers
WHERE city = 'Patna';