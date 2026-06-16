-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : ORDER BY and LIMIT
-- Day         : 04
-- ==================================================

-- Sort by name ascending

SELECT *
FROM students
ORDER BY name ASC;

-- Sort by city descending

SELECT *
FROM students
ORDER BY city DESC;

-- First 2 records

SELECT *
FROM students
LIMIT 2;

-- First record after sorting by name

SELECT *
FROM students
ORDER BY name
LIMIT 1;