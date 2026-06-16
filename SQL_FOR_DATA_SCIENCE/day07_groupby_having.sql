-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : GROUP BY and HAVING
-- Day         : 07
-- ==================================================

-- Count students city-wise

SELECT city,
       COUNT(*) AS Total_Students
FROM students
GROUP BY city;


-- Count students course-wise

SELECT course,
       COUNT(*) AS Total_Students
FROM students
GROUP BY course;


-- Cities having more than 1 student

SELECT city,
       COUNT(*) AS Total_Students
FROM students
GROUP BY city
HAVING COUNT(*) > 1;


-- Courses having more than 1 student

SELECT course,
       COUNT(*) AS Total_Students
FROM students
GROUP BY course
HAVING COUNT(*) > 1;