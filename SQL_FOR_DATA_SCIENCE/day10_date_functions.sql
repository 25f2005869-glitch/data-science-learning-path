-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Date Functions
-- Day         : 10
-- ==================================================

-- Current Date

SELECT DATE('now') AS Current_Date;


-- Current Time

SELECT TIME('now') AS Current_Time;


-- Current Date and Time

SELECT DATETIME('now') AS Current_DateTime;


-- Date after 7 days

SELECT DATE('now', '+7 days') AS Date_After_7_Days;


-- Date before 30 days

SELECT DATE('now', '-30 days') AS Date_Before_30_Days;


-- Current Year

SELECT STRFTIME('%Y', 'now') AS Current_Year;


-- Current Month

SELECT STRFTIME('%m', 'now') AS Current_Month;


-- Current Day

SELECT STRFTIME('%d', 'now') AS Current_Day;