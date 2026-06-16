-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : LIKE, BETWEEN, IN
-- Day         : 05
-- ==================================================

-- Names starting with S

SELECT *
FROM students
WHERE name LIKE 'S%';

-- Names ending with a

SELECT *
FROM students
WHERE name LIKE '%a';

-- Students from Patna or Delhi

SELECT *
FROM students
WHERE city IN ('Patna', 'Delhi');

-- IDs between 1 and 3

SELECT *
FROM students
WHERE id BETWEEN 1 AND 3;