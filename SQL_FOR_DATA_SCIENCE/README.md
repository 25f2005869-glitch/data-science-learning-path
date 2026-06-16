# SQL for Data Science – 35 Day Learning Journey

## Project Overview

This repository documents my complete SQL learning journey as part of the **IIT Madras BS Degree in Data Science and Applications** program.

The repository covers SQL fundamentals, intermediate concepts, advanced analytics queries, database design principles, and hands-on projects using SQLite.

The goal of this repository is to build a strong foundation in SQL for Data Science, Data Analytics, Database Management Systems (DBMS), and future Machine Learning applications.

---

## Author

**Saloni Tiwari**
IITM BS Degree in Data Science and Applications

---

## Tools Used

* SQLite 3
* Visual Studio Code
* Git
* GitHub

---

## Repository Structure

### SQL Foundation (Day 01 – Day 10)

* Day 01 – SQL Introduction
* Day 02 – SELECT, DISTINCT, ALIAS
* Day 03 – WHERE, AND, OR, NOT
* Day 04 – ORDER BY, LIMIT
* Day 05 – LIKE, IN, BETWEEN
* Day 06 – Aggregate Functions
* Day 07 – GROUP BY, HAVING
* Day 08 – CASE WHEN
* Day 09 – String Functions
* Day 10 – Date Functions

---

### SQL Joins (Day 11 – Day 15)

* Day 11 – INNER JOIN
* Day 12 – LEFT JOIN
* Day 13 – RIGHT JOIN
* Day 14 – FULL JOIN
* Day 15 – SELF JOIN

---

### Intermediate SQL (Day 16 – Day 20)

* Day 16 – UNION & UNION ALL
* Day 17 – Subqueries
* Day 18 – Common Table Expressions (CTE)
* Day 19 – Window Functions
* Day 20 – RANK, DENSE_RANK, ROW_NUMBER

---

### Advanced SQL (Day 21 – Day 30)

* Day 21 – Views
* Day 22 – Indexes
* Day 23 – Triggers
* Day 24 – Transactions
* Day 25 – Data Cleaning SQL
* Day 26 – UPDATE Statement
* Day 27 – DELETE Statement
* Day 28 – Constraints
* Day 29 – Database Design & Normalization
* Day 30 – SQL Capstone Project

---

### Analytics SQL (Day 31 – Day 35)

* Day 31 – Advanced Joins Challenge
* Day 32 – Advanced Subqueries
* Day 33 – Recursive CTE
* Day 34 – Advanced Window Functions
* Day 35 – SQL Analytics Mega Project

---

## Projects

### Project 01 – Student Database Management System

Features:

* CREATE TABLE
* INSERT INTO
* UPDATE
* DELETE
* PRIMARY KEY
* FOREIGN KEY
* JOINS
* GROUP BY
* HAVING

### Project 02 – Library Management System

Features:

* Books Management
* Member Management
* Borrowing Records
* SQL Queries for Reporting

### Project 03 – Sales Analytics

Features:

* Revenue Analysis
* Product Performance
* Customer Insights
* Aggregation Queries

### Project 04 – E-Commerce Analytics

Features:

* Orders Analysis
* Customer Analytics
* Product Analytics
* Window Functions

### Project 05 – SQL Analytics Mega Project

Features:

* Joins
* Subqueries
* CTE
* Recursive CTE
* Window Functions
* Ranking Functions
* Views
* Constraints
* Analytics Reporting

---

## Sample Query

```sql
SELECT
    student_name,
    marks,
    DENSE_RANK() OVER (
        ORDER BY marks DESC
    ) AS rank_position
FROM students;
```

---

## Learning Outcomes

By completing this repository, I learned:

* SQL Fundamentals
* Database Design
* Data Cleaning
* Data Analysis using SQL
* Relational Database Concepts
* Joins and Relationships
* Window Functions
* Query Optimization
* Transaction Management
* Analytics Reporting

---

## Course Information

SQL for Data Science

Part of the IIT Madras BS Degree in Data Science and Applications Program.

---

## Future Roadmap

* Advanced DBMS
* PostgreSQL
* MySQL
* Data Analytics Projects
* Power BI Integration
* Machine Learning Data Pipelines

---

## Repository Status

✅ 35 Days Completed

✅ SQL Foundations Completed

✅ Intermediate SQL Completed

✅ Advanced SQL Completed

✅ Analytics SQL Completed

✅ Portfolio Projects Completed

---

## Connect

GitHub Portfolio created as part of my journey in the IIT Madras BS Degree in Data Science and Applications program.

Author: Saloni Tiwari
