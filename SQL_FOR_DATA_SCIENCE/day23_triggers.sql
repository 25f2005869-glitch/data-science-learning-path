-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Triggers
-- Day         : 23
-- Description : Automatic actions on database events
-- ==================================================

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS student_logs;

-- ==========================================
-- Create Students Table
-- ==========================================

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    marks INTEGER
);

-- ==========================================
-- Create Log Table
-- ==========================================

CREATE TABLE student_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT
);

-- ==========================================
-- Create Trigger
-- ==========================================

CREATE TRIGGER trg_student_insert

AFTER INSERT ON students

BEGIN

    INSERT INTO student_logs(message)
    VALUES ('New Student Added');

END;

-- ==========================================
-- Insert Records
-- ==========================================

INSERT INTO students VALUES (1,'Saloni',95);
INSERT INTO students VALUES (2,'Rahul',80);

-- ==========================================
-- Check Logs
-- ==========================================

SELECT *
FROM student_logs;