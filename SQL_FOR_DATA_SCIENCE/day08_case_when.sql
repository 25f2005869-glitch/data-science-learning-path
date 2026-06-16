-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : CASE WHEN
-- Day         : 08
-- ==================================================

-- Categorize students based on city

SELECT id,
       name,
       city,
       CASE
           WHEN city = 'Patna' THEN 'Bihar Student'
           WHEN city = 'Delhi' THEN 'Delhi Student'
           ELSE 'Other State Student'
       END AS Student_Category
FROM students;


-- Categorize students based on course

SELECT id,
       name,
       course,
       CASE
           WHEN course = 'Data Science' THEN 'DS Learner'
           WHEN course = 'Python' THEN 'Python Learner'
           ELSE 'Other Course'
       END AS Course_Category
FROM students;


-- Assign Level using ID

SELECT id,
       name,
       CASE
           WHEN id <= 2 THEN 'Beginner'
           WHEN id <= 4 THEN 'Intermediate'
           ELSE 'Advanced'
       END AS Student_Level
FROM students;