-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : SELECT Statement, Specific Columns,
--               DISTINCT and Aliases
-- Day         : 02
-- Description : Learning how to retrieve data from
--               tables using SELECT, DISTINCT and AS
-- ==================================================

-- ==================================================
-- PART 1 : CREATE SAMPLE TABLE
-- ==================================================

CREATE TABLE students (
id INTEGER,
name TEXT,
city TEXT,
course TEXT
);

-- ==================================================
-- PART 2 : INSERT SAMPLE DATA
-- ==================================================

INSERT INTO students VALUES (1,'Saloni','Patna','Data Science');
INSERT INTO students VALUES (2,'Rahul','Delhi','Python');
INSERT INTO students VALUES (3,'Aman','Patna','SQL');
INSERT INTO students VALUES (4,'Neha','Mumbai','Python');
INSERT INTO students VALUES (5,'Saloni','Patna','Data Science');

-- ==================================================
-- PART 3 : SELECT ALL COLUMNS
-- ==================================================

SELECT * FROM students;

-- ==================================================
-- PART 4 : SELECT SPECIFIC COLUMNS
-- ==================================================

SELECT name FROM students;

SELECT city FROM students;

SELECT name, city FROM students;

-- ==================================================
-- PART 5 : DISTINCT
-- ==================================================

SELECT DISTINCT city FROM students;

SELECT DISTINCT course FROM students;

-- ==================================================
-- PART 6 : ALIASES (AS)
-- ==================================================

SELECT name AS Student_Name
FROM students;

SELECT city AS Student_City
FROM students;

SELECT course AS Course_Name
FROM students;

-- ==================================================
-- PART 7 : COMBINING SELECT + DISTINCT + ALIAS
-- ==================================================

SELECT DISTINCT city AS Unique_Cities
FROM students;

SELECT DISTINCT course AS Available_Courses
FROM students;

-- ==================================================
-- PART 8 : PRACTICE QUERIES
-- ==================================================

SELECT name, course
FROM students;

SELECT DISTINCT name
FROM students;

SELECT city AS Location
FROM students;

SELECT DISTINCT city, course
FROM students;
