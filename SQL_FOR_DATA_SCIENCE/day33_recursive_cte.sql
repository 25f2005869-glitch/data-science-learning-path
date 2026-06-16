-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Recursive CTE
-- Day         : 33
-- Description : Generating hierarchical and
--               recursive data using WITH RECURSIVE
-- ==================================================

-- ==========================================
-- Example 1 : Generate Numbers 1 to 10
-- ==========================================

WITH RECURSIVE numbers(n)
AS
(
    SELECT 1

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 10
)

SELECT *
FROM numbers;

-- ==========================================
-- Example 2 : Employee Hierarchy
-- ==========================================

DROP TABLE IF EXISTS employees;

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

WITH RECURSIVE employee_hierarchy
AS
(
    SELECT
        emp_id,
        emp_name,
        manager_id,
        1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.emp_id,
        e.emp_name,
        e.manager_id,
        eh.level + 1
    FROM employees e
    INNER JOIN employee_hierarchy eh
        ON e.manager_id = eh.emp_id
)

SELECT *
FROM employee_hierarchy;