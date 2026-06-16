-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : UNION and UNION ALL
-- Day         : 16
-- Description : Combining results from multiple queries
-- ==================================================

DROP TABLE IF EXISTS science_students;
DROP TABLE IF EXISTS commerce_students;

-- ==========================================
-- Create Science Students Table
-- ==========================================

CREATE TABLE science_students (
    id INTEGER,
    name TEXT
);

INSERT INTO science_students VALUES (1,'Saloni');
INSERT INTO science_students VALUES (2,'Rahul');
INSERT INTO science_students VALUES (3,'Aman');

-- ==========================================
-- Create Commerce Students Table
-- ==========================================

CREATE TABLE commerce_students (
    id INTEGER,
    name TEXT
);

INSERT INTO commerce_students VALUES (3,'Aman');
INSERT INTO commerce_students VALUES (4,'Neha');
INSERT INTO commerce_students VALUES (5,'Riya');

-- ==========================================
-- UNION
-- Removes duplicates
-- ==========================================

SELECT name
FROM science_students

UNION

SELECT name
FROM commerce_students;

-- ==========================================
-- UNION ALL
-- Keeps duplicates
-- ==========================================

SELECT name
FROM science_students

UNION ALL

SELECT name
FROM commerce_students;