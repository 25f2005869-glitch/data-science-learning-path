-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : String Functions
-- Day         : 09
-- ==================================================

-- Convert names to uppercase

SELECT id,
       UPPER(name) AS Name_Uppercase
FROM students;


-- Convert names to lowercase

SELECT id,
       LOWER(name) AS Name_Lowercase
FROM students;


-- Find length of names

SELECT id,
       name,
       LENGTH(name) AS Name_Length
FROM students;


-- Extract first 3 characters

SELECT id,
       name,
       SUBSTR(name, 1, 3) AS First_3_Chars
FROM students;


-- Concatenate name and city

SELECT id,
       name || ' - ' || city AS Student_Info
FROM students;