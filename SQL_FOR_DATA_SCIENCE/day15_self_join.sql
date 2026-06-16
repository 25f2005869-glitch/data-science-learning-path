-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : SELF JOIN
-- Day         : 15
-- Description : Joining a table with itself
-- ==================================================

DROP TABLE IF EXISTS employees;

-- ==========================================
-- Create Employees Table
-- ==========================================

CREATE TABLE employees (
    emp_id INTEGER,
    emp_name TEXT,
    manager_id INTEGER
);

INSERT INTO employees VALUES (1,'Saloni',NULL);
INSERT INTO employees VALUES (2,'Rahul',1);
INSERT INTO employees VALUES (3,'Aman',1);
INSERT INTO employees VALUES (4,'Neha',2);
INSERT INTO employees VALUES (5,'Riya',2);

-- ==========================================
-- SELF JOIN
-- ==========================================

SELECT
    e.emp_name AS Employee,
    m.emp_name AS Manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.emp_id;