-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : WHERE, AND, OR, NOT
-- Day         : 03
-- ==================================================

SELECT *
FROM students
WHERE city = 'Patna';

SELECT *
FROM students
WHERE course = 'Python';

SELECT *
FROM students
WHERE city='Patna'
AND course='SQL';

SELECT *
FROM students
WHERE city='Delhi'
OR city='Mumbai';

SELECT *
FROM students
WHERE NOT city='Patna';