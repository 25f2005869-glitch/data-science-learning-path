-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Aggregate Functions
-- Day         : 06
-- ==================================================

-- Total students

SELECT COUNT(*) AS Total_Students
FROM students;

-- Highest ID

SELECT MAX(id) AS Highest_ID
FROM students;

-- Lowest ID

SELECT MIN(id) AS Lowest_ID
FROM students;

-- Average ID

SELECT AVG(id) AS Average_ID
FROM students;

-- Sum of IDs

SELECT SUM(id) AS Total_ID_Sum
FROM students;